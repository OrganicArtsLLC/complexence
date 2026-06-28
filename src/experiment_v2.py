#!/usr/bin/env python3
"""experiment_v2.py — the central bet under a lossy channel (capability sweep).

v0.1 (experiment.py) tied conditions A and B at a 3-hop toy task: with a clean channel
and a short invariant, telephone never drifts, so a shared form has nothing to save.
That null pointed at the real question — does the shared form help when the channel is
LOSSY? v0.2 tests exactly that, isolating one variable.

Design: an N-hop relay where the text passed BETWEEN agents goes through a lossy
channel (word-dropout at rate p — a stand-in for weak agents / noisy links). The two
conditions differ in exactly one thing: whether the true invariant survives the channel.

  A (anchored):  every hop sees the FULL invariant (clean, re-pinned) + lossy(work).
  B (telephone): every hop sees only lossy(previous text). The invariant lives only in
                 hop 0's output, then decays with the channel.

Sweep p and watch the gap. Fidelity is measured THREE ways (triangulated, because a
single model-judge scalar was the v0.1 bottleneck):

  1. rubric         — fraction of the invariant's named claims still expressed (0-1),
  2. reconstruction — can a fresh agent rebuild the original essence from the final? (0/1),
  3. holistic       — median of three 0-10 fidelity judgments, normalized to 0-1.

PRE-REGISTERED PREDICTION (committed before the run — see git history):
  · p = 0.0 : A and B TIE on rubric (|delta| < 0.15) — clean channel, nothing to save.
  · p = 0.6 : A beats B on rubric by >= +0.20 — the anchor pays off as the channel
              degrades. The bet's signature is delta GROWING with p.
  If delta stays flat near 0 across p, that is honest evidence AGAINST the bet (or that
  it does not hold for capable models on this task). Either way it is a real result.

Usage: python experiment_v2.py [--hops 5] [--trials 2] [--noise 0.0,0.6] [--three-arm]
Needs a model adapter on PATH (the `claude` CLI by default, via demo.claude).
"""
from __future__ import annotations

import argparse
import json
import random
import re
import statistics
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from demo import claude  # the swappable model adapter

HERE = Path(__file__).parent
WORKERS = 6


# ── The lossy channel (the "weak agent / noisy link" knob) ───────────────────

def lossy(text: str, p: float, rng: random.Random) -> str:
    """Drop each word with probability p — degrades what the next hop receives.
    p=0 is a clean channel; p=0.6 keeps ~40% of the words (broken but on-topic)."""
    if p <= 0 or not text:
        return text
    kept = [w for w in text.split() if rng.random() > p]
    return " ".join(kept) if kept else text.split()[0] if text.split() else text


# ── The relay (the only difference between conditions is the anchor) ─────────

def relay(condition: str, invariant: str, hops: int, p: float, rng: random.Random) -> str:
    work = invariant  # hop 0's input is the clean invariant under every condition
    for i in range(hops):
        seen = lossy(work, p, rng) if i > 0 else work
        if condition == "A":  # anchored: full invariant re-pinned clean every hop
            prompt = (
                "You are one agent in a relay building a shared artifact. The CORE INTENT "
                "below is fixed and must be honored exactly. Elaborate the work one step "
                "further (add concrete detail or structure, short paragraph) while staying "
                "true to the core intent. Output only the elaboration.\n\n"
                f"CORE INTENT (do not drift from this):\n{invariant}\n\nWORK SO FAR:\n{seen}")
        elif condition == "Bprime":  # generic anchor, but NOT the true invariant
            prompt = (
                "You are one agent in a relay. Stay on the original topic and do not drift. "
                "Elaborate the text one step further (add concrete detail or structure, short "
                "paragraph). Output only the elaboration.\n\nTEXT SO FAR:\n" + seen)
        else:  # B telephone: only the (lossy) previous text, no anchor
            prompt = (
                "Take the following and elaborate it one step further — add concrete detail "
                "or structure, keep it to a short paragraph. Output only the elaboration.\n\n"
                + seen)
        work = claude(prompt)
    return work


# ── Three fidelity instruments (triangulated) ────────────────────────────────

def _present(claim: str, final: str) -> int:
    out = claude(
        "Is the following idea still clearly expressed in the TEXT? Answer only YES or "
        f"NO on the first line.\n\nIDEA: {claim}\n\nTEXT:\n{final}")
    return 1 if out.upper().lstrip().startswith("YES") else 0


def metric_rubric(essence: str, constraints: list[str], final: str) -> float:
    """Fraction of the invariant's named claims still expressed. The strong instrument:
    it scores each claim separately, so partial preservation is visible."""
    claims = [essence] + list(constraints)
    return sum(_present(c, final) for c in claims) / len(claims)


def metric_reconstruction(essence: str, final: str) -> int:
    """Can a fresh agent rebuild the original essence from the final text alone? (0/1)"""
    recon = claude(
        "Below is one representation of an idea. In one sentence, state the core idea it "
        "is expressing.\n\nREPRESENTATION:\n" + final)
    verdict = claude(
        "Do these two statements express the SAME core idea? Answer only YES or NO on the "
        f"first line.\n\nA: {essence}\n\nB: {recon}")
    return 1 if verdict.upper().lstrip().startswith("YES") else 0


def _holistic_one(essence: str, final: str) -> int | None:
    out = claude(
        "Score 0-10 how faithfully the TEXT still expresses the ORIGINAL idea (10 = fully "
        f"preserved, 0 = lost). Reply with ONLY a single integer.\n\nORIGINAL:\n{essence}\n\n"
        f"TEXT:\n{final}")
    nums = re.findall(r"\b(?:10|[0-9])\b", out)
    return int(nums[0]) if nums else None


def metric_holistic(essence: str, final: str) -> float:
    scores = [s for s in (_holistic_one(essence, final) for _ in range(3)) if s is not None]
    return (statistics.median(scores) / 10.0) if scores else float("nan")


# ── One full trial cell (runs sequentially; cells run concurrently) ──────────

def run_cell(condition: str, p: float, trial: int, inv: dict, hops: int) -> dict:
    rng = random.Random(int(p * 1000) + trial * 7 + (1 if condition == "B" else 0))
    essence = inv["essence"]
    final = relay(condition, essence, hops, p, rng)
    return {
        "condition": condition, "p": p, "trial": trial,
        "rubric": metric_rubric(essence, inv.get("constraints", []), final),
        "recon": metric_reconstruction(essence, final),
        "holistic": metric_holistic(essence, final),
        "final_preview": final[:160],
    }


def summarize(rows: list[dict], conds: list[str], noises: list[float]) -> dict:
    out = {}
    for p in noises:
        out[p] = {}
        for c in conds:
            cell = [r for r in rows if r["p"] == p and r["condition"] == c]
            out[p][c] = {m: round(statistics.mean([r[m] for r in cell]), 3)
                         for m in ("rubric", "recon", "holistic")} if cell else {}
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hops", type=int, default=5)
    ap.add_argument("--trials", type=int, default=2)
    ap.add_argument("--noise", type=str, default="0.0,0.6")
    ap.add_argument("--three-arm", action="store_true", help="add control arm B' (generic anchor)")
    ap.add_argument("--out", type=str, default="experiment_v2_results.json")
    args = ap.parse_args()

    noises = [float(x) for x in args.noise.split(",")]
    conds = ["A", "B"] + (["Bprime"] if args.three_arm else [])
    inv = json.loads((HERE / "example.cform.json").read_text(encoding="utf-8"))["invariant"]

    print(f"central-bet v0.2 — lossy-channel sweep")
    print(f"  hops={args.hops}  trials={args.trials}  noise={noises}  conditions={conds}")
    print(f"  invariant: {inv['essence']}\n  claims scored: {1 + len(inv.get('constraints', []))}\n")

    cells = [(c, p, t) for p in noises for t in range(args.trials) for c in conds]
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        rows = list(pool.map(lambda a: run_cell(a[0], a[1], a[2], inv, args.hops), cells))
    dt = time.time() - t0

    summ = summarize(rows, conds, noises)
    (HERE / args.out).write_text(json.dumps({"summary": summ, "rows": rows, "seconds": dt,
                                             "hops": args.hops, "trials": args.trials}, indent=2))

    print("=" * 64)
    print(f"  {'noise':>6}  {'cond':>6}  {'rubric':>7}  {'recon':>6}  {'holistic':>8}")
    for p in noises:
        for c in conds:
            s = summ[p][c]
            print(f"  {p:>6}  {c:>6}  {s.get('rubric', 0):>7.2f}  {s.get('recon', 0):>6.2f}  {s.get('holistic', 0):>8.2f}")
        if "A" in summ[p] and "B" in summ[p] and summ[p]["A"] and summ[p]["B"]:
            d = summ[p]["A"]["rubric"] - summ[p]["B"]["rubric"]
            print(f"  {p:>6}  {'A-B':>6}  {d:>+7.2f}  (rubric delta)")
        print("  " + "-" * 60)
    print(f"  {len(cells)} cells, {dt:.0f}s → {args.out}")

    # Pre-registered verdict (committed in the docstring before the run)
    print("=" * 64)
    if len(noises) >= 2:
        lo, hi = min(noises), max(noises)
        if summ[lo].get("A") and summ[hi].get("A"):
            d_lo = summ[lo]["A"]["rubric"] - summ[lo]["B"]["rubric"]
            d_hi = summ[hi]["A"]["rubric"] - summ[hi]["B"]["rubric"]
            print(f"  delta(rubric) at p={lo}: {d_lo:+.2f}   at p={hi}: {d_hi:+.2f}")
            if d_hi - d_lo >= 0.20 and d_hi >= 0.20:
                print("  → evidence FOR the bet: the anchor's advantage GROWS as the channel")
                print("    degrades — a boundary condition, not an always-true claim.")
            elif abs(d_hi) < 0.15 and abs(d_lo) < 0.15:
                print("  → null even under a lossy channel: no advantage at this task/scale.")
                print("    Honest evidence the bet does not hold for capable models here.")
            else:
                print("  → mixed / underpowered. Needs more trials or a harder task.")
    print("=" * 64)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

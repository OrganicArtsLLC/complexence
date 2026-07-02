#!/usr/bin/env python3
"""experiment.py — the central bet (§9.1), tested with numbers.

Does coordinating through a shared Cognitive Form beat passing independent text?
N agents elaborate an idea in a relay, under two conditions:

  A (shared form): each agent sees the canonical INVARIANT plus the accumulated work;
     the invariant is re-pinned every hop.
  B (telephone):   each agent sees only the previous agent's text. No invariant anchor.

After N hops, measure SEMANTIC DRIFT: score how faithfully the final output still
expresses the ORIGINAL invariant (0-10, model-judged). Higher = less drift. If A
drifts less than B, that is evidence for the bet; if not, that is honest negative
evidence — which the framework explicitly invites (§10.5).

v0.1 experiment: small N, model-judged, toy task. Not a published result — a runnable,
falsifiable first cut of the §9.4 multi-agent design.

Usage: python experiment.py [--hops 4] [--trials 2]
Needs a model adapter on PATH (the `claude` CLI by default). Licensed MIT.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import time
from pathlib import Path

from demo import claude  # the swappable model adapter

HERE = Path(__file__).parent


def relay_telephone(seed: str, hops: int) -> str:
    """Condition B: each agent sees only the previous text. Drift can accumulate."""
    text = seed
    for _ in range(hops):
        text = claude(
            "Take the following and elaborate it ONE step further — add concrete detail "
            "or structure, keep it to a short paragraph. Output only the elaboration.\n\n"
            + text)
    return text


def relay_shared_form(invariant: str, hops: int) -> str:
    """Condition A: each agent sees the canonical invariant + accumulated work. The
    invariant is re-pinned every hop, so meaning has an anchor that cannot drift."""
    work = ""
    for _ in range(hops):
        work = claude(
            "You are one agent in a relay building a shared artifact. The CORE INTENT "
            "below is fixed and must be honored exactly. Elaborate the work ONE step "
            "further — add concrete detail or structure, short paragraph — while staying "
            "true to the core intent. Output only the elaboration.\n\n"
            f"CORE INTENT (do not drift from this):\n{invariant}\n\n"
            f"WORK SO FAR:\n{work or '(none yet)'}")
    return work


def _one_judge(original: str, final: str) -> int | None:
    out = claude(
        "Score 0-10 how faithfully the FINAL text still expresses the ORIGINAL core "
        "intent (10 = fully preserved, 0 = lost). Reply with ONLY a single integer.\n\n"
        f"ORIGINAL:\n{original}\n\nFINAL:\n{final}")
    nums = re.findall(r"\b(?:10|[0-9])\b", out)
    return int(nums[0]) if nums else None  # None = parse failure, NOT a real 0


def drift_score(original: str, final: str, judges: int = 3) -> float | None:
    """Median of `judges` independent 0-10 ratings. None on total parse failure.
    The median across judges damps the high single-call variance v0.1 showed."""
    scores = [s for s in (_one_judge(original, final) for _ in range(judges)) if s is not None]
    return statistics.median(scores) if scores else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hops", type=int, default=4)
    ap.add_argument("--trials", type=int, default=2)
    args = ap.parse_args()

    form = json.loads((HERE / "example.cform.json").read_text(encoding="utf-8"))
    invariant = form["invariant"]["essence"]
    print(f"central-bet experiment — {args.hops} hops, {args.trials} trial(s)\n")
    print(f"invariant (the intent that must survive):\n  {invariant}\n")

    a_scores: list[int] = []
    b_scores: list[int] = []
    t0 = time.time()
    for i in range(args.trials):
        print(f"trial {i+1}:")
        a_final = relay_shared_form(invariant, args.hops)
        a = drift_score(invariant, a_final)
        a_scores.append(a)
        print(f"  A shared-form  fidelity = {a}/10")
        b_final = relay_telephone(invariant, args.hops)
        b = drift_score(invariant, b_final)
        b_scores.append(b)
        print(f"  B telephone    fidelity = {b}/10")
    dt = time.time() - t0

    a_vals = [s for s in a_scores if s is not None]
    b_vals = [s for s in b_scores if s is not None]
    a_mean = statistics.mean(a_vals) if a_vals else float("nan")
    b_mean = statistics.mean(b_vals) if b_vals else float("nan")
    delta = a_mean - b_mean
    THRESH = 1.5  # below this, treat as noise at v0.1 scale — do not claim a signal
    print("\n" + "=" * 56)
    print(f"  A (shared Cognitive Form): mean fidelity {a_mean:.1f}/10  trials={a_vals}")
    print(f"  B (independent telephone): mean fidelity {b_mean:.1f}/10  trials={b_vals}")
    print(f"  delta (A - B): {delta:+.1f}   ({dt:.0f}s)")
    if not a_vals or not b_vals or abs(delta) < THRESH:
        print(f"  → WITHIN NOISE (|delta| < {THRESH}). No trustworthy signal at this N.")
        print("    Finding: at v0.1 the MEASUREMENT is the bottleneck, not the bet (§10.5).")
        print("    Next: more trials, a calibrated rubric judge, a less gameable task.")
    elif delta > 0:
        print("  → evidence FOR the bet: the shared form preserved intent better.")
    else:
        print("  → evidence AGAINST: telephone held intent better. Honest negative result.")
    print("=" * 56)
    print("\nv0.1 caveats: small N, model-judged drift, one toy task. This is a runnable,")
    print("falsifiable first cut of §9.4 — not a published result.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

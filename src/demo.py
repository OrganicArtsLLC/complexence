#!/usr/bin/env python3
"""demo.py — run the Cognitive Form operators in practice, with a real model.

Wires the semantic operators of `cognitive_form.py` to a live model (here the local
`claude` CLI as one example adapter — swap in any model) and runs a small end-to-end
loop on a Cognitive Form:

  1. project the invariant into a new representation,
  2. translate that representation into another,
  3. a ROUND-TRIP invariant check (the first real, if crude, `invariant_preserved`):
     reconstruct the essence from a representation alone, then ask the model whether
     the meaning survived — "meaning is what survives transformation" (§7.2), tested.

Each transform is timed as a meaning-velocity proxy (§9.3). This is the v0.1
measurement-harness seed (ROADMAP Phase 2). Honest: the invariant check is a model's
judgment, not a proof — but it is a real, runnable check, not a stub.

Usage:
    python demo.py [path.cform.json]      # defaults to example.cform.json
Requires a model adapter on PATH (the `claude` CLI by default).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import cognitive_form as cf

HERE = Path(__file__).parent


# ── Model adapter (swap this for any model) ──────────────────────────────────

def claude(prompt: str) -> str:
    """One example adapter: the local `claude` CLI. Replace with any model call."""
    exe = shutil.which("claude") or os.path.expanduser("~/.claude/local/claude")
    if not (exe and os.path.exists(exe)):
        raise RuntimeError("no `claude` CLI found — point this adapter at any model.")
    env = {k: v for k, v in os.environ.items()
           if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL")}
    r = subprocess.run([exe, "-p", prompt], capture_output=True, text=True, env=env, timeout=120)
    return r.stdout.strip()


def timed(label, fn):
    t0 = time.time()
    out = fn()
    dt = time.time() - t0
    print(f"  · {label:28} {dt:5.1f}s")
    return out, dt


# ── A real invariant_preserved: reconstruct + judge ──────────────────────────

def round_trip_preserved(essence: str, representation: str) -> tuple[bool, str]:
    """Reconstruct the core idea from a representation alone, then ask the model if it
    matches the original essence. A crude but real test of meaning survival (§7.2)."""
    recon = claude(
        "Below is one representation of an idea. In one sentence, state the core idea "
        "it is expressing.\n\nREPRESENTATION:\n" + representation)
    verdict = claude(
        "Do these two statements express the SAME core idea? Answer strictly 'YES' or "
        f"'NO' on the first line, then one short reason.\n\nA: {essence}\n\nB: {recon}")
    ok = verdict.upper().lstrip().startswith("YES")
    return ok, f"reconstructed: {recon}\n  verdict: {verdict.splitlines()[0] if verdict else '?'}"


# ── Run ──────────────────────────────────────────────────────────────────────

def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "example.cform.json"
    form = json.loads(path.read_text(encoding="utf-8"))
    ok, errs = cf.validate(form)
    print(f"load + validate {path.name}: {'✓ valid' if ok else '✗ ' + '; '.join(errs)}")
    if not ok:
        return 1
    essence = form["invariant"]["essence"]
    print(f"\ninvariant essence:\n  {essence}\n\nrunning operators (real model):")

    total = 0.0
    # 1. project: invariant -> a fresh representation (a metaphor)
    form, dt = timed("project -> metaphor", lambda: cf.project(
        form, "text", lambda f: claude(
            "Express this idea as a vivid two-sentence metaphor a smart teenager would "
            f"get. No preamble.\n\nIDEA: {essence}")))
    total += dt
    metaphor = form["representations"][-1]["content"]
    print(f"    {metaphor[:120]}")

    # 2. translate: metaphor -> pseudocode
    (form, dt) = timed("translate -> pseudocode", lambda: cf.translate(
        form, "text", "code", lambda f: claude(
            "Turn this metaphor into 4-6 lines of readable pseudocode that captures its "
            f"structure. Code only.\n\nMETAPHOR: {metaphor}")))
    total += dt
    print(f"    {form['representations'][-1]['content'].splitlines()[0][:120]} ...")

    # 3. round-trip invariant check (real invariant_preserved) on the metaphor
    (res, dt) = timed("invariant round-trip", lambda: round_trip_preserved(essence, metaphor))
    total += dt
    preserved, detail = res
    print(f"    {detail}")
    print(f"    invariant_preserved = {preserved}")

    n = 3
    print(f"\nmeaning-velocity proxy: {n} transforms in {total:.1f}s "
          f"= {n/total:.2f} transforms/s (toy figure; §9.3)")
    print("\nNote: the invariant check is a model's judgment, not a proof — but it is a "
          "real, runnable operationalization of 'meaning survives transformation'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

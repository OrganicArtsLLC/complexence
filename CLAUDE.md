# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`complexence` is the **public, canonical home of a three-layer idea**, not a
conventional application. It ships a *method* (specs + prompt contracts + blank
templates) and an early *science* (a Python reference implementation and
falsifiable experiments). There is no app to install and no service to run.

The three layers, each with a canonical spec in `spec/`:

| Layer | What it is | Spec |
|---|---|---|
| **Capability** | orienting under load (an eight-level map, L0–L7) | `spec/complexence-capability.md` |
| **Operating method (OS)** | turn thought into artifacts via agent roles — *the runnable-today part* | `spec/complexence-os.md` |
| **Foundation (science)** | ontology + recursive cognitive equation + two calculi + a research program | `spec/complexence-science.md` |
| **Labs & measurement (v2)** | installable `.complexence/` runtime, typed-ID research index, the Λ measure, one-way publish pipeline | `spec/complexence-labs.md` |

The specs are the source of truth. The `src/` code is a *partial* instantiation of
Theory B from the science spec — treat the spec as authoritative when they diverge.

## The one hard constraint: public repo, private data

**This repository is PUBLIC and git history is permanent.** Read `GUARDRAILS.md`
before writing anything committable. The governing rule is **"method in public,
data in private."** Never write into any tracked file anything that identifies a
real person, employer, client, project codename, or private number — even in
examples, tests, or commit messages. A user's actual usage lives in `instance/`
(gitignored) or a separate private repo, never here.

Before any commit, the pre-commit guard must pass:

```bash
./scripts/check-no-secrets.sh   # scans staged diff for PII/secrets + .private-denylist terms
```

This is not boilerplate caution — it is the primary operational risk in this repo.
When editing docs or adding examples, keep every concrete detail invented and
generic.

## Repository layout

```text
spec/        the four canonical specifications (start here — source of truth)
RESEARCH.md  v2 research index: open RQs + typed-ID registry (A/D/O/L/H/RQ/ADR/CEX/EXP)
agents/      six role prompt contracts: chief-of-staff (router) + 5 specialists
             (daily-brief, asset-steward, publisher, cartographer, critic)
editors/     drop-in VS Code Copilot integration (prompt files + instructions template)
templates/   blank, shareable artifact templates (safe to commit; filled-in = private)
install/     the .complexence/ runtime scaffold copied by scripts/complexence-install.sh
docs/        START-HERE, layers, bootstrap, instantiate, automation; adr/ = decisions
src/         Python reference implementation of the science (MIT-licensed)
proofs/      candidate derivations for the science's claimed bounds
scripts/     new-day.sh, complexence-install.sh, and check-no-secrets.sh
instance/    a user's PRIVATE data — gitignored, you never create or commit this
```

## Working with `src/` (the science reference implementation)

Pure Python, **stdlib-only**. `jsonschema` is used for validation *if installed*,
otherwise a structural fallback runs — there is no requirements file, no build, and
no test suite. Scripts use **relative imports** (`from demo import claude`), so
**run them from inside `src/`**, not the repo root.

```bash
cd src
python cognitive_form.py validate example.cform.json   # the compliance check
python cognitive_form.py reflect  example.cform.json   # ℭ describing itself
python demo.py                                          # end-to-end loop vs a live model
python experiment.py --hops 3 --trials 3               # central-bet relay (A vs B)
python experiment_v2.py --hops 5 --trials 2 --noise 0.0,0.6   # lossy-channel sweep
```

`demo.py`, `experiment.py`, and `experiment_v2.py` need a **model adapter on PATH**.
The default adapter is the local `claude` CLI (`demo.claude()`), designed to be
swapped for any model call. `cognitive_form.py` needs no model.

Key modules:
- `cognitive_form.py` — the `CognitiveForm` operators. Deterministic ops
  (`validate`, `compose`, `reflect`) are real; semantic ops (`project`, `translate`,
  `compress`, `execute`, …) delegate the meaning-bearing step to a caller-supplied
  `transform` callable, then call `invariant_preserved(...)` — a **deliberate stub**
  standing in for the open isomorphism (science §10). Do not "fix" that stub into a
  fake solution; it marks unsolved research.
- `cognitive-form.schema.json` — canonical `ℭ = (I, R, T, F, H)` interchange format.
- `experiment_v2_results.json` / `*_run.log` — run artifacts, **gitignored**;
  regenerate by running the scripts.

### Scientific-integrity norm

This repo tracks results honestly, including null and invalid runs (see the
existing "honest null result" and "first v0.2 run was invalid" write-ups in
`src/README.md` and `ROADMAP.md`). Preserve that: report what a run actually showed,
flag contamination/artifacts, and never present a conjecture, proof-sketch, or
stubbed operator as an established result. The specs deliberately scope claims as
"candidate" / "conjectured" — keep that hedging intact when editing.

## The OS method (`agents/` + `templates/`)

The runnable-today workflow is prompt-driven and needs no code: capture into a dated
inbox, route the inbox through the `chief-of-staff` prompt, which delegates to the
five specialist roles to produce durable markdown artifacts, reviewed via a weekly
cadence. `spec/complexence-os.md` is the full contract; `docs/layers.md` explains the
Layer 0–4 "cognitive orchestration" ladder. When adapting the method, the guidance
is: **change only the nouns (categories, what an "asset" is, who owns decisions);
keep the contracts identical** (confidence rubric, routing thresholds ≥90/70–89/<70,
the five daily-brief sections).

## Conventions

- Licensing is split by content type: prose/docs are **CC BY 4.0**; code
  (`src/`, `scripts/`) is **MIT**. Keep new files under the right license and don't
  mix.
- Commit messages follow `type(scope): summary` (e.g. `feat(src):`, `docs:`,
  `review(complexence):`), often with a parenthetical fix count for review passes.

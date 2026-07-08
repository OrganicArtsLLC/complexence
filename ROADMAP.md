# Roadmap — The Science of Complexence

Complexence is published as an **open research program**, not a finished science.
This file is where its edges, direction, and falsifiable claims live in the open.
The point of versioning it is itself part of the theory: a foundation developed
without feedback drifts ([`spec/complexence-science.md`](./spec/complexence-science.md)
§8.5), so git history, issues, and pull requests *are* the feedback loop.

**Status:** v0.1 — formal spec stable enough to build on and argue with; the
reference implementation runs (Phase 1) and the measurement harness has its first
falsifiable experiments (Phase 2 seed). First result: an honest null. Second run
(v0.2): invalid, with raw numbers leaning against the prediction, written up
below, not buried.

---

## The central bet

> Human–AI collaboration improves when cognition operates on representation-invariant
> **Cognitive Forms** rather than on independent documents, prompts, diagrams, and
> code. (`complexence-science.md` §9.1)

(A Cognitive Form is the meaning kept separate from any one way of writing it down —
the same idea whether it's an essay, a diagram, or code. "Representation-invariant"
is that property. Defined in the spec, §7.)

This is the claim everything else is in service of, and the thing that has to be
*measured*, not just asserted, before "science" loses its caveat.

## Open edges (the live research questions)

From `complexence-science.md` §10 — these are tracked, not hidden, because the open
edges *are* the field:

1. **Which primitive is deepest** — potential, distinction, or constraint? Fixes the bottom of the ontology.
2. **Are the two calculi dual?** The Metacognitive Calculus (process) and the Calculus of Cognitive Forms (object) both compress to `ℭ_{t+1} = Φ(ℭ_t, …)`. A formal duality is the most-wanted theorem.
3. **Ontology vs. processing** — the §4 separation is asserted, not proven.
4. **Linear vs. recursive-graph form** — the mature object needs a precise graph definition (nodes, edge types, fixed points).
5. **Measurability is the whole bet** — meaning velocity, throughput, and trust must be estimated and shown to predict performance, or this stays a well-structured program, not a result.

## Phases

| Phase | Goal | Done when |
|---|---|---|
| **0 — Spec (now)** | The formal foundation, public and versioned | `spec/complexence-science.md` v0.1 published |
| **1 — Reference implementation** | Make the object runnable | a `CognitiveForm` type + operators (`project`, `translate`, `compress`, `reflect`, `execute`, `correct`) in `src/`, MIT-licensed |
| **2 — Measurement harness** | Turn the falsifiable claims into tests | estimators for meaning velocity, throughput, attention, trust; toy experiments (§9.4) |
| **3 — Multi-agent benchmarks** | Test the central bet | shared-Cognitive-Form vs. independent-prompt coordination, measured |
| **4 — Validated laws** | Earn the word *science* without a caveat | measures shown to predict performance in humans, AIs, and hybrid teams |

Phase 1 onward is the "devops the science" work: the spec gets a reference
implementation, the implementation gets tests, the tests operationalize the claims,
and the loop closes: `correct(ℭ, F)` producing the next version.

## Landed so far (the loop in motion)

The feedback the §8.5 argument predicts started running within hours of going
public. Honest framing: the first outside passes came from me putting the spec in
front of other frontier models and vetting what came back — solicited, model-assisted
feedback, not community traction. Genuine external review (minds not under my
direction) is still pending, and saying so is the point:

- **`src/cognitive-form.schema.json`** — the Cognitive Form interchange format (Phase 1).
  First draft contributed by Google Gemini against the public spec, then vetted here
  (operator enum aligned to §7.3: added `correct`; `$schema` URI fixed). MIT.
- **`proofs/channel-capacity-sketch.md`** — the §6.6 bound *derived under three explicit
  (still-unjustified) assumptions*. Contributed + vetted. It relocates the debt to its
  premises rather than erasing it; honest progress, not a closed result.
- **`src/demo.py`** — the operators run end-to-end against a live model: project →
  translate → a real (if crude) round-trip `invariant_preserved` check. The Phase-2
  measurement-harness seed.
- **`src/experiment.py`** — a first, falsifiable cut at the central bet (§9.4): N-hop
  relay under condition A (shared invariant re-pinned each hop) vs. B (telephone, text
  only), scored for semantic drift.
- **`src/experiment_v2.py`** — the v0.2 lossy-channel sweep: the same relay, but the
  text passed between hops goes through word-dropout at rate p, isolating the one
  variable the v0.1 null pointed at. Its docstring carries a pre-registered
  prediction, written before the run (the run artifacts are gitignored, so the
  ordering is stated, not provable from git history).

### First experiment result — honest negative / inconclusive

The first run *looked* like evidence for the bet (A beat B). It was an artifact: the
v0.1 drift scorer silently defaulted unparseable judgments to `0`, and a single
model-judge swung wildly (per-trial scores of 0 and 8 for the *same* condition).
Hardening the scorer (median of three judges, parse-failure ≠ 0) collapsed the
variance to `A=[5,7,7]` vs `B=[6,7,7]`: **mean 6.3 vs 6.7, delta −0.3, inside noise.**

So the first measured finding is **no signal at this scale**, and the real lesson is
the one §10.5 names in advance: *measurability is the whole bet.* The bottleneck is the
measurement, not (yet) the claim: a toy task at 3 hops preserves intent under both
conditions, so there is nothing for a shared form to save. The bet predicts the gap
opens as hops, agent count, and task difficulty grow; testing that is Phase 3 with a
calibrated rubric judge (or embeddings), more trials, and a harder task. Recorded here
rather than buried, because a program that hides its null results is just a brand.

### Second experiment result (v0.2) — invalid run, raw direction against the prediction

The v0.2 docstring pre-registered a signature for the bet: A and B tie on rubric at
p=0.0, and A beats B by ≥ +0.20 at p=0.6, the delta growing with noise. The run
happened on 2026-06-28. It did not deliver a valid test, and what it did produce
leaned the other way. Both facts belong here, in order of importance:

1. **The run is invalid.** At p=0.6 the model adapter returned API-refusal text
   ("Claude Code is unable to respond to this request…") instead of elaborations.
   The refusals entered the relay as if they were work products, then went to the
   judges as if they were finals; one pure refusal was scored **rubric 1.0**, a
   graded artifact expressing nothing. The v0.1 lesson repeated one layer down: I
   hardened the scorer, and then the *harness* fed it garbage it trusted. §10.5 in
   practice, again: measurement validity is the whole bet.
2. **For the record, the raw deltas ran against the pre-registered signature:**
   rubric delta A−B was **−0.12 at p=0.0 and −0.38 at p=0.6** — the anchored
   condition did *worse* as the channel degraded, the inverse of the prediction.
   Because of (1), this is not clean evidence against the bet; it is an invalid run
   whose direction happened to be adverse. It is reported anyway, because a public
   pre-registration with a silent outcome is worse than no pre-registration at all.

What changes before the re-run: the harness now rejects refusal/error outputs (a
nonzero adapter exit raises; a refusal signature invalidates the trial instead of
scoring it), and every cell reports its validity rate. Then v0.2 runs again, clean.
Until that lands, the pre-registration stands as an open debt, and this section is
the receipt.

That is the whole point of versioning the science in public: critique, contribution,
and *honest negative results* all become commits.

## v2 — the labs & measurement layer

A parallel track, additive to the phases above: turn the method into an *installable*
runtime so real work can feed the science without exposing what the work is. The
architecture is [`spec/complexence-labs.md`](./spec/complexence-labs.md), decided in
[`docs/adr/ADR-0001-labs-architecture.md`](./docs/adr/ADR-0001-labs-architecture.md);
open questions are indexed in [`RESEARCH.md`](./RESEARCH.md).

| Step | Goal | Done when |
|---|---|---|
| **v2.1 — Install scaffold** | Make the method installable | `./scripts/complexence-install.sh` scaffolds `.complexence/` (landed, seed) |
| **v2.2 — Research framework** | Give the repo a front door | `RESEARCH.md` + typed IDs (`A/D/O/L/H/RQ/ADR/CEX/EXP`) (landed, seed) |
| **v2.3 — Measurement** | Instrument orientation | a lab reports an orientation delta / Λ proxy tracking a real outcome (`RQ-009`) |
| **v2.4 — Role library** | Extend the runtime | domain roles packaged as installable contracts alongside `chief-of-staff` |
| **v2.5 — Publishing pipeline** | Close the loop | the first real pattern card promotes a public operator (labs §7) |

The load-bearing caution (labs §8.1, `RQ-007`): **don't over-build the install before
the method is validated.** v2.1–v2.2 are deliberately thin; v2.3 is where the science
actually gets tested, and Λ stays a *candidate* measure until a lab shows it predicts
something (labs §6.2).

## How to contribute

Issues and pull requests are the feedback term `F`. Argue with the spec, propose a
proof or a counterexample, sharpen a definition, or build a piece of the reference
implementation. Prose is **CC BY 4.0**; code is **MIT**. Credit where it came from.

---

**Last Updated:** 2026-07-07.

# Roadmap — The Science of Complexence

Complexence is published as an **open research program**, not a finished science.
This file is where its edges, direction, and falsifiable claims live in the open.
The point of versioning it is itself part of the theory: a foundation developed
without feedback drifts ([`spec/complexence-science.md`](./spec/complexence-science.md)
§8.5), so git history, issues, and pull requests *are* the feedback loop.

**Status:** v0.1 — formal spec stable enough to build on and argue with; the
reference implementation runs (Phase 1) and the measurement harness has its first
falsifiable experiment (Phase 2 seed), whose first result is an honest null (below).

---

## The central bet

> Human–AI collaboration improves when cognition operates on representation-invariant
> **Cognitive Forms** rather than on independent documents, prompts, diagrams, and
> code. (`complexence-science.md` §9.1)

This is the claim everything else is in service of, and the thing that has to be
*measured*, not just asserted, before "science" loses its caveat.

## Open edges (the live research questions)

From `complexence-science.md` §10 — these are tracked, not hidden, because a field
that hides its open edges is just a brand:

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
and the loop closes — `correct(ℭ, F)` producing the next version.

## Landed so far (the loop in motion)

The feedback the §8.5 argument predicts is already running — the published spec drew
external review and contributions within hours of going public:

- **`src/cognitive-form.schema.json`** — the Cognitive Form interchange format (Phase 1).
  First draft contributed by Google Gemini against the public spec, then vetted here
  (operator enum aligned to §7.3 — added `correct`; `$schema` URI fixed). MIT.
- **`proofs/channel-capacity-sketch.md`** — the §6.6 bound *derived under three explicit
  (still-unjustified) assumptions*. Contributed + vetted. It relocates the debt to its
  premises rather than erasing it — honest progress, not a closed result.
- **`src/demo.py`** — the operators run end-to-end against a live model: project →
  translate → a real (if crude) round-trip `invariant_preserved` check. The Phase-2
  measurement-harness seed.
- **`src/experiment.py`** — a first, falsifiable cut at the central bet (§9.4): N-hop
  relay under condition A (shared invariant re-pinned each hop) vs. B (telephone, text
  only), scored for semantic drift.

### First experiment result — honest negative / inconclusive

The first run *looked* like evidence for the bet (A beat B). It was an artifact: the
v0.1 drift scorer silently defaulted unparseable judgments to `0`, and a single
model-judge swung wildly (per-trial scores of 0 and 8 for the *same* condition).
Hardening the scorer — median of three judges, parse-failure ≠ 0 — collapsed the
variance to `A=[5,7,7]` vs `B=[6,7,7]`: **mean 6.3 vs 6.7, delta −0.3, inside noise.**

So the first measured finding is **no signal at this scale**, and the real lesson is
the one §10.5 names in advance: *measurability is the whole bet.* The bottleneck is the
measurement, not (yet) the claim — a toy task at 3 hops preserves intent under both
conditions, so there is nothing for a shared form to save. The bet predicts the gap
opens as hops, agent count, and task difficulty grow; testing that is Phase 3 with a
calibrated rubric judge (or embeddings), more trials, and a harder task. Recorded here
rather than buried, because a program that hides its null results is just a brand.

That is the whole point of versioning the science in public: critique, contribution,
and *honest negative results* all become commits.

## How to contribute

Issues and pull requests are the feedback term `F`. Argue with the spec, propose a
proof or a counterexample, sharpen a definition, or build a piece of the reference
implementation. Prose is **CC BY 4.0**; code is **MIT**. Credit where it came from.

---

**Last Updated:** 2026-06-28.

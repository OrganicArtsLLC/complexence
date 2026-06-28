# Roadmap — The Science of Complexence

Complexence is published as an **open research program**, not a finished science.
This file is where its edges, direction, and falsifiable claims live in the open.
The point of versioning it is itself part of the theory: a foundation developed
without feedback drifts ([`spec/complexence-science.md`](./spec/complexence-science.md)
§8.5), so git history, issues, and pull requests *are* the feedback loop.

**Status:** v0.1 — formal spec stable enough to build on and argue with; the
measurement layer is not yet built.

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

## How to contribute

Issues and pull requests are the feedback term `F`. Argue with the spec, propose a
proof or a counterexample, sharpen a definition, or build a piece of the reference
implementation. Prose is **CC BY 4.0**; code is **MIT**. Credit where it came from.

---

**Last Updated:** 2026-06-28.

# RESEARCH — the navigation layer

Complexence is an open **research program** (see
[`spec/complexence-science.md`](./spec/complexence-science.md) and
[`ROADMAP.md`](./ROADMAP.md)). This file is its front door: the live research
questions and the registry of typed, citable identifiers everything else references.

It exists so that an agent, a contributor, or a future you can say **"`D-002` changed
after `EXP-018`"** instead of "remember that orientation thing." Every claim in the
corpus gets an ID; every experiment in a private lab links back to these IDs (see
[`spec/complexence-labs.md`](./spec/complexence-labs.md) §5).

> **Public grammar only.** This index holds *questions and structure*, never data.
> Experiments (`EXP-NNN`) run inside private labs and are **not** listed here; only
> their abstracted results ever promote a public artifact. See
> [`GUARDRAILS.md`](./GUARDRAILS.md).

**Status:** v0.1 — seeded from the existing specs. Counts marked *(private)* live in
labs, not in this repo. **Last Updated:** 2026-07-07.

---

## Open research questions

Each `RQ-NNN` is a question the program is actually working, with its status and the
public artifacts attached to it. "Experiments" counts run in private labs; the number
is a measure of activity, not a promise of public data.

| ID | Question | Status | Attached |
|---|---|---|---|
| `RQ-001` | Can orientation be measured? | Active | `D-003`, `L-001`, Λ (labs §6) |
| `RQ-002` | Can cognitive entropy be reduced through AI summarization? | Open | — |
| `RQ-003` | Does graph/artifact coherence correlate with engineering throughput? | Open | — |
| `RQ-004` | Does coordinating agents through a shared Cognitive Form beat independent prompts? (**the central bet**) | Active | `H-001`, science §9.1, `src/experiment.py` |
| `RQ-005` | Are Theory A and Theory B dual? | Open | science §10.2 |
| `RQ-006` | Which ontological primitive is deepest — potential, distinction, or constraint? | Open | science §4.2 |
| `RQ-007` | What is the minimum viable `.complexence/` install? | Open | labs §8.1 |
| `RQ-008` | When does a lab pattern become a public operator? | Open | labs §7, §8.5 |
| `RQ-009` | Is Λ a cardinal measure or only an ordinal comparison scaffold? | Active | Λ (labs §6.2) |

Questions are added, not renumbered. A closed question keeps its ID and is marked
*Resolved* with the artifact that resolved it.

---

## The typed-identifier registry

Nine artifact types. All are public except `EXP`, which is private by construction
(an experiment runs over real lab data).

| Prefix | Type | Where it lives |
|---|---|---|
| `A-NNN` | Assumption | public |
| `D-NNN` | Definition | public |
| `O-NNN` | Operator | public |
| `L-NNN` | Law | public |
| `H-NNN` | Hypothesis | public |
| `RQ-NNN` | Research Question | public (above) |
| `ADR-NNN` | Architecture Decision | public (`docs/adr/`) |
| `CEX-NNN` | Counterexample | public (abstracted) |
| `EXP-NNN` | Experiment | **private** (a lab's `.complexence/experiments/`) |

### Definitions (`D`)

| ID | Definition | Source |
|---|---|---|
| `D-001` | **Cognitive Form** `ℭ = (I, R, T, F, H)` — meaning kept separate from any one representation | science §7.1 |
| `D-002` | **Meaning velocity** = Δmeaning / Δtime — the north-star metric | science §8.2 |
| `D-003` | **Orientation** — a person's ability to answer *what is this / where am I / what matters / what changes next / what can I do* about a system | labs §2, §6.1 |
| `D-004` | **Legibility Λ** — candidate measure; legible when `Λ > 1` (ordinal, not yet cardinal) | labs §6 |
| `D-005` | **Orientation delta** — the ordinal before/after change in orientation an experiment reports | labs §2, §5 |

### Operators (`O`)

The eight Cognitive-Form operators (science §7.3), reference-implemented in
[`src/cognitive_form.py`](./src/cognitive_form.py):

| ID | Operator | Kind |
|---|---|---|
| `O-001` | `project(ℭ, repr)` | semantic |
| `O-002` | `translate(ℭ, i, j)` | semantic |
| `O-003` | `compress(ℭ)` | semantic |
| `O-004` | `expand(ℭ)` | semantic |
| `O-005` | `compose(ℭ₁, ℭ₂)` | deterministic |
| `O-006` | `reflect(ℭ)` | deterministic |
| `O-007` | `execute(ℭ)` | semantic |
| `O-008` | `correct(ℭ, F)` | semantic |

### Laws (`L`)

The seven laws of the Calculus of Cognitive Forms (science §7.5):

| ID | Law |
|---|---|
| `L-001` | Meaning is invariance across transformation |
| `L-002` | The map is a projection, not the form: `R_i(ℭ) ⊂ ℭ` |
| `L-003` | Power without feedback drifts: `Power × NoFeedback = Drift` |
| `L-004` | Compression must preserve essence |
| `L-005` | Translation requires repair |
| `L-006` | Reflection without feedback hallucinates |
| `L-007` | Execution reveals meaning: `Meaning(ℭ) = what ℭ makes possible` |

### Hypotheses (`H`)

| ID | Hypothesis | Source |
|---|---|---|
| `H-001` | Human–AI collaboration improves when cognition operates on representation-invariant Cognitive Forms rather than independent artifacts (**the central bet**) | science §9.1 |

### Assumptions (`A`)

| ID | Assumption (candidate, unproven — see science §1a, §10) | Source |
|---|---|---|
| `A-001` | The ontology's primitive set is minimal and generative | science §4.3 |
| `A-002` | `Meaning()` can be grounded operationally as consequences-for-action under a goal | science §7.1 note |

### Counterexamples (`CEX`)

None recorded yet. A `CEX-NNN` is an abstracted result that counts *against* a public
claim; the first honest null/adverse runs are written up narratively in
[`ROADMAP.md`](./ROADMAP.md) and will be assigned IDs as they are distilled.

---

## How a lab contributes

A private lab links its experiments to these IDs via the front-matter in
[`install/experiments/EXP-000.template.md`](./install/experiments/EXP-000.template.md)
(`depends_on`, `tests`, `updates`, `supports`, `contradicts`). When a result recurs
across contexts and is abstracted (labs §7), it promotes a new or revised public
artifact here through a
[pattern card](./templates/pattern-card.template.md). Raw experiments never appear in
this file.

---

## Relations

- [`spec/complexence-labs.md`](./spec/complexence-labs.md) — the framework this index serves (§5)
- [`spec/complexence-science.md`](./spec/complexence-science.md) — where the definitions, laws, and open questions come from
- [`docs/adr/ADR-0001-labs-architecture.md`](./docs/adr/ADR-0001-labs-architecture.md) — the decision that created this layer
- [`ROADMAP.md`](./ROADMAP.md) — phases and the narrative record of experiment results

# Complexence Labs & Measurement

**The v2 layer beneath [Complexence OS](./complexence-os.md): how running instances
feed the [science](./complexence-science.md) without exposing what they are.** An
installable runtime, a measurement discipline, and a one-way pipeline that turns
private observation into public abstraction.

**Status:** Public seed spec — v0.1, instance-agnostic. This is a *proposal for
structure*, not a validated result; where it names measures (Λ, orientation delta)
they are **candidate** instruments under the same honesty rules as
[`complexence-science.md`](./complexence-science.md) §1a — read them as conjectures
to be earned, not as established quantities.

> **This document is grammar, not knowledge.** It defines *how* a lab is organized
> and measured, never *what* any lab contains. The moment a file names a real
> project, person, employer, metric value, or observation, it is lab data and
> belongs in a private lab, never here. See [`../GUARDRAILS.md`](../GUARDRAILS.md).

---

## Table of contents

- [1. What this document is](#1-what-this-document-is)
- [2. The reframe: orientation as the objective function](#2-the-reframe-orientation-as-the-objective-function)
- [3. The three-layer architecture](#3-the-three-layer-architecture)
- [4. The installation model](#4-the-installation-model)
- [5. The research framework: typed identifiers and the index](#5-the-research-framework-typed-identifiers-and-the-index)
- [6. Measurement: the legibility measure Λ](#6-measurement-the-legibility-measure-λ)
- [7. The publishing pipeline](#7-the-publishing-pipeline)
- [8. What is honestly unresolved](#8-what-is-honestly-unresolved)
- [9. Relations](#9-relations)

---

## 1. What this document is

The v1 stack — [capability](./complexence-capability.md) (orient under load),
[OS](./complexence-os.md) (turn thought into artifacts), and
[science](./complexence-science.md) (the formal foundation and its research program)
— defines a method and a theory. It leaves two things unbuilt:

1. **No path from daily work to the science.** Every place the method actually gets
   used generates observations, experiments, and small results. None of that feeds
   the research program (`complexence-science.md` §9) in any structured way. There
   is no measurement harness connecting practice to theory.
2. **No install model.** Today the method is *read and manually applied*. It should
   be *installed* — a thin scaffold that makes any repository a participant in the
   research loop **without embedding anything private in the public runtime**.

This document specifies the architecture that closes both gaps, and it is written to
respect the constraint that makes the whole thing viable: the public repository must
never reveal the private work running on top of it.

The frame is deliberately borrowed from operating systems. Linux does not contain
your documents; Git does not contain your business; Terraform does not know your
architecture. Each provides a *language* the private world runs on. Complexence OS
should provide a language for **orientation** — and, like those systems, should never
know what is running on it.

---

## 2. The reframe: orientation as the objective function

The public mission has been *Making Complexity Visible*. That is the right name for
the mission. The v2 refinement adds the objective *underneath* it:

> **Making complexity visible** is one method.
> **Engineering orientation** is the objective function.

The distinction earns its keep by giving every lab a single shared question,
regardless of domain:

> *Does this system improve a person's orientation while reducing their cognitive
> effort?*

Complexity is made visible **so that** orientation improves; visibility is
instrumental, orientation is the target. This ties dashboards, maps, agents, and
algorithms to one optimizable objective without requiring any of them to share a
repository or a domain.

The operational consequence: **every lab experiment reports an orientation delta**,
not just a task outcome. Orientation delta is the plain-language proxy; the science's
**meaning velocity** (`complexence-science.md` §8.2) is its formalization; the
**legibility measure Λ** (§6 below) is the candidate instrument that connects them.
This section is a *framing* claim — that orientation is the right objective — and
like every claim here it is earned only if measuring it predicts anything (§8).

This reframe is registered as an open research question, not asserted as settled:
`RQ-001 — Can orientation be measured?` (see [`../RESEARCH.md`](../RESEARCH.md)).

---

## 3. The three-layer architecture

The public repo holds **grammar**. Labs hold **knowledge**. Flow between them is
one-way — from private observation to public abstraction — and no raw data ever
travels back down.

```text
                     PUBLIC  (this repository)
        ============================================
          THEORY        definitions, operators, laws, ontology
          REFERENCE OS  templates, schemas, roles, install tooling
        ============================================
                          │  installs into
              ┌───────────┼───────────┐
              │           │           │
           lab A        lab B        lab C        LABORATORIES
         (private)    (private)    (private)      one per project; own data
              │           │           │
              └───────────┴───────────┘
                          │  produces (sanitized abstractions only)
                          ▼
              Public improvements → Complexence OS vN+1
```

> **Naming note.** These three tiers are deliberately *not* numbered "Layer 1–3":
> this repo already uses "the layers" for the Layer 0–4 cognitive-orchestration
> ladder of [`../docs/layers.md`](../docs/layers.md), which is a different axis (how
> far *one practitioner* has externalized their thinking). The ladder is climbed
> *inside* a lab; the tiers here describe where artifacts *live*.

**Theory** (public). Definitions, operators, mathematical objects, foundational
laws, architectural decisions. Nothing domain-specific. Changes rarely, and only
through the science's own feedback loop.

**Reference OS** (public). Templates, schemas, roles, prompts, and the install
tooling — the runtime. Domain-agnostic. Updates when a pattern validated in a lab is
abstracted up (§7).

**Laboratories** (private). Each active project is a lab. It installs the OS, runs
the roles, and generates experiments. Its data stays private. Only sanitized
patterns — stripped of all domain knowledge — may move up to the Reference OS.

The load-bearing discipline, in one line:

> **Labs are consumers of Complexence. They are not Complexence.**

This is the same separation as an operating system and the applications that run on
it. The OS does not become your documents; Complexence does not become your
experiments. The public roster of *which* labs exist, and what each studies, is
itself lab knowledge — it lives in a private index, never here.

---

## 4. The installation model

A repository participates by **installing** the runtime, which creates a thin
scaffold holding only structural artifacts — no domain knowledge.

```text
.complexence/
    charter.md               # why this repo exists (a scope statement)
    operating-principles.md  # local adaptations of the core principles
    roles/                   # installed role prompts (copied from the Reference OS)
    experiments/             # EXP-NNN.md, one per active experiment
    metrics/                 # the orientation log + measures this lab tracks
    schemas/                 # local data schemas
    prompts/                 # role and session prompts
    summaries/               # generated weekly summaries
```

The reference implementation of the installer and its templates lives in
[`../install/`](../install/) and [`../scripts/complexence-install.sh`](../scripts/complexence-install.sh).
The runtime is **identical across all repos**; only the *installed roles* differ. Role
prompts are public (they are grammar); the private role *invocations* — the actual
conversations, briefs, and outputs — stay in the lab and are gitignored there.

**Relation to the v1 instance model.** An *instance*
([`complexence-os.md`](./complexence-os.md) §10, [`../docs/instantiate.md`](../docs/instantiate.md))
is a deployment of the daily method: `inbox/ today/ decisions/ …`, the capture →
route → produce → review loop. A *lab* is a repository participating in the research
loop. **They compose; neither replaces the other.** The `.complexence/` scaffold is
the *research overlay* — charter, experiments, metrics, summaries — laid alongside
whatever instance folders the repo keeps. A personal instance becomes a lab the day
it installs the scaffold and starts logging orientation deltas; a project repo can be
a lab without running the full daily cadence. The v1 quickstart
([`../docs/START-HERE.md`](../docs/START-HERE.md)) is still the front door for
*practicing the method*; installing a lab is the door for *contributing to the
science*.

**Install, don't copy.** A lab installs the runtime rather than forking a customized
copy, so a correction to a definition or a role propagates to every lab through a
versioned release while each lab keeps its own data. This is the same reason you
`apt install` a package instead of pasting its source into your project.

**Roles are specializations, not additions.** The `chief-of-staff` router
([`../agents/chief-of-staff.prompt.md`](../agents/chief-of-staff.prompt.md)) is
universal — every lab installs it. A *domain chief* (a risk officer, an engineer, an
editor…) is not a seventh specialist — the six-role cap of
[`complexence-os.md`](./complexence-os.md) §5 stands. It is the **same router
contract with the nouns localized** to the lab's domain, under the existing rule:
change only the nouns, keep the contracts (rubric, routing thresholds, brief
sections) identical. Which specialization a given lab runs is a private choice
recorded in that lab's charter, not a public fact. The public repo ships the *role
contracts*; it does not enumerate who installed what.

The Chief of Staff asks the same eight questions in every lab, independent of domain
— the last one is the gate that protects private work:

1. What changed? 2. What matters? 3. What is blocked? 4. What should be measured?
5. What should become an experiment? 6. What should become an ADR? 7. What should
become a reusable operator? 8. **What should become public?**

Question 8's answer is never *publish* — it is *abstract* (§7).

---

## 5. The research framework: typed identifiers and the index

The public repo has a research program (`complexence-science.md` §9,
[`../ROADMAP.md`](../ROADMAP.md)) but no systematic way for labs to contribute
observations to it. The framework adds two public artifacts and one lab-side
convention.

**[`../RESEARCH.md`](../RESEARCH.md) — the navigation layer** (public). Every open
research question gets an `RQ-NNN` entry with its status and the counts of artifacts
attached to it. It turns the repo's front door from "a pile of specs" into "a set of
questions being worked."

**Typed identifiers** (public registry in `RESEARCH.md`). Every artifact in the
system gets an unambiguous, citable ID, so an agent says "`D-004` changed after
`EXP-018`" instead of "remember that orientation thing":

| Prefix | Type | Lives in |
|---|---|---|
| `A-NNN` | Assumption | public |
| `D-NNN` | Definition | public |
| `O-NNN` | Operator | public |
| `L-NNN` | Law | public |
| `H-NNN` | Hypothesis | public |
| `RQ-NNN` | Research Question | public |
| `ADR-NNN` | Architecture Decision | public |
| `CEX-NNN` | Counterexample | public (abstracted) |
| `EXP-NNN` | Experiment | **private** (lives in a lab's `.complexence/experiments/`) |

Only `EXP-NNN` is private: an experiment is run inside a lab, over real data. Its
*result*, once abstracted, may promote a public definition or operator (§7) — but the
experiment record itself never leaves the lab.

**Experiment links** (lab-side convention). Every `EXP-NNN.md` in a lab declares its
relationships to the public knowledge graph in structured front-matter:

```yaml
depends_on: [A-002, D-006]   # public assumptions/definitions it relies on
tests: [H-004]               # hypotheses it tests
updates: [D-006]             # definitions it would revise
supports: [L-002]            # laws it provides evidence for
contradicts: []              # public claims it counts against
orientation_delta: +1.2      # measured in the lab's own units (see §6)
```

The public repo accumulates *validated structure* (`A/D/O/L/H`); the private labs
accumulate *measurements* (`EXP`). The links let the two form one knowledge graph
without any measurement crossing the public boundary. The JSON schema for this
front-matter ships at
[`../install/schemas/experiment.schema.json`](../install/schemas/experiment.schema.json).

---

## 6. Measurement: the legibility measure Λ

Orientation (§2) needs an instrument. This section proposes one — and is scrupulous
about how little it currently is. **The exploratory dialogue this measure came from
also warned, correctly, that it is easy to build a framework broad enough to describe
anything and too vague to be useful.** Λ is presented here as a *structured comparison
scaffold*, not a computed scalar, precisely to stay on the useful side of that line.

### 6.1 The candidate

A map `M` of a system `S` becomes *legible* — complexity becomes visible — in
proportion to:

```text
        Compression × Prediction × Actionability
  Λ  =  ─────────────────────────────────────────
              Distortion × Cognitive load
```

- **Compression** — the map is smaller than the territory it represents.
- **Prediction** — the map predicts the system's behavior: `P(S | M)`.
- **Actionability** — the map answers the orientation questions: *what is this, where
  am I, what matters, what changes next, what can I do, what happens if I act?*
- **Distortion** — the error the compression introduces.
- **Cognitive load** — the cost of understanding and using the map: `C(M)`.

**Threshold (candidate):** a system is legible when `Λ > 1` — the map gives more
usable orientation than it costs or distorts. Corollary: a bad map makes complexity
*simpler but false* (`Λ < 1`, distortion-dominated); a good map makes it *simpler and
more actionable* (`Λ > 1`).

### 6.2 What Λ is not (yet)

Read this before using Λ as if it were a number.

1. **It is not yet a computed scalar.** The five factors are on no common scale, so
   the product as written is a *dimensional cartoon* — a picture of the intended
   trade-off, not an evaluable expression. This is the same class of debt as the
   `⋂` notation in `complexence-science.md` §7.1, and it is tracked, not hidden.
2. **Its honest use today is ordinal.** Hold `S` fixed, compare two maps `M₁, M₂`,
   and ask *which raises the ratio* — more compression/prediction/actionability for
   less distortion/load. That before-vs-after judgment is real and useful even while
   the absolute number is undefined. An "orientation delta" (§2, §5) is exactly this
   ordinal comparison, reported per experiment.
3. **The factors are not independent.** Compression and distortion are coupled
   (compress harder, distort more); actionability and load trade off. A valid
   cardinal Λ would need those couplings modeled, not multiplied as if orthogonal.

### 6.3 The two factors that can be grounded first

Two of the five are already operational, and give a defensible *partial* measure:

```text
  Point legibility:   L(S, M) = P(S | M) / C(M)
```

`P(S | M)` (how well the map predicts the system) and `C(M)` (the cost of using it)
map directly onto Theory A's measurable quantities — predictive power and cognitive
cost/channel effort (`complexence-science.md` §6.3). `L = P/C` is the honest core of
Λ: *a smaller representation is good when it lets an agent navigate better than direct
exposure to the whole.* The full five-factor Λ is the aspiration; `L = P/C` is what a
lab can estimate now.

A companion precondition — is the system even mappable?

```text
  Mappability:  M = (stable relations) / (total observed relations)
```

A thing becomes mappable when its relationships form repeatable structure rather than
noise (`noise → clusters → pathways → hierarchy → causal graph`). Below some
mappability there is no stable map to be legible about.

### 6.4 The threshold, restated

The `Λ > 1` line is the same statement as:

```text
  Compression gain  >  Information loss
```

— the simplification helps more than it distorts. Stated this way it is *falsifiable
in principle*: for a given map you can, in a given task, measure whether acting on the
compressed map beats acting on the raw system. Whether Λ (or `L = P/C`) actually
*predicts* task performance across domains is the whole bet, and it is unproven
(`complexence-science.md` §10.5). Until a lab shows a Λ proxy tracking a real outcome,
Λ is a well-structured comparison scaffold, not a validated measure.

**The mission, restated precisely:** *Making Complexity Visible = increasing Λ.* That
is a slogan with a research program attached, not a theorem.

---

## 7. The publishing pipeline

The one-way flow from private lab to public abstraction has a canonical sequence.
Nothing domain-specific survives the **Abstraction** step; what moves up is structure.

```text
  Private observation
        ↓
  Experiment            EXP-NNN in a lab's .complexence/experiments/
        ↓
  Measurement           orientation delta / Λ proxy / other lab metric (§6)
        ↓
  Pattern               a stable, repeatable result — seen ≥ 3× across contexts
        ↓
  Abstraction           domain knowledge stripped; only structure preserved
        ↓
  Operator / Definition O-NNN / D-NNN promoted into the public repo
        ↓
  Role or Schema update the OS gains a capability
        ↓
  Public Complexence vN+1
```

The raw experiments, measurements, and observations stay **permanently** in the lab.
The promotion artifact is a **pattern card** (template:
[`../templates/pattern-card.template.md`](../templates/pattern-card.template.md)) — a
sanitized abstraction, reviewed for leakage before it moves. This runs through the
Chief of Staff's weekly cadence: question 8 ("what should become public?") is answered
with a pattern card, never with raw data.

**Promotion criteria (candidate).** A pattern is eligible to become an operator when
it has recurred in **at least three distinct contexts**, its statement carries no
domain nouns, and it survives a leakage review against `GUARDRAILS.md`. The exact
"stable enough" bar is itself an open question (§8).

---

## 8. What is honestly unresolved

These are the v2 open edges. Each should become an `RQ-NNN` in
[`../RESEARCH.md`](../RESEARCH.md).

1. **What is the minimum viable `.complexence/`?** How thin can the install be and
   still produce useful orientation data? The real risk is over-engineering the
   tooling before the method is validated. Start smaller than feels complete.
2. **How do labs report to the science without coupling to it?** The `EXP-NNN`
   front-matter must be light enough that labs actually fill it in, yet structured
   enough to feed the research program. That tension is unresolved.
3. **What is the right granularity of an orientation delta?** Per session, per week,
   per experiment? Self-reported or derived from artifacts? Undecided (§2, §6).
4. **Is Λ a real measure or a comparison scaffold?** As of v0.1 it is the latter
   (§6.2). Promoting it to a cardinal quantity requires a common carrier for its
   factors, a model of their couplings, and — the whole bet — evidence that it
   predicts performance (`complexence-science.md` §10.5).
5. **When does a pattern become an operator?** The pipeline (§7) names the steps but
   the promotion bar ("stable enough") is informal. It needs a definition with an ID.
6. **Does the three-layer architecture scale past one operator?** The model is clean
   for a single practitioner. Whether the Chief of Staff coordination mechanism holds
   across many labs producing many experiments at once is untested.
7. **Does the install model survive a repo changing purpose?** A lab that starts as
   one thing and becomes another needs its charter and experiment history to migrate
   without breaking the knowledge graph.

---

## 9. Relations

- **Theory this serves:** [`complexence-science.md`](./complexence-science.md) — the
  ontology, the recursive equation, and the research program (§9) whose measures Λ
  operationalizes and whose central bet (§10.5) it is subordinate to.
- **Method it extends:** [`complexence-os.md`](./complexence-os.md) — the daily
  operating method; the Chief of Staff cadence this document adds a measurement and
  publishing discipline to.
- **Capability underneath:** [`complexence-capability.md`](./complexence-capability.md)
  — orientation under load, the thing §2 makes the objective function.
- **The decision:** [`../docs/adr/ADR-0001-labs-architecture.md`](../docs/adr/ADR-0001-labs-architecture.md)
  — the terse architectural directive this spec expands.
- **The index:** [`../RESEARCH.md`](../RESEARCH.md) — live research questions and the
  typed-identifier registry.
- **The runtime:** [`../install/`](../install/) and
  [`../scripts/complexence-install.sh`](../scripts/complexence-install.sh) — the
  install model's reference implementation.

---

**Status:** v0.1 (seed). **Last Updated:** 2026-07-07. Licensed CC BY 4.0.

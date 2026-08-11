# ADR-0002: The Four-Plane Architecture — Complexence as Cognitive Relief

**Status:** Accepted
**Date:** 2026-07-29
**Author:** Joshua Ayson / OA LLC
**Scope:** Complexence architecture — the internal anatomy of any running Complexence instance
**Related:**
- [ADR-0001-labs-architecture.md](./ADR-0001-labs-architecture.md)
- [spec/complexence-os.md](../spec/complexence-os.md) — the operating method this anatomizes
- [spec/complexence-science.md](../spec/complexence-science.md) — the foundational science

---

## Context

Complexence has described the full loop:

```
complex reality → observation → modeling → legibility → understanding → decision → action → changed reality
```

What was missing was an internal anatomy — where inside that loop do different kinds of work happen? Without an anatomy, every loop becomes ad hoc. The discipline of maintaining state, interpreting reality, governing agency, and selectively engaging human cognition had no assigned home.

The 2026-07-29 design session worked a related question first:

> What is the difference between an information warehouse and a cognitive relief system?

A warehouse is optimized to preserve and retrieve knowledge. A cognitive relief system is optimized to reduce the amount of knowledge, uncertainty, and obligation a human must actively carry. They overlap, but they are not interchangeable.

The insight that followed: **Complexence is not an information warehouse. It is a cognitive relief system.** The four planes are the internal anatomy that makes that distinction operational.

These planes are not new. They are a formalization of the architecture already latent inside Complexence. The existing loop description — *observe, model, make legible, understand, decide, act, record* — always required these four kinds of work. This ADR names them so every future loop inherits the grammar instead of guessing.

---

## Decision

**The four planes are the canonical internal anatomy of Complexence OS.** They cross-cut every domain. They are not rigid layers (implying a single linear stack that every interaction traverses exactly once) but architectural planes: domains of responsibility that exist across every loop.

### The Four Planes

```
                        ATTENTION PLANE
                  What becomes visible now?
                             ▲
                       GOVERNANCE PLANE
            What may act, decide, interrupt, suppress,
                     escalate, or wait?
                             ▲
                         MEANING PLANE
             What does the observed information represent
                        in this situation?
                             ▲
                         MEMORY PLANE
           What happened, what exists, and what evidence
                       can be recovered?
                             ▲
                        LIVED REALITY
```

Flow is bidirectional. Actions flow back downward:

```
Reality → observe → Memory → interpret → Meaning → govern → Governance → surface → Attention
   ↑                                                                                     │
   └──────────────────────── human or agent action ──────────────────────────────────────┘
```

This is a complete Complexence loop.

---

### Memory Plane — Persistence

**Central question:** What happened, and can we reconstruct it?

Contains:
- Facts, events, documents, messages, metrics, observations
- Prior decisions and their outcomes
- Provenance for what any agent believes
- System state history

The memory plane makes the system durable. Without it, every loop begins again from zero.

**Invariant:** Memory without meaning creates accumulation.

**First obligation:** Facts and interpretations must never occupy the same record. What was observed and what an agent concluded must be separately inspectable. This is the architectural basis for trust.

---

### Meaning Plane — Coherence

**Central question:** What does this observed information represent in this situation?

Contains:
- Entity and relationship graphs
- Ontologies and semantic contracts
- Obligations, commitments, and deadlines
- Operational state (waiting, watching, active, closed)
- Interpretations derived from memory

A warehouse may know an email exists. The meaning plane must determine whether that email represents: information only, a request, a promise, a decision, a deadline, a delegated task, a waiting condition, or noise. That semantic transformation is where most of the cognitive value is created.

**Invariant:** Meaning without governance creates uncontrolled interpretation.

**Operational state machine (minimum viable):**

```
OBSERVED → INTERPRETED → TRIAGED → {ACTIVE | WAITING | WATCHING | PARKED | DISMISSED} → CLOSED
```

---

### Governance Plane — Bounded Agency

**Central question:** Given this meaning, what authority, confidence, and risk rules apply?

Contains:
- Policies and thresholds
- Permission and ownership models
- Risk tolerance and consequence assessment
- Confidence requirements for autonomous action
- Escalation rules and reversibility tests
- Human approval requirements

Governance prevents the system from confusing intelligence with authority. Increased legibility creates increased capability — a system that can see patterns must know when to act, when to ask, when to wait, when to remain silent, and who owns the decision.

**Invariant:** Governance without attention creates invisible control.

Governance decisions must be recorded: you must be able to explain later why an item was hidden, surfaced, or acted upon.

---

### Attention Plane — Human Legibility

**Central question:** What must the human see now, later, on demand, or never?

Contains:
- Daily briefs
- NOW · NEXT · WAITING · WATCHING views
- Dashboards, maps, and visualizations
- Decision packets and exception reports
- Progressive disclosure surfaces

The attention plane is where the Complexence capability becomes visible to the human. Machines may not need a visual map of a complex domain — the human does. A map is not decoration; it is a human-facing cognitive interface that allows the person to see relationships, recognize state, inspect an agent's interpretation, verify logic, know where uncertainty remains, and regain orientation quickly.

**Invariant:** Attention without compression recreates overwhelm. Attention without evidence destroys trust.

**The attention view is a compiled product, not a window.** Every collector, loop, and agent routes through the attention compiler rather than signaling directly. The human receives what governance determines they should see, at the moment it matters, in the form that minimizes carrying cost.

---

## The Planes Repeat Across Domains

The same architecture applies in every domain a Complexence instance serves:

| Domain | Memory | Meaning | Governance | Attention |
|---|---|---|---|---|
| Work ops | Events, logs, deployments | Patterns, ownership, failure modes | Remediation bounds, escalation rules | Ops brief, dashboards |
| Learning | Questions, answers, study history | Knowledge graph, weak edges, mastery | Review cadence, exam-readiness criteria | Map, next exercise |
| Household | Receipts, inventory, expiration dates | Meals available, waste risk, preferences | Budget, dietary rules, pickup method | Use-soon list, dinner choices |
| Finance | Trades, positions, receipts | Regime, exposure, risk profile | Tier limits, max-loss rules | Dashboard, regime alert |

That repetition is what makes the planes part of the Complexence kernel, not merely one application.

---

## The Loop Contract

Every Complexence loop must declare its plane boundaries. This makes capability legible at the control-plane level.

```yaml
schema_version: complexence.loop.v1

id: example-loop
description: ...

memory:
  consumes:
    - <event-type>
  produces:
    - <artifact-type>

meaning:
  interpreter: <agent-name>
  ontology: <ontology-name>
  produces:
    - <interpretation-kind>

governance:
  policy_sets:
    - <policy-name>
  allowed_actions:
    - <action>
  prohibited_actions:
    - <action>

attention:
  channels:
    - <channel-name>
  interrupt_conditions:
    - <condition>

closure:
  terminal_states:
    - resolved
    - accepted_risk
    - false_positive
    - superseded
```

A loop that cannot name what it produces in the meaning plane has no business interrupting the attention plane.

---

## The Canonical Contracts

The planes imply five canonical object schemas. These belong in `contracts/`:

| Object | Plane | Purpose |
|---|---|---|
| `complexence.event.v1` | Memory | Universal observation envelope — facts only, no interpretation |
| `complexence.interpretation.v1` | Meaning | Derived artifact referencing original evidence, with confidence and uncertainty |
| `complexence.obligation.v1` | Meaning | Obligation with owner, state, due date, closure evidence |
| `complexence.governance-decision.v1` | Governance | Record of why an item was surfaced, suppressed, or acted upon |
| `complexence.attention-view.v1` | Attention | Compiled view: NOW · NEXT · WAITING · WATCHING · suppressed count |

These are the load-bearing primitives. Any Complexence instance should eventually hold all five.

---

## What Complexence Is, Sharpened

The four planes sharpen the definition:

> **Complexence is the discipline and architecture of transforming complex system state into governed, actionable human legibility.**

More architecturally:

> **Complexence is a four-plane cognitive control architecture in which durable memory is transformed into meaning, meaning is constrained through governance, and governed significance is selectively presented through attention.**

The purpose:

> To make complexity visible enough to navigate without forcing the human to continuously carry the complexity.

---

## The Practical North Star

```
Nothing should reach attention directly from raw data.
Nothing should leave attention without an explicit durable state transition.
```

---

## On a Fifth Plane

Action was considered and deliberately deferred as a fifth plane. The current framing is:

```
MEMORY → MEANING → GOVERNANCE → ATTENTION
   ▲                                  │
   └──────── action and feedback ─────┘
```

Action is the mechanism by which the architecture changes the world — the execution fabric between and beneath the four planes. Elevating it to a fifth plane is possible but weakens the model's memorability and focuses the anatomy on structure rather than motion. Action is motion; the four planes are structure.

Revisit if the four-plane model proves insufficient in practice.

---

## Consequences

- `spec/complexence-os.md` should reference these four planes as the anatomy of any running Complexence instance. A brief paragraph pointing to this ADR is sufficient; the spec itself remains instance-agnostic.
- The `contracts/` directory should hold the five canonical schema files listed above.
- Instances (labs) should document their plane architecture alongside their loop registry.
- The `spec/complexence-science.md` recursive cognitive equation maps naturally onto the planes: the equation's observation-interpretation-action-learning cycle corresponds to the Memory-Meaning-Governance-Attention flow. This alignment warrants a note in the science spec but is not a change to the equation.
- This ADR is public (it is part of the Complexence public repo). The session that produced it is private.

---

*Last updated: 2026-07-29 — Joshua Ayson / OA LLC*

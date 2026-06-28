# Complexence

**Purpose:** Canonical facts-only specification for the complexence map.
**Status:** Public, versioned. Part of the Complexence repo (CC BY 4.0).
**Scope:** Define orientation and navigation levels so the framework can be
recreated consistently.

---

## 1. Definition

Complexence is the capability of maintaining orientation inside complex systems
and converting orientation into coherent action.

Core loop:

```text
Perception -> Mapping -> Orientation -> Decision -> Action -> Feedback -> Learning
```

Formal basis: this loop is the human-language form of the recursive cognitive
equation `Σ -> ω -> μ -> π -> η -> α -> τ(Σ) -> Σ'` defined in
[The Science of Complexence](./complexence-science.md) (section 5). The
capability is that loop run well under load; the equation defines what "well"
means precisely.

## 2. Stack Placement

| Layer | Name | Function |
|---|---|---|
| Mission | Making Complexity Visible | Make system state legible |
| Framework | Coherent Complexity | Preserve legibility without reductionism |
| Capability | Complexence | Execute orientation and navigation under load |

## 3. Orientation Map Levels

The map is defined as eight levels. All levels are required.

| Level | Name | Question Answered | Primary Output |
|---|---|---|---|
| L0 | Boundary and Objective | What system and outcome are in scope? | Scope statement |
| L1 | Signals | What is happening now? | Observations with timestamps |
| L2 | Structure | How is the system composed? | Component and relation map |
| L3 | Dynamics | How does state change over time? | Trend and transition view |
| L4 | Constraints and Risks | What limits and failure modes exist? | Constraint list + risk register |
| L5 | Orientation State | Where are we now relative to objective? | Position assessment |
| L6 | Navigation Options | What moves are available next? | Option set with tradeoffs |
| L7 | Execution and Learning | What was done and what changed? | Action log + learning update |

## 4. Navigation Protocol

### 4.1 Inputs

- system objective
- current signals
- historical context
- constraints and authorities
- available resources

### 4.2 Process

1. establish L0 boundary and objective
2. collect L1 signals
3. update L2 structure map
4. evaluate L3 dynamics
5. check L4 constraints and risks
6. compute L5 orientation state
7. generate L6 navigation options
8. execute selected option
9. record L7 feedback and learning
10. repeat loop

### 4.3 Outputs

- current orientation snapshot
- ranked next actions
- explicit risks and dependencies
- learning deltas from previous cycle

## 5. Orientation State Model

Orientation state is represented by five fields:

- objective clarity (low/medium/high)
- map confidence (0-100)
- risk pressure (low/medium/high)
- decision latency (minutes/hours/days)
- coherence score (0-100)

Minimum decision gate:

- if map confidence < 60, gather signals before major action
- if risk pressure is high, prefer bounded options first

## 6. Failure Modes

| Failure Mode | Description | Corrective Action |
|---|---|---|
| Reduction Error | Oversimplified model hides key variables | Expand L2 and L4 before acting |
| Signal Flood | Raw input exceeds processing capacity | Filter by objective at L0 |
| Premature Action | Decision made before orientation is stable | Enforce L5 gate |
| Analysis Stall | Endless mapping without action | Time-box L6 and execute bounded move |
| Loop Break | No feedback capture after action | Require L7 logging |

## 7. Calibration Metrics

Track these metrics per cycle:

- orientation accuracy (expected vs observed state)
- decision quality (outcome vs objective)
- reorientation speed (time to recover after new signal)
- loop closure rate (actions with recorded feedback)

## 8. Implementation Surfaces

Complexence can be implemented in three surfaces:

- personal cognition workflow
- team operating cadence
- software artifact layer (orientation graph and dashboards)

All three surfaces must preserve the same level model and loop semantics.

## 9. Relations

- This file is the canonical map spec.
- Scientific basis: [The Science of Complexence](./complexence-science.md)
  (the formal theory under this capability — the two calculi, the foundational
  ontology, and the recursive cognitive equation).
- Strategy and naming context: blog ADR-023.

## 10. Source Inputs

- `sources/better-map-framework-research.md`
- `sources/naming-and-domain-strategy-research.md`
- `sources/origin-rabbit-hole-domainideas.md`
- `sources/A Better Map of Modern Complexity.pdf`
- `sources/The Better Map of Modern Complexity.pdf`

**Last Updated:** 2026-06-28

# Complexence OS — Specification

**Purpose:** Portable, facts-only specification for an operating method that turns
voice-native thought into durable, structured artifacts using a small set of agent
roles, prompts, and (later) scripts.
**Status:** Public seed spec — instance-agnostic.
**Scope:** Define the roles, contracts, cadence, and instantiation protocol so the
same method can be stood up in any context (personal, work, a new project).

> This document is the *method*. An *instance* is one deployment of the method.
> Keep your instance data private (see `GUARDRAILS.md`). This spec stays generic.

---

## 1. Definition

Complexence OS is the operating layer that executes *Complexence* — the capability
of maintaining orientation inside complex systems and converting orientation into
coherent action — as a daily practice. Where Complexence is the *capability*,
Complexence OS is the *machine* that runs the loop with minimal desk friction.

One-line model:

```text
voice in  ->  one router  ->  specialist roles  ->  durable artifacts  ->  weekly review
```

## 2. Stack Placement

| Layer | Function |
|---|---|
| Mission | Make system state legible |
| Framework | Preserve legibility without reductionism |
| Capability (Complexence) | Execute orientation and navigation under load |
| **Operating (Complexence OS)** | Convert thought into artifacts with delegated roles |

Complexence OS does not replace an orientation map; it *feeds and consumes* one
(the Cartographer role produces map artifacts).

## 3. Design Principles

| Principle | Meaning |
|---|---|
| Voice-first | Capture happens by speaking, not by sitting at a desk. |
| One interface | A single router (Chief of Staff) is the only thing the operator talks to. |
| Artifact-first | Every role produces exactly one kind of durable file. |
| Delegate by default | Roles act without asking; they escalate only exceptions. |
| Manual before automated | Prove the flow with prompts before writing any script. |
| One artifact per role | Prevents file sprawl; each role owns one output type. |
| Minimum viable day | On depleted days, capture only. Everything else can wait 48h. |

## 4. Core Loop

```text
Capture -> Route -> Produce -> Review -> Govern -> (repeat)
```

| Step | Owner | Input | Output |
|---|---|---|---|
| Capture | Operator (voice) | raw thought | inbox entries |
| Route | Chief of Staff | inbox | classified + routed items |
| Produce | Specialist roles | routed items | domain / essay / asset artifacts |
| Review | Operator | daily brief | accept / queue / block decisions |
| Govern | Operator + Chief of Staff | week of artifacts | weekly synthesis + focus |

## 5. Role Roster

One router and a capped set of specialists. Start with these six. Do not add a
seventh until the first six are boring and reliable.

| Role | Function | Single Artifact |
|---|---|---|
| Chief of Staff | Classify, route, summarize, escalate | daily brief |
| Daily Brief | Compose the constrained daily readout | `today/<date>` |
| Cartographer | Build orientation maps | `domains/<topic>/map` |
| Asset Steward | Track tracked-asset health and next actions | `assets/census` |
| Publisher | Turn ideas into draft documents | `essays/drafts/<slug>` |
| Critic | Adversarially review drafts before publish | `essays/reviews/<slug>` |

Each role is defined by a prompt contract under `agents/`.

## 6. Artifact Contracts

All contracts are markdown. An instance must implement every contract below.

### 6.1 Inbox (`inbox/<date>`)

Each captured item: timestamp; source (`voice` / `manual` / `import`); raw text;
optional tags.

### 6.2 Daily Brief (`today/<date>`)

Required sections, in order: Top 3 priorities; Completed processing; Review queue;
Blocked decisions; One forward action.

### 6.3 Blocked Decision (`decisions/<date>`)

Each blocked item: item id; reason blocked; confidence score; options (minimum 2);
recommended option; decision owner; due date.

### 6.4 Asset Census (`assets/census`)

Columns: asset; status (`active` / `maintenance` / `archive`); risk; next action;
owner; review date.

> "Asset" generalizes to whatever you track: code repositories, services,
> dashboards, runbooks, documents. Keep the columns; change the noun.

## 7. Operating Schema

### 7.1 Categories

`idea`, `question`, `task`, `essay`, `asset`, `personal`, `work`, `finance`,
`research`, `archive`.

Instances may rename or extend categories but must keep `archive` and `task`.

### 7.2 Confidence Rubric (required)

Score every routed item with the same five factors. Total = sum (0-100).

| Factor | Question | Score |
|---|---|---|
| Intent clarity | Is the request unambiguous? | 0-20 |
| Context sufficiency | Is enough context available to act safely? | 0-20 |
| Artifact determinism | Is the output format clearly defined? | 0-20 |
| Risk sensitivity | Could this affect legal, money, or sensitive relationships? | 0-20 |
| Reversibility | Can the result be undone cheaply if wrong? | 0-20 |

### 7.3 Routing Policy

- `>= 90` — auto-process and log in completion summary.
- `70-89` — process and place in review queue.
- `< 70` — escalate as a blocked decision.

### 7.4 Interruption Policy

A role may interrupt the operator only for: legal risk; money risk; sensitive
relationship issue; publishing approval; confidence below threshold. Everything
else proceeds without interruption.

## 8. Cadence

### 8.1 Daily

- Morning (~10 min): run Chief of Staff over inbox, produce daily brief.
- Midday (~5 min): append captures.
- Evening (~10 min): close loop, process remainder, log blocked decisions.

### 8.2 Weekly

1. review all blocked decisions
2. review census and stale items
3. select top 5 synthesized ideas from the week
4. archive low-value residue
5. set next-week operating focus

## 9. Adoption Phases

| Phase | Goal | Exit Condition |
|---|---|---|
| 0 — Prompt-only MVP | Prove flow with no build | 7 consecutive days of inbox processing + 1 daily brief/day |
| 1 — Light automation | Reduce friction | voice→inbox < 2 min; weekly digest < 5 min; daily session < 20 min |
| 2 — Orchestration | One-entry triage | one prompt runs full daily triage; escalations carry options |
| 3 — Stability | Boring reliability | < 5% artifacts need major rewrite; no duplicate daily files |

Do not start a phase before the previous phase's exit condition holds.

## 10. Instantiation Protocol

To stand up a new instance:

1. **Pick a private root** (a gitignored `instance/` folder, or a separate private repo).
2. **Create the folders:** `inbox/`, `today/`, `agents/`, `domains/`, `assets/`,
   `decisions/`, `archive/` (add `essays/` only if publishing applies).
3. **Copy the six role prompts** into `agents/`. Edit only the *nouns*.
4. **Localize the schema:** adjust categories and the census noun to the context.
5. **Keep the contracts identical** — same confidence rubric, routing policy, and
   daily-brief sections. Portability depends on this.
6. **Run Phase 0 manually** for 7 days before automating anything.

### 10.1 What stays fixed vs. what changes

| Stays fixed (the method) | Changes per instance (the content) |
|---|---|
| Core loop, role roster, artifact contracts | Category names, census noun |
| Confidence rubric, routing policy | Decision owners, escalation contacts |
| Daily/weekly cadence, phase gates | Sensitivity rules, what counts as "risk" |

## 11. Failure Modes

| Failure Mode | Description | Corrective Action |
|---|---|---|
| Babysitting return | Operator re-checks every step | Enforce interruption + routing policy |
| Over-engineering | Building before using | Hold Phase 0 prompt-only first |
| Role sprawl | Too many specialists | Cap at six until boring |
| File entropy | Duplicate/scattered artifacts | One artifact per role + weekly archive sweep |
| Capture gap | Days with no inbox | Allow minimum-viable-day (capture only) |
| Leakage | Sensitive content exposed | Private instance root, no auto-publish path |

## 12. Metrics

- Throughput: inbox-zero within 24h (target ≥ 80% of days); daily top-3 produced
  (target 100% of workdays); weekly synthesis (target 1/week).
- Quality: artifact acceptance without heavy rewrite; duplicate-note reduction;
  decision latency for blocked items.
- Experience: reduced evening triage time; more voice ideas converted to durable
  outputs.

**Last Updated:** 2026-06-25

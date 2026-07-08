# ADR-0001 — The Labs Architecture (Architectural Directive 0001)

**Status:** Accepted (v0.1 seed) · **Date:** 2026-07-07 · **Supersedes:** — ·
**Full spec:** [`../../spec/complexence-labs.md`](../../spec/complexence-labs.md)

This ADR is the terse, citable statement of the v2 direction. The reasoning,
diagrams, and the measurement detail live in the labs spec; this file is what an
agent or a contributor reads to know the rule.

---

## Context

The v1 stack ships a method (capability + OS) and a theory
([science](../../spec/complexence-science.md)) but leaves two gaps: there is no
structured path from daily work to the research program, and the method is *read and
applied* rather than *installed*. A naive fix — letting the public repo accumulate
real notes and results — would leak private work and turn a reference implementation
into a notebook. The decision below avoids that.

## Decision

Complexence OS is a **substrate-independent operating system for engineering
orientation**. It does not store domain knowledge. It defines the grammar by which
adaptive systems are observed, measured, organized, and improved. It is governed by
six principles.

**1. Separate runtime from knowledge.** The public repo contains methods, schemas,
roles, templates, and operators. Domain repositories contain data, code, experiments,
and decisions. These never mix.

**2. Install, don't copy.** Every repository *installs* the runtime via a
`.complexence/` scaffold rather than forking a customized copy. Runtime corrections
propagate through versioned releases; each lab keeps its own data.

**3. Role-based orchestration.** Every repository is managed by one or more installed
roles. The `chief-of-staff` is universal; a domain chief is the same router contract
with its nouns localized (the six-role cap of the OS spec stands). Roles orchestrate
workflow; they do not own domain knowledge.

**4. Laboratories are isolated.** Every project is its own lab. No private or
proprietary information is ever synchronized into the public runtime. The boundary is
the Abstraction step of the publishing pipeline.

**5. Publish only abstractions.** Only generalized operators, schemas, definitions,
ADRs, and validated methods may move from a private lab into the public repo. Raw
observations, implementations, and personal records stay permanently private.

**6. Research before documentation.** Every significant observation begins as an
experiment. Repeated evidence produces definitions; stable definitions produce
operators; operators produce architecture; architecture becomes Complexence OS.

**Canonical flow:**

```text
Observe → Experiment → Measure → Pattern → Definition → Operator → Role → Runtime
```

## Consequences

- The public repo gains: this ADR, [`RESEARCH.md`](../../RESEARCH.md) (typed-ID index),
  the [`install/`](../../install/) scaffold + [`complexence-install.sh`](../../scripts/complexence-install.sh),
  and the labs/measurement spec. The **lab roster and role assignments are private** —
  naming which projects are labs is itself lab knowledge (Principle 4).
- Measurement is subordinate to honesty: the orientation objective and the Λ measure
  (labs spec §2, §6) are **candidate** instruments, not validated results, held to the
  same rules as `complexence-science.md` §1a.
- The risk this directive most has to manage is **over-engineering the install before
  the method is validated** (labs spec §8.1). Bias toward the thinnest scaffold that
  produces usable orientation data.

## Success criterion

Complexence succeeds when any new repository can install the runtime, select
appropriate roles, and immediately begin increasing orientation — **without exposing
any domain-specific knowledge**.

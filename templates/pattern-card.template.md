# Pattern Card — <abstracted pattern name>

> The one artifact that crosses the public boundary. A pattern card is a **sanitized
> abstraction** of a result seen in a private lab: domain knowledge stripped, only
> structure kept (labs spec §7). This template is public; a *filled* card is only
> safe to publish after a leakage review against [`../GUARDRAILS.md`](../GUARDRAILS.md).

**Proposed by:** <lab role, not lab name> · **Date:** <YYYY-MM-DD>
**Promotes to:** <O-NNN new operator | D-NNN definition revision | L-NNN evidence | ADR>

## The pattern (domain-free)

<State the recurring structure in substrate-independent terms. If a real noun
(project, client, tool, metric value) is needed to state it, it is not abstract
enough yet — keep it in the lab.>

## Evidence it recurs

- Seen in **≥ 3 distinct contexts** (required for operator promotion, labs §7).
- Contexts (described structurally, never named): <context 1>, <context 2>, <context 3>.
- Orientation effect: <direction and rough magnitude, ordinal — labs §6.2>.

## What it would change in the public repo

<The specific edit: a new O-NNN in RESEARCH.md + src/, a revised D-NNN, an L-NNN this
supports/contradicts. Reference the ids.>

## Leakage review

- [ ] No real names, employers, clients, or project codenames.
- [ ] No proprietary methods or numbers.
- [ ] Statement holds without any of the lab's domain nouns.
- [ ] `./scripts/check-no-secrets.sh` clean on the resulting diff.

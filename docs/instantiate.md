# Stand up your own instance

An *instance* is one deployment of Complexence OS for a specific context — your
personal life, a team at work, a single project. The method stays the same; only
the content changes.

## Steps

1. **Pick a private root.** Either use the gitignored `instance/` folder in this
   clone, or — better for work — create a **separate private repository**. Never
   put instance data in this public repo.

2. **Create the folders:**
   ```text
   inbox/ today/ agents/ domains/ assets/ decisions/ archive/
   ```
   Add `essays/` only if you'll draft documents.

3. **Copy the six role prompts** from `agents/` into your instance. Edit only the
   *nouns* — what an "asset" is, which categories matter, who owns decisions.

4. **Localize the schema.** Adjust categories and the census noun to your context.
   At work, "asset" might mean services, dashboards, or runbooks.

5. **Keep the contracts identical.** Same confidence rubric, same routing policy,
   same five daily-brief sections. This is what makes your instance portable and
   comparable across contexts.

6. **Run Phase 0 manually** for seven days before automating anything.

## What stays fixed vs. what changes

| Stays fixed (the method) | Changes per instance (the content) |
|---|---|
| Core loop, role roster, artifact contracts | Category names, census noun |
| Confidence rubric, routing policy | Decision owners, escalation contacts |
| Daily/weekly cadence, phase gates | Sensitivity rules, what counts as "risk" |

## Adoption phases

These phases are how you **climb the layers** ([`layers.md`](./layers.md)) in your
own area — by hand, by typing, one rung at a time. Don't automate a rung you
haven't first run manually.

| Phase | Goal | Exit condition |
|---|---|---|
| 0 — Prompt-only MVP | Prove the flow with no build | 7 straight days of inbox processing + 1 brief/day |
| 1 — Light automation | Reduce friction | voice→inbox < 2 min; daily session < 20 min |
| 2 — Orchestration | One-entry triage | one prompt runs full triage; escalations carry options |
| 3 — Stability | Boring reliability | < 5% artifacts need major rewrite; no duplicate files |

Don't start a phase before the previous phase's exit condition holds.

## A note for work instances

If you deploy this at work, the guardrails matter even more. Keep the work instance
in a **private** repository your employer's policies allow, route decision
ownership and escalation contacts to real roles, and define "risk sensitivity"
against your actual legal/compliance context before you trust auto-processing.

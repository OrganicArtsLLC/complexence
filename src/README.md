# src — reference implementation (Phase 1)

The first runnable pieces of the science (see [`../ROADMAP.md`](../ROADMAP.md)).

- `cognitive-form.schema.json` — the canonical interchange format for a Cognitive Form
  (`ℭ = (I, R, T, F, H)`), instantiating Theory B of
  [`../spec/complexence-science.md`](../spec/complexence-science.md) §7. MIT-licensed.

This is a **candidate** format. The projection logic that decides whether two
representations are the same `ℭ` is unproven (the open isomorphism, science §10).

## Validation (the compliance check)

The schema is not just a format — it is the **active check** that closes the loop.
Validating a produced artifact against `cognitive-form.schema.json` is the
*compliance* step of the method: it confirms a form carries its invariant,
representations, transformations, feedback, and history before it is trusted
downstream. This is the machine half of what the **Critic** role
([`../agents/critic.prompt.md`](../agents/critic.prompt.md)) does by judgment — the
two together are governance (Chief of Staff routes) → execution (specialists
produce) → compliance (schema + Critic validate). Wire it as a step, not a new
layer: `validate(artifact) against ℭ-schema` before `execute(ℭ)`.

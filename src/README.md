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

## Operators — `cognitive_form.py`

A v0.1 reference implementation that turns the schema into runnable transforms.
Stdlib-only; schema validation uses `jsonschema` if installed, else a structural check.

- **Deterministic operators (real):** `validate` (the compliance check), `compose`,
  `reflect` (ℭ operating on its own structure), and the mechanical management of
  representations, transformations, feedback, and history.
- **Semantic operators (model-backed interfaces):** `project`, `translate`, `compress`,
  `expand`, `execute`, `correct`. Each delegates the meaning-bearing step to a
  caller-supplied `transform` callable (an LLM or other model) and then calls
  `invariant_preserved(...)` — a **stub**, because deciding whether two representations
  are the same `ℭ` is the open isomorphism (science §10). The hook is where that
  research plugs in; it is not pretended-solved.

```bash
python cognitive_form.py validate example.cform.json   # the compliance check
python cognitive_form.py reflect  example.cform.json   # ℭ describing itself
```

`example.cform.json` is a worked instance (complexence as a Cognitive Form, fittingly
recursive). Next on the ROADMAP: real `invariant_preserved` checks, then the
measurement harness that tests meaning velocity.

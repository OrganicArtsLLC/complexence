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
recursive).

## Demo — operators with a real model (`demo.py`)

`demo.py` runs the loop end-to-end against a live model (the local `claude` CLI as
one swappable adapter): it **projects** the invariant into a metaphor, **translates**
that into pseudocode, then runs a **round-trip invariant check** — reconstruct the
core idea from a representation alone and ask the model whether the meaning survived.
That is a first *real* `invariant_preserved` (a model's judgment, not a proof, but
runnable), the Phase-2 measurement-harness seed. It also times each transform as a
meaning-velocity proxy (§9.3).

```bash
python demo.py            # needs a model adapter on PATH (claude CLI by default)
```

A sample run: `project -> metaphor`, `translate -> pseudocode`, `invariant round-trip
= preserved (YES)`, 3 transforms in ~30s. The central claim — *meaning is what
survives transformation* — run end-to-end and judged by a model, once. Not proof;
motion.

## Central-bet experiment — `experiment.py`

A first falsifiable cut at the central bet (§9.1 / §9.4): does coordinating through a
shared Cognitive Form beat passing independent text? An N-hop relay runs under two
conditions — **A** (the invariant is re-pinned every hop) vs. **B** (telephone: each
agent sees only the previous text) — then both are scored for semantic drift against
the original invariant (median of three model judges).

```bash
python experiment.py --hops 3 --trials 3
```

**First result is an honest null.** An early run looked like evidence *for* the bet;
it was a scorer artifact (single-judge variance + parse failures defaulting to 0).
With a hardened scorer the conditions tie inside noise (`A 6.3` vs `B 6.7`, delta
−0.3). The finding matches what science §10.5 predicts in advance: *measurability is
the whole bet* — at a toy 3-hop task both conditions preserve intent, so there is
nothing for a shared form to save. See [`../ROADMAP.md`](../ROADMAP.md) for the full
write-up and the Phase-3 plan (harder task, more hops/agents, calibrated judge).

## Lossy-channel experiment — `experiment_v2.py`

v0.2 isolates the variable the v0.1 null pointed at: the channel. The same relay,
but the text passed between hops goes through word-dropout at rate `p`; condition A
re-pins the full invariant clean at every hop, B gets only the degraded previous
text. Fidelity is triangulated three ways (per-claim rubric, reconstruction, holistic
judge). The docstring carries a pre-registered prediction, written before the run;
the run artifacts are gitignored, so the ordering is stated, not provable from git
history.

```bash
python experiment_v2.py --hops 5 --trials 2 --noise 0.0,0.6
```

**The first v0.2 run was invalid, and its raw direction went against the prediction.**
At p=0.6 the adapter returned API-refusal text, refusal text flowed through the relay
and into the judges, and one pure refusal was scored rubric 1.0. The raw rubric deltas
(A−B −0.12 at p=0.0, −0.38 at p=0.6) ran opposite the pre-registered signature — but
the contamination means this is an invalid run whose direction happened to be adverse,
not clean evidence against the bet. The harness now raises on adapter errors,
invalidates (rather than scores) refusal outputs, and reports a per-cell validity
rate; a clean re-run is the open next step. Full write-up in
[`../ROADMAP.md`](../ROADMAP.md).

# install/ — the Complexence runtime scaffold

The reference source for `complexence install`. Running
[`../scripts/complexence-install.sh`](../scripts/complexence-install.sh) inside a
project copies these templates into a `.complexence/` directory, turning that repo
into a **lab** (see [`../spec/complexence-labs.md`](../spec/complexence-labs.md) §4).

These files are **blank templates** — grammar, not knowledge. They are safe to be
public. The `.complexence/` they generate, once filled in, is **private lab data**
and must live in a private repo, never in this public one. The installer refuses to
run against the public Complexence repo itself for exactly this reason.

## What gets installed

```text
.complexence/
    charter.md              # from charter.template.md — why this repo exists
    operating-principles.md # from operating-principles.template.md
    roles/                  # role prompts copied from ../agents/ (you pick which)
    experiments/            # EXP-NNN.md — one per experiment (private)
    metrics/                # orientation-log.md and any measures this lab tracks
    schemas/                # experiment.schema.json, copied for local validation
    prompts/                # session prompts
    summaries/              # generated weekly summaries
    .gitignore              # keeps the scaffold, ignores nothing by default*
```

\* In a **private** lab repo you commit the whole `.complexence/`. The generated
`.gitignore` is a placeholder; adjust it to your lab's privacy needs.

## Deliberately thin

Open question `RQ-007` (labs §8.1): *how thin can the install be and still produce
useful orientation data?* The bias is toward under-building. Start with a charter, one
role, and the orientation log; add experiments and schemas only when a real question
needs them.

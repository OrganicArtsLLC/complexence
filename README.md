# Complexence OS

**An operating method that turns raw thought into durable, structured artifacts
using a small set of agent roles, prompts, and blank templates.**

You capture a thought — **by typing or by speaking**. One router agent — a *Chief
of Staff* — sorts it into a short daily brief and hands the rest to specialist
roles. You review only the exceptions.

```text
a thought in  ->  one router  ->  specialist roles  ->  durable artifacts  ->  weekly review
```

> **New here? Start by typing.** Voice capture is one optional door, not a
> requirement — it removes desk friction once you're fluent, but typing is the
> clearer way to *learn* what this is, because you watch exactly what goes in.
> Open a chat, paste one prompt, point it at a few typed lines. That's the whole
> first rung.

> ⚠️ **This repo is public, and git history is permanent.** It contains the method
> only — spec, role prompts, and *blank* templates. Your real captures and outputs
> are private data and must never be committed here. **Read [GUARDRAILS.md](./GUARDRAILS.md)
> before you commit anything.**

---

## What this is

Complexence OS is the operating layer of a larger idea — *Complexence*, the
capability of staying oriented inside complex systems and converting that
orientation into coherent action. This repo is the part you can run today: a
lightweight, prompt-driven workflow that works with any capable AI assistant and
plain markdown files. No app to install, no service to run.

It is designed for people whose bottleneck is not *having* ideas but *capturing
and structuring* them without long desk hours.

## How it works

- **Capture** by typing (or speaking) into a dated inbox file.
- **Route** the whole inbox through one Chief of Staff prompt.
- **Produce** artifacts via a capped set of roles (six to start: one router plus five specialists).
- **Review** only a five-section daily brief — mostly just blockers.
- **Govern** weekly: resolve decisions, synthesize, archive, set focus.

The full method is specified in **[`spec/complexence-os.md`](./spec/complexence-os.md)**.

## What you're actually building (the layers)

Under the workflow is a ladder of **cognitive orchestration** — each rung moves a
piece of your thinking out of your head and into a durable, inspectable system:

```text
Layer 0   nothing                 it all lives in your head
Layer 1   a prompt.md             one reusable thinking contract
Layer 2   prompts in a hierarchy  a small team of contracts, each owning one job
Layer 3   agents that run them    contracts that execute over your data
Layer 4   a runner of agents      one orchestrator that routes the others (Chief of Staff)
```

Each step up is the same move: take something you were doing ad hoc and externalize
it into something stable enough to delegate. You climb deliberately, by hand, and
**stop at whatever rung is paying off** — most of the leverage is in Layers 1–2,
which you reach by typing, today. Read the full walk-through in
**[`docs/layers.md`](./docs/layers.md)**.

## Quickstart (manual, ~10 minutes)

1. Read [`docs/START-HERE.md`](./docs/START-HERE.md).
2. Create your private working area: `mkdir instance` (it's gitignored).
3. Copy `templates/inbox.template.md` to `instance/inbox/YYYY-MM-DD.md` and dump
   a few thoughts into it.
4. Open a fresh AI chat, paste the Chief of Staff prompt from
   [`agents/chief-of-staff.prompt.md`](./agents/chief-of-staff.prompt.md), and
   point it at your inbox file.
5. Read the daily brief it produces. Look at *Top 3* and *Blocked decisions* only.

That's a complete day. Everything else is optional refinement.

## Repository layout

```text
spec/         the method specification (start here for the full model)
agents/       role prompt contracts (Chief of Staff + 5 specialists)
templates/    blank, shareable templates for each artifact type
docs/         START-HERE, instantiation, and automation (capture→triage→feedback) guides
scripts/      helper + the pre-commit secret guard
instance/     YOUR private data — gitignored, never committed (you create this)
```

## Standing up your own instance

See [`docs/instantiate.md`](./docs/instantiate.md). The short version: copy the
templates and role prompts, change only the *nouns* (your categories, what an
"asset" is, who owns decisions), keep the contracts identical, and run it manually
for a week before automating anything.

## Status & scope

This repo is a **seed**, not the system. It deliberately ships the *method* — the
spec, the contracts (`agents/`), and *blank* templates — and nothing else. **Your
instance is the system**, and it lives in **your own private area**: the gitignored
`instance/` folder here, or — better — a separate private repository. Every real
thought, brief, decision, and asset stays there; this repo only ever holds the
shape.

> The seed is the method. Your repo is the system. Your data never leaves your area.

Adapt it freely. The contracts (confidence rubric, routing policy, daily-brief
sections) are the part worth keeping stable — they are what make an instance
portable across contexts.

## License

Dual-licensed, by content type:

- **The method and documentation** (everything except `scripts/`) — Creative
  Commons Attribution 4.0 International (**CC BY 4.0**). You may share and adapt it,
  including commercially, **with attribution**. See [LICENSE](./LICENSE).
- **The code** (`scripts/`) — **MIT License**. See [scripts/LICENSE](./scripts/LICENSE).

Copyright © 2026 Organic Arts LLC.

**Attribution:** "Complexence OS by Organic Arts LLC, licensed under CC BY 4.0,"
linking back to this repository.

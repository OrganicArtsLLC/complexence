# Complexence

**Complexence is a word I made up for something specific: staying oriented inside
a system too big to hold in your head — a codebase, a job, a life — and turning
that orientation into action you'd stand behind.** This repo holds the map of
that capability, the working method I run it with, and the early, unproven
science underneath. One word, three layers of depth, one versioned repo.

This repo is the canonical, open home of the whole stack:

| Layer | What it is | Spec |
|---|---|---|
| **Capability** | orienting and navigating under load (an eight-level orientation map, L0–L7: from "what's in scope" to "what did we learn") | [`spec/complexence-capability.md`](./spec/complexence-capability.md) |
| **Operating method** | turn raw thought into durable artifacts with a few agent roles — *runnable today* (below) | [`spec/complexence-os.md`](./spec/complexence-os.md) |
| **Foundation** | the formal science underneath: what has to exist before thinking can (an ontology), the loop it runs (one recursive equation), and the one number that matters — how fast useful meaning moves (meaning velocity) | [`spec/complexence-science.md`](./spec/complexence-science.md) |
| **Labs & measurement** | the v2 applied layer: install the method as isolated *labs*, measure orientation, and promote only sanitized abstractions back up | [`spec/complexence-labs.md`](./spec/complexence-labs.md) |

Narrative versions live on the blog: [Complexence](https://joshuaayson.com/2026/06/17/complexence/)
(capability), [Complexence OS](https://joshuaayson.com/2026/06/25/complexence-os/)
(method), [The Science of Complexence](https://joshuaayson.com/2026/06/28/science-of-complexence/)
(foundation). The science is an **open research program**; its edges and direction
live in [`ROADMAP.md`](./ROADMAP.md).

---

## What you can run today: Complexence OS

You capture a thought, **typed or spoken**. One router agent (a *Chief of Staff*)
sorts it into a short daily brief and hands the rest to specialist roles. You
review only the exceptions.

```text
a thought in  ->  one router  ->  specialist roles  ->  durable artifacts  ->  weekly review
```

> **New here? Start by typing.** Voice capture is one optional door, not a
> requirement. It removes desk friction once you're fluent, but typing is the
> clearer way to *learn* what this is, because you watch exactly what goes in.
> Open a chat, paste one prompt, point it at a few typed lines. That's the whole
> first rung.

> ⚠️ **This repo is public, and git history is permanent.** It holds the *public
> stack* — the specs (capability, method, and the science), the role prompts, and
> *blank* templates. All of that is meant to be public. What must **never** be
> committed here is **your** private data: your real captures, outputs, and filled-in
> instance. **Read [GUARDRAILS.md](./GUARDRAILS.md) before you commit anything.**

---

## What this is

Complexence OS is the operating layer of a larger idea, *Complexence*: the
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
- **Review** only a five-section daily brief, mostly just blockers.
- **Govern** weekly: resolve decisions, synthesize, archive, set focus.

The full method is specified in **[`spec/complexence-os.md`](./spec/complexence-os.md)**.

## What you're actually building (the layers)

Under the workflow is a ladder of **cognitive orchestration**: each rung moves a
piece of your thinking out of your head and into a durable, inspectable system.

```text
Layer 0   nothing                 it all lives in your head
Layer 1   a prompt.md             one reusable thinking contract
Layer 2   prompts in a hierarchy  a small team of contracts, each owning one job
Layer 3   agents that run them    contracts that execute over your data
Layer 4   a runner of agents      one orchestrator that routes the others (Chief of Staff)
```

Each step up is the same move: take something you were doing ad hoc and externalize
it into something stable enough to delegate. You climb deliberately, by hand, and
**stop at whatever rung is paying off**. Most of the payoff is in Layers 1–2,
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

## Fastest start — let an agent unpack it (VS Code Copilot, Claude, Cursor)

Prefer not to wire it up by hand? Paste this into a capable AI agent **inside your
private working repo**. It sets your privacy guardrails first, asks for your
context (it does *not* assume it already knows it), then generates your folders and
your re-runnable `/complexence-*` prompts, customized to you. This is the seed
"unpacking itself" into your own area.

~~~text
Stand up a private Complexence OS instance (github.com/OrganicArtsLLC/complexence)
in THIS repo, which is my private area. Phases, in order:

1) GUARDRAILS first: confirm this repo is private (else stop and ask); ask me what
   is sensitive in my context and record it as a denylist; for routine work use
   file edits only (no shell/network/sends), and keep outward actions as separate
   steps I approve. Never write anything that identifies a real person/employer/
   client into a file that could become public.
2) GATHER (ask, don't guess): my context (personal/work/project); my categories and
   what "asset" means to me; who owns decisions and what counts as "risk"; my
   writing voice.
3) BUILD in my area: folders inbox/ today/ decisions/ domains/ assets/ archive/
   (+ essays/); .github/copilot-instructions.md from the seed's
   editors/copilot/copilot-instructions.template.md (method + my schema +
   guardrails, so it is always in context); and re-runnable prompt files in
   .github/prompts/ — complexence-capture, -triage, -census, -map, -draft, -review
   — based on editors/copilot/prompts/ and agents/. Keep the fixed contracts
   identical (confidence rubric, routing >=90/70-89/<70, the five daily-brief
   sections); change only the nouns.
4) EXPLAIN as you go which layer each piece is (docs/layers.md), then tell me to
   enable "chat.promptFiles" in VS Code and try /complexence-capture then
   /complexence-triage.

This repo is a seed; I am the system; my data stays here. Change nouns, keep method.
~~~

Annotated version + what it produces: [`docs/bootstrap.md`](./docs/bootstrap.md).
Drop-in files to copy by hand instead: [`editors/copilot/`](./editors/copilot/).

## Repository layout

```text
spec/         the specifications: capability, os, science, and labs (start here)
RESEARCH.md   the navigation layer — open research questions + typed-ID registry
agents/       role prompt contracts (Chief of Staff + 5 specialists)
editors/      drop-in editor integrations (VS Code Copilot prompt files + instructions)
templates/    blank, shareable templates for each artifact type (incl. pattern card)
install/      the .complexence/ runtime scaffold that `complexence install` copies
docs/         START-HERE, layers, bootstrap, instantiation, automation; adr/ decisions
src/          the science's reference implementation: Cognitive Form schema,
              operators, demo, and the falsifiable experiments (MIT)
proofs/       candidate derivations for the science's claimed bounds
scripts/      helper scripts, the pre-commit secret guard, and complexence-install.sh
instance/     YOUR private data — gitignored, never committed (you create this)
```

### v2: the labs architecture

Complexence is growing from a personal method into an **installable, measurable
runtime**. Any repo can `./scripts/complexence-install.sh` a thin `.complexence/`
scaffold and become a *lab*: it runs the roles, measures orientation, and promotes
only **sanitized abstractions** back to this public repo — never raw data. The public
repo is grammar; labs are knowledge; the flow between them is one-way. A lab
*composes with* the instance model above (your instance is simply the first lab); it
does not replace it. The full
design is [`spec/complexence-labs.md`](./spec/complexence-labs.md), decided in
[`docs/adr/ADR-0001-labs-architecture.md`](./docs/adr/ADR-0001-labs-architecture.md),
and the live questions are indexed in [`RESEARCH.md`](./RESEARCH.md).

## Standing up your own instance

See [`docs/instantiate.md`](./docs/instantiate.md). The short version: copy the
templates and role prompts, change only the *nouns* (your categories, what an
"asset" is, who owns decisions), keep the contracts identical, and run it manually
for a week before automating anything.

## Status & scope

This repo is a **seed**, not the system. It deliberately ships the *method* (the
specs, the contracts in `agents/`, blank templates) plus the science's early
artifacts (`src/`, `proofs/`) — and nothing private, nothing filled in. **Your
instance is the system**, and it lives in **your own private area**: the gitignored
`instance/` folder here, or (better) a separate private repository. Every real
thought, brief, decision, and asset stays there; this repo only ever holds the
shape.

> The seed is the method. Your repo is the system. Your data never leaves your area.

Adapt it freely. The contracts (confidence rubric, routing policy, daily-brief
sections) are the part worth keeping stable; they are what make an instance
portable across contexts.

## License

Dual-licensed, by content type:

- **The method and documentation** (everything except the code directories) —
  Creative Commons Attribution 4.0 International (**CC BY 4.0**). You may share and
  adapt it, including commercially, **with attribution**. See [LICENSE](./LICENSE).
- **The code** (`scripts/`, `src/`) — **MIT License**. See
  [scripts/LICENSE](./scripts/LICENSE) and [src/LICENSE](./src/LICENSE).

Copyright © 2026 Organic Arts LLC.

**Attribution:** "Complexence OS by Organic Arts LLC, licensed under CC BY 4.0,"
linking back to this repository.

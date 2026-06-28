# Bootstrap — let an agent unpack the system for you

Complexence OS is a seed. You *can* copy the templates and role prompts by hand
([`instantiate.md`](./instantiate.md)). Or you can paste **one prompt** into a
capable AI agent — VS Code Copilot **agent mode**, Claude Code, Cursor — and have
it stand up your instance: guardrails first, then your folders, then your
re-runnable `/complexence-*` prompts, all customized to your context.

The prompt is written to **ask you** what it needs rather than assume it's already
in context. That matters: a fresh agent may not know your categories, what's
sensitive, or where your private repo is. The bootstrap gathers that *before* it
writes anything — so you don't have to remember to load it yourself.

> Run this **in your private working repo** (or a gitignored `instance/` folder),
> never in a public clone. It writes real, possibly sensitive structure.

## The prompt

Copy the whole block into your agent, in agent (or edit) mode:

~~~text
Stand up a private Complexence OS instance (github.com/OrganicArtsLLC/complexence)
in THIS repository, which is my private working area. Work in phases; do not skip
the guardrails phase.

PHASE 1 — GUARDRAILS (before writing anything):
1. Confirm this repo is private, OR that we are working inside a gitignored
   `instance/` folder. If you cannot confirm it is private, STOP and ask me.
2. Ask me what is sensitive in my context (employer, clients, people, financial,
   legal, health, internal URLs / credentials). Record these as a private denylist.
3. State the rule you will follow: method and structure can be generic, but nothing
   that identifies a real person / employer / client goes into any file that could
   become public. For routine work you will use file edits only — no shell, no
   network, no sends — and outward or irreversible actions are separate steps I
   approve.

PHASE 2 — GATHER (ask me; do not guess):
- Context: personal, a team at work, or a single project?
- The categories I capture, and what "asset" means for me (services? dashboards?
  runbooks? repos? documents?).
- Who owns decisions and escalation, and what counts as "risk" for me.
- A line or two describing my writing voice (for drafts).

PHASE 3 — BUILD (in my private area, showing me each file as you go):
1. Create folders: inbox/ today/ decisions/ domains/ assets/ archive/ (+ essays/
   if I draft).
2. Write `.github/copilot-instructions.md` capturing the method, my localized
   schema, and my guardrails — so every future chat has this context and I never
   re-explain it. Base it on the seed's
   editors/copilot/copilot-instructions.template.md.
3. Generate re-runnable agentic prompt files under `.github/prompts/`, one per
   operation, localized to my nouns, based on the seed's editors/copilot/prompts/
   and the role contracts in agents/: complexence-capture, complexence-triage,
   complexence-census, complexence-map, complexence-draft, complexence-review.
4. KEEP THE FIXED CONTRACTS IDENTICAL: the confidence rubric (0-100 = five factors
   x 0-20), routing (>=90 auto / 70-89 review / <70 escalate), and the five
   daily-brief sections. Change only the nouns.

PHASE 4 — EXPLAIN & HAND OFF:
- As you build, tell me which layer each piece is (capture = Layer 1; the prompt
  files = Layers 2-3; a future script that runs them = Layer 4), per docs/layers.md.
- End by telling me to enable prompt files in VS Code ("chat.promptFiles": true)
  and to try /complexence-capture, then /complexence-triage.

Remember: this repo is a seed. I am the system; my data stays in my private area.
Change the nouns; keep the method.
~~~

## What you get

After it runs, your private repo has:

- `inbox/ today/ decisions/ domains/ assets/ archive/` folders
- `.github/copilot-instructions.md` — your method + guardrails, always in context
- `.github/prompts/complexence-*.prompt.md` — your re-runnable `/` commands

Then a day is: `/complexence-capture` a few times, `/complexence-triage` once, read
the brief. That is Layers 1–3 working by hand. Add a script later for Layer 4
([`automation.md`](./automation.md)).

## Why "unpack itself"

The seed ships the *shape*; the bootstrap reads that shape and writes *your*
instance from it. You learn the layers by watching them assemble, and you end with
prompts that are near-agents — one step (a script) away from fully automated. See
[`layers.md`](./layers.md) for what each rung means and
[`../editors/copilot/`](../editors/copilot/) for the drop-in files if you would
rather copy them by hand.

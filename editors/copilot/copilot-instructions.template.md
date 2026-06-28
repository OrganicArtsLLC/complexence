# Complexence OS — workspace instructions (TEMPLATE)

> Copy this to `.github/copilot-instructions.md` in your **private** working repo
> and fill in every `< ... >` placeholder. GitHub Copilot loads this file into
> every chat automatically, so the method and your guardrails are always in
> context — you never have to re-explain them, and a fresh chat can't lose them.
> This template ships **no private data**; the specifics are yours to add locally.

## What this workspace is

This repo is my private Complexence OS instance. I capture raw thoughts into a
dated inbox; a Chief of Staff triages them into one short daily brief; specialist
roles produce durable artifacts. The method comes from the public seed
(github.com/OrganicArtsLLC/complexence); my data lives only here.

## Guardrails (highest priority — never violate)

- This is my private area, but still never write anything that would identify a
  real person, employer, client, or sensitive number into a file that could ever
  become public. Method and structure can be generic; specifics stay here.
- Sensitive in my context (treat as a denylist): <e.g. employer name, client
  names, financials, legal matters, health, internal URLs / credentials>.
- For routine runs, use **file edits only** — read and write markdown in this repo.
  Do not run shell commands, push, send, or use the network unless I explicitly
  ask in that message.
- Outward or irreversible actions (publish, send, push, pay) are never automatic.
  They are a separate step I approve.

## My schema (localize these nouns — this is all that changes per instance)

- Context: <personal | a team at work | a single project>
- Categories I capture: <idea, question, task, essay, asset, personal, work,
  finance, research, archive — keep `task` and `archive`>
- "Asset" means: <services | dashboards | runbooks | repos | documents>
- Decision owners / escalation contacts: <roles>
- What counts as "risk" for me: <my legal / compliance / relationship sensitivity>
- My writing voice (for drafts): <one or two lines, or a link>

## Fixed contracts (do NOT change — these make the instance portable)

- **Confidence rubric:** 0-100 = sum of five factors (each 0-20): intent clarity,
  context sufficiency, artifact determinism, risk sensitivity, reversibility.
- **Routing:** `>=90` auto-process; `70-89` review queue; `<70` escalate as a
  blocked decision.
- **Daily brief sections, in order:** Top 3 priorities; Completed processing;
  Review queue; Blocked decisions; One forward action.
- **Inbox entries are write-once:** never change `raw:` (add a `clean:` line if
  tidying a transcript).

## Folders

`inbox/ today/ decisions/ domains/ assets/ archive/` (add `essays/` if I draft).

## Re-runnable prompts (in `.github/prompts/`, invoke with `/`)

- `/complexence-capture` — record a thought (Layer 1)
- `/complexence-triage` — Chief of Staff: inbox → daily brief
- `/complexence-census` — Asset Steward
- `/complexence-map` — Cartographer
- `/complexence-draft` — Publisher (draft only)
- `/complexence-review` — Critic

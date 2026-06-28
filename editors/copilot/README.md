# Complexence OS in VS Code (GitHub Copilot)

This turns the portable role contracts in [`../../agents/`](../../agents/) into
**re-runnable, agentic prompts** you invoke by name in Copilot Chat — e.g.
`/complexence-triage`. They are the method's Layers 2–3 made real in an editor:
named prompts (Layer 2) that run as agents over your files (Layer 3). See
[`../../docs/layers.md`](../../docs/layers.md).

## What's here

- `copilot-instructions.template.md` — workspace instructions Copilot auto-loads
  into every chat (the method + your guardrails + your localized schema), so the
  context is always present and you never re-explain it.
- `prompts/*.prompt.md` — one reusable prompt per operation: capture, triage,
  census, map, draft, review.

These are **generic templates** — no private data. You customize copies of them in
your own private repo.

## Install (in your PRIVATE working repo)

1. Copy `copilot-instructions.template.md` → `.github/copilot-instructions.md` and
   fill in the `< ... >` placeholders (your categories, what "asset" means, your
   guardrails / denylist, your voice).
2. Copy `prompts/` → `.github/prompts/`.
3. In VS Code, make sure prompt files are enabled (setting
   `"chat.promptFiles": true`; on by default in current builds).
4. Open Copilot Chat, switch to **agent** mode, type `/` — you'll see
   `/complexence-capture`, `/complexence-triage`, and the rest.

**Or skip the manual copy:** paste the bootstrap prompt from
[`../../docs/bootstrap.md`](../../docs/bootstrap.md) into Copilot agent mode and let
it generate all of this — customized to your context, after walking you through the
guardrails first.

## How the prompt files map to the role contracts

| Prompt | Role contract | Output |
|---|---|---|
| `/complexence-capture` | (capture) | one inbox entry |
| `/complexence-triage` | [chief-of-staff](../../agents/chief-of-staff.prompt.md) + [daily-brief](../../agents/daily-brief.prompt.md) | `today/<date>` brief |
| `/complexence-census` | [asset-steward](../../agents/asset-steward.prompt.md) | `assets/census` |
| `/complexence-map` | [cartographer](../../agents/cartographer.prompt.md) | `domains/<topic>/map` |
| `/complexence-draft` | [publisher](../../agents/publisher.prompt.md) | `essays/drafts/<slug>` |
| `/complexence-review` | [critic](../../agents/critic.prompt.md) | `essays/reviews/<slug>` |

The prompt files carry only the *specific job*. The shared method (categories,
confidence rubric, routing, brief sections, guardrails) lives once in
`.github/copilot-instructions.md` so it stays consistent across all of them — edit
the contracts in one place.

## Other editors

The same pattern works anywhere reusable prompts live — Cursor rules, Claude Code
slash-commands / subagents, JetBrains AI. Keep the fixed contracts identical;
change only the editor wrapper.

## The next layer: scripts

A prompt file is a near-agent you fire by hand. Wrap that invocation in a small
script — run on each new capture, or on a schedule — and you reach **Layer 4**: a
runner of agents. Keep it edit-only and gate every outward action. See
[`../../docs/automation.md`](../../docs/automation.md).

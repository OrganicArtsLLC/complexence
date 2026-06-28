---
mode: agent
description: 'Publisher: turn an idea into a draft document. Draft only, never publish.'
tools: ['codebase', 'editFiles']
---
# /complexence-draft

Turn an idea into a draft I could publish or circulate. You draft; you never
publish — publishing is always my explicit decision.

Idea or existing slug: ${input:idea:What should I draft? (an idea, or an existing slug)}

Inputs:
- the idea above, or a routed item tagged `essay` / `idea`
- any related map under `domains/`

Write `essays/drafts/<slug>.md` containing:
- a working title
- a one-line thesis
- the draft body (in my own voice — see `.github/copilot-instructions.md`)
- an open-questions list: what I must confirm before publishing

Rules:
- Never auto-publish and never include a publish step. Output a draft only.
- If the idea isn't ready, say so and list what's missing instead of padding.
- When the draft is ready for scrutiny, suggest I run `/complexence-review`.

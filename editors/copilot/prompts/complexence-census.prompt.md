---
mode: agent
description: 'Asset Steward: keep the asset census current — status, risk, next action.'
tools: ['codebase', 'editFiles']
---
# /complexence-census

Keep my tracked assets legible. "Asset" means whatever this instance tracks (see
`.github/copilot-instructions.md`).

Inputs:
- items tagged `asset` from today's triage, or the asset I name below
- the existing census at `assets/census.md`

Asset to update (blank = full sweep): ${input:asset:Asset to update (leave blank to sweep all)}

Maintain `assets/census.md` as one table:

| asset | status | risk | next action | owner | review date |
|---|---|---|---|---|---|

- **status** — `active`, `maintenance`, or `archive`
- **risk** — short phrase ("no owner", "stale 90d", "untested")
- **next action** — the single most useful move
- **review date** — when to look again

Rules:
- One row per asset; update in place, never duplicate.
- Flag any asset with no owner or no review date as a risk.
- End with a short "needs attention" list: the top stale or unowned assets.

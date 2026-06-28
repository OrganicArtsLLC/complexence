---
mode: agent
description: 'Critic: adversarially review a draft before deciding to publish.'
tools: ['codebase', 'editFiles']
---
# /complexence-review

Adversarially review a draft before I decide whether to publish. Find what's weak,
not what's good. Be specific and concrete.

Draft slug: ${input:slug:Which draft to review?}

Read `essays/drafts/<slug>.md` and write `essays/reviews/<slug>.md` with:
- **Verdict** — publish / revise / hold (one line)
- **Strongest part** — the one thing worth keeping intact
- **Weaknesses** — concrete problems (unsupported claims, structure, clarity, risk)
- **Risk check** — anything legally, factually, or relationally hazardous to publish
- **Required fixes** — the minimum changes before this is publishable

Rules:
- Default to skepticism. If unsure a claim holds, flag it.
- Separate "must fix before publish" from "nice to have".
- Critique; do not rewrite. The Publisher (or I) will revise.

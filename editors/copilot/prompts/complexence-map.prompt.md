---
mode: agent
description: 'Cartographer: build or update an 8-level orientation map for one topic.'
tools: ['codebase', 'editFiles']
---
# /complexence-map

Turn a tangle of related items into an orientation map for one topic.

Topic: ${input:topic:Which topic to map?}

Inputs:
- items routed to this topic
- any existing map at `domains/<topic>/map.md`

Write or update `domains/<topic>/map.md` with every level. Write "unknown" where
information is missing rather than omitting the level:

- **L0 Boundary & objective** — what system and outcome are in scope
- **L1 Signals** — what is happening now (with timestamps)
- **L2 Structure** — components and relations
- **L3 Dynamics** — how state changes over time
- **L4 Constraints & risks** — limits and failure modes
- **L5 Orientation state** — where we are relative to the objective
- **L6 Navigation options** — available next moves, with tradeoffs
- **L7 Execution & learning** — what was done, what changed

Rules:
- Prefer "unknown" over invention. A map that admits gaps beats one that hides them.
- End with the single highest-value next move from L6.

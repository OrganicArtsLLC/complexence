---
mode: agent
description: 'Record a raw thought into the current inbox. No processing.'
tools: ['codebase', 'editFiles']
---
# /complexence-capture

Append one new entry to today's inbox, then stop. Do not triage, classify, or act
on it — capture is just recording. This is Layer 1: get the thought out of my head.

Thought to capture: ${input:thought:What do you want to capture?}

Steps:
1. Determine today's date (YYYY-MM-DD). The inbox file is `inbox/<date>.md` in my
   private working area. If it does not exist, create it with the heading
   `# Inbox — <date>`.
2. Append a new entry in exactly this shape:
   ```
   ## Entry
   - timestamp: <ISO 8601 local time>
   - source: manual
   - raw: <the thought, verbatim — do not rewrite or summarize>
   - optional-tags:
   ```
3. Confirm in one line what you captured. Nothing else.

Rules:
- Never edit or reword existing entries. Capture is write-once.
- `raw:` is verbatim. If I rambled, keep it; triage cleans later.
- Do not run any other role. Respect the guardrails in
  `.github/copilot-instructions.md`.

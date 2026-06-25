# Automating the loop — capture, autonomous triage, feedback (safely)

This describes how to run Complexence OS closer to hands-off: capture by voice or
chat, let an agent triage new captures, and get status back in a chat channel —
**without an agent taking risky actions while you're not watching.**

It is method-level and instance-agnostic. Keep your instance (data, tokens,
personal specifics) private; only the pattern belongs in a public repo.

## The loop

```text
capture (voice memo / chat DM)
   -> transcribe (local) -> inbox entry
   -> [new captures] -> Chief of Staff triage run (headless agent)
   -> artifacts (brief, journal, queued decisions)
   -> feedback channel (chat): start / questions / completion
   -> you review only the exceptions and approvals
```

Two doors, one room: voice and chat both feed the **same inbox** and the **same
agent**. Use whichever fits the moment.

## Components

| Piece | Role | Notes |
|---|---|---|
| Capture source | voice memo and/or a chat DM | voice via an OS shortcut saving audio to a watched folder |
| Transcription | speech → text, **local** | a local model keeps capture private and offline |
| Watcher | a session-scoped loop that ingests new captures | plain automation; no intelligence |
| Triage run | an LLM agent invoked **headlessly** on new captures | this is the only "smart" step |
| Feedback channel | a chat (Slack/Discord/Telegram/…) the agent posts to | start, questions, completion; optionally two-way |

## What actually "runs the agent"

A background watcher/daemon is **dumb** automation — it does one deterministic
thing. The intelligent steps only happen when you **invoke the LLM**: a headless
agent run, fired per new capture or on a schedule. Nothing triages or acts on its
own unless you wire that invocation. Be deliberate about when it fires.

## Safety patterns (the important part)

1. **Edit-only autonomy.** Run the unattended triage agent with file tools only and
   the shell/network **denied**. It can read, draft, triage, and write your notes,
   but it physically cannot upload, push, pay, or send. The guarantee is structural,
   not a promise in a prompt.
2. **Gate every outward/irreversible action.** Publishing, payments, pushes, sends:
   route them through a *staging* step plus an explicit human approval. Build a
   deterministic, single-purpose script that can ONLY do the safe (e.g. private /
   draft) part; the agent may call that, but "go public" is a separate, manual step.
   Worst case unattended is then a private draft, never a public mistake.
3. **Feedback, not silence.** Report on activity start, when a decision or
   clarification is needed, and on completion. Let the agent compose its own status;
   let the dumb loop deliver it. Silence is how autonomy goes wrong unnoticed.
4. **Off by default + a kill switch.** Put autonomy behind explicit flags; make one
   command stop everything.
5. **Local-first capture.** Transcribe locally; keep raw captures and any private
   data out of every public surface.
6. **Debounce and budget.** Each agent run costs tokens. Fire on *new* input
   (debounced), not on every poll.

## Two-way chat (optional)

The feedback channel can also be an input: a chat message becomes a capture, the
agent runs, and its status returns as the reply. This makes one chat both your
command line and your readout. Restrict it to your own user id, and keep the same
edit-only / gated-outward rules.

## Minimal checklist to add this to your instance

- [ ] a watched capture folder + local transcription into `inbox/`
- [ ] a headless agent invocation over new captures (edit-only permissions)
- [ ] a chat notifier the loop calls on start / question / done
- [ ] a private-only staging script for any outward action; public = manual approve
- [ ] enable flags (default off) and a documented stop command

**Last Updated:** 2026-06-25

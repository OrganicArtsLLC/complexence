# The layers — what you're actually building

Complexence OS looks like a note-taking workflow. It isn't. It's a ladder of
**cognitive orchestration** — a sequence of abstractions, each one moving a piece
of your thinking out of your head and into a durable, inspectable system you can
read, version, and improve.

The point of this page is to make the ladder visible, because once you can see it
you can climb it deliberately — and you can stop at whatever rung is paying off.

You don't have to automate anything to get value here. Most of the leverage is in
the first two rungs, and you reach them by **typing**, today, in a chat window.

---

## The ladder

```text
Layer 0   nothing                 it all lives in your head
Layer 1   a prompt.md             one reusable thinking contract
Layer 2   prompts in a hierarchy  a small team of contracts, each owning one job
Layer 3   agents that run them    contracts that execute over your data
Layer 4   a runner of agents      one orchestrator that routes the others (Chief of Staff)
```

Each step up is the same move repeated: **take a unit of cognition you were doing
ad hoc, and externalize it into something stable enough to delegate.**

### Layer 0 — Nothing

You think, you decide, you act. Everything — the intent, the context, the
priorities, the follow-through — is held in working memory. This is infinitely
flexible and completely unscalable. Nothing is inspectable; nothing is repeatable;
the load is entirely on you, and it resets every morning.

This is the baseline. The rest of the ladder is about moving load off it.

### Layer 1 — A `prompt.md` (one contract)

You write down **one** repeatable thinking task as a plain-text contract: what it
takes in, what it does, what it produces. "Read my inbox, classify each entry,
tell me the top three things and what's blocked."

That's the first abstraction, and it's a big one. You've turned an act of
cognition into an **artifact** — something outside your head that is reusable,
editable, and shareable. Run it today, run it next week, hand it to someone else:
same contract, same shape of output. You can now improve *the thinking itself* by
editing a file, instead of trying to remember to think differently next time.

**This is where you start, and you start by typing.** Open a chat, paste one
prompt, point it at five lines you typed into a file. Feel that the leverage is
real before you build anything.

### Layer 2 — Prompts in a hierarchy (a small team of contracts)

One contract becomes a few, each owning exactly one job, organized so they
compose: a router that sorts, specialists that produce. This repo ships six
(`agents/`) — one Chief of Staff plus five specialists — capped on purpose.

This is **separation of concerns for thought**. The hierarchy *is* the structure
of your cognition made explicit: here is the part that triages, here is the part
that drafts, here is the part that tracks assets, here is the part that critiques.
When something feels muddy, you can point at exactly which contract owns it and fix
that one. You're no longer improving a vague habit; you're improving a named role.

### Layer 3 — Agents that run them

An **agent** is a `prompt.md` given a runtime: a capable AI assistant that
executes the contract over your actual data and writes the artifact. The contract
stops merely *describing* the work and starts *doing* it.

Nothing magic happens here, and that's important to internalize: the intelligence
is in the model, the *structure* is in your contract, and the agent is just the
two meeting over your inbox. You moved from "instructions I follow" to "instructions
that run." The better your Layer 1–2 contracts, the better this behaves — the
abstraction below is what makes the abstraction above worth having.

### Layer 4 — A runner of agents (the Chief of Staff)

One orchestrator sits above the specialists and decides **which agent runs on
what**, routes each item, escalates the genuinely uncertain ones, and composes
everything into a single short brief. You stop talking to five roles and talk to
one. You manage by exception.

This is **meta-cognition as a system**: an agent whose entire job is orchestrating
other agents. It's the same abstraction move one more time — the act of "deciding
what to think about next and who should handle it" was the last thing still living
only in your head, and now it's a contract too.

(Above this, optionally, the loop can become hands-off — captures trigger the
runner automatically and status comes back to you in a chat. That's
[`automation.md`](./automation.md), and it's strictly optional. Layer 4 is already
a complete system run by hand.)

---

## Why climbing matters

Each rung converts a piece of invisible, in-the-head work into something
**durable, inspectable, and improvable**:

- **Durable** — it survives the day. Your thinking doesn't reset; it accumulates.
- **Inspectable** — you can *read your own cognition* as files and see where it's
  weak. A bad brief points at a bad contract, not a bad mood.
- **Improvable** — you fix a system by editing text, then everything downstream
  inherits the fix. Leverage compounds.
- **Delegable** — anything contract-shaped can be handed to an agent, a teammate,
  or future-you, without re-explaining.

The goal isn't automation for its own sake. It's that you get to **see your own
thinking as a system** and refine it on purpose, instead of re-improvising it
every morning.

## How to actually use this

**Learn it by climbing one rung at a time, by hand, by typing.**

1. Live at **Layer 1** until it's boring. Type a few thoughts, run the Chief of
   Staff prompt over them, read the brief. Do it for a week
   ([`START-HERE.md`](./START-HERE.md), Phase 0 in [`instantiate.md`](./instantiate.md)).
2. Add **Layer 2** when one prompt is clearly doing several jobs — split it into
   the specialist roles in `agents/`.
3. Reach **Layer 3–4** when running the contracts by hand is reliable and the only
   thing left to remove is the friction of invoking them.
4. Only then consider **automation** (the optional loop). Don't automate a process
   you haven't run by hand — you'll just be scaling confusion.

Don't climb a rung until the one below it is dull and dependable. Most people get
enormous value and never leave Layer 1–2. That's a success, not a shortfall.

## Where this lives: a seed, and your own area

This repo is a **seed** — the method, the contracts (`agents/`), and *blank*
templates. It is not the system; **your instance is the system**, and it lives in
**your own private area**: the gitignored `instance/` folder here, or — better — a
**separate private repository**.

> The seed is the method. Your repo is the system. Your data never leaves your area.

You climb the ladder *in your own space*, with your own captures, categories, and
roles. This repo only ever holds the shape; everything real — every thought,
brief, decision, and asset — stays private to you. See
[`instantiate.md`](./instantiate.md) for standing up your area and
[`GUARDRAILS.md`](../GUARDRAILS.md) for keeping data out of anything public.

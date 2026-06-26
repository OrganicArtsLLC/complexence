# START HERE

This is the only page you need to run a day. If you're tired, read just the box.

> **Minimum viable day.** If you do nothing else: open today's inbox file, type
> or speak your thoughts into it, save. That's a valid day. Routing can wait up to
> 48 hours. Capture is the only thing you can't recover later.

> ⚠️ Keep your real notes in `instance/` (gitignored). This repo is public — see
> [GUARDRAILS.md](../GUARDRAILS.md).

---

## The whole system in one breath

You capture a thought — **type it or speak it**. One agent (Chief of Staff) sorts
what you wrote into a short daily brief and hands the rest to specialist agents.
You review only the exceptions.

```text
a thought (typed or spoken) -> inbox -> Chief of Staff -> today's brief -> you review only blockers
```

New here? **Type.** Voice is an optional door for later; typing is how you see the
system work. Curious what you're really building? See [`layers.md`](./layers.md).

## One-time setup

```bash
mkdir -p instance            # your private, gitignored working area
# optional: install the secret guard as a pre-commit hook
ln -s ../../scripts/check-no-secrets.sh .git/hooks/pre-commit
```

## Morning — 10 minutes

1. Create today's files:
   ```bash
   ./scripts/new-day.sh
   ```
   (or copy `templates/inbox.template.md` to `instance/inbox/YYYY-MM-DD.md` by hand)
2. **Dump** any thoughts into the inbox as entries.
3. **Run the Chief of Staff:** open a fresh AI chat, paste
   [`agents/chief-of-staff.prompt.md`](../agents/chief-of-staff.prompt.md), and
   point it at today's inbox file.
4. **Read** the brief it writes. Look only at *Top 3 priorities* and
   *Blocked decisions*.

## Midday — 5 minutes

- Append captures to today's inbox. Don't process. Just dump.

## Evening — 10 minutes

1. Re-run the Chief of Staff over the inbox.
2. Clear *Blocked decisions* — pick an option for each (the brief recommends one).
3. Confirm *One forward action* for tomorrow. Done.

## Weekly — 20 minutes, once

1. Read the week's decisions and resolve anything open.
2. Update your asset census.
3. Pick the **top 5 ideas** from the week's briefs.
4. Archive dead weight.
5. Write next week's one-line focus.

---

## When it feels like too much

- You don't have to process. **Capture is enough** (48h tolerance).
- You don't have to read the whole brief. **Top 3 + Blocked decisions only.**
- You don't have to run all six agents. **Chief of Staff alone is a complete day.**
- Skipping a day is allowed. Pick it back up at the next capture. Nothing breaks.

---

## What's where

- What you're really building (the layers): [`layers.md`](./layers.md)
- Full method: [`spec/complexence-os.md`](../spec/complexence-os.md)
- Role prompts: [`agents/`](../agents/)
- Blank templates: [`templates/`](../templates/)
- Stand up your own instance: [`docs/instantiate.md`](./instantiate.md)
- Safety rules: [`GUARDRAILS.md`](../GUARDRAILS.md)

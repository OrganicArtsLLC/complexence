# GUARDRAILS — read before you commit

**This repository is PUBLIC.** Everything committed here is world-readable, and
**git history is permanent** — deleting a file in a later commit does *not* remove
it from history. Assume anything committed here can be read by anyone, forever,
even if you "delete" it afterward.

This repo holds the **method only** (the spec, role prompts, and blank templates).
Your actual usage — your captures, briefs, decisions, maps — is private data and
must never be committed here.

---

## The one rule

> **Method in public. Data in private.**
> Nothing that identifies a real person, place, employer, project, or number
> belongs in this repo.

---

## Never commit

- Real names (yours or anyone's), employers, teams, clients, coworkers
- Family, health, legal, or financial details
- Internal URLs, hostnames, ticket IDs, project codenames
- Credentials, tokens, API keys, `.env` files
- Anything copied out of a real instance (`inbox/`, `today/`, `decisions/`,
  `domains/`, `essays/`)
- Anything from a **lab's** `.complexence/` (charters, experiments, metrics,
  summaries — see `spec/complexence-labs.md`). The blank templates in `install/`
  are the public grammar; a *filled* scaffold is lab data. The only lab artifact
  that may ever cross into this repo is a **pattern card**
  (`templates/pattern-card.template.md`) that has passed its leakage checklist.

If you are unsure whether something is safe, it is not. Leave it out.

## Where your data goes instead

- Put your working instance in **`instance/`** — it is gitignored and never tracked.
- Or keep your instance in a **separate private repo** entirely (recommended).

The blank templates in `templates/` are safe to share. The moment you fill one in
with real content, it is private data — move it under `instance/`.

## Before every commit

1. Run the local check:
   ```bash
   ./scripts/check-no-secrets.sh
   ```
2. Read the staged diff with your own eyes:
   ```bash
   git diff --staged
   ```
3. Only then commit.

### Local denylist (recommended)

Create a file named **`.private-denylist`** in the repo root (it is gitignored).
Put one sensitive term per line — your name, employer, project codenames, family
names, anything that must never leak. `check-no-secrets.sh` will block any commit
that contains those terms. Because the file is gitignored, your private terms
never enter the public repo themselves.

```text
# .private-denylist  (example — yours stays local and untracked)
Acme Corp
Project Bluebird
```

## If something private gets committed anyway

Treat it as **already leaked** — assume it was cloned or indexed the moment it was
pushed. Then:

1. Rotate any exposed secret immediately (it is compromised regardless).
2. Redact the content and commit the redaction.
3. If warranted, rewrite history with
   [`git filter-repo`](https://github.com/newren/git-filter-repo) and force-push —
   but understand this does not un-leak what was already public.

## Reviewing contributions

If you accept pull requests, review every diff for accidental personal data
*before* merging. Contributors may not know your guardrails.

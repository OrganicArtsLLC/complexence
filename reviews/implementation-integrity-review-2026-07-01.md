# Implementation & Repo Integrity Review — Complexence (public repo)

**Date:** 2026-07-01
**Lens:** Implementation quality + repo integrity + privacy/leak audit (ADR-051: public repo is method-only)
**Scope:** Working tree + full git history (all 15 commits, single branch `main`, no tags, reflog, dangling objects), src/, scripts/, agents/, editors/, templates/, spec/, docs/, proofs/, root docs.
**Method notes:** Full `git log -p` swept for real names (family, coworkers, employer), private roster/agent names, trading/financial/health content, daily-log content, tailnet hostnames/IPs, private-system paths, secrets/token patterns. Read-only scripts executed (`cognitive_form.py validate|reflect`); network-calling scripts (`demo.py`, `experiment*.py`) reviewed, not run. All relative markdown links machine-checked.

---

## Part A — Privacy / leak audit

**Verdict: CLEAN. No history rewrite required.** No commit in history (or in the reflog / dangling objects) contains personal names beyond the author's own public business identity, private roster names, trading/financial specifics, health/family matter, daily-log content, tailnet hostname/IP, private-system paths, or secrets. The two below are the only items found, both informational.

### P-1 · LOW · Dead `sources/` references leak private-workspace filenames
- **File:** `spec/complexence-capability.md:132-138` (§10 "Source Inputs"); present since commit `0611fa7`.
- Lists five files (`sources/better-map-framework-research.md`, `sources/naming-and-domain-strategy-research.md`, `sources/origin-rabbit-hole-domainideas.md`, two "…Map of Modern Complexity" PDFs) that do not exist in this repo and never did (verified against full history). They are filenames from the private workspace — not personal data, but instance-layout breadcrumbs and dead references for any adopter.
- **Fix:** delete §10 or replace with "private research notes (not published)". No history action needed — filenames alone are low-sensitivity.

### P-2 · LOW · Two pointers to "blog ADR-023"
- **Files:** `spec/complexence-capability.md:130` (§9) and `spec/complexence-science.md:619` (§8.5).
- References a decision record in another (personal) repo that a stranger cannot resolve. Reveals only that a numbered ADR system exists elsewhere; content not exposed.
- **Fix:** reword to "kept in a private strategy record" or drop the identifier.

### Informational (no action)
- **Git identity** (`Joshua Ayson <j@organicartsllc.com>`) appears on all 15 commits — intentional public attribution for a CC BY repo. Note it technically contradicts GUARDRAILS' literal "Never commit: Real names (yours…)"; see I-8.
- **Dangling objects (local only, never pushed):** amended-away initial commit `9870a10` differs from `a0eeefa` only in LICENSE files (MIT → CC BY split). Dangling blobs are two `check-no-secrets.sh` drafts plus two obvious test fixtures for the guard ("CONFIDENTIAL note here"; `jane.doe@example.com` / fake `api_key=ABCD…`). Harmless; they also demonstrate the guard was actually tested.
- **Untracked run artifacts** (`src/experiment_v2_results.json`, `src/experiment_v2_run.log`, `src/__pycache__/`) are correctly gitignored, were never tracked at any point in history, and contain no private data (only experiment output text).
- The early `agents/repo-steward.prompt.md` (renamed to `asset-steward` in `a109cab`) shares a filename with a private-instance role, but its committed content is fully generic in every revision — no leak.
- `src/example.cform.json:29` credits "external review (Gemini, Google, Grok)" — AI models, not people; fine.

---

## Part B — Implementation quality + continuity

### B-1 · HIGH · The "pre-registered" claim in experiment_v2 is not supported by the evidence
- **File:** `src/experiment_v2.py:24` ("PRE-REGISTERED PREDICTION (committed before the run — see git history)"); commit `ae3a8f4` (2026-06-28 08:13 -0700), currently **unpushed**.
- The local run artifacts (`experiment_v2_results.json` / `_run.log`, mtime 2026-06-28 06:43) predate the commit by ~90 minutes — so the prediction was *not* committed before the run. Worse, results are gitignored (`0eccdae`), so git history can never verify the claim either way. For a repo whose stated ethos is honest, verifiable results, an unverifiable pre-registration claim is the largest integrity exposure here.
- **Fix (pick one):** (a) reword to "prediction written in the docstring before the run" and drop "see git history"; or (b) commit the prediction, then re-run cleanly and publish the result. Do this **before pushing** `ae3a8f4`/`0eccdae` — it is fixable without history rewrite while unpushed.

### B-2 · HIGH · experiment_v2 ran, produced evidence-against, and it is written up nowhere
- **Files:** `src/experiment_v2_run.log` (local), vs `ROADMAP.md:49-84` ("Landed so far" + null write-up) and `src/README.md` — both stop at v1 (`experiment.py`).
- The v2 run's own verdict: rubric delta A−B = **−0.12 at p=0.0 and −0.38 at p=0.6** — the anchored condition did *worse* as the channel degraded, opposite the pre-stated signature; script printed "mixed / underpowered." ROADMAP says "a program that hides its null results is just a brand" — yet the v2 code ships with no mention in ROADMAP or src/README, and its less-flattering result exists only in a gitignored log.
- **Fix:** add an experiment_v2 subsection to ROADMAP "Landed so far" (design, pre-registration caveat, the mixed/negative numbers, what's next) and a v2 paragraph to `src/README.md`, before pushing.

### B-3 · HIGH · License split is internally inconsistent about `src/`
- **Files:** `README.md:174-179` ("everything except `scripts/` — CC BY 4.0"; "The code (`scripts/`) — MIT") vs `src/cognitive_form.py:18` ("Licensed MIT"), `src/cognitive-form.schema.json:6` ("Licensed MIT"), `src/README.md:7` ("MIT-licensed"), `ROADMAP.md:40,90` ("code is MIT"). No `src/LICENSE` exists.
- By README's directory rule, `src/` code is CC BY 4.0 (a poor code license); by every in-file claim it's MIT. An adopter cannot tell which governs.
- **Fix:** change README §License to "code (`scripts/`, `src/`) — MIT" and add `src/LICENSE` (copy of `scripts/LICENSE`), or move to a single content-type rule stated in one place. Also: `demo.py`, `experiment.py`, `experiment_v2.py` carry no license line at all — add one each.

### B-4 · MEDIUM · README layout and scope statements are stale (deny src/ and proofs/ exist)
- **File:** `README.md:140-148` (layout block lists spec/agents/editors/templates/docs/scripts/instance — no `src/`, no `proofs/`, no `reviews/`) and `README.md:159-160` ("deliberately ships the *method* — the spec, the contracts (`agents/`), and *blank* templates — **and nothing else**").
- `src/` (5 Python files + schema + example) and `proofs/` landed after these lines were written; README never mentions `src` once (grep-verified). The "nothing else" claim is now false, and a stranger reading only README misses the Phase-1/2 artifacts entirely.
- **Fix:** add `src/` and `proofs/` rows to the layout block; soften "nothing else" to name the science artifacts.

### B-5 · MEDIUM · Science spec §8.4 overclaims what Complexence OS is
- **File:** `spec/complexence-science.md:573-577`: Complexence OS's "`CognitiveForm` type, projection layer, agent runtime, memory layer, and feedback layer are the engineering instantiation of Theory B."
- `spec/complexence-os.md` defines none of those — it is a markdown-and-prompts method (roles, contracts, cadence). The OS spec's word "(later) scripts" is its only nod to a runtime. The two specs describe different objects under one name.
- **Fix:** reword §8.4 to aspiration ("its planned kernel object…") or point at `src/` as the current partial instantiation.

### B-6 · LOW · `cognitive_form.py` usage output prints a stray docstring line
- **File:** `src/cognitive_form.py:168-170` — on bad args it prints `__doc__.splitlines()[-3]`, which is the literal line "CLI:", then the real usage line. Cosmetic; the CLI otherwise works (`validate` and `reflect` both run clean against `example.cform.json`, exit codes correct).
- **Fix:** drop line 169.

### B-7 · LOW · Type/robustness nits in the experiments
- `src/experiment.py:89-101` — `a_scores: list[int]` but `drift_score()` can return `None`, which is appended and printed as "None/10" before being filtered. Annotate `list[int | None]` or skip-append.
- `src/experiment_v2.py:133` — RNG seed gives conditions A and B′ identical noise draws but B a different one; the paired-noise design is inconsistent across arms. Seed on `(p, trial)` only if pairing is intended.
- `src/experiment_v2.py:127` — `metric_holistic` can return `NaN`, which silently propagates through `statistics.mean` in `summarize`.

### B-8 · LOW · GUARDRAILS' "one rule" contradicts the repo's own attribution
- **File:** `GUARDRAILS.md:24` ("Never commit: Real names (yours or anyone's)") vs the repo's committed author identity, "Copyright © 2026 Organic Arts LLC," and joshuaayson.com links — all intentional and required for CC BY attribution.
- **Fix:** scope the rule to *captured/instance* content ("no real names from your captures — the maintainer's public attribution is the one exception").

### B-9 · LOW · `assets/census` vs `assets/census.md` drift
- `spec/complexence-os.md:106` and `agents/asset-steward.prompt.md` say `assets/census`; `editors/copilot/prompts/complexence-census.prompt.md:13,17` says `assets/census.md` (likewise `map.md`, `<slug>.md` in the other prompt files vs extension-less paths in agents/spec). Trivial, but the spec says contracts must stay identical — pick one convention and state it.

### Verified-good (checked, not assumed)
- **Scripts run / are sound:** `cognitive_form.py validate` ✓ and `reflect` ✓ against `example.cform.json`; `check-no-secrets.sh` logic reviewed line-by-line (bash-3.2-portable as claimed, denylist path correct, symlink instruction resolves correctly from `.git/hooks/`), and dangling test-fixture blobs show it was exercised; `new-day.sh` writes only under gitignored `instance/` as claimed.
- **Templates match the spec contracts:** daily-brief template = the five §6.2 sections in order; decision template = §6.3 fields; census = §6.4 columns; inbox = §6.1 fields; domain map = the L0–L7 levels.
- **Role roster coherent:** 6 prompt files = 1 router + 5 specialists, matching README, spec §5, and the editors/ mapping table; the CoS/Daily-Brief split is explained in spec §5.
- **Contracts consistent everywhere:** the confidence rubric (5×0-20), routing thresholds (≥90/70-89/<70), and brief sections are identical across README, spec, agents/, editors/, and bootstrap prompt.
- **All relative markdown links resolve** (machine-checked, every .md file). The only dead references are the non-link `sources/` and "blog ADR-023" citations (P-1, P-2).
- **Method-only discipline in spirit: holds.** Nothing assumes the private instance; the bootstrap prompt explicitly gathers the adopter's context instead of assuming Joshua's; quickstart is genuinely runnable by a stranger with only a chat window. The only adopter stalls are minor: `demo.py`/`experiment*.py` require the `claude` CLI (stated, with a swap-the-adapter note), and README's missing `src/` row hides those artifacts (B-4).
- **.gitignore correctly walls off** `instance/`, `.private-denylist`, env/keys, run artifacts, pycache.

---

## Count summary

| Severity | Privacy | Implementation | Total |
|---|---|---|---|
| CRITICAL | 0 | 0 | 0 |
| HIGH | 0 | 3 (B-1, B-2, B-3) | 3 |
| MEDIUM | 0 | 2 (B-4, B-5) | 2 |
| LOW | 2 (P-1, P-2) | 4 (B-6, B-7, B-8, B-9) | 6 |
| **Total** | **2** | **9** | **11** |

**History rewrite required: NO.** The full history is clean; P-1/P-2 are fixable with ordinary forward commits.

**Priority before the next `git push`:** B-1 and B-2 — the two unpushed commits (`ae3a8f4`, `0eccdae`) ship an unverifiable pre-registration claim and an unpublished evidence-against result; both are cheap to fix now and expensive to the repo's credibility later.

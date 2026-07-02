# Voice & Content-Filters Review — Complexence (public repo)

**Date:** 2026-07-01
**Scope:** README.md, spec/ (3 files), docs/ (5 files), GUARDRAILS.md, ROADMAP.md,
proofs/channel-capacity-sketch.md, src/README.md, agents/ prompts, templates/,
editors/copilot/ — plus a held outbox note from the author's private instance
(the *coherence steward* pattern, staged for possible publication here).
**Calibration:** read against the author's published freewriting corpus
(incl. *Breathe. Then Prompt.*, *Stay Out of the Way*, and
*Hormesis, Universe, and Late-Night Flow*).

**A scoping note before the findings.** The two spec files declare themselves
"facts-only specification," and the agents/ prompts and templates are contracts.
A spec is allowed a tighter, flatter register than freewriting — that's honest to
the genre, and those files mostly pass. The filters bite hardest where a stranger
first meets the material: README, docs/, ROADMAP, and the narrative passages of
the science spec. That's where the findings concentrate.

**What already passes, and unusually well (worth protecting in any edit):**

- The honesty discipline is the best thing in the repo. "Candidate," "conjectured,"
  "unproven," §1a's read-this-first scoping rules, §10's ledger of logical debts,
  and above all the **honest null result** written up in ROADMAP.md:67-84 and
  src/README.md:77-83. Almost nobody publishes their own scorer artifact. Filter 4
  is largely *met*, not just attempted.
- The seed metaphor ("The seed is the method. Your repo is the system.") is
  plain-words-first, analogy-first — exactly the pattern the coined terms need.
- The warmth in START-HERE.md ("If you're tired, read just the box," the
  minimum-viable-day, "Skipping a day is allowed... Nothing breaks") is his
  register: easy on the depleted reader.
- Precision that holds a distinction instead of borrowing prestige:
  science:487-490 explicitly says the map-territory limit is **not** Gödel's
  incompleteness theorem. That's the Bohr register working.
- "Two doors, one room" (automation.md:21) and "it is a test, not a vibe"
  (science:671) sound like a person.

---

## Filter 1 — Define every coined term / acronym in plain words at first use, analogy first

### HIGH — README first contact: the coined word is defined by abstraction, no analogy, no concrete moment

`README.md:3-5`

> "**The capability of staying oriented inside complex systems and turning that
> orientation into coherent action — plus the method that runs it and the science
> under it.** One coined word, three altitudes, in one versioned repo."

This is the front door, and a stranger's first contact is three abstractions deep
("capability... complex systems... coherent action") plus an unglossed spatial
metaphor ("three altitudes"). His own filter: universal analogy first, then the
term. Nothing here lands on lived ground — no codebase, no job, no life.

*Suggested rewrite (register-matched):*

> "Complexence is a word I made up for something specific: staying oriented inside
> a system too big to hold in your head — a codebase, a job, a life — and turning
> that orientation into action you'd stand behind. This repo holds the map of that
> capability, the working method I run it with, and the early, unproven science
> underneath. One word, three layers of depth, one versioned repo."

### HIGH — "Cognitive Form" is used repeatedly before it is defined; the analogy arrives last

Reading path: README links straight to ROADMAP ("its edges and direction live in
ROADMAP.md"), where the reader hits, undefined:

`ROADMAP.md:17-19`

> "Human–AI collaboration improves when cognition operates on representation-invariant
> **Cognitive Forms** rather than on independent documents, prompts, diagrams, and
> code."

"Representation-invariant Cognitive Forms" is jargon squared at first contact. In
the science spec the term first appears at line 50-51 ("a *structural* algebra of
meaning (the **Calculus of Cognitive Forms**)"), gets its formal definition at
§4.4 (line 259) and §7.1 (line 436), and the one universal analogy that actually
makes it land — the abstract syntax tree — waits until §8.3 (line 566). The
plain-words-then-formalism order is inverted for the repo's central coined object.

*Fix:* put a one-breath plain version at every first use. E.g. for ROADMAP:17,
add after the block quote: "(A Cognitive Form is the meaning kept separate from
any one way of writing it down — the same idea whether it's an essay, a diagram,
or code. Defined in the spec, §7.)" And in science §1, gloss it at line 51 the
same way.

### HIGH — "AST of thought" uses an unexpanded acronym

`spec/complexence-science.md:96`

> "The **Cognitive Compiler**; cognitive forms as the 'AST of thought'; **Complexence OS**"

AST is never spelled out here; the expansion ("abstract syntax tree") appears 470
lines later at §8.3. This is verbatim the phrase that triggered the filter in the
first place — assume readers will ask what it means.

*Fix:* "cognitive forms as the 'AST of thought' (AST = abstract syntax tree — the
structure a compiler keeps after it throws away your exact wording)". Or drop the
acronym in the table and say "the parse tree of thought."

### HIGH — OODA is never expanded, anywhere in the repo

`spec/complexence-science.md:167-171`

> "**OODA (Boyd).** *Shared:* the loop, and the centrality of Orientation..."

The reader is told what OODA lacks before being told what the letters say. It is
used five times and never once spelled out.

*Fix:* first use becomes "**OODA (Boyd's observe–orient–decide–act loop, from air
combat).**" One parenthesis; done.

### MEDIUM — "the L0–L7 map" appears in README with no explanation

`README.md:11`

> "orienting and navigating under load (the L0–L7 map)"

First use; a stranger has no idea there are eight levels of anything yet.
*Fix:* "(an eight-level orientation map, L0–L7 — from 'what's in scope' to 'what
did we learn')".

### MEDIUM — README foundation row is a jargon pile at first use

`README.md:13`

> "the formal science: an ontology, a recursive equation, two calculi, meaning velocity"

Four coined/technical terms, zero glosses, in the third row a stranger reads.
"Meaning velocity" is his own coined metric and appears here first, undefined.
*Fix (table cell, keep terse):* "the formal science underneath: what has to exist
before thinking can (an ontology), the loop it runs (one recursive equation), and
the one number that matters — how fast useful meaning moves (meaning velocity)".
Or gloss just "meaning velocity (Δmeaning/Δtime — how fast useful meaning moves)".

### MEDIUM — "MVP" never expanded

`spec/complexence-os.md:167`, `docs/instantiate.md:57`

> "0 — Prompt-only MVP | Prove flow with no build"

*Fix:* "Prompt-only MVP (minimum viable product — prove the flow with no build)".
Or just say "Prompt-only start".

### MEDIUM — "LLM" never expanded

First doc-path use `docs/automation.md:31` ("an LLM agent invoked **headlessly**"),
also `spec/complexence-science.md:419`. The repo's stated audience includes people
who have never built anything.
*Fix at first use:* "an LLM (large language model — the kind of AI behind chat
assistants) agent".

### LOW — "headless" unglossed

`docs/automation.md:31,37` — "invoked **headlessly**" / "a headless agent run."
*Fix:* "headlessly (no chat window — it runs and writes files, nobody watching)".

### LOW — Greek loop lands early in the capability spec

`spec/complexence-capability.md:20-23` — `Σ -> ω -> μ -> π -> η -> α -> τ(Σ) -> Σ'`
arrives in section 1 before a reader has any reason to care. The facts-only genre
excuses it, and the human-language loop is given first. Fine to leave; if touched,
move the formal-basis paragraph to §9 Relations.

---

## Filter 2 — Freewriting voice, not LLM-academic

The corpus check: his freewriting is first person, breath-paced, concrete, and
almost never uses an em-dash. The repo prose is competent but carries clear
co-drafting tells — em-dash density far above his hand, mirrored "not X but Y"
pairs, bolded aphorism-declarations, and one repeated slogan.

### MEDIUM — em-dash clusters, pervasive

Density: ROADMAP.md 24 em-dashes in 94 lines; docs/layers.md 29 in 157;
README.md 24 in 184. His freewriting corpus: near zero. Worst single cluster:

`README.md:25-27`

> "You capture a thought — **by typing or by speaking**. One router agent — a *Chief
> of Staff* — sorts it into a short daily brief..."

Two em-dash interruptions in two sentences at the very top of the page.
*Fix pattern:* convert most parenthetical em-dashes to commas, parentheses, or a
second sentence. E.g. "You capture a thought, typed or spoken. One router agent
(a Chief of Staff) sorts it into a short daily brief and hands the rest to
specialist roles." A one-pass sweep of README, docs/layers.md, and ROADMAP would
cut the count by half without losing anything.

### MEDIUM — "It isn't. It's Y" machine tell (also flattens a both/and — see Filter 5)

`docs/layers.md:3-4`

> "Complexence OS looks like a note-taking workflow. It isn't. It's a ladder of
> **cognitive orchestration**..."

Classic tell, and it denies something true: it *is* a note-taking workflow — and
also a ladder. His register holds both.
*Suggested rewrite:* "Complexence OS looks like a note-taking workflow, and it is
one. It's also a ladder: each rung moves a piece of your thinking out of your
head and into files you can read, version, and improve."

### MEDIUM — "thus not X but Y" in the science spec

`spec/complexence-science.md:616-617`

> "Working in the open is thus not a marketing choice but the loop's own requirement."

"Thus" + mirrored pair in one clause is the LLM-academic cadence. (He does use
"thus" in freewriting, but never welded to a "not X but Y".)
*Fix:* "So working in the open isn't a marketing choice. The loop requires it."

### MEDIUM — floating self-quote tagline inside the formal spec

`spec/complexence-science.md:556-557`

> "A good cognitive system increases the rate at which useful meaning becomes
> visible, transformable, and actionable. 'The mathematics of working with minds
> that think back.'"

An unattributed pull-quote of the project's own tagline, plus a triad, in a
document that elsewhere works hard to be sober. It reads like a slide deck leaked
into a spec.
*Fix:* cut the quoted sentence, or own it plainly: "The short version I keep
coming back to: the mathematics of working with minds that think back."

### MEDIUM — the "just a brand" aphorism runs twice in one file

`ROADMAP.md:26-27` — "a field that hides its open edges is just a brand"
`ROADMAP.md:81` — "a program that hides its null results is just a brand"

Good line once; a repeated slogan is a machine tell (and a thought-leader one).
*Fix:* keep the second (it's earned by the null result it sits next to); at line
26-27 say "because the open edges are the field" or simply "because hiding them
would defeat the point."

### LOW — "leverage" density

`docs/layers.md:11,51,113`, `README.md:83-84` — "most of the leverage," "feel that
the leverage is real," "Leverage compounds." It's in his working vocabulary, but
four-plus uses across the entry docs is productivity-blog cadence. Vary: "payoff,"
"the gain is real," "fixes compound."

### LOW — repeated tagline

"The seed is the method. Your repo is the system. Your data never leaves your
area." appears verbatim at `README.md:166` and `docs/layers.md:151`. Defensible as
a deliberate refrain (it's the safety rule); if kept, keep exactly these two and
don't let it spread.

### LOW — mirrored pair in the audience line

`README.md:55-56` — "people whose bottleneck is not *having* ideas but *capturing
and structuring* them." One mirrored pair is fine; noted only because the page
already carries several.

### LOW — triads sprinkled

"durable, inspectable, and improvable" (`docs/layers.md:107`), "visible,
transformable, and actionable" (`spec/complexence-science.md:556`), "critique,
contribution, and *honest negative results*" (`ROADMAP.md:83`). Individually
harmless; collectively a rhythm. Break one leg off a couple of them.

### LOW — bolded "This is **X**" declaration rhythm

`docs/layers.md:60` ("This is **separation of concerns for thought**"), `:92`
("This is **meta-cognition as a system**"). The insight is good; the bolded
coinage-drop twice per page is thought-leader cadence. Unbold, or fold into the
sentence: "the hierarchy is separation of concerns, applied to thought."

---

## Filter 3 — Humble practitioner, not a movement

### HIGH — "Most people" claims a user base that doesn't exist

`docs/layers.md:141-142`

> "Most people get enormous value and never leave Layer 1–2. That's a success,
> not a shortfall."

There are no "most people" — there is one practitioner and a repo published days
ago. This is the clearest adoption-implying claim in the repo.
*Fix:* "You can get enormous value and never leave Layer 1–2. That's a success,
not a shortfall." (Keep the second sentence — it's the warm, true part.)

### HIGH — "external review and contributions" oversells a solicited model pass

`ROADMAP.md:51-52`

> "the published spec drew external review and contributions within hours of going
> public"

The "contributions" named below are drafts from Google Gemini — a model run
against the spec, then vetted here. The per-item attributions are honest
(ROADMAP.md:54-55, proofs/channel-capacity-sketch.md:7-8 both say "contributed by
Google Gemini... vetted here"), but the headline sentence reads as community
traction: strangers reviewing the work unprompted. One practitioner prompting a
second model is a real and interesting feedback loop — say that.
*Fix:* "the loop started running within hours of going public — the first outside
pass came from putting the spec in front of another model (Gemini) and vetting
what came back:". Honest verbs: "came from," "was run," not "drew."

### MEDIUM — the field-positioning ladder needs one grounding line

`spec/complexence-science.md:113-121`

> "just as mathematics sits above arithmetic and metamathematics sits above
> mathematics, there is an under-formalized level above both... `cognitive
> structure → COMPLEXENCE`"

Placing the coined word in caps at the top of a ladder containing mathematics,
logic, and computer science is the repo's peak altitude. It is *mostly* earned:
§1a scopes it, §3a names the neighbors and calls the differentiation "a
positioning claim to be *earned*," §10 lists the debts. What's missing is one
sentence of practitioner scale at the claim itself, before the reader has met the
hedges.
*Fix:* after the ladder, add: "That's the claim, and it's one person's bet, not a
consensus — §3a says what the neighbors already cover, and §10 says what this
still owes." Also consider lowercasing COMPLEXENCE in the ladder; the caps do
manifesto work the prose then has to walk back.

*(Related, no action needed: "Complexence (the field) studies..." — present tense
for a field of one. §1a's "research program, not a finished science" mostly covers
it, and rewriting every verb to subjunctive would be worse. The grounding line
above is the cheaper fix.)*

---

## Filter 4 — Evidence honest to verb strength

This filter is the repo's strength; only edges remain.

### MEDIUM — "executed and checked" overstates a single model self-judgment

`src/README.md:62-63`

> "The central claim — *meaning is what survives transformation* — executed and
> checked, not just asserted."

The check is one model judging its own round-trip, and the paragraph above says
so honestly ("a model's judgment, not a proof, but runnable"). The closing line
then re-inflates it.
*Fix:* "The central claim — *meaning is what survives transformation* — run
end-to-end and judged by a model, once. Not proof; motion."

### LOW — "is validated with numbers" (targets, not results)

`spec/complexence-os.md:215` — "so 'reduced desk friction' is validated with
numbers, not feel." Nothing has been validated yet; these are proxies to track.
*Fix:* "so 'reduced desk friction' can be checked with numbers, not feel."

### LOW — "the description is exact rather than poetic"

`spec/complexence-science.md:583` — "It can, and the description is exact rather
than poetic." "Exact" claims a rigor the reflexive argument doesn't yet have (the
operators it invokes are themselves unproven, per §10).
*Fix:* "It can, and the description uses the calculus's own operators rather than
metaphor."

---

## Filter 5 — Holds contradictions without flattening

Mostly good. The best passage in the repo for this register is
`spec/complexence-science.md:592-593`: "The looseness is not vagueness; it is the
residue that limit guarantees" — a deliberately loose central term defended *by*
the theory's own limit. That's Bohr, not slogan. Likewise §7.2's Gödel
disambiguation and §10's refusal to pick the deepest primitive.

Two flattenings, both already logged above with fixes:

- `docs/layers.md:3-4` — "It isn't. It's a ladder" denies the true half (it *is* a
  note-taking workflow). See Filter 2, MEDIUM.
- Outbox note: "Coherence is not a byproduct. It is a role." — see below, LOW.
  Coherence in a real system is both emergent *and* stewarded; the method's actual
  claim is only that it can't be *left* as a byproduct.

---

## The outbox note — the coherence-steward pattern (private instance, staged)

**Verdict: push after two small softenings.** It is method-only (checked: no
roster, no names, no instance data), the pattern is real and belongs in the
public repo, and structurally it fits the house style (pattern → what it does →
invariant → public/private split). The voice is pattern-language third person
throughout, which is acceptable for the repo genre, though it contains zero first
person — the repo's best pages ("I made up," "my bet") earn trust that this note
doesn't try for. Optional, not blocking.

Line edits:

1. **MEDIUM (filter 3) — line 47:**
   > "Every growing multi-agent system hits this wall."

   Universal claim from an instance of one. Soften to lived scale:
   *"Any system I've grown this way has hit this wall, and the failure mode is
   general: the pattern — give coherence an owner — travels; the roster it audits
   is yours."* (Then trim the now-duplicated next sentence.)

2. **LOW (filter 3/4) — lines 41-43:**
   > "This holds across structurally different domains: codebases accrete dead
   > paths, prose drifts out of internal agreement..."

   "This holds" is a proven-law verb. *Fix:* "The same shape keeps showing up
   across structurally different domains: ..." — same content, honest verb.

3. **LOW (filter 2/5) — line 43:**
   > "Coherence is not a byproduct. It is a role."

   Mirrored aphorism, and it flattens a both/and (coherence is partly emergent).
   *Fix, if touched:* "Coherence doesn't stay a byproduct for long. Past a certain
   size it needs an owner." Fine to leave if the sentence earns its place for him.

Also fine as-is, worth keeping: "Each addition is locally sensible; the *sum*
sprawls" (line 14-15) — precise, human, holds the tension. "A finding without a
fix is half-done" (line 30) and "A stale map is worse than none" (line 31) are in
his register. The five decays are defined inline by their own list — passes
filter 1.

Housekeeping on push: strip the "> **DRAFT for the public Complexence repo**..."
header block (lines 3-5) — it references the outbox/approval gate, which is
instance detail. Decide its destination path (reads like `docs/` or a new
`patterns/`) and add it to the README "What's where"/layout list so it's on the
reading path, plus a "Last Updated" footer to match house style.

---

## Count summary

| Severity | Repo | Outbox note | Total |
|---|---|---|---|
| HIGH | 6 | 0 | 6 |
| MEDIUM | 11 | 1 | 12 |
| LOW | 9 | 2 | 11 |
| **Total** | **26** | **3** | **29** |

By filter (repo): F1 first-use/jargon — 4 HIGH, 4 MEDIUM, 2 LOW. F2 voice — 4
MEDIUM, 5 LOW. F3 humility — 2 HIGH, 1 MEDIUM. F4 evidence — 1 MEDIUM, 2 LOW.
F5 contradiction-holding — 0 standalone (2 findings shared with F2/F3).

**One-line verdicts.**
(a) *The repo:* the honesty architecture (nulls, debts, "candidate" discipline) is
genuinely his and genuinely rare — the fixes needed are surface voice work
(em-dash sweep, four undefined terms on the front path, two adoption-implying
sentences), not structural.
(b) *The outbox note:* not quite as-is — push it the same day after softening the
one universal claim (line 47), swapping "This holds" for "keeps showing up," and
stripping the draft-gate header.

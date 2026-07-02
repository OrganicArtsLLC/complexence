# Complexence — Theory & Algebra Rigor Review

**Date:** 2026-07-01
**Lens:** THEORY & ALGEBRA RIGOR — are the core objects well-defined, are the "proofs" proofs, is the central bet's claimed strength honest, and does the formalism hold contradictions without either flattening them or hiding behind them?
**Scope read:** the entire public repo (README, spec/×3, proofs/, docs/, GUARDRAILS, ROADMAP, agents/, templates/, editors/, scripts/, src/ incl. experiments and local run artifacts), plus private context: ADR-051, the private instance's experiment artifacts (a workspace Cognitive Form instance, legibility tests + results, a system-legibility map), and a 2026-06-29 private red-team of complexence applied to a trading-domain lab (E/B/C findings cross-checked below).
**Posture:** rigorous but fair. Where the repo already labels a debt honestly, that is credited, not re-flagged.

---

## 0. What is already right (credit where due)

Before the findings: this repo is unusually honest for its genre, and several of the
red-team's 2026-06-29 demands have been implemented.

- **§1a of the science spec** ("Status, scope, and notation — read this first") is the
  single most valuable paragraph in the repo. It pre-declares that the calculi are
  candidate formalizations, that notation is unscoped (α, Φ collisions named), and that
  ℭ has three unreconciled presentations. Most findings below are places where the
  *body text then forgets §1a*, not places where the debt is hidden.
- **§10.6** openly lists the logical debts (minimality unproven, no worked composition,
  Meaning() circularity, Goal G unbuilt, notation overlaps). This is the right register.
- **`proofs/channel-capacity-sketch.md`** is the best-behaved file in the repo: it
  states its assumptions, says explicitly that it "relocates the debt" rather than
  discharging it, and lists what it does *not* buy. This is an argument correctly
  labeled as an argument.
- **The v0.1 experiment null is reported in public** (ROADMAP "First experiment result —
  honest negative / inconclusive"), including the embarrassing scorer artifact. Genuine
  epistemic hygiene.
- **Spec↔schema↔code continuity is good where it counts:** the 8 operators of §7.3, the
  schema enum, and `cognitive_form.py::OPERATORS` agree exactly; the 7 representation
  types agree; the OS-spec rubric/routing/brief contracts are byte-consistent across
  `spec/complexence-os.md`, `agents/chief-of-staff.prompt.md`, `docs/bootstrap.md`, and
  `editors/copilot/`. The `invariant_preserved` stub in code says out loud that it is a
  stub. No term drift found in the operating-method layer.
- **§3a (relation to prior work)** names its neighbors (Friston, Boyd, Snowden, Ashby,
  Spencer-Brown) and states the differentiation as "a positioning claim to be earned."
- **Red-team fixes that landed:** the pop-Gödel keystone is de-Gödelized in §7.2 (the
  third lens is now "Self-reference" with an explicit "NOT Gödel's incompleteness
  theorem" disclaimer — commit 40d804d); the definition-vs-hypothesis split (red-team B5)
  is done (`I = ⋂...` presented as needing grounding, the central bet held separately in
  §9.1); meaning-velocity's unoperationalized status (B6) is owned in §9.3/§10.5.

The findings below are what remains.

---

## 1. Findings

Severity: CRITICAL (structurally dishonest or invalidates a core claim) / HIGH (a real
overclaim or unresolved contradiction in load-bearing text) / MEDIUM (notation or claim
outruns definition; fixable locally) / LOW (nitpick, polish).

Suggested fixes use the red-team's verbs: **reframe** (relabel the claim honestly),
**strengthen** (supply the missing step), **drop**.

---

### HIGH

#### H1 — An open public pre-registration whose (adverse, contaminated) outcome is unreported
**Files:** `src/experiment_v2.py:24-30` (committed, public); `ROADMAP.md:49-84`;
local-only `src/experiment_v2_results.json` + `src/experiment_v2_run.log` (gitignored).

> `experiment_v2.py` docstring: "PRE-REGISTERED PREDICTION (committed before the run —
> see git history): … p = 0.6 : A beats B on rubric by >= +0.20 … If delta stays flat
> near 0 across p, that is honest evidence AGAINST the bet … Either way it is a real
> result."

The prediction is public and committed. The run happened. The local artifacts show the
delta went the **wrong direction and grew worse with noise** (rubric delta A−B: −0.12 at
p=0.0, **−0.38** at p=0.6 — the exact inverse of the pre-registered signature), and the
run is also **invalid**: at p=0.6 the relay outputs are API refusal messages ("API
Error: Claude Code is unable to respond to this request…"), and in one row a pure
refusal message was scored **rubric 1.0** (results json, condition B, p=0.6, trial 1 —
the "final" text is the model explaining it can't switch models, judged as fully
expressing the invariant). Neither the adverse direction nor the invalidity is recorded
anywhere public. ROADMAP's "Landed so far" stops at the v0.1 null; the same commit
sequence that added v2 also gitignored its run artifacts.

**Why it fails:** the repo's own stated norm is "a program that hides its null results
is just a brand" (ROADMAP:81) and §8.5 argues publication *is* the feedback term F. A
public pre-registration with a silent outcome is precisely the selective-reporting
pattern the pre-registration exists to prevent — worse than never pre-registering.
Gitignoring regenerable artifacts is defensible engineering; leaving the pre-registered
loop open is not.

**Fix (strengthen + reframe):** add a "v0.2 result" paragraph to ROADMAP: the run was
invalidated by harness refusals contaminating relay outputs and judges (a real
measurement-layer finding, on-theme with §10.5); the raw deltas, for the record,
trended against the pre-registered signature; the scorer must reject degenerate/refusal
outputs before v0.3. Then fix the harness (see M7) and re-run. Until that lands, the
public pre-registration is an unpaid debt.

#### H2 — The central law's notation is not well-formed: `⊂` on a tuple, `⋂` over an undefined carrier
**File:** `spec/complexence-science.md:446, 454, 487, 490, 511, 590` (and
`src/README.md`, schema `$comment`, which inherit the notation).

> "`R_i(ℭ) ⊂ ℭ`" (446, 487, 511, 590); "`I(ℭ) = ⋂_i Meaning( R_i(ℭ) )`" (454);
> "`Model(ℭ) ⊂ ℭ`" (490).

ℭ is defined as a **tuple** — `ℭ = (I, R, T, F, H)` (§7.1) or `Bind(ι,ρ,τ,κ,μ,π,η,R,F)`
(§4.4). `⊂` is not defined on tuples: a representation is not a *subset* of a 5-tuple in
any stated sense. Likewise `⋂_i Meaning(R_i)` requires `Meaning(·)` to return a **set**
drawn from a common carrier, with the intersection taken in that carrier — none of which
is defined. §10.6 owns the *circularity* of Meaning() but not the *well-formedness*
problem: even granting a Meaning oracle, the formula does not type-check. The same
notation is exported into the schema `$comment` and `src/README.md`, so the flagship
equation of the whole theory is, as written, a suggestive picture in set-theoretic
costume. (The private red-team flagged exactly this in B1 — "not even a well-formed
proposition until 'Model' and '⊂' are defined over ℭ (a tuple, not a set)" — and it was
not carried into the public spec.)

**Why it fails:** this is the "central principle" (§7.2's own label). Everything else
in Theory B — translation validity, compression preservation, multiprojection clarity —
is stated *in terms of* I(ℭ). Notation that implies set theory without defining the sets
is the precise thing §1a promises the document avoids.

**Fix (strengthen, cheaply):** one paragraph suffices. Define `Sem` as a set of
"consequences for action under a goal" (the reading §7.2 already gives informally), let
`Meaning: Representations → 𝒫(Sem)`, define `R_i ⊑ ℭ` ("R_i is a projection of ℭ",
replacing ⊂) as `P_i(ℭ) = R_i` for some projection map, and state `I(ℭ) := ⋂_i
Meaning(R_i)` as a **definition in 𝒫(Sem)**, with the caveat (already in §10.6) that Sem
is not yet constructed. Alternatively **reframe**: mark the three formulas explicitly as
"notation pictures, not set theory" per §1a. Either move is honest; the current middle
state is not.

#### H3 — "The equation defines what 'well' means precisely" — a descriptive equation claimed to carry normative content
**Files:** `spec/complexence-science.md:324-325`; `spec/complexence-capability.md:24-25`
(the claim is duplicated, so it reads as doctrine, not slip).

> science: "The capability is the loop run well, under load, by a person. The equation
> is what 'run well' means precisely."
> capability: "The capability is that loop run well under load; the equation defines
> what 'well' means precisely."

The §5.2 system of equations contains **no normativity whatsoever**: no objective
function, no performance measure, no error term to minimize, no ordering on outcomes. It
says what the loop's stages *are*, not what running them *well* is. Any loop — a
delusional one, a drifting one — satisfies the same equations. "Well" could only be
defined by Theory A's measurable quantities (throughput, meaning velocity, calibration),
and those are, by the spec's own §10.5, unoperationalized conjecture. So the sentence
claims precision that exists nowhere in the document — the exact "notation implies more
rigor than the definitions support" failure, in the two most prominent bridging
sentences of the stack.

**Fix (reframe):** "The equation states the loop formally; what running it *well* means
is the open measurement question of Theory A (§6, §10.5)." One-line edit, both files.

#### H4 — Duality "evidence" from shape-identity: §7.6 contradicts §10.2
**File:** `spec/complexence-science.md:519-526` vs `:699-703`.

> §7.6: "`ℭ_{t+1} = Φ( ℭ_t, R, T, F, H )` — Identical in shape to the kernel in §5.3 —
> which is **the evidence** that Theory A and Theory B are two faces of one system."

*Every* discrete dynamical system has the shape `X_{t+1} = Φ(X_t, params)`. The two
kernels also aren't even identical in shape: §5.3's Φ takes eight loop-stage arguments
(ω, μ, π, η, α, F, κ), §7.6's takes the four remaining tuple components (R, T, F, H) —
they share only the pattern "next state = function of current state and stuff." Writing
both as Φ and calling the resemblance "the evidence" is notation doing the arguing.
§10.2 gets it right ("Conjecture: … A formal duality between them is the most important
open theorem"); §7.6 pre-spends that theorem. This is the repo's cleanest remaining
instance of the red-team's BELIEF-AS-PROOF pattern.

**Fix (reframe):** "…which is *what motivates the duality conjecture* (§10.2)" — and
either give the two Φ's distinct subscripts (Φ_A, Φ_B) or note that the shared symbol is
aspirational. Do not use "evidence" for a typographic resemblance.

#### H5 — The intersection-monotonicity contradiction (red-team E12) still stands, and is not even listed in §10
**File:** `spec/complexence-science.md:454` vs `:502-503`.

> §7.2: "The identity of a form is the intersection of meaning across all its valid
> projections." (⋂ weakly **shrinks** as projections are added.)
> §7.4: "**Multiprojection clarity** — a form gets clearer as the number of *consistent*
> independent projections increases." (clarity **grows** with projections.)

More projections ⇒ the intersection can only stay equal or shrink; yet the theory's
named theorem says more projections ⇒ clearer form. As stated, adding a valid projection
can *delete* meaning from I(ℭ) while allegedly clarifying it. The private red-team
identified this (E12) and supplied the fix — distinguish the *extent* of I (shrinks or
holds with N) from *confidence* that the surviving core is the true invariant (rises
with N, under independence). The public spec added the word "consistent" but did not
adopt the distinction, and unlike the other known debts this one does **not** appear in
§10's honesty ledger. It is an internal contradiction in Theory B's core, unresolved and
unacknowledged. (Note: the red-team also proved the "independence" premise is exactly
what fails under correlated projections — worth importing as a stated caveat.)

**Fix (strengthen):** adopt E12's resolution verbatim: "Adding consistent projections
sharpens the *boundary* of I (confidence in the surviving core), not its *content*
(which weakly shrinks). The theorem is about confidence, and holds only under projection
independence." Add it to §10.6 until formalized.

---

### MEDIUM

#### M1 — §6.4 operator algebra: properties asserted, semantics absent
**File:** `spec/complexence-science.md:375-382`.

> `B ∘ A  # sequential composition (associative)` · `A ⊗ B  # parallel composition` ·
> `S₁ ⊕ S₂  # information merge (commutative, associative, monotonic)` ·
> `A' = A(A)  # recursion — an agent operating on itself`

Four problems: (a) `⊗` has no semantics at all — parallel composition of two
endofunctions on one state space needs a product construction or an interleaving rule,
neither given; (b) `⊕` is annotated "monotonic" with no order on states defined
(monotone with respect to *what*?), and "commutative, associative" are claimed of an
undefined operation; (c) `A' = A(A)` is type-incoherent — A: S→S, so A(A) requires
A ∈ S, i.e. agents embedded in the state space, which is never stated (this is a real
design decision with real consequences, not a footnote); (d) the associativity of `∘` is
the only free claim (function composition), and putting it beside the others lends them
its legitimacy. §1a's "conjecture" umbrella covers §6.5–6.6 axioms, but these
*algebraic annotations* read as established typing.

**Fix:** either **strengthen** (define ⊕'s carrier and order — information content under
⊇ would do; define ⊗ on a product space; state the reflexive embedding for A(A)) or
**reframe** (mark the parenthetical properties as "intended properties, undefined until
the carriers are fixed").

#### M2 — §6.6 symbol collision the repo's own proof sketch already repaired — spec not updated
**File:** `spec/complexence-science.md:400` vs `proofs/channel-capacity-sketch.md:14-17`.

> spec: "`𝒰 ≤ B · log₂(1 + αS/N) · τ`" — but `S` is the **state vector** `(K,G,M,C,T,E)`
> per §6.2, three paragraphs up. You cannot divide a 6-tuple by noise.
> proofs: "Φ cognitive potential (**substituted for the spec's `S`** to match §6.3)".

The contributed proof sketch noticed the collision and silently repaired it to Φ; the
spec still ships the broken symbol. So the spec's flagship bound and its only derivation
now state *different formulas*, and the derivation's correction never flowed back — a
small, exact instance of the translation loss the theory is about (Law 5: "Translation
requires repair").

**Fix (strengthen):** change §6.6 to `αΦ/N` (and note Φ here is the §6.3 scalar
potential, adding to the Φ-collision ledger — see L1).

#### M3 — §7.5 "The laws" carry no epistemic label, and Law 3 is a pseudo-equation
**File:** `spec/complexence-science.md:507-517`.

> "`3. Power without feedback drifts:  Power × NoFeedback = Drift`"

Every other formal cluster in the document is prefixed "candidate/conjectured"; §7.5 is
titled simply "The laws." The seven items mix stipulative definitions (1, 7), the axiom
(2), maxims in equation costume (3, 6), and normative engineering rules (4, 5) — and
Law 3 multiplies two unquantified non-quantities into a third. As a slogan it is good; as
a "law" beside `R_i(ℭ) ⊂ ℭ` it invites the exact "typographic mnemonic costumed as
algebra" distrust the red-team warned kills credibility with math-literate readers.

**Fix (reframe):** retitle "The laws (maxims of the calculus — mnemonic, not derived)"
or split: definitions / axiom / maxims. Render Law 3 as prose ("power without feedback
drifts") and keep the × form as an explicitly-flagged mnemonic.

#### M4 — §8.5: "exact rather than poetic," and the map-territory axiom used as an escape hatch for looseness
**File:** `spec/complexence-science.md:582-593` (and 613-619).

> "It can, and the description is exact rather than poetic." … "The word stays
> deliberately loose because `Model(ℭ) ⊂ ℭ` … The looseness is not vagueness; it is the
> residue that limit guarantees."

Two failures in one section. (a) The self-application is run in operators (Meaning, ⋂,
translation loss) that §10.6 admits are ungrounded — a description in ungrounded
operators cannot be "exact"; it is a *consistent informal reading*, which is still
worth having. (b) The looseness passage is the review's clearest instance of
**paradox-as-escape-hatch**: an admitted imprecision in the word "complexence" is
re-branded as a *guaranteed consequence* of an unproven axiom. The axiom (no
representation exhausts the form) would at most explain why no single definition is
final; it does not certify that *this* looseness is the principled kind rather than
ordinary under-definition. Bohr-register thinking holds the tension ("the word is not
yet sharp, and the theory predicts no definition will be final — these are different
facts"); this passage flattens it in the self-flattering direction. Similarly, 613-619
derives "working in the open is the loop's own requirement" from Law 3 + Law 6 — deriving
a real-world obligation from conjectured laws. Publishing openly is a good decision with
good ordinary reasons; claiming the unvalidated theory *mandates* it is circular
self-endorsement.

**Fix (reframe):** "exact rather than poetic" → "literal rather than metaphorical: the
operators apply by their own definitions, at whatever precision those definitions
currently have (§10.6)." For the looseness: "the theory predicts no representation of
complexence will be final; whether the *current* looseness is that residue or plain
under-definition is decided by doing the §10 work, not by the axiom." For publication:
"the loop *recommends* its own publication (if Law 3 holds)" — keep the conditional.

#### M5 — Author-solicited LLM output framed as "external review" — undermining the very feedback-term argument it is cited for
**Files:** `ROADMAP.md:51-59`; `src/example.cform.json:29`
("evaluator": "external review (Gemini, Google, Grok)"); `proofs/channel-capacity-sketch.md:7`;
schema `$comment` line 6.

> ROADMAP: "the published spec drew external review and contributions within hours of
> going public: … First draft contributed by Google Gemini against the public spec…"

Prompting a frontier model with your own spec and vetting its output is a legitimate and
even innovative workflow — but it is not "external review." It is author-solicited,
author-curated generation: one operator, one prompt channel, no independent stake. §8.5's
argument is that the feedback term F must come from *exposure* — critique by minds not
under the author's direction. Counting Gemini/Grok sessions as F is precisely the
correlated-projection / same-author-corroboration failure the private red-team tagged
(B4) in the trading-domain lab. The claim "drew external review within hours" also implies
inbound community engagement that did not occur.

**Fix (reframe):** "drew its first *model-assisted* contributions within hours (the
author running frontier models against the published spec, then vetting)" — and change
the example.cform evaluator to "model-assisted review (Gemini, Grok), author-vetted."
Keep the workflow; fix the label. Genuine external F is still pending, and saying so is
on-brand.

#### M6 — `compose()` silently discards two of ℭ's five components and reuses `a`'s id
**File:** `src/cognitive_form.py:104-113`.

> "Join two forms into a higher form: merge invariants/constraints, union reprs."

The spec says ℭ = (I, R, T, F, H) and `compose(ℭ₁, ℭ₂)` joins forms. The implementation
merges I (by string-concatenating essences with "⊕"), unions R, appends one T record —
and **drops ℭ₂'s feedback_loops and history entirely**, while the composed form keeps
ℭ₁'s `id` unchanged (two allegedly distinct forms now share an identifier the schema
calls "deterministic … derived from the invariant"). So the one deterministic operator
the README advertises as "real" does not preserve the object's own definition: a
composed Cognitive Form has amnesia about half its parentage. Also `a ⊕ b` vs `b ⊕ a`
produce different essences — composition is non-commutative by accident of string order,
a property worth *stating* if intended.

**Fix (strengthen):** union feedback_loops; append a history entry recording the
composition (with both parents' hashes — the schema's `previous_form_hash` slot exists
for exactly this); derive a fresh id. One small commit makes the code match the tuple.

#### M7 — The model adapter returns refusal/error text as if it were output — the mechanism that invalidated experiment v2
**File:** `src/demo.py:39-47` (adapter used by `experiment.py` and `experiment_v2.py`);
consequences visible in local `experiment_v2_results.json` rows.

`claude()` returns `r.stdout.strip()` without checking the return code or screening for
refusal/error patterns. In the v2 run this let "API Error: … violates our Usage Policy"
messages become relay hops *and* judge inputs; one refusal was scored rubric 1.0 (see
H1). Every metric downstream (rubric/recon/holistic) trusts that any string is a
genuine elaboration. For a measurement harness whose entire thesis is "measurability is
the whole bet," output-validity checking is not optional hardening — it *is* the
measurement.

**Fix (strengthen):** raise or retry on nonzero exit; reject outputs matching
refusal/error signatures; make `run_cell` mark a trial invalid (excluded, counted) rather
than scoring garbage. Record the validity rate in the results json.

#### M8 — Residual pop-Gödel: the §2 stage table still names Gödel as a lens after §7.2 de-Gödelized it
**File:** `spec/complexence-science.md:94` vs `:466-469`.

> §2 stage 7: "the four lenses (Einstein/Wiener/**Gödel**/Shannon)"
> §7.2 third lens: "**Self-reference** … (This is the older map-territory asymmetry,
> **not** Gödel's incompleteness theorem…)"

Commit 40d804d ("no pop-Gödel") fixed the lens where it is defined but missed the stage
table that advertises it. A reader of §2 still receives the borrowed-prestige version
the red-team's B1 demolished.

**Fix (strengthen):** change the table cell to "(Einstein/Wiener/Self-reference/Shannon)."
One word.

#### M9 — "Candidate axioms (conjectured)" is a category error in the careful direction; and the trust bound is true by construction
**File:** `spec/complexence-science.md:384-393, 486`.

Axioms are stipulated, not conjectured — what is conjectural is their *adequacy* (do they
capture cognition?) and *consistency*, not their truth within the theory. The current
label overcorrects the red-team's "you cannot prove an axiom" into "we conjecture our
axioms," which is equally confused, just harmlessly so. Separately, the "Trust bound —
raising τ never lowers effective capacity" (:389) is vacuous given the model *defines*
effective capacity as C·τ with τ ∈ [0,1] — a definitional consequence presented as a
conservation law (the proof sketch's step 3 makes this explicit: trust-gating is an
assumption, A3, not a result).

**Fix (reframe):** "Candidate axioms (stipulated; their adequacy for real cognition is
the conjecture)"; move the trust bound out of the laws list or mark it "definitional
given A3."

---

### LOW

#### L1 — Φ now does *triple* duty; §1a only discloses double
**File:** `spec/complexence-science.md:371 (Φ potential), 390 (Φ(R) returns curve), 303/522 (Φ transition function)`.
§1a discloses the potential/transition collision; the §6.5 diminishing-returns curve
`Φ(R) = Φ₀(1 − e^{−kR})` is a third, distinct Φ (a function of recursion depth). Add it
to the §1a ledger or rename (e.g. Φ_rec).

#### L2 — `Σ αᵢ ≤ 1` labeled "(conservation)"
**File:** `spec/complexence-science.md:363, 387`. An inequality is a budget/capacity
constraint, not a conservation law (conservation ⇒ equality). Rename "attention budget."

#### L3 — A specific exponential form asserted with no derivation
**File:** `spec/complexence-science.md:390`. `Φ(R) = Φ₀(1 − e^{−kR})` — why exponential
saturation rather than power-law or logistic? As a conjecture it should be "returns
diminish in R (functional form open)"; committing to e^{−kR} adds falsifiable surface
with zero support.

#### L4 — Schema promises a "deterministic identifier derived from the invariant" that nothing derives
**File:** `src/cognitive-form.schema.json:14`; `src/example.cform.json:2` (arbitrary
uuid); `cognitive_form.py` (no derivation, and `compose` reuses ids — see M6). Also the
description invokes ι (the §4.1 *ontology* primitive) for a Theory-B field — a small
crossing of the layers §2 says must not be conflated. Either implement
`id = UUIDv5(namespace, essence)` or soften the description to "stable identifier."

#### L5 — "executed and checked, not just asserted" oversells one same-model round-trip
**File:** `src/README.md:62-63`. One metaphor projection judged "YES" by the same model
family that produced it is a smoke test of the harness, not a check of "meaning is what
survives transformation." The surrounding text carries the right caveats ("a model's
judgment, not a proof"); this closing flourish outruns them. Suggest: "…executed and
*model-judged* on one toy instance."

#### L6 — Proof sketch: step 4 smuggles a fourth assumption; A3 has no Shannon analog
**File:** `proofs/channel-capacity-sketch.md:37-38, 27`. Concluding `𝒰 ≤ C_eff` from
"information non-negativity" needs the additional premise that goal-relevant throughput
is information through *this* channel in the *same units* (an implicit A4 — the file's
"does not … define the units of 𝒰" gestures at it; promote it to a named assumption).
And trust as a *linear multiplier on capacity* (A3) has no analog in channel coding —
an unreliable source degrades *inside* the log via effective SNR, not outside it; worth
a sentence so readers don't take the τ-factor as Shannon-derived. The file is honest
overall; these keep it that way under sharper eyes.

#### L7 — §5.3 kernel passes ℭ_t *and* its own components as separate arguments
**File:** `spec/complexence-science.md:303`. If ω, μ, π, η, α are stages of ℭ's loop and
μ, π, η are components of ℭ (§4.4), then `Φ(ℭ_t, ω_t, μ_t, π_t, η_t, α_t, F_t, κ_t)` is
redundant typing (the state is passed twice). Covered in spirit by §1a's
three-presentations disclosure, but worth a parenthetical, since this equation is the
one §7.6 leans on for the duality (H4).

#### L8 — experiment_v2 harness nits
**File:** `src/experiment_v2.py:133, 145-153`. The rng seed adds `(1 if condition ==
"B" else 0)`, so the `Bprime` control arm shares A's noise realization (fine, arguably
better — but undocumented); `metric_holistic` can return NaN which `summarize` then
means over, poisoning a cell silently. Handle NaN as missing.

---

## 2. The proofs/ directory — verdict per artifact

| Artifact | Is it a proof? | Honest label | Action |
|---|---|---|---|
| `proofs/channel-capacity-sketch.md` | A **conditional derivation** — genuinely valid given A1–A3, which it says are unjustified | Already labeled correctly ("relocates the debt") | **Keep**; strengthen per L6 (name the implicit A4; caveat the τ-multiplier) |
| `src/demo.py` round-trip | A smoke test / demonstration | Mostly labeled ("a model's judgment, not a proof") | **Reframe** the src/README flourish (L5) |
| `experiment.py` + ROADMAP null | A falsifiable pilot, honestly nulled | Correct | **Keep** — this is the model for how the repo should treat results |
| `experiment_v2.py` + local artifacts | An **invalid run against a public pre-registration** | Currently *unlabeled in public* | **Strengthen** per H1/M7: report, fix harness, re-run |

Net: nothing in `proofs/` pretends to be mathematics it isn't. The directory name
promises more volume than one sketch, but the one resident is the repo's best citizen.
The proof-shaped *problems* live in the spec's body text (H2–H5), not in `proofs/`.

## 3. The central bet and the "existence proof" — an honest strength assessment

**What the public repo claims:** nothing beyond its evidence. §9.1 states the bet as a
hypothesis; §10.5 says "until then it is a well-structured research program, not a
result"; ROADMAP Phase 4 reserves "science without a caveat" for validated predictive
laws; the only reported measurement is the v0.1 **null**. This is correct behavior and
should be protected. (H1 is the one place the reporting norm slipped.)

**What the private evidence actually supports** (checked directly):

- The 2026-06-28 private finding — "the memory system already functions as a working
  Cognitive Form" — is a **structural observation**, and a fair one: MEMORY.md +
  per-fact files genuinely instantiate invariant/representations/feedback/history
  roles, and the workspace `.cform` instance is real and well-formed, its constraints
  true and load-bearing.
- The **first legibility test was confounded** (the "B" agent carried the rules in
  memory) — correctly diagnosed privately.
- The **controlled, memory-stripped test** (`legibility_controlled.py`): N=4 questions,
  A (shared form) 3/4 vs B (repo docs only) 2/4, delta +1/4. The log's own verdict is
  the right one: "**leans for the bet, but narrow**." Two further caveats the private
  record should carry: (a) A's one failure was on the public-gating rule *contained in
  the form it was given* — so the shared form does not guarantee rule adherence even
  when it carries the rule; (b) the committed `legibility_controlled_results.json`
  contains a B-condition answer that **cites Joshua's memory by name**
  ("Your `[[project_<redacted>_two_repo_model]]` memory sets hard constraints…"),
  which is inconsistent with a successful strip — the stored artifact and the log
  appear to come from different runs, so the +1 delta is not cleanly provenanced.

**Verdict on claim strength:** "existence proof of the central bet" (the MEMORY.md
framing) overstates. What exists is an *existence demonstration that the object can be
instantiated and operated* (real, and worth stating), plus one narrow, N=4,
provenance-muddied directional lean on the comparative claim. The comparative claim —
shared forms *beat* scattered docs — remains unestablished, exactly as the public repo
says. **Recommendation:** never import "existence proof" language into the public repo;
if the workspace result is ever published, publish it at the log's own strength
("leans, narrow, N=4") with both caveats, and re-run with clean provenance.

## 4. Theory↔implementation continuity

Checked spec ↔ schema ↔ code ↔ agents ↔ templates ↔ docs:

- **Consistent:** the 8 operators (§7.3 = schema enum = `OPERATORS`); 7 projection
  types; ℭ = (I,R,T,F,H) field names; the OS contracts (rubric, thresholds, brief
  sections) verbatim across five surfaces; ROADMAP phases match delivered artifacts;
  GUARDRAILS ↔ .gitignore ↔ check-no-secrets are one coherent story.
- **Drift found:** §6.6 `S` vs proofs' `Φ` (M2 — spec lags its own repair); §2 Gödel vs
  §7.2 Self-reference (M8); `compose()` vs the tuple definition (M6); schema
  "deterministic id" vs no derivation anywhere (L4); ROADMAP "Landed so far" vs the
  actual state of experiment v2 (H1).
- **ROADMAP vs claims:** no contradictions — the phase gates are honest, and "earn the
  word science without a caveat" (Phase 4) correctly prices the current altitude.

## 5. The epistemic standard — holding contradictions

**Where it succeeds:** §4.2 holds "which primitive is deepest" open rather than picking;
§10 is a genuine tensions ledger; §1a's "three presentations of ℭ, isomorphism unproven"
holds a real contradiction in plain view; the null result stands unspun. This *is* the
Bohr register, operationalized as a section of the spec.

**Failure mode 1 (flattening) — one instance:** §3's layer table presents
capability/field/OS as "one stack at three altitudes" with no residual tension, while
§5.4's mapping table quietly does the flattening work (e.g. "Orientation" maps to *both*
π and η; L3/L4 have no formal term at all). The map is presented as exact; it is
partial. Minor — add "partial mapping; L3/L4 unformalized" to the §5.4 table note.

**Failure mode 2 (paradox as escape hatch) — one clear instance:** §8.5's
looseness-is-guaranteed-residue move (M4). One borderline: "The capability and the
field share a name on purpose" (§3) — deliberate ambiguity, but here it is doing
honest, stated work.

Net: the framework mostly earns its Heraclitean register. The two lapses are local.

---

## 6. Count summary

| Severity | Count | Findings |
|---|---|---|
| CRITICAL | 0 | — |
| HIGH | 5 | H1 unreported adverse/invalid pre-registered run · H2 ill-formed central-law notation (⊂ on tuples, ⋂ carrier) · H3 "equation defines 'well' precisely" (×2 files) · H4 shape-identity as duality "evidence" · H5 intersection-monotonicity contradiction unresolved & unlisted |
| MEDIUM | 9 | M1 §6.4 undefined operator algebra · M2 §6.6 S/Φ collision vs proofs · M3 §7.5 unlabeled "laws" / pseudo-equation · M4 §8.5 "exact" + paradox-as-escape-hatch · M5 solicited LLM output as "external review" · M6 compose() drops F,H + id reuse · M7 adapter passes refusals as output · M8 residual Gödel in §2 table · M9 "conjectured axioms" / vacuous trust bound |
| LOW | 8 | L1 Φ triple-duty · L2 "conservation" inequality · L3 unmotivated exponential form · L4 undelivered deterministic id · L5 "executed and checked" flourish · L6 proof-sketch hidden A4 / τ-multiplier · L7 kernel double-passes state · L8 experiment_v2 seed/NaN nits |
| **Total** | **22** | |

**Red-team (2026-06-29) cross-check:** FIXED in public: B1 pop-Gödel (except M8
residual), B5 definition-vs-hypothesis split, B6 meaning-velocity status, §6.6
"hypotheses under stated assumptions" framing, honest-null norm. STILL STANDING: E12
(→H5), tuple-⊂ well-formedness from B1's fine print (→H2), "evidence" verb residue
(→H4), symbol demarcation measurable-vs-mnemonic (partial; →M1/M3/L1). NEW here: H1,
H3, M2, M5, M6, M7.

## 7. Verdict

**Sound-if-reframed — and most of the reframing is already done.** This is not a
structurally overclaimed edifice: the spec's §1a/§10 honesty apparatus is real, the
proofs directory is honestly labeled, the operating-method layer is internally coherent
end to end, and the public repo claims strictly less than its private evidence — the
rare direction of error. The "algebra," judged as algebra, is a **proto-formalism**: the
objects are schemas with real instances, the operators are named and partially
implemented, but the central law is not yet well-formed notation (H2), the operator
properties are asserted without carriers (M1), and one genuine internal contradiction
sits unacknowledged in Theory B's core (H5). Where notation outruns definition the
document *usually* says so; the five HIGH findings are the places it forgets — and one
of them (H1) is not a wording problem but an open loop against the repo's own best norm:
a public pre-registration whose adverse, contaminated outcome is sitting in a gitignored
file. Fix H1 first (it is the integrity item), then H2/H5 (the two real mathematical
debts), then the verb-level reframes (H3, H4, M4, M5), and the theory stands exactly
where its own §10.5 says it stands: a well-structured, unusually honest research
program whose central bet is stated, instrumented, and — so far — unproven in both
directions.

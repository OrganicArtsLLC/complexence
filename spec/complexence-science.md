# The Science of Complexence

**The formal foundation under the [Complexence capability](./complexence-capability.md)
and [Complexence OS](./complexence-os.md): the forms, transformations, and
navigation of complexity, studied independent of domain.** A foundational ontology,
a recursive cognitive equation, two complementary calculi, and a falsifiable
research program.

**Status:** Public, versioned, evolving. This is an open **research program**, not
a finished science (see §10) — published openly because the theory itself says so
(§8.5: a foundation developed without feedback drifts). Improve it, fork it,
falsify it; the prose is **CC BY 4.0**, the code (when it lands) **MIT**.

> Reader's narrative version: the essay
> [*The Science of Complexence*](https://joshuaayson.com/2026/06/28/science-of-complexence/).
> This document is the canonical formal spec that essay points at.
> The raw exploratory dialogue behind it is kept private.

---

## Table of Contents

- [1. What this document is](#1-what-this-document-is)
- [2. How the inquiry evolved](#2-how-the-inquiry-evolved)
- [3. Positioning: complexence as a field](#3-positioning-complexence-as-a-field)
- [4. The foundational ontology](#4-the-foundational-ontology)
- [5. The recursive cognitive equation](#5-the-recursive-cognitive-equation)
- [6. Theory A — the Metacognitive Calculus](#6-theory-a--the-metacognitive-calculus)
- [7. Theory B — the Calculus of Cognitive Forms](#7-theory-b--the-calculus-of-cognitive-forms)
- [8. The human-machine layer](#8-the-human-machine-layer)
- [9. Research program](#9-research-program)
- [10. Open questions and tensions](#10-open-questions-and-tensions)
- [11. Relations](#11-relations)

---

## 1. What this document is

The work began as a raw, chronological exploratory dialogue (kept private). It was
valuable but unstructured: it looped,
renames itself several times, and reaches the same ideas from different angles.
This document is the **distilled version** — the same intellectual content
organized so it can be built on, cited, and falsified.

Three things came out of the dialogue that are worth keeping:

1. **A field claim** — that there is a level *above* mathematics and logic: a
   formal study of cognitive structure, named **complexence**.
2. **Two complementary theories** — a *measurable* science of cognitive
   amplification (the **Metacognitive Calculus**) and a *structural* algebra of
   meaning (the **Calculus of Cognitive Forms**). (A Cognitive Form is meaning
   kept separate from any one way of writing it down — the same idea whether it
   appears as an essay, a diagram, or code. Defined in §7.)
3. **One foundational ontology** — a minimal generative stack of primitives
   (potential through agency) from which both theories can be built.

The raw dialogue is kept private as the historical record. This document is the
canonical public scientific reference.

---

## 1a. Status, scope, and notation (read this first)

This is a **research program**, not a finished science (see §10). Three scoping
rules hold throughout, so the rest of the document is read at the right altitude:

1. **Stages differ.** The ontology (§4) and the recursive equation (§5) are the
   stable core. The two calculi (§6, §7) are **candidate formalizations** — their
   "axioms," "theorems," and bounds are conjectures and proof-sketches under
   development, not established results, even where the prose states them plainly.
   Read §6 and §7 as proposals to be proven or falsified (§9), not as proofs.
2. **Notation is scoped per theory and not yet unified.** Some symbols are reused
   across theories with different meanings — most importantly **α** (agency in the
   ontology, §4.1; attention in the Metacognitive Calculus, §6.3) and **Φ** (a
   scalar potential in §6.3; the state-transition function in §5.3 / §7.6). Context
   disambiguates; a single unified notation is open work (§10).
3. **ℭ has more than one presentation.** §4.4, §5.3, and §7.1 give different
   component lists for the Cognitive Form. They are intended as views of one object,
   but the isomorphism between them is unproven and is part of the central open
   duality (§10.2).

## 2. How the inquiry evolved

The dialogue moved through ten recognizable stages. Tracking the arc matters
because each turn was a correction of the previous one — the final position is
the residue of those corrections.

| Stage | Move | What it produced |
|---|---|---|
| 1 | "What sits above mathematics?" | The premise: a language for cognition itself |
| 2 | Name the field | **Complexence** — forms, transformations, navigation of complexity, domain-independent |
| 3 | Demand Shannon-style rigor | **Metacognitive Calculus** — measurable quantities, axioms, conservation laws |
| 4 | "Deep research" pass | Foundations (Shannon, Kolmogorov, Turing, ACT-R/Soar, Minsky), theorems, experiments |
| 5 | Reframe the north star | Human-machine *meaning transfer*; the metric is **meaning velocity** (Δmeaning/Δtime) |
| 6 | Introduce representation invariance | Pivot from equations to **Cognitive Forms** — meaning independent of representation |
| 7 | Distill the law | "Meaning is what survives transformation"; the four lenses (Einstein/Wiener/Self-reference/Shannon) |
| 8 | Full formalization | **The Calculus of Cognitive Forms** — principles, axioms, theorems, laws |
| 9 | Make it practical | The **Cognitive Compiler**; cognitive forms as the "AST of thought" (AST = abstract syntax tree — the structure a compiler keeps after it throws away your exact wording); **Complexence OS** |
| 10 | Go beneath cognition | The **foundational ontology**: potential → ... → agency, as a *recursive graph*, not a line |

The two most important corrections, made late, are load-bearing:

- **Ontology is not processing.** The emergence of a *world* (potential →
  distinction → identity → relation → structure) is a different chain from the
  operation of a *mind within it* (observation → memory → prediction → meaning →
  agency). Earlier drafts conflated them.
- **Cognition is a loop, not a pipeline.** The mature form is a recursive
  directed graph closed by feedback, not a one-way derivation ending in
  "meaning" or "agency."

---

## 3. Positioning: complexence as a field

The opening claim: just as mathematics sits above arithmetic and metamathematics
sits above mathematics, there is an under-formalized level above both —
**a formal study of cognitive structure**.

```text
quantity      → mathematics
truth         → logic
computation   → computer science
cognitive structure → COMPLEXENCE
```

That's the claim, and it's one person's bet, not a consensus — §3a says what the
neighbors already cover, and §10 says what this still owes.

Complexence (the field) studies the **forms, transformations, and navigation of
complexity independent of any particular domain**. Its primitives are not numbers
or propositions but cognitive entities: agent, goal, map, state, belief,
constraint, observation, signal, pattern, context, transformation, boundary.

This field claim sits on top of the existing capability stack and gives it a
theoretical floor:

| Layer | Name | Function | This document |
|---|---|---|---|
| Mission | Making Complexity Visible | Make system state legible | — |
| Framework | Coherent Complexity | Legibility without reductionism | — |
| Capability | [Complexence](./complexence-capability.md) | Orient and navigate under load | the human capability |
| Operating | [Complexence OS](./complexence-os.md) | Convert thought into artifacts | the runtime |
| **Foundation** | **Complexence (the field)** | **Formal study of cognitive structure** | **this document** |

The capability and the field share a name on purpose: the field is the science of
the thing the capability does.

---

## 3a. Relation to prior work — what it shares, what is distinct

A claim to a level above mathematics, logic, and computer science (§3) has obvious
neighbors, and the honest move is to name them and say what is shared and what is
new. The differentiation is a positioning claim to be *earned* by what Complexence
predicts or unifies that extensions of these do not — the central bet (§9) is one
such test — but the lines are stateable now.

- **Active Inference / the Free Energy Principle (Friston).** The closest neighbor: a
  formal, recursive perception–action loop in which an agent minimizes variational
  free energy (surprise) through a generative model and belief updating. *Shared:*
  the recursive loop, prediction, feedback, the agent-in-a-world. *Distinct:* the
  Free Energy Principle theorizes how **one** agent's inference minimizes surprise,
  in Bayesian mechanics over belief states; Complexence studies cognitive
  **structure** domain- and substrate-independently across humans, machines, and
  teams. Its object is the **Cognitive Form** — meaning invariant across
  representations (§7) — which has no analog in Active Inference: that framework does
  not theorize "the same meaning across text, diagram, code, and agent." Its figure
  of merit is **meaning transfer between minds** (§8), not one agent's surprise. The
  clean relation: Active Inference is a candidate theory of the *dynamics inside one
  node* of the §5 loop; Complexence studies the forms moved around it. They compose;
  they do not compete.
- **OODA (Boyd's observe–orient–decide–act loop, from air combat).** *Shared:* the
  loop, and the centrality of Orientation (the L0–L7
  map is orientation-heavy by design). *Distinct:* OODA is an informal strategic
  heuristic — no ontology, no recursive equation, no representation-invariance, no
  measurable quantities. The §5 loop is OODA's structure made formal; Theory B adds
  the meaning layer it never had. OODA is the human strategic loop as a special case.
- **Cynefin (Snowden).** *Shared:* navigating complexity, context-sensitivity.
  *Distinct:* Cynefin classifies a situation's complexity regime so you know *how* to
  act; Complexence is the process (loop + forms) you run *within* any regime. Cynefin
  classifies the terrain; Complexence is how you navigate it.
- **Cybernetics and predictive processing.** *Shared:* feedback-as-regulation
  (Ashby's requisite variety is the ancestor of `Power × NoFeedback → Drift`) and
  prediction-error minimization. *Distinct:* the representation-invariance and
  meaning-velocity layers are in neither.
- **Category theory and Laws of Form.** *Resonant, and a formalization target.* The
  Cognitive Form — an invariant under projection, with projections that preserve it —
  is category-theoretic in flavor (objects, structure-preserving maps); giving Theory
  B precise categorical semantics is open, high-leverage work (§10). The ontology
  begins at **distinction** (Δ, §4.1), Spencer-Brown's primitive in *Laws of Form*;
  connecting the two is a live thread.

**The distinct claim, in one line.** What Complexence asserts that the neighbors do
not is a *domain-independent study of cognitive structure whose central object is the
representation-invariant form and whose figure of merit is meaning transfer between
human and machine minds.* The loop it shares with everyone; the **Cognitive Form and
meaning velocity are the new ground**, and the field stands or falls on whether they
buy predictions the neighbors cannot make (§9, §10).

---

## 4. The foundational ontology

The deepest question the dialogue reached: *what must exist before cognition is
even possible?* The answer is a generative stack of primitives. The corrected
version separates three layers.

### 4.1 The primitive stack (three layers)

**Layer A — Ontology (what can exist).** Timeless. The emergence of a structured
world.

| Symbol | Primitive | Meaning |
|---|---|---|
| ◇ | Potential | The possibility space prior to any distinction |
| Δ | Distinction | `A ≠ B`; the first mark |
| β | Boundary | Where one distinction ends and another begins |
| ι | Identity | Persistent boundary |
| ρ | Relation | Structured difference between identities |
| Σ | Structure | A configuration of identities and relations (no time yet) |

**Layer B — Dynamics (how things change).** Introduces ordering/time.

| Symbol | Primitive | Meaning |
|---|---|---|
| χ | Ordering | Sequence; the precondition for transformation |
| τ | Transformation | `Σ_t → Σ_{t+1}` |
| κ | Constraint | Limits which transformations are possible |

**Layer C — Cognition (how systems learn).** A mind *within* the world.

| Symbol | Primitive | Meaning |
|---|---|---|
| ω | Observation | Agent-dependent reading of structure |
| μ | Memory | Retained trace of transformation/observation |
| π | Prediction | Memory projected forward under constraint |
| F | Feedback | Consequence returned to the system |
| η | Meaning | Consequence-bearing prediction; constraint on possible futures |
| α | Agency | Meaning capable of constrained action |

### 4.2 Two candidate "deepest" primitives

The dialogue did not settle which primitive is truly first. Two strong
candidates, kept as an open question (see §10):

- **Potential (◇)** — nothing can be distinguished until it is possible.
- **Constraint (κ)** — physics, computation, evolution, and inference are all
  increasingly described as *lawful constraint*; identity, relation, and
  transformation may be special cases of constraint.

### 4.3 The three tests a foundation must pass

A primitive set is only worth defending if it is:

1. **Minimal** — no primitive can be removed without losing expressive power.
2. **Generative** — every higher concept (agents, goals, language, teams, AI,
   civilizations) can be composed from the primitives.
3. **Empirically useful** — it makes new predictions or enables better tools
   (interfaces, multi-agent coordination, instruments).

This is the bar that separates a foundational language from elegant notation.

### 4.4 Defining a cognitive form from the primitives

A **Cognitive Form** emerges only when the primitives become mutually bound:

```text
ℭ = Bind( ι, ρ, τ, κ, μ, π, η, R, F )
```

where `R` is the set of representations and `F` is feedback. Identity alone is
static; relation alone is structure; transformation alone is change. None is
cognition. Bound together — so the system can hold identity, change state,
remember the change, predict the next change, appear in a representation, and
correct itself by consequence — they are the minimal pattern of cognition.

---

## 5. The recursive cognitive equation

The candidate unifying structure. Both theories below are *conjectured* to be
special cases of one recursive state-transition system; establishing that duality is
the central open theorem (§10.2). This is the mature, non-linear form.

### 5.1 The loop

```text
Σ  →  ω  →  μ  →  π  →  η  →  α  →  τ(Σ)  →  Σ′  ↺
```

> Structure is observed; observation updates memory; memory projects prediction;
> prediction under consequence becomes meaning; meaning under choice becomes
> agency; agency transforms structure; the new structure is observed again.

### 5.2 The system of equations

```text
ω_t     = Obs( Σ_t, α_t )                  # observation is agent-relative
μ_{t+1} = Update( μ_t, ω_t, F_t )          # memory absorbs observation + consequence
π_{t+1} = Predict( μ_{t+1}, κ_t )          # prediction under constraint
η_t     = Meaning( π_t, F_t, G_t )         # meaning relative to feedback and goal
α_{t+1} = Choose( η_t, π_t, κ_t )          # agency = constrained choice
Σ_{t+1} = Transform( Σ_t, α_{t+1}, κ_t )   # action changes structure
```

### 5.3 The compact kernel

```text
ℭ_{t+1} = Φ( ℭ_t, ω_t, μ_t, π_t, η_t, α_t, F_t, κ_t )
```

In words: **cognition is the recursive transformation of meaning-bearing forms
across representations, through memory, prediction, feedback, and constraint.**

### 5.4 Bridge to the existing orientation loop

This equation is the formal expression of the [Complexence](./complexence-capability.md)
orientation loop and its eight-level map. The capability doc already states the
loop in human terms; this is the same loop in formal terms.

| Orientation loop (capability) | Map level | Formal term (§5.2) |
|---|---|---|
| Perception | L1 Signals | `ω` Observation |
| Mapping | L2 Structure | `Σ` Structure |
| Orientation | L5 Orientation state | `π`, `η` Prediction, Meaning |
| Decision | L6 Navigation options | `η → α` Meaning to choice |
| Action | L7 Execution | `α → τ(Σ)` Agency transforms structure |
| Feedback / Learning | L7 Learning | `F`, `μ` Feedback, Memory update |

The capability is the loop run well, under load, by a person. The equation states
the loop formally; what running it *well* means is the open measurement question
of Theory A (§6, §10.5).

---

## 6. Theory A — the Metacognitive Calculus

The **measurable** theory. Built in the spirit of Shannon: ignore *what* an agent
thinks about, formalize *how* cognition transforms information under constraint,
and define quantities that can be estimated from data.

### 6.1 Axiom 0 — cognition is transformation

A cognitive system is defined solely by its ability to transform states:

```text
A : S_t → S_{t+1}
```

### 6.2 The state vector

```text
S = (K, G, M, C, T, E)
```

- **K** Knowledge (beliefs, world model — declarative)
- **G** Goals (objectives — procedural)
- **M** Memory (working + long-term)
- **C** Constraints (internal load + external rules)
- **T** Tools / capabilities (internal modules + external aids)
- **E** Environment (relevant external state)

### 6.3 Measurable quantities

These are the candidate "Shannon entropies" of the theory — each is meant to be
operationalized (see §9).

| Quantity | Symbol | Reading |
|---|---|---|
| Attention | α | Fraction of resources on a task; `Σ αᵢ ≤ 1` (conservation) |
| Trust | τ | Reliability weight on a source; raises effective channel capacity |
| Bandwidth | B | Max information flow between parts (bits/s) |
| Noise | N | Uncertainty/error in a signal |
| Recursive depth | R | Levels of thinking-about-thinking |
| Externalization ratio | ε | Fraction of cognition offloaded to tools/agents |
| Cognitive throughput | 𝒰 | Goal-relevant transformations per unit time |
| Cognitive energy / potential | ℰ / Φ | Expected uncertainty reduction per unit cost; useful work remaining |
| **Meaning velocity** | — | **Δmeaning / Δtime** — the north-star metric (§8) |

### 6.4 Operators

```text
A(S)            # agent transform
B ∘ A           # sequential composition (associative)
A ⊗ B           # parallel composition
S₁ ⊕ S₂         # information merge (commutative, associative, monotonic)
Ω(A, S)         # amplification by external tools
A' = A(A)       # recursion — an agent operating on itself
```

### 6.5 Candidate axioms and conservation laws (conjectured)

- **Information non-negativity** — `I(S'; S) ≥ 0` for any transform.
- **Attention conservation** — `Σ αᵢ ≤ 1`; throughput splits, never multiplies.
- **Merge monotonicity** — `S₁ ⊕ S₂` carries at least as much information as either.
- **Trust bound** — for `0 ≤ τ ≤ 1`, raising τ never lowers effective capacity.
- **Recursion diminishing returns** — `Φ(R) = Φ₀(1 − e^{−kR})`.
- **Externalization trade-off** — `α + ε ≤ 1`; offloading frees internal focus
  only if attention is reallocated.

### 6.6 Shannon-style theorems (candidate bounds)

Stated as hypotheses to be proven under stated assumptions, not as established
results.

- **Cognitive channel capacity** — useful understanding is bounded:
  `𝒰 ≤ B · log₂(1 + αS/N) · τ`.
- **Conservation of cognitive effort** —
  `α·𝒰(α) + ε·𝒰_ext(ε) ≤ Φ` (a fixed cognitive budget).
- **Coordination efficiency** — for n agents,
  `𝒰_team ≤ Σ 𝒰ᵢ + γ Σ I_{ij}`, with coordination overhead `γ` causing
  sublinear scaling.
- **Meta-processing bound** — recursion `R` multiplies throughput by at most a
  sub-exponential factor `f(R)`; it prevents infinite regress from yielding
  unbounded gain.

### 6.7 Foundations it stands on

| Source | Contribution borrowed |
|---|---|
| Shannon | Channel capacity, entropy, noisy-channel limits |
| Kolmogorov / Chaitin | Minimal description length; knowledge has irreducible complexity |
| Turing / Church–Turing | Cognitive transforms are computable functions |
| Soar / ACT-R | Declarative vs procedural split (`K` vs `G`/skills) |
| Minsky (*Society of Mind*) | Cognition as interacting sub-agents/modules |
| LLM (large language model) scaling laws | Power-law performance vs resources; motivates a cognitive scaling law |

The cognitive scaling-law conjecture:
`𝒞 = f(I, A, M, X, R, F)` — capability scales not only with information `I` but
with attention `A`, memory `M`, external infrastructure `X`, recursion `R`, and
feedback quality `F`.

---

## 7. Theory B — the Calculus of Cognitive Forms

The **structural** theory. Where Theory A measures the *process*, Theory B
formalizes the *object* — meaning that survives changing representation.

### 7.1 The object

```text
ℭ = (I, R, T, F, H)
```

- **I** Invariant identity — what stays constant across representations
- **R** Representations — the forms it can take (text, math, diagram, code, agent…)
- **T** Transformations — what it can do
- **F** Feedback — how it corrects itself
- **H** History — its evolution over time

A representation is a **projection** `R_i = P_i(ℭ)`, and the projection is never
the form: `R_i(ℭ) ⊂ ℭ`. The map is not the territory; the equation is not the
concept; the prompt is not the agent.

**Notation note (read with §1a).** ℭ is a tuple, not a set, so as written `⊂` has
no defined sense here and the `⋂` in §7.2 has no constructed carrier — these
formulas are **candidate notation**: a picture of the intended claim, not yet set
theory. The intended reading, stated so the debt is payable: let `Sem` be a set of
*consequences for action under a goal*; let `Meaning : representations → 𝒫(Sem)`;
read `R_i ⊂ ℭ` as "`R_i` is a projection of ℭ that never exhausts it"
(`P_i(ℭ) = R_i` for some projection map `P_i`); then `I(ℭ) := ⋂_i Meaning(R_i)` is
a definition in `𝒫(Sem)`. `Sem` itself is not yet constructed — that is tracked in
§10.6, and until it is, the formulas carry the argument informally.

### 7.2 The central principle

> **Meaning is what survives transformation.**

```text
I(ℭ) = ⋂_i Meaning( R_i(ℭ) )
```

The identity of a form is the intersection of meaning across all its valid
projections. Here `Meaning(R)` is read operationally as the consequences a
representation entails for action under a goal — what it lets you predict and do;
grounding it precisely so the intersection is computable is open (§10). Four lenses
sharpen the principle:

- **Einstein** — the *invariant*: what stays true when the representation changes.
- **Wiener** — the *feedback loop*: how the form corrects itself through action.
- **Self-reference** — the *map-territory limit*: a model stands outside what it
  models, so no representation exhausts the form. (This is the older map-territory
  asymmetry, **not** Gödel's incompleteness theorem, which concerns provability,
  not containment.)
- **Shannon** — the *channel*: how much meaning survives transmission through noise.

### 7.3 Operators

```text
project(ℭ, repr)      # express meaning in a chosen form
translate(ℭ, i, j)    # move between representations
compress(ℭ)           # reduce form, preserve invariant
expand(ℭ)             # unfold hidden structure
compose(ℭ₁, ℭ₂)       # join forms into a higher form
reflect(ℭ)            # form operates on itself
execute(ℭ)            # turn meaning into action
correct(ℭ, F)         # update by feedback
```

### 7.4 Selected axioms and theorems

**Candidate axioms (abbreviated, conjectured):** every form has at least one representation; no
representation exhausts the form (`R_i(ℭ) ⊂ ℭ`); a translation is valid iff it
preserves invariant identity; any form in a changing environment degrades without
feedback; a self-referential system cannot fully represent itself
(`Model(ℭ) ⊂ ℭ`, the map-territory limit).

**Candidate theorems (proof sketches under development):**

- **Representation invariance** — if two representations preserve the same
  invariant, they express the same form.
- **Compression preservation** — a compression is valid iff identity survives it.
- **Translation loss** — every representation change risks meaning loss unless
  checked by feedback; `Loss(τ_{ij}) ≥ 0`.
- **Cognitive amplification** — externalizing/re-internalizing forms with
  preserved identity raises transformation capacity:
  `Amplification = (useful transformation output) / (internal effort)`.
- **Multiprojection clarity** — adding consistent projections sharpens the
  *boundary* of I(ℭ) — confidence that the surviving core is the true invariant —
  not its *content*, which weakly shrinks (an intersection can only hold or lose
  elements as projections are added). The theorem is about confidence, and holds
  only under projection *independence*; correlated projections (same author, same
  model family) can raise confidence spuriously. (Tracked as an open tension in
  §10.6.)
- **Executable meaning** — executable forms (prompt, workflow, agent, simulation)
  carry greater transformative density than descriptive ones.

### 7.5 The laws

```text
1. Meaning is invariance across transformation.
2. The map is a projection, not the form:        R_i(ℭ) ⊂ ℭ
3. Power without feedback drifts:                 Power × NoFeedback = Drift
4. Compression must preserve essence.
5. Translation requires repair.
6. Reflection without feedback hallucinates.
7. Execution reveals meaning:  Meaning(ℭ) = what ℭ makes possible.
```

### 7.6 The compact form

```text
ℭ_{t+1} = Φ_B( ℭ_t, R, T, F, H )
```

The same recursive pattern as the §5.3 kernel — next state as a function of current
state — though the two Φ's take different arguments (call them Φ_A and Φ_B; the
shared symbol is aspirational, per §1a). The resemblance is what *motivates* the
duality conjecture (§10.2); it is not evidence of it. Every discrete dynamical
system has this shape.

---

## 8. The human-machine layer

The applied purpose. The whole framework exists to formalize the **shared
operating layer between human and machine cognition**.

### 8.1 The amplification relation

```text
H ⊗ M ⊗ X → C⁺
```

- **H** human cognition
- **M** machine cognition
- **X** external tools, memory, agents, simulations
- **C⁺** amplified cognition

### 8.2 The metric

The object of interest is not tokens, prompts, or compute. It is:

```text
meaning velocity = Δmeaning / Δtime
```

A good cognitive system increases the rate at which useful meaning becomes
visible and actionable. The short version I keep coming back to: the mathematics
of working with minds that think back.

### 8.3 Cognitive forms as the canonical object

The practical claim: today's interface is low-bandwidth —
`thought → language → LLM → answer`. A richer interface constructs a **Cognitive
Form** first (intent, knowledge, constraints, desired projections, confidence,
unknowns), then projects it into essay, diagram, code, prompt, agent, workflow,
or simulation while preserving the invariant.

This makes the Cognitive Form to cognition what the **abstract syntax tree** is to
programming: a representation-independent structure from which many concrete
forms are derived. Humans edit it, LLMs reason over it, agents execute it,
software validates it, tools render it.

### 8.4 Relation to Complexence OS

[Complexence OS](./complexence-os.md) is the operating method where the Cognitive
Form is intended as the kernel object. Today the OS spec is markdown and prompt
contracts (roles, rubrics, cadence), not a runtime; the current partial
instantiation of Theory B is the reference implementation in `../src/` (the
`CognitiveForm` schema and operators), with the full projection/agent/memory/
feedback runtime still aspiration, driven by the recursive loop of §5. The capability (orient under load), the field
(this document), and the OS (the machine) are one stack at three altitudes.

### 8.5 The recursive case — complexence applied to itself

The framework must pass its own generativity test (§4.3): a foundational language
for cognitive structure should be able to describe its own development. It can, and
the description uses the calculus's own operators rather than metaphor — at
whatever precision those operators currently have (§10.6).

The complexence corpus — this document, the capability spec, the operating-system
spec, the public essays, the seed repository — is itself one Cognitive Form,
`ℭ_complexence`. Each document is a projection `R_i(ℭ)`: the formal foundation, the
L0–L7 map, the runtime spec, the voiced essay, the method seed. By the central law
(§7.2) the identity of complexence is the *intersection* of meaning across all of
them, and no single one exhausts it (`R_i(ℭ) ⊂ ℭ`). The word "complexence" is not
yet sharp, and the theory predicts no representation of it will ever be final
(`Model(ℭ) ⊂ ℭ`, the map-territory limit, §7.4). Those are two different facts:
whether the *current* looseness is that guaranteed residue or plain
under-definition is decided by doing the §10 work, not by the axiom.

Maintaining the corpus is therefore itself a complexence operation, run by the loop
of §5:

- the corpus is the structure `Σ` under observation;
- drift between projections — a public essay still encoding an older invariant than
  the private foundation — is **translation loss** (§7.4), the mechanism of Law 3,
  `Power × NoFeedback → Drift`;
- the repair is `correct(ℭ, F)`: re-project the lagging surfaces from the current
  invariant;
- adding *consistent* projections raises clarity (multiprojection clarity, §7.4),
  so aligning the essays, the spec, and the repo makes complexence itself clearer,
  not merely better-documented.

Two consequences follow.

1. **`reflect(ℭ)` is literal here.** Refining the definition of complexence is
   complexence executing on itself — the operator the calculus already names, not a
   metaphor laid over editing.
2. **The loop recommends its own publication.** `Power × NoFeedback → Drift`, and
   *reflection without feedback hallucinates* (Law 6): a foundation developed only
   in private accrues unchecked translation loss. The feedback term `F` is supplied
   by exposure — critique, use, falsification (§9). So working in the open isn't a
   marketing choice: *if* Law 3 holds, the loop recommends its own publication.
   (Publishing openly also has ordinary good reasons that need no theory.) What
   stays private is not the theory but the **un-projected source** (the raw
   dialogue, un-distilled notes) and what lies outside the form entirely
   (domain/market strategy, kept in a private strategy record).

---

## 9. Research program

What turns this from philosophy into science: measurable quantities and
falsifiable claims.

### 9.1 Central hypothesis

> Human-AI collaboration improves when cognition operates on
> representation-invariant Cognitive Forms rather than on independent documents,
> prompts, diagrams, and code artifacts.

### 9.2 Testable questions

1. Do Cognitive Forms reduce semantic drift across software artifacts over time?
2. Do multiple agents coordinate better through a shared Cognitive Form than
   through independent prompts?
3. Does preserving Cognitive Forms improve human↔AI knowledge transfer?
4. Can artifacts be regenerated from a canonical form with preserved consistency?
5. Does maintaining forms reduce documentation entropy on long-lived projects?

### 9.3 Candidate measures

| Measure | Symbol | Operationalization | Related construct |
|---|---|---|---|
| Throughput | 𝒰 | Accuracy-weighted tasks/sec (digit-symbol, N-back) | Processing speed |
| Attention | α | Dual-task performance cost | Resource allocation |
| Trust | τ | Multi-agent coordination payoff; survey | Behavioral trust |
| Bandwidth | B | Channel capacity from stimulus-rate sweeps | Shannon capacity |
| Noise | N | Response variance under distractors | Entropy |
| Externalization | ε | Performance with vs without tools | Cognitive offloading |
| Recursive depth | R | Number of meta-reasoning iterations | Metacognition |
| Meaning velocity | — | Useful decisions/artifacts per unit time | (novel) |

**Meaning velocity** has no off-the-shelf instrument, so it needs proxies.
Candidates, strongest first:

- **Shared-form vs. prompt coordination payoff** — N agents solving a task through a
  shared Cognitive Form vs. independent prompts; measure accuracy, latency, and
  semantic drift across rounds (the §9.4 multi-agent design). A direct, falsifiable
  test of the central bet (§9.1).
- **Time-to-usable-artifact** — capture → a durable artifact someone acts on.
- **Decision-relevant information gain per unit time** — uncertainty reduction about
  the *next action*, not raw information volume.
- **Compression-preservation** — does a compressed form still let an agent
  reconstruct the same decisions (§7.4)? Invariant per byte.
- **Semantic-drift rate** — how fast meaning degrades across representation hops
  without feedback (translation loss), measured over a corpus through time.

Start with the first; it is a test, not a vibe.

### 9.4 Experimental designs

- **Psychophysics** — vary information load; fit channel models to estimate `B`, `N`.
- **Dual-task** — split attention; infer `α`, `τ` from throughput drop.
- **Tool/augmentation** — solve tasks with vs without AI; measure `𝒰`, `ε`.
- **Multi-agent** — control communication bandwidth and trust; measure team
  performance vs individual baselines (coordination efficiency).
- **Load monitoring** — EEG/pupillometry to estimate `α`, `ℰ`.

### 9.5 Roadmap

- **Short term** — formal definitions + toy proofs under simplifying assumptions;
  single-agent experiments.
- **Medium term** — multi-agent benchmarks; refine measures; build the Cognitive
  Form interchange format.
- **Long term** — integrated cognitive-augmentation tooling (Complexence OS),
  benchmarks for "multi-agent cognition," validated cognitive scaling laws.

---

## 10. Open questions and tensions

Honest record of what is unresolved. These are the live research edges.

1. **Which primitive is deepest?** Potential, distinction, or constraint (§4.2).
   Resolving this fixes the bottom of the ontology.
2. **Are Theory A and Theory B dual?** Both compress to
   `ℭ_{t+1} = Φ(ℭ_t, …)`. Conjecture: the Metacognitive Calculus measures the
   *dynamics* of the loop; the Calculus of Cognitive Forms describes the *object*
   moved around the loop. A formal duality between them is the most important
   open theorem.
3. **Ontology vs processing.** The separation in §4 is asserted, not proven; the
   exact ordering of observation/memory/prediction is a design choice to be
   tested, not a fact.
4. **Linear vs recursive-graph form.** The linear "first sentence" is a teaching
   device; the mature object is a recursive directed graph. The graph needs a
   precise definition (nodes, edge types, fixed points).
5. **Measurability is the whole bet.** The framework only becomes science if
   `meaning velocity`, throughput, and trust can be estimated and shown to
   predict performance in humans, AIs, and hybrid teams. Until then it is a
   well-structured research program, not a result.
6. **The formalism's own logic is unverified — these are logical debts, distinct
   from the empirical bet above, and tracked openly.** Minimality and generativity
   (§4.3) are *claimed*, not demonstrated: no removal-test shows the primitive set
   is irreducible, and no worked composition derives goal, language, or agent from
   the primitives. The three presentations of ℭ (§4.4, §5.3, §7.1) need a unifying
   isomorphism. `Meaning()` (§7.2) needs an operational grounding to escape
   circularity. Goal `G` is used in §5.2 but is not yet built from the primitives.
   The notation overlaps (α, Φ) need a unified convention.
7. **The central law is not yet well-formed notation.** ℭ is a tuple, so
   `R_i(ℭ) ⊂ ℭ` uses `⊂` with no defined sense on tuples, and
   `I(ℭ) = ⋂_i Meaning(R_i)` needs a constructed common carrier before the
   intersection means anything. The intended reading is stated in the §7.1
   notation note (a carrier `Sem` of consequences-for-action, with
   `Meaning : representations → 𝒫(Sem)`); building `Sem` is the debt. Until then
   the three flagship formulas (§7.1, §7.2, §7.4's `Model(ℭ) ⊂ ℭ`) are candidate
   notation, not set theory.
8. **Intersection vs. clarity — an open tension in Theory B's core.** The
   identity `I(ℭ)` weakly *shrinks* as valid projections are added (that is what
   intersections do), while multiprojection clarity says a form gets *clearer*
   with more consistent projections. The working resolution, stated in §7.4 and
   not yet formalized: added projections sharpen *confidence* in the surviving
   core, not its *content* — and only under projection independence, which is
   exactly what fails when the projections share an author or a model family.
   Until formalized, this stands as a recorded contradiction, not a theorem.

---

## 11. Relations

- **Capability:** [`complexence-capability.md`](./complexence-capability.md) — the
  human capability and the eight-level orientation map this theory formalizes (§5.4).
- **Operating method:** [`complexence-os.md`](./complexence-os.md) — the runtime
  where the Cognitive Form is the kernel object (§8.4).
- **The layers:** [`../docs/layers.md`](../docs/layers.md) — how prompts become
  agents become an orchestrated runtime; this document is the floor beneath that ladder.
- **Public essays:** [*Complexence*](https://joshuaayson.com/2026/06/17/complexence/)
  (the capability), [*Complexence OS*](https://joshuaayson.com/2026/06/25/complexence-os/)
  (the machine), and [*The Science of Complexence*](https://joshuaayson.com/2026/06/28/science-of-complexence/)
  (this foundation, in narrative form).
- **Roadmap:** open questions (§10) and the research program (§9) are tracked in
  [`../ROADMAP.md`](../ROADMAP.md).

---

**Status:** v0.1 (research program). **Last Updated:** 2026-07-01. Licensed CC BY 4.0.

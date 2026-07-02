# Proof sketch — the Cognitive Channel Capacity bound (§6.6)

**Status:** Candidate derivation. It shows the §6.6 bound *follows from Shannon's
theorem under three explicit assumptions*. It does **not** establish the bound for
cognition, because the assumptions are themselves unjustified — it **relocates the
debt** from the inequality to its premises. Honest framing per `complexence-science.md`
§10. First sketch drafted by Google Gemini (the author ran the model against the
published spec — solicited, model-assisted), then vetted here.

## Claim

The Metacognitive Calculus conjectures (§6.6):

```
𝒰 ≤ B · log₂(1 + αΦ/N) · τ
```

where 𝒰 is cognitive throughput, B bandwidth, α attention, Φ cognitive potential
(substituted for the spec's `S` to match §6.3), N noise, τ trust.

## Assumptions (this is where the real work hides)

- **A1.** The cognitive channel is a discrete-time, memoryless channel under
  additive Gaussian noise `N`.
- **A2.** Attention `α ∈ [0,1]` acts as a linear power-scaling filter on cognitive
  potential, so effective signal power `P = αΦ`.
- **A3.** Trust `τ ∈ [0,1]` is a linear fidelity multiplier on the external→internal link.

None of A1–A3 is justified. A1 in particular ("cognition is a Gaussian channel") is
the open empirical question, not a given.

## Derivation (valid *given* A1–A3)

1. **Shannon grounding.** By the Noisy-Channel Coding Theorem, a channel of bandwidth
   `B`, signal power `P`, noise `N` has capacity `C = B · log₂(1 + P/N)`.
2. **Resource allocation (A2).** Substitute `P = αΦ`: `C = B · log₂(1 + αΦ/N)`.
3. **Trust gating (A3).** Scale by τ: `C_eff = C · τ`. (τ=1 → full capacity; τ=0 → zero.)
4. **Throughput bound.** By information non-negativity (§6.5), goal-relevant throughput
   cannot exceed effective capacity: `𝒰 ≤ C_eff = B · log₂(1 + αΦ/N) · τ`. ∎ (under A1–A3)

## What this does and does not buy

- **Does:** moves the bound from "asserted candidate" to "derivable under stated
  assumptions" — exactly what §6.6 asked for ("hypotheses to be proven under stated
  assumptions").
- **Does not:** justify A1–A3, define the units of 𝒰, or operationalize Φ and N in
  cognitive terms. Those are the next debts (§10), and they are the whole empirical bet.

## Next steps (open)

- Justify or replace A1 (is cognition channel-like? under what conditions?).
- Operationalize 𝒰, Φ, N with units and a measurement protocol (§9.4).
- Simulate the bound under fluctuating α, N to see if it predicts anything (a candidate
  Phase-2 experiment).

---

**Last Updated:** 2026-06-28. Licensed CC BY 4.0.

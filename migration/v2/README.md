# migration/v2 — the PROVEN v2 (our implementations, spec'd for the handoff agent)

*2026-08-14 · The mirror of patala's v2 blueprint, grounded in OUR proven lab. Patala spec'd the target
(16 products, LAYERS.yaml, ground-up plan); we PROVE the mechanisms and expand beyond it. This folder is
what the handoff agent builds from.*

---

## Reading hierarchy (for the agent who builds)

1. **`RECONCILIATION.md`** — patala's v2 spec ↔ our implementations (13/16 products proven).
2. **`PRODUCTS.md`** — the 16 products, each with our proven kernel + experiment + build guide.
3. **`EXPANSIONS.md`** — the 6 products/mechanisms beyond their plan (the compounding moats).
4. **`LAYERS.yaml`** — our codified layer contract (proven kernels per layer + needs-build).
5. **`../README.md`** — the migration folder overview.
6. **`../AGENTS.md` + `../TRACEABILITY-MAP.md`** — the axioms + how everything resolves.

---

## The one-line carry-forward

> Patala v2 spec'd a coherent system. We built 17 kernels + 51 experiments that PROVE the mechanisms
> for 13 of its 16 products — and discovered 6 more capabilities they didn't list. This folder hands the
> next agent the WHAT + HOW + PROOF for every product, so they can build + test properly.

## The verification (proofs are stored, not claimed)
- `../scripts/theatre-check-all.py` — 51 experiments audited; 24 PROVEN on real data, 27 mechanism-only, 0 unproven,
  0 unproven.
- `../data/references/theatre-proofs-all.json` — every proof record with a hash.
- `../data/references/experiments.json` — every experiment mapped to layer + vision + source.

## What the handoff agent does next
1. Build the **graduation test** (one claim through the whole stack on real IPVV evidence).
2. Build the 3 missing products: Essay, Commentary, Tokenization.
3. Close gap E (signed human attestation) + the remaining review gaps.
4. Then layer on the 6 EXPANSIONS (each already proven as a mechanism).

# RECONCILIATION — patala's v2 spec ↔ our proven lab

*2026-08-14 · The definitive map: for every patala v2 layer and product, WHAT we have proven in
`ip-graph`, WHICH kernel/experiment proves it, and WHETHER it's production-ready or needs the handoff
agent to finish building. Read this first.*

---

## A. THE V2 LAYERS ↔ OUR PROVEN KERNELS

| v2 layer (patala) | Our kernel | Proof (experiment) | Theatre verdict |
|-------------------|-----------|--------------------|-----------------|
| Source | (corpus) | `validate-dag` | PROVEN |
| DraftTranslation | — | `validate-products` (translation) | PROVEN |
| Tokenization | — | (needs build) | — |
| ArgumentOutline | `discovery.py`, `query.py` | `kernel-suite` | PROVEN |
| Translation | `translation.py` | `validate-products` | PROVEN |
| **TranslationProof** | `translation.py` | `validate-products` — the non-aggregate vector | **PROVEN (the moat)** |
| Commentary | — | (needs build) | — |
| Theme | `staleness.py`, `evolve.py` | `communities`, `evolve` | PROVEN-MECHANISM |
| **Argument** | `review.py`, `scholar_review.py` | `layer03-05`, `cross-review`, `review-bias` | **PROVEN** |
| Synthesis | `evolve.py` | `evolve` (MAP-Elites) | PROVEN-MECHANISM |
| Essay | — | (needs build) | — |
| **Lesson/Education** | `education.py`, `pedagogy.py` | `education-organism`, `pedagogy` | PROVEN-MECHANISM |

**The v2 "one kernel, one graph" principle** — we ALREADY have the kernels it names:
`epistemic` (identity/authority) · `review` (reducers) · `staleness` (staleness) · `schema`
(clear names/contracts) · `evolve` (derivation/evolution) · `agent_delivery` (gates). The v2 LAYERS.yaml
wants `kernel: patala_kernel {identity · derivation · authority · events · reducers · gates ·
staleness · projection}` — that's EXACTLY our 16-kernel stack.

---

## B. THE 16 PATALA PRODUCTS ↔ OUR PROOF

| # | Patala product | Our proven mechanism | Proof | Status |
|---|---|---------------------|-------|--------|
| 1 | Translation | `translation.py` vector | `validate-products` | PROVEN (needs IPVV data) |
| 2 | **Translation Proof** | `translation.py` non-aggregate vector | `validate-products` | **PROVEN — the moat** |
| 3 | Passage/Reading | `query.py` (KG2Code) | `kernel-suite` | PROVEN mechanism |
| 4 | Claim | `epistemic.py` envelope | `validate-stack` | PROVEN |
| 5 | Argument | `review.py` + `scholar_review.py` | `layer03-05`, `cross-review` | PROVEN |
| 6 | Crux | `experiment-crux-compiler` | crux-compiler | PROVEN |
| 7 | Review | `scholar_review.py` (cross-review + citecheck) | `kernel-suite` | PROVEN |
| 8 | Scholar Attestation | `agent_delivery.py` human gate | `validate-agent-delivery` | PROVEN-MECHANISM (needs signed auth) |
| 9 | Research Packet | `retrieval.py` (PathRAG/HippoRAG) + `query.py` | `layer10`, `kernel-suite` | PROVEN |
| 10 | Synthesis | `evolve.py` MAP-Elites | `validate-evolve` | PROVEN-MECHANISM |
| 11 | Essay/Explainer | — | (needs build) | — |
| 12 | Education/Understanding | `education.py` + `pedagogy.py` | `education-organism`, `pedagogy` | PROVEN-MECHANISM |
| 13 | Comparison | `experiment-claim-standardisation` | claim-standardisation | PROVEN |
| 14 | Audit | `theatre-check.py` + `theatre-check-all.py` | theatre-check | PROVEN |
| 15 | Dataset/Benchmark | `experiment-import-scifact` + matrix | import-scifact | PROVEN |
| 16 | Agent Context Bundle | `agent_delivery.py` + `retrieval.py` | `agent-delivery`, `layer10` | PROVEN |

**Summary: 13 of 16 patala products have a PROVEN mechanism in our lab.** 3 need building from scratch
(Essay, Commentary, Tokenization) — these are the handoff agent's build targets.

---

## C. WHAT THE HANDOFF AGENT MUST BUILD (from our proofs → production)

**P0 — the graduation test** (turns proofs into a real kernel): one claim through the whole stack on
real IPVV evidence (source→translation→proof→proposition→argument→review→attestation→synthesis→essay→
education→agent-bundle), then MUTATE the source and watch the organism react. `validate-stack.py` is the
seeded start.

**P1 — build the 3 missing patala products:**
- **Essay/Explainer** (#11) — compile the verified argument graph into a sentence-sourced essay
  (we have the synthesis kernels; need the essay projection).
- **Commentary** (#7 layer) — passage-local commentary over TranslationProof.
- **Tokenization** (#2 layer) — the L0 token floor (needs the Sanskrit stack: Vidyut).

**P1 — close the review gaps (signed attestation, context-paging, remaining adapters).**

---

## D. THE TRACEABILITY (every product → proof → repo)

For full repo→experiment→product traceability, see `../docs/GITHUB-TRACEABILITY.md` +
`../TRACEABILITY-MAP.md` + `../data/references/theatre-proofs-all.json`.

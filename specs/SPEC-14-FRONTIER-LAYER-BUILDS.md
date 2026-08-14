# FRONTIER BUILDS — Layer-by-Layer optimized construction for Pāṭala

*2026-08-14. For each of Pāṭala's 13 layers (from `docs/layers/`), the most frontier-optimized build
using our studied papers (SPEC-08 arXiv) + cloned repos (SPEC-07/09/11/12) + proven experiments
(`scripts/experiment-*.py`). Each entry: what to build · which borrowed mechanism · why it's frontier.
These are build specs, not vision — concrete and implementable.*

> **Grounding:** the layer docs already cite many of the repos we've read (knowledgeProvenance, Eigenius,
> Graphiti, SocraticKG, geometricengine, Stencila, CapiTainS, Saktumiva). This spec pulls the *frontier
> mechanism* for each — the algorithmic edge — from our research, and the *proven implementation* from
> our experiments.

---

## LAYER 00 — GOVERNANCE (constitution + axioms)

**Frontier build:** make the governing docs **machine-checkable**, not prose.
- **Mechanism:** Stencila-style one canonical YAML schema → compiled contracts (from patala's own
  SCHEMA-AUDIT finding).
- **From our work:** the epistemic envelope (`lib/epistemic.py`) IS the canonical schema; enforce it as
  the single contract via a schema-validator (like herdr's `component_digest`).
- **Why frontier:** kills schema-drift at the root; every layer compiles against one truth.

## LAYER 01 — INGESTION (sources → canonical objects)

**Frontier build:** the 5-adapter generalization test + proof-carrying import.
- **Mechanism:** RKA's backend adapters (openalex/crossref/arxiv/semantic-scholar) + our
  `ExternalRecord → CanonicalCandidate → Validation → Proposal → AcceptedObject` pipeline.
- **From our work:** `experiment-unified-epistemic.py` proves the validation path.
- **Why frontier:** one engine ingests Sanskrit + Western + Science — the generalization bet.

## LAYER 02 — ATLAS (canonical graph + storage)

**Frontier build:** content-addressed, deterministically-serialized, self-consistent graph.
- **Mechanism:** nano-graphrag stable-LCC + GraphML (proven) + SHA-256 content-addressing.
- **From our work:** `experiment-nano-stable-graph.py` gives byte-reproducible serialization.
- **Why frontier:** the graph is a compile-output, never a drifting second-DB (sage-wiki).

## LAYER 03 — FACTORY (the DAG compiler)

**Frontier build:** the canonical DAG as the incremental-rebuild + staleness engine.
- **Mechanism:** our `canonical-dag.yaml` + RKA blast-radius = one traversal for correctness AND speed.
- **From our work:** `experiment-rka-staleness.py` (retraction flags 8 layers) + `validate-dag.py`.
- **Why frontier:** staleness-walk = dependency-graph = rebuild-scheduler — one graph (SPEC-13 thesis).

## LAYER 04 — EVIDENCE (contracts + adapters + evals)

**Frontier build:** verifier ensemble with calibrated abstention.
- **Mechanism:** RefChecker/FActScore (atomic claims) + AlignScore (cheap entailment) + conformal
  prediction (abstain when uncertain) + TechGraphRAG evidence-sufficiency gate.
- **From our work:** the epistemic ceiling gates evidence (SPEC-02), tested in the argument graph.
- **Why frontier:** separates deterministic checks, cheap witnesses, expensive critics — only borderline
  cases escalate.

## LAYER 05 — RESEARCH / EPISTEMIC CORE (the moat)

**Frontier build:** executable, evidence-anchored ArgumentSynthesis.
- **Mechanism:** herdr reducer (promotion gate) + RKA staleness (self-maintenance) + KG2Code queries.
- **From our work:** `experiment-herdr-review.py` + `experiment-kg2code.py` + the AIF argument graph
  (`argument.json`).
- **Why frontier:** the upper projections (synthesis/essay/education = 0 today) become executable
  renderers over a self-consistent argument core.

## LAYER 06 — COMMENTARIAL GRAPH (secondary scholarship)

**Frontier build:** the two-graph (reality vs literature) + verifier-ensemble extraction.
- **Mechanism:** KORAL two-graph separation (primary vs interpretation) + SocraticKG/ORKG contribution
  abstraction + geometricengine hyperedge pattern.
- **From our work:** the epistemic envelope enforces `PRIMARY ≠ RATIÉ ≠ PĀṬALA ACCEPTS`.
- **Why frontier:** scholarly debate preserved without intellectual drift; analogy≠identity.

## LAYER 07 — VERIFICATION PLANE (external judge)

**Frontier build:** the two-plane architecture with conformal abstention + PathRAG evidence retrieval.
- **Mechanism:** Inspect AI runtime + RefChecker/AlignScore ensemble + conformal calibration +
  `experiment-pathrag.py` (retrieve evidence paths for the judge).
- **Why frontier:** every claim falsifiable; only genuine borderline cases reach expensive critics.

## LAYER 08 — HUMAN AUTHORITY (review/adjudication)

**Frontier build:** the herdr/Vouch gate, promoted to first-class.
- **Mechanism:** herdr reducer + ReviewPhase/FindingStatus + Vouch git-native gate + ReviewEvent ledger.
- **From our work:** `experiment-herdr-review.py` (thesis stays CORRECTION_REQUIRED until grounded).
- **Why frontier:** nothing promotes without evidence; human adjudication is the only path to the top
  ceiling (ADJUDICATED).

## LAYER 09 — ORGANISM (human understanding graph)

**Frontier build:** the Q-variable as structured epistemic data.
- **Mechanism:** Graphiti temporal user graph (episodes as provenance, validity periods, MCP) + pyBKT
  learner state + Knowledge Space Theory (prerequisites + outer fringe).
- **From our work:** the envelope generalizes user-beliefs to the same epistemic ladder.
- **Why frontier:** the second first-class graph makes the consumer app a sensor for understanding —
  the uncopyable moat variable.

## LAYER 10 — SURFACES (sites + APIs + products)

**Frontier build:** the Argument Map over compiled projections.
- **Mechanism:** Astro static + Cloudflare Workers (SPEC-00) + KG2Code query DSL over MCP +
  PathRAG/HippoRAG retrieval.
- **From our work:** `experiment-kg2code.py` (executable queries) + `experiment-hipporag.py` +
  `experiment-bounded-context.py` — the agent surface.
- **Why frontier:** zero-JS reading + one-request agent bundles + executable knowledge (Bet 2).

## LAYER 11 — ORG/ECONOMICS (scholar credit + market)

**Frontier build:** provenance-driven credit + the autonomous review institute economics.
- **Mechanism:** arcan event-sourcing (immutable history) + herdr publication gate + the universal
  schema's Task→Decision→Supersede chain.
- **Why frontier:** every contribution is attributable and versioned; credit flows from verified state.

## LAYER 12 — LIVE SYSTEM (agents · state · docs · staleness)

**Frontier build:** the epistemic work queue + scholar attestation vertical + staleness as first-class.
- **Mechanism:** the 7-piece live-system (per layer 12) + RKA review_queue (lexicographic policy) +
  arcan event-sourcing + our `STATE.yaml`/staleness propagation.
- **From our work:** `experiment-rka-staleness.py` + `experiment-unified-epistemic.py` — the loop closes.
- **Why frontier:** the whole system is self-describing and self-maintaining; agents advance layers via
  the vision→chunk→layer map.

---

## THE FRONTIER THREAD ACROSS ALL 13

Every layer resolves to the SAME two frontier mechanisms:
1. **Epistemic honesty** (SPEC-02 envelope + herdr reducer + RKA staleness) — correctness.
2. **Compile-once + content-address + executable retrieval** (SPEC-00 + KG2Code/PathRAG/HippoRAG) — speed.

And the unifying fact: **the dependency graph is simultaneously the staleness propagator, the
incremental-rebuild scheduler, and the retrieval index.** Each layer is a different projection of that
one graph. Build them in layer order 00→12, reusing `lib/` (epistemic, review, staleness, query,
retrieval) which we've already proven in experiments.

## Implementation status
- **Proven in experiments (promote to lib/ first):** epistemic, review (herdr), staleness (RKA), query
  (KG2Code), retrieval (PathRAG/HippoRAG/bounded-context), stable-graph (nano).
- **Designed:** all 13 layers' frontier mechanisms above.
- **Next:** `lib/` promotion (F3/F4 from SPEC-13) then the 5 import adapters (generalization test).

See `docs/ALGORITHMS.md`, `docs/EXPERIMENT-REPORT.md`, `specs/SPEC-13-STALENESS-PERFORMANCE.md` for proofs.

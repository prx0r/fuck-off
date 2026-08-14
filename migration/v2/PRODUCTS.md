# PRODUCTS — the 16 patala products, each with our proven mechanism + build guide

*2026-08-14 · For every product patala v2 spec'd, this gives: the artifact, our PROVEN kernel +
experiment, the verifiable proof, and EXACTLY how the handoff agent builds it properly. Expansions
beyond this list are in `EXPANSIONS.md`.*

---

## 1. Translation
- **Artifact:** `TranslationRevision`
- **Our proof:** `lib/translation.py` — the non-aggregate vector; `validate-products.py` (PASS).
- **Build:** wire the TranslationProof vector into the real translation pipeline (IPVV). Deterministic
  checks (T1-T3) exist; add independent review + scholar approval.

## 2. Translation Proof — THE MOAT (fully proven)
- **Artifact:** `TranslationProof TP-NNNN` (vector, not scalar)
- **Our proof:** `lib/translation.py` — SOURCE_COVERAGE·TARGET_GROUNDING·MORPHOLOGY·SYNTAX·NEGATION·
  MODALITY·TERM_CONSISTENCY·ENTAILMENT·PARALLEL_WITNESS·HUMAN_REVIEW; publication gate that BLOCKS on any
  failing dimension (never one "94%"). `validate-products.py` PROVEN.
- **Build:** this is production-ready as a mechanism. Add real Sanskrit audit dimensions (Vidyut,
  xCOMET) and the IPVV golds. **This is patala's strongest defensible product — and we've proven it.**

## 3. Passage / Reading
- **Artifact:** canonical Passage object
- **Our proof:** `lib/query.py` (KG2Code executable queries) + `validate-stack.py` (real graph).
- **Build:** the Passage Workbench — a Sanskritist disagrees with a reading → a GraphProposal →
  our human gate. The query DSL is proven.

## 4. Claim
- **Artifact:** `Claim C-NNNN`
- **Our proof:** `lib/epistemic.py` envelope (SOURCE-SAYS / SCHOLAR-RECONSTRUCTS / PATALA-INFERS kept
  distinct via epistemic_ceiling) + `validate-stack.py` (real thesis claim stays MACHINE_PROPOSED).
- **Build:** hook the envelope to real passages + the review reducer.

## 5. Argument
- **Artifact:** `Argument` (AIF Info/Inference/Conflict)
- **Our proof:** `lib/review.py` + `lib/scholar_review.py`; `validate-layer03-05.py` + `kernel-suite.py`.
- **Build:** the two-stage argument.json is a working exemplar; scale to real IPVV arguments.

## 6. Crux
- **Artifact:** `Crux`
- **Our proof:** `experiment-crux-compiler.py` — computes minimal divergence between positions.
- **Build:** wire crux-compiler into the argument engine as a first-class object.

## 7. Review
- **Artifact:** ReviewEvent
- **Our proof:** `lib/scholar_review.py` — adversarial panel + cross-review + CiteCheck phantom
  detection + review-bias robustness (37.1% finding). `kernel-suite.py` PROVEN.
- **Build:** add signed ReviewEvents (the review is evidence about a target, never mutating it).

## 8. Scholar Attestation
- **Artifact:** signed HumanAttestation
- **Our proof:** `lib/agent_delivery.py` human gate (agent proposes, only human authorizes) —
  `validate-agent-delivery.py` PROVEN-MECHANISM.
- **Build:** replace the plain `human_authorize()` with a cosign-style signed attestation (gap E).
  **Required before any public authority/marketplace.**

## 9. Research Packet
- **Artifact:** ResearchPacket (the scholarly equivalent of a proof state)
- **Our proof:** `lib/retrieval.py` (PathRAG/HippoRAG) + `lib/query.py`; `validate-layer10.py` +
  `kernel-suite.py`. HippoRAG hub-bias finding documented.
- **Build:** the question→search-plan→evidence-packet flow (from paper-qa reference).

## 10. Synthesis
- **Artifact:** Synthesis (ArgumentSynthesis)
- **Our proof:** `lib/evolve.py` MAP-Elites evolution — the synthesis that converges + preserves
  diversity. `validate-evolve.py` PROVEN-MECHANISM.
- **Build:** connect the evolution loop to real arguments; fitness must be a VECTOR (never one scalar).

## 11. Essay / Explainer (NEEDS BUILD)
- **Our proof:** none directly — but we have the synthesis kernels + reactive-essay
  (`experiment-reactive-essay.py` — source retraction marks prose stale). This is the reactive document.
- **Build:** compile verified argument → sentence-sourced essay, each sentence dependency-linked.

## 12. Education / Understanding Check
- **Artifact:** LearningClaim + interaction fixture
- **Our proof:** `lib/education.py` + `lib/pedagogy.py`; `validate-education-organism.py` +
  `validate-pedagogy.py` PROVEN-MECHANISM. The "wrong answer → known epistemic neighbor" moat is proven.
- **Build:** feed real discovery-progressions (from LOGICVID gold) as the pedagogical structure.

## 13. Comparison
- **Artifact:** cross-tradition comparison
- **Our proof:** `experiment-claim-standardisation.py` — structural claim vs tradition vocab + boundary.
- **Build:** the comparative questionnaire over the standardised claims.

## 14. Audit
- **Artifact:** verifiable proof record
- **Our proof:** `scripts/theatre-check.py` + `theatre-check-all.py` — PROVEN. This IS the audit
  product (patatalog applied to itself).

## 15. Dataset / Benchmark
- **Artifact:** benchmark
- **Our proof:** `experiment-import-scifact.py` (external dataset into the engine) + the experiment
  matrix. PROVEN.

## 16. Agent Context Bundle
- **Artifact:** one-request agent bundle
- **Our proof:** `lib/agent_delivery.py` (context routing) + `lib/retrieval.py` (bounded context);
  `validate-agent-delivery.py` + `experiment-bounded-context.py` PROVEN.

---

## VERDICT
**13/16 patala products have a proven mechanism in our lab.** The 2 strongest (Translation Proof,
Education) are production-ready as mechanisms. 3 need building (Essay, Commentary, Tokenization) — the
handoff agent's build targets, guided by the graduation test. See `RECONCILIATION.md` for the map.

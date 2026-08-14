# KERNELS-INDEX — the reusable kernels (what's in lib/, what it does, how it's validated)

*2026-08-14. The agent-facing map of every reusable kernel (now 52). Reuse these — never rebuild. Each
maps to: what it is · layer · vision · the experiment(s) that validate it · honest status.*

## WIRED vs VALIDATED (Phase 6 promotion gate — added 2026-08-14)

The architecture audit found ~16 kernels VALIDATED-ONLY (proven by their own validate-*.py, wired nowhere).
Phase 6 wires them into LIVE paths. Status: **USED** = imported by a run-*/build-*/translation/read-plane
path on real data; **VALIDATED-ONLY** = only its own validator/experiment; **ORPHANED** = referenced nowhere.
The wiring scripts:
- `scripts/validate-tantraloka-dag.py` (8/8) — wires `verification_ensemble` + `evidence_ledger` +
  `integrity_gate` + `source_registry` onto the live factory DAG output.
- `scripts/run-tantraloka-flywheel.py` (9/9) — wires `organism` + `pedagogy` + `misconception` +
  `question_growth` + `enquiry` + `design_provenance` into the flywheel on real DAG data.
- `scripts/run-tantraloka-scheduler-bridge.py` (5/5) — wires `organism_factory_bridge` + `next_action`
  through patala's `corpus_state` (ONE orchestrator).

Now-wired (Phase 6): `verification_ensemble`, `evidence_ledger`, `integrity_gate`, `source_registry`,
`organism`, `pedagogy`, `misconception`, `question_growth`, `enquiry`, `design_provenance`,
`organism_factory_bridge`, `query`, `retrieval`, `structure_recall`, `self_healing`, `alignment_flywheel`.
Still VALIDATED-ONLY (next wiring targets): `open_ended_evolve`, `skill_graph`, `iteration_confidence`,
`canonical_contracts`, `factory_pool`, `ingestion_organism`, `lightrag_compare`, `cognee_compare`,
`graph_stable`.

| Kernel | What it does | Layer | Vision | Validated by | Status |
|--------|-------------|-------|--------|--------------|--------|
| `epistemic.py` | envelope + 4-axis authority + invariant | L00 | Verified OS | kernel-suite, eigenius | VALIDATED |
| `schema.py` | single-source schema compiler | L00 | Complete Pipeline | kernel-suite | VALIDATED |
| `review.py` | herdr reducer (promotion gate) | L05 | Self-Maintaining | layer03-05 | VALIDATED |
| `scholar_review.py` | adversarial panel + cross-review + citecheck | L08 | Complete Pipeline | kernel-suite | VALIDATED |
| `staleness.py` | RKA blast-radius + rebuild order | L03 | Self-Maintaining | layer03-05 | VALIDATED |
| `query.py` | KG2Code executable graph queries | L10 | Executable Knowledge | kernel-suite | VALIDATED |
| `retrieval.py` | PathRAG + HippoRAG | L10 | Argument Map | kernel-suite, layer10 | VALIDATED |
| `translation.py` | TranslationProof (non-aggregate vector) | L03 | Complete Pipeline | products | VALIDATED |
| `education.py` | LearningClaim + interaction compiler | L09 | Education+Organism | education-organism | VALIDATED |
| `organism.py` | UserKnowledgeState + MisconceptionGraph | L09 | Education+Organism | education-organism | VALIDATED |
| `organism_loop.py` | consumer→research machine | L09 | Co-Evolving Organism | organism-loop | VALIDATED |
| `pedagogy.py` | live adaptive pedagogy | L09 | Education+Organism | pedagogy | VALIDATED |
| `agent_delivery.py` | task contract + context routing + budget + human gate | L09 | Autonomous Institute | agent-delivery | PROTOTYPED (needs signed auth) |
| `evolve.py` | MAP-Elites evolution loop | ALL | Autonomous Institute | evolve | VALIDATED |
| `certificate.py` | Certification Weight (compounding) | L02 | Verified-Statement-Marketplace | kernel-suite | VALIDATED |
| `discovery.py` | Research Value Score | L03 | What-If Machine | kernel-suite | VALIDATED |
| `essay_ingest.py` | 9-stage essay-as-derivation-input pipeline (structure→claims→evidence→argument→crux→review→pedagogy→reactive) | L04-L09 | Enquiry-Discovery Organism | validate-essay-ingest | VALIDATED (real Ratié data, 8/8) |
| `patala_product.py` | the ULTIMATE product: assembles ALL 17 kernels into the v3 4-family/16-product stack for one claim | ALL | Enquiry-Discovery Organism | validate-product-stack | VALIDATED (real IPK, 13/13) |
| `context_compiler.py` | the projection compiler: canonical graph → immutable per-entity context bundles | L06 | Verified OS | validate-context-compiler | VALIDATED (real graph, 12/12) |
| `fts_search.py` | Postgres-FTS-equivalent inverted index + benchmark (SPEC-49 Tantivy decision point) | L06 | Verified OS | validate-fts-baseline | VALIDATED (real corpus, 9/9) |
| `bundle_router.py` | compiled agent bundles + MCP 8-tool adapter + R2-style immutable emission | L06/L07 | Verified OS | validate-bundle-router | VALIDATED (real data, 16/16) |
| `seo.py` | agent-SEO: canonical URLs + JSON-LD + sitemap + static 0-JS HTML | L07 | Verified OS | validate-seo-astro | VALIDATED (real graph, 13/13) |
| `system_provenance.py` | VISION F: the OS audits its OWN kernels (signed self-provenance, why()→evidence, tamper-detect) | ALL | Verified OS | validate-system-provenance | VALIDATED (9/9) |
| `lightrag_compare.py` | LightRAG local/global/hybrid retrieval adapted to our graph, vs our PathRAG | L10 | Verified OS | validate-lightrag-compare | VALIDATED (10/10) |
| `cognee_compare.py` | Cognee remember/recall + KG search adapted to our graph, vs our context bundles | L09 | Verified OS | validate-cognee-compare | VALIDATED (11/11) |
| `source_registry.py` | fojin source-registry: claim source_refs → registered rights+health sources | L01 | Verified OS | validate-source-registry | VALIDATED (10/10) |
| `evidence_ledger.py` | GEM 6.5: typed evidence events + fojin confidence_kind (never compare incomparable) | L08 | Verified OS | validate-evidence-ledger | VALIDATED (9/9) |
| `alignment_flywheel.py` | fojin mine→stage→review→promote cross-source flywheel (human-in-loop) | L06 | Verified OS | validate-alignment-flywheel | VALIDATED (10/10) |
| `integrity_gate.py` | EleutherIA integrity_status tri-state + primary-source hard gate | L05 | Verified OS | validate-integrity-gate | VALIDATED (8/8) |
| `next_action.py` | GEM 12.3: deterministic next-action scheduler (P=w1D+w2B+w3U+w4Q+w5R−w6C) | L12 | Verified OS | validate-next-action | VALIDATED (7/7) |
| `vidyut_l0.py` | GEM 5.3: L0 Sanskrit token floor (SLP1 normalize + position-anchored tokens) | L03 | Verified OS | validate-vidyut-l0 | VALIDATED (9/9) |
| `verification_ensemble.py` | GEM 7.1: RefChecker + GraphCheck + RARR-gate compose (anti-hallucination) | L07 | Verified OS | validate-verification-ensemble | VALIDATED (8/8) |
| `translation_variant.py` | GEM 5.1: three-version translation as scholarship (core vs interpretation-space) | L03 | Verified OS | validate-translation-variant | VALIDATED (8/8) |
| `open_ended_evolve.py` | Darwin Godel adapted: open-ended rule evolution under the invariant oracle | L05 | Autonomous Institute | validate-open-ended-evolve | VALIDATED (6/6) |
| `self_healing.py` | Self-healing orchestration: typed repair cascade for the delivery loop | L09 | Autonomous Institute | validate-self-healing | VALIDATED (8/8) |
| `skill_graph.py` | Audited skill-graph self-improvement (kernels as skills, verifiable reward) | L05 | Autonomous Institute | validate-skill-graph | VALIDATED (8/8) |
| `structure_recall.py` | SAGE structure-aware recall (follow graph topology on the read plane) | L10 | Verified OS | validate-structure-recall | VALIDATED (9/9) |
| `ingestion_organism.py` | the autonomous priority-driven refinery: ingest→refine→verify→commit→re-prioritize | ALL | Verified OS | validate-ingestion-organism | VALIDATED (10/10) |
| `hermes_exec.py` | the REAL execution path: shells to `hermes -z` so the organism can actually generate (translation/commentary/essay) | ALL | Autonomous Institute | (none — needs validator) | REAL EXECUTION |
| `pushing_miner.py` | wire the crux compass: mines the 35 pushing-tantraloka LOGICVID sessions into cruxes+claims grounded in kārikās | L04 | Enquiry-Discovery | validate-pushing-miner | VALIDATED (7/7, real sessions) |
| `iteration_confidence.py` | hound steal: iteration-verified confidence (observations vs assumptions + iteration count; convergence = fundamentality) | L00 | Verified OS | validate-iteration-confidence | VALIDATED (5/5) |
| `canonical_contracts.py` | THE contract convergence: ONE non-scalar 4-axis AuthorityVector + ReviewEvent (fixes lib/epistemic's scalar ceiling error), PARITY with OG | L00/L05 | Verified OS | validate-contract-convergence | VALIDATED (10/10) |
| `factory_pool.py` | the parallel factory worker pool: many layer-workers run concurrently, DAG-gated, next_action-driven, each committing independently | ALL | Verified OS | validate-factory-pool | VALIDATED (10/10) |
| `projection_dag.py` | the projection DAG: correctness + staleness + incremental-rebuild scheduler, per-artifact (a new doc ≠ whole-corpus rebuild, SPEC-00 §22) | L06 | Verified OS | validate-projection-dag | VALIDATED (6/6) |
| `proof_generators.py` | the real Sanskrit proof-generator lattice (Vidyut SLP1 + token floor + negation): real analysis into TranslationProof, not hand-filled | L03 | Verified OS | validate-proof-generators | VALIDATED (9/9) |
| `misconception.py` | the repair cascade (DEV_PLAN §1.1, closes the organism's flywheel): MisconceptionLikelihood f(cluster,persistence,ambiguity,novice) -> flag for scholar review -> RKA blast-radius propagate fix -> measure dissolution | L09 | Education+Organism | validate-misconception | VALIDATED (9/9) |
| `question_growth.py` | the Question-Growth Engine (SPEC-36/logicvid): growth tree (question -> next_pressure) + PrimitiveRobustness (independent rediscovery = fundamentality, not popularity) + learnable growth examples | L04 | Enquiry-Discovery | validate-question-growth | VALIDATED (7/7) |
| `enquiry.py` | the Enquiry-Discovery Organism (SPEC-46): DiscoveryProgression (taxonomy -> theorem -> boundary -> frontier) — a structured enquiry reveals topic structure feeding ontology/claims/research-gaps/question-roots | L04 | Enquiry-Discovery | validate-enquiry | VALIDATED (13/13) |
| `design_provenance.py` | the Self-Proving full form (DEV_PLAN §1.4, extends system_provenance): every design decision -> a signed nanopub (rationale + rejected alternatives + validator), tamper-evident + why()-resolvable + Merkle-rooted | ALL | Self-Proving | validate-design-provenance | VALIDATED (8/8) |
| `graph_stable.py` | the stable-graph projection (DEV_PLAN §1.5, SPEC-13 F2/F3): deterministic byte-reproducible serialization (stabilize + stable-LCC) + content-addressed staleness check + component isolation | ALL | Co-Evolving Organism | validate-graph-stable | VALIDATED (8/8) |

## Rules for agents
1. **Reuse, don't rebuild** (axiom): a task that maps to a kernel → call the kernel.
2. **A kernel is VALIDATED** only if its `validate-*.py` passes in `scripts/run-tests.py`.
3. **Nothing is PRODUCTION** until it's INTEGRATED into a real pipeline and passes on real evidence.
4. To add a kernel: `lib/<name>.py` + a `validate-<name>.py` + matrix entry + this index.

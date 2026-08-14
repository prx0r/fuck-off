# EXPERIMENT MATRIX — what's been tested

*2026-08-14. 86 experiments mapped to layer / source repo / vision / kernel / result.*
Machine form: `data/references/experiments.json`.

## Argument Map (7)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-bounded-context.py` | L10 | PathRAG/SPEC-08 | retrieval | PASS |
| `experiment-communities.py` | L02 | nano-graphrag/GraphRAG | themes | PASS |
| `experiment-context-coverage.py` | L10 | PathRAG/SPEC-08 | retrieval | RUN |
| `experiment-crux-compiler.py` | L04 | SPEC-19 #5 | argument | PASS |
| `experiment-hipporag.py` | L10 | HippoRAG (arXiv) | retrieval | RUN |
| `experiment-pathrag.py` | L10 | PathRAG (arXiv+cloned) | retrieval | RUN |
| `validate-layer10.py` | L10 | PathRAG+HippoRAG+KG2Code | retrieval | PASS |

## Autonomous Institute (4)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-execution-replay.py` | L09 | agentstateprotocol+DML (cloned) | execution | RUN |
| `experiment-self-improve.py` | L05 | self-improving-agent (cloned) | review | PASS |
| `validate-agent-delivery.py` | L09 | loom+maestro+arcan+herdr (cloned) | agent-delivery | RUN |
| `validate-evolve.py` | ALL | openevolve+axplorer (cloned) | evolution | RUN |

## Co-Evolving Epistemic Organism (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-bkt-mastery.py` | L09 | pyBKT (cloned) | learner-state | RUN |
| `validate-organism-loop.py` | L09 | patala organism vision (R2) | organism | RUN |

## Comparative Philosophy (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-claim-standardisation.py` | L06 | comparative pushing | standardisation | RUN |
| `experiment-koral-twograph.py` | L06 | KORAL (arXiv) | commentarial | PASS |

## Complete Pipeline (3)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-cross-review.py` | L08 | adversarial-review (cloned) | scholar_review | PASS |
| `experiment-review-bias.py` | L08 | AgentReview (cloned) | scholar_review | PASS |
| `validate-products.py` | L03+L08+L00 | SPEC-15/16/17 | translation+review+schema | PASS |

## Education+Organism (5)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-curiosity-patterns.py` | L09 | LOGICVID gold exemplars (live human curiosity) | curiosity | RUN |
| `experiment-evolving-memory.py` | L09 | evolving-memory (cloned) | memory | PASS |
| `experiment-graphiti-temporal.py` | L09 | graphiti (cloned) | temporal | PASS |
| `validate-education-organism.py` | L09 | patala education/organism vision | education+organism | PASS |
| `validate-pedagogy.py` | L09 | patala education vision (R2) | pedagogy | RUN |

## Enquiry-Discovery (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-gem-extraction.py` | L04 | pushing-tantraloka | gem-extraction | RUN |

## Enquiry-Discovery Organism (5)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-enquiry-discovery.py` | L04 | logic5 presence enquiry (SPEC-46) | enquiry | RUN |
| `experiment-essay-as-engine.py` | L04/L06 | Ratié literature review (research-library) | essay-as-engine | RUN |
| `validate-essay-ingest.py` | L04/L06/L09 | Ratié essay (real data) | essay-ingest | RUN |
| `validate-product-stack.py` | ALL | real IPK primary text | v3-product | RUN |
| `validate-pushing-miner.py` | L04 | 35 pushing-tantraloka LOGICVID sessions | pushing-miner | RUN |

## Executable Knowledge (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-kg2code.py` | L10 | KG2Code (arXiv) | query | RUN |

## General Engine (4)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-generalization.py` | L08 | EleutherIA (SPEC-07) | core | PASS |
| `experiment-import-scifact.py` | L01 | SciFact (cloned) | ingestion | PASS |
| `experiment-nano-stable-graph.py` | L02 | nano-graphrag (cloned) | stable-graph | RUN |
| `experiment-salsa-incremental.py` | L03 | salsa (cloned) | incremental | RUN |

## Self-Maintaining (3)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-herdr-review.py` | L05 | herdr-workflow (cloned) | review | RUN |
| `experiment-rka-staleness.py` | L03 | RKA (cloned) | staleness | RUN |
| `experiment-unified-epistemic.py` | L03-L06 | herdr+RKA+kappa | epistemic | RUN |

## Self-Proving System (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-causal-operational-graph.py` | L12 | patalamix review #12 | causal-operational | RUN |
| `experiment-signed-statement.py` | L12 | cosign (cloned) | signing | RUN |

## Verified Epistemic OS (43)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `audit-state.py` | ALL | state.json + lib/ + experiments | state-gate | RUN |
| `audit-theatre-dataflow.py` | ALL | validator data-flow | theatre-dataflow | RUN |
| `audit-traceability.py` | ALL | index docs | traceability | RUN |
| `experiment-eigenius-grades.py` | L00 | eigenius (cloned) | epistemic | PASS |
| `experiment-mutation-testing.py` | L07 | SPEC-19 #3 | verification | PASS |
| `experiment-reactive-essay.py` | L12 | SPEC-19 #4 | reactive | PASS |
| `experiment-signed-corpus.py` | L12 | SPEC-19 #6/7 | merkle | PASS |
| `experiment-verified-lifecycle.py` | ALL | the OS synthesis | all | PASS |
| `theatre-check-all.py` | ALL | the full anti-theatre audit | verification | RUN |
| `theatre-check.py` | ALL | the anti-theatre skill | verification | RUN |
| `validate-alignment-flywheel.py` | L06 | IPK/IPVV corpus | alignment-flywheel | RUN |
| `validate-bundle-router.py` | L06/L07 | real graph + corpus | bundle-router | RUN |
| `validate-cognee-compare.py` | L09 | real graph + cognee (topoteretes ⭐30k) | cognee | RUN |
| `validate-context-compiler.py` | L06 | real graph (490/6578) | projection-compiler | RUN |
| `validate-contract-convergence.py` | L00/L05 | 6 divergent ReviewEvent/Authority defs | contract-convergence | RUN |
| `validate-evidence-ledger.py` | L08 | typed events | evidence-ledger | RUN |
| `validate-fts-baseline.py` | L06 | real corpus (425) | fts-baseline | RUN |
| `validate-graduation-ipvv.py` | ALL | real IPK primary text (Torella) + Ratié | ipvv-graduation | RUN |
| `validate-graduation.py` | ALL | real graph/argument/canonical-dag | graduation | RUN |
| `validate-hermes-exec.py` | ALL | real AbhT_1.52 kārikā via agentic hermes chat | hermes-generation | RUN |
| `validate-ingestion-organism.py` | ALL | sivaqueue-style Sanskrit targets | ingestion-organism | RUN |
| `validate-integrity-gate.py` | L05 | real IPK sources | integrity-gate | RUN |
| `validate-iteration-confidence.py` | L00 | real reflexivity claim (AbhT_1.52) | iteration-confidence | RUN |
| `validate-layer03-05.py` | L03+L05 | herdr+RKA (cloned) | review+staleness | PASS |
| `validate-lightrag-compare.py` | L10 | real graph + LightRAG (HKUDS ⭐38k) | lightrag | RUN |
| `validate-next-action.py` | L12 | IPK tasks | next-action | RUN |
| `validate-open-ended-evolve.py` | L05 | Darwin Godel (dgm ⭐2.2k) | open-ended-evolve | RUN |
| `validate-provenance.py` | L02 | knowledgeProvenance (cloned) | provenance | PASS |
| `validate-self-healing.py` | L09 | agent delivery | self-healing | RUN |
| `validate-seo-astro.py` | L07 | real graph | seo-astro | RUN |
| `validate-skill-graph.py` | L05 | 33 kernels as skills | skill-graph | RUN |
| `validate-source-registry.py` | L01 | real IPK/Ratié sources | source-registry | RUN |
| `validate-stack.py` | ALL | graduation test | integration | RUN |
| `validate-structure-recall.py` | L10 | real graph | structure-recall | RUN |
| `validate-system-provenance.py` | ALL | lib/ kernel index | self-provenance | RUN |
| `validate-tantraloka-argument.py` | L04 | AbhT_1.52 + pushing cruxes | tantraloka-argument | RUN |
| `validate-tantraloka-atlas.py` | L01 | Tantrāloka root + Dyczkowski + Jayaratha | tantraloka-atlas | RUN |
| `validate-tantraloka-fullstack.py` | ALL | real theme cluster CL-3 + Ahnika-1 | tantraloka-fullstack | RUN |
| `validate-tantraloka-translation.py` | L03 | AbhT_1.52 real Sanskrit root | tantraloka-translation | RUN |
| `validate-tantraloka-vs-dyczkowski.py` | L03 | AbhT_1.52 root + Dyczkowski vol1 | tantraloka-validation | RUN |
| `validate-translation-variant.py` | L03 | IPK 1.5.19 translations | translation-variant | RUN |
| `validate-verification-ensemble.py` | L07 | registered sources + edges | verification-ensemble | RUN |
| `validate-vidyut-l0.py` | L03 | vidyut + SLP1 | vidyut-l0 | RUN |

## Verified-Statement-Marketplace (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-certification-weight.py` | L02 | VISION marketplace | certificate | RUN |
| `experiment-rival-argument.py` | L08 | VISION D verifier-as-rival | scholar_review | RUN |

## What-If Machine (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-counterfactual-engine.py` | L03 | VISION B counterfactual | discovery | RUN |
| `experiment-question-growth.py` | L04 | pushing method (research-library) | question-growth | RUN |

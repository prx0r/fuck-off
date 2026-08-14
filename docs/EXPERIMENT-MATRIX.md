# EXPERIMENT MATRIX — what's been tested

*2026-08-14. 36 experiments mapped to layer / source repo / vision / kernel / result.*
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

## Autonomous Institute (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-self-improve.py` | L05 | self-improving-agent (cloned) | review | PASS |
| `validate-evolve.py` | ALL | openevolve+axplorer (cloned) | evolution | RUN |

## Co-Evolving Epistemic Organism (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-bkt-mastery.py` | L09 | pyBKT (cloned) | learner-state | RUN |

## Comparative Philosophy (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-koral-twograph.py` | L06 | KORAL (arXiv) | commentarial | PASS |

## Complete Pipeline (3)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-cross-review.py` | L08 | adversarial-review (cloned) | scholar_review | PASS |
| `experiment-review-bias.py` | L08 | AgentReview (cloned) | scholar_review | PASS |
| `validate-products.py` | L03+L08+L00 | SPEC-15/16/17 | translation+review+schema | PASS |

## Education+Organism (3)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-evolving-memory.py` | L09 | evolving-memory (cloned) | memory | PASS |
| `experiment-graphiti-temporal.py` | L09 | graphiti (cloned) | temporal | PASS |
| `validate-education-organism.py` | L09 | patala education/organism vision | education+organism | PASS |

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

## Self-Proving System (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-signed-statement.py` | L12 | cosign (cloned) | signing | RUN |

## Verified Epistemic OS (7)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-eigenius-grades.py` | L00 | eigenius (cloned) | epistemic | PASS |
| `experiment-mutation-testing.py` | L07 | SPEC-19 #3 | verification | PASS |
| `experiment-reactive-essay.py` | L12 | SPEC-19 #4 | reactive | PASS |
| `experiment-signed-corpus.py` | L12 | SPEC-19 #6/7 | merkle | PASS |
| `experiment-verified-lifecycle.py` | ALL | the OS synthesis | all | PASS |
| `validate-layer03-05.py` | L03+L05 | herdr+RKA (cloned) | review+staleness | PASS |
| `validate-provenance.py` | L02 | knowledgeProvenance (cloned) | provenance | PASS |

## Verified-Statement-Marketplace (2)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-certification-weight.py` | L02 | VISION marketplace | certificate | RUN |
| `experiment-rival-argument.py` | L08 | VISION D verifier-as-rival | scholar_review | RUN |

## What-If Machine (1)

| script | layer | source | kernel | result |
|--------|-------|--------|--------|--------|
| `experiment-counterfactual-engine.py` | L03 | VISION B counterfactual | discovery | RUN |

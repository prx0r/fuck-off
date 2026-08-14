# GAPS — known holes / what's not built yet

*Honest gaps between where we are and the vision. Each maps to a Layer + a SPEC. Update as things close.*

## Critical gaps
| Gap | Layer | Spec | Notes |
|-----|-------|------|-------|
| Typed relations not in the main graph | 02 | SPEC-03 | co_occurs still dominates; only argument.json has typed edges |
| No ReviewEvent/Adjudication records | 05 | SPEC-02 | envelope + invariant exist; full review chain not built |
| No projection compiler | 06 | SPEC-00 | no per-entity bundles yet |
| No retrieval (PathRAG/ToG-2 style) | 06 | SPEC-08 | no bounded-context agent retrieval |
| No surfaces (Astro/API/MCP) | 07 | SPEC-05 | nothing served yet |
| No domain expansions | 08 | VISION | science/philosophy/sanskrit subclasses not built |
| 8 scanned PDFs un-OCR'd | 01 | SPEC-00 | ocr-scanned-pdfs.py written, not run |
| No agent execution loop | 09 | SPEC-06 | vision→layer→task map exists; no automation |

## From SPEC-08 (graph reasoning) — not yet adopted
| Pinch | Status |
|-------|--------|
| GFM-RAG graph abstraction (`export_gfm_graph()`) | not started |
| ToG-2 alternating text↔graph search (`trace()`/`investigate()`) | not started |
| PathRAG/SubgraphRAG bounded context (`context(... token_budget=N)`) | not started |
| Graphiti/AriGraph epistemic-vs-event separation | not started — review events should be separate from claims |
| Hypergraph support for Argument objects | not started |
| Executable graph queries (KG2Code: `path(from=…,via=[…]).filter()` ) | not started — this is the agent-query frontier |

## Ecosystem datasets not yet ingested (SPEC-07)
| Dataset | Purpose |
|---------|---------|
| SciFact | scientific claim↔evidence gold (adapters) |
| xAIF (ARG Tech) | argument graphs |
| EleutherIA | free-will philosophy |
| FactKG | 108k claims |
| OpenAlex / S2ORC | bibliography layer |

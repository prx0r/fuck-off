# GAPS — known holes / what's not built yet

*2026-08-15. Honest gaps between where we are and the vision. Each maps to a Layer + a SPEC. This was
rewritten in the Phase-0 record reconciliation because it had gone stale (it claimed the projection
compiler, retrieval, and surfaces were unbuilt when they are all VALIDATED). Update as things close.*

## Status ladder reminder
DISCOVERED < PROTOTYPED < VALIDATED < INTEGRATED < PRODUCTION. A gap below is the distance between
VALIDATED and PRODUCTION unless noted.

## Critical gaps
| Gap | Layer | Spec | Notes |
|-----|-------|------|-------|
| Typed relations not in the main graph | 02 | SPEC-03 | `co_occurs_with` still dominates; only `argument.json` has typed edges. Needs LLM tagging + verbatim `evidence_quote`. |
| No live ReviewEvent/adjudication records | 05 | SPEC-02 | envelope + invariant + scholar_review exist; no persisted ReviewEvent rows yet |
| Read plane BUILT but NOT DEPLOYED | 06/07 | SPEC-49 | compiler 12/12 + fts 9/9 + bundles 16/16 + seo 13/13 all validate; no `wrangler deploy` — FTS is local DuckDB, not Postgres |
| Signed human attestation (Gap E) | 05 | SPEC-06 | `human_authorize()` is a plain state flip; needs real crypto (ed25519/ecdsa) — **blocks any public authority/marketplace** |
| Context paging (Gap A) | 06 | SPEC-49 | `context_compiler.py` does prose projection only; no lossless virtualization |
| No domain expansions | 08 | VISION | `lib/domains/` is EMPTY — the domain-expansion plane is unbuilt |
| 8 scanned PDFs un-OCR'd | 01 | SPEC-00 | `ocr-scanned-pdfs.py` written, not run |
| `hermes_exec` used for generation | 03/09 | DEV_PLAN | wired into translation runners, but in tension with the canonical "patala produces, ip-graph validates" split (see CONTEXT-REVIEW-2 §3) |

## SPEC-08 (graph reasoning) — status
| Pinch | Status |
|-------|--------|
| GFM-RAG graph abstraction (`export_gfm_graph()`) | DISCOVERED |
| ToG-2 alternating text↔graph search (`trace()`/`investigate()`) | **BUILT** — `lib/retrieval.py` + `validate-tog2.py` (VALIDATED) |
| PathRAG/SubgraphRAG bounded context (`context(... token_budget=N)`) | **BUILT** — `lib/retrieval.py` (VALIDATED) |
| Graphiti-style temporal validity (`TemporalFact`/`active_facts_at`) | **BUILT** — `lib/staleness.py` + `validate-tempvalidity.py` (VALIDATED) |
| Hypergraph support for Argument objects | DISCOVERED |
| Executable graph queries (KG2Code: `path(from=…,via=[…]).filter()`) | DISCOVERED — the agent-query frontier |

## Ecosystem datasets not yet ingested (SPEC-07 / L01)
| Dataset | Purpose |
|---------|---------|
| xAIF (ARG Tech) | argument graphs |
| EleutherIA | free-will philosophy |
| FactKG | 108k claims |
| OpenAlex / S2ORC | bibliography layer |
| Mitchell/Mitra samgraha + MITRA (S↔T↔C) | benchmark/error-family validators (TRANSLATION-PRODUCTION T4) |

*(SciFact was removed — its adapter is done: `import_scifact` VALIDATED, per STATE.yaml L01.)*

## Coordination gaps (cross-repo, see CONTEXT-REVIEW-2)
- The `patala_*` MCP orchestration verbs (`patala_next_action`, `patala_get_work_state`,
  `patala_propose_translation`) are NOT built — the single biggest gap to "Hermes orchestrates the
  factory."
- The `patala` Hermes profile + external skill dir not set up.
- `schema.py` collision (ip-graph vs patala) forces separate processes.
- The 63 L200 + 63 C1 IPVV golds not bulk-ingested with Derivation edges.

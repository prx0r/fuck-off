# FRONTIER-MAP — implementations, todos, validations per patala layer

*2026-08-14. Turns SPEC-14 (frontier layer builds) into concrete, verifiable implementations. Each
layer → a buildable `lib/` kernel or `scripts/` validation, with a TODO and a verifiable comparison.
Status: [x] done · [~] in progress · [ ] open.*

---

## The reusable kernel (`lib/`) — promote from proven experiments first

| Kernel | What it is | From experiment | TODO |
|--------|-----------|-----------------|------|
| `lib/epistemic.py` | envelope + 4-axis authority + invariant | built | [x] |
| `lib/review.py` | herdr reducer state machine | experiment-herdr-review | [x] |
| `lib/staleness.py` | RKA blast-radius + review_queue | experiment-rka-staleness | [x] |
| `lib/query.py` | KG2Code executable graph queries | experiment-kg2code | [x] |
| `lib/retrieval.py` | PathRAG + HippoRAG + bounded-context | experiments | [x] |
| `lib/graph_stable.py` | nano stable-LCC + GraphML | experiment-nano-stable-graph | [x] |

## Layer implementations + validations

| Layer | Build | Validation / comparison | Status |
|-------|-------|-------------------------|--------|
| 00 Governance | schema contract (epistemic as canonical) | schema-validate all graph objects | [ ] |
| 01 Ingestion | 5-import adapters | ingest scifact sample → same engine | [ ] |
| 02 Atlas | content-addressed stable graph | deterministic GraphML round-trip | [ ] |
| 03 Factory | DAG=staleness+rebuild | retract→stale flags + incremental | [x] | |
| 04 Evidence | verifier ensemble + conformal | abstention calibration | [ ] |
| 05 Research | herdr reducer + KG2Code synthesis | promotion trace | [x] | |
| 06 Commentarial | KORAL two-graph | source vs interpretation separation | [ ] |
| 07 Verification | two-plane + PathRAG | path-retrieval for judge | [ ] |
| 08 Human Authority | herdr/Vouch gate | reducer reaches ADJUDICATED only via human | [ ] |
| 09 Organism | Graphiti + pyBKT | user-state + prerequisite graph | [ ] |
| 10 Surfaces | Argument Map + retrieval | **PathRAG vs HippoRAG vs KG2Code** | [x] | |
| 11 Org/Economics | arcan event-sourcing | append-only history replay | [ ] |
| 12 Live System | epistemic work queue | staleness loop + STATE.yaml | [ ] |

---

## The validated thread (proven so far)
- `scripts/experiment-*.py` — 10 working experiments (herdr, RKA, KG2Code, PathRAG, HippoRAG,
  bounded-context, stable-graph, evidence-weights, unified-epistemic, context-coverage).
- All 8 gates in `scripts/run-tests.py` pass.

## This file's companion
- `specs/SPEC-14-FRONTIER-LAYER-BUILDS.md` — the *why* per layer.
- `docs/ALGORITHMS.md` — the granular algorithm findings.
- `data/graph/test-results.json` — machine-readable validation output.

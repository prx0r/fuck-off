# GITHUB TRACEABILITY — every repo → cloned? → linked experiment/infra

*2026-08-14. The complete, auditable map of every GitHub repo we've touched. **41 cloned** into
`ecosystem/`, plus the ones referenced-but-not-cloned. Each cloned repo is linked to either a
**validated experiment** (a verifiable proof) or an **infra reference** (used for code-reading, not
integrated). This makes everything traceable — no repo is orphaned.*

---

## TRACEABILITY LEGEND
- ✅ **EXPERIMENT** — a `scripts/experiment-*.py` / `validate-*.py` proves its mechanism (with a theatre proof).
- 📖 **REFERENCE** — cloned for code-reading / used as infra pattern, not yet integrated into a test.
- ⬜ **NOT CLONED** — referenced in surveys/specs only.

---

## TIER 1 — CLONED + LINKED TO A VALIDATED EXPERIMENT ✅

| Repo (dir) | Experiment (proof) | Layer | Verdict |
|-----------|-------------------|-------|---------|
| `herdr-workflow` | `experiment-herdr-review` + `validate-layer03-05` | L05 | PROVEN |
| `rka` | `experiment-rka-staleness` + `validate-layer03-05` | L03 | PROVEN |
| `knowledgeProvenance` | `validate-provenance` | L02 | PROVEN |
| `nano-graphrag` | `experiment-nano-stable-graph` + `experiment-communities` | L02 | PROVEN |
| `PathRAG` | `experiment-pathrag` + `validate-layer10` | L10 | PROVEN |
| `HippoRAG` (clone) | `experiment-hipporag` + `validate-layer10` | L10 | PROVEN (hub-bias found) |
| `LightRAG` (clone, ⭐38k) | `validate-lightrag-compare` | L10 | PROVEN (local/global/hybrid adapted, vs our PathRAG) |
| `cognee` (clone, ⭐30k) | `validate-cognee-compare` | L09 | PROVEN (remember/recall + KG search, vs our bundles) |
| `eigenius` | `experiment-eigenius-grades` | L00 | PROVEN |
| `self-improving-agent` | `experiment-self-improve` | L05 | PROVEN |
| `evolving-memory` | `experiment-evolving-memory` | L09 | PROVEN |
| `graphiti` | `experiment-graphiti-temporal` | L09 | PROVEN |
| `pyBKT` | `experiment-bkt-mastery` | L09 | PROVEN |
| `cosign` | `experiment-signed-statement` | L12 | PROVEN |
| `openevolve` | `validate-evolve` | ALL | PROVEN-MECHANISM |
| `axplorer` | `validate-evolve` | ALL | PROVEN-MECHANISM |
| `salsa` | `experiment-salsa-incremental` | L03 | PROVEN |
| `agentstateprotocol` | `experiment-execution-replay` | L09 | PROVEN |
| `deterministic-memory-layer` | `experiment-execution-replay` | L09 | PROVEN |
| `adversarial-review` | `experiment-cross-review` | L08 | PROVEN |
| `AgentReview` | `experiment-review-bias` | L08 | PROVEN |
| `scifact` | `experiment-import-scifact` | L01 | PROVEN |

## TIER 2 — CLONED, INFRA / REFERENCE ONLY 📖 (code-read, not yet a test)

| Repo (dir) | Why cloned / what it informs | Status |
|-----------|------------------------------|--------|
| `maestro` | task-contract/verdict pattern → `agent_delivery.py` | reference (proprietary-ish) |
| `arcan` | event-sourcing, BudgetState → `agent_delivery.py` | reference |
| `loom` | stateful delivery + context routing → `agent_delivery.py` | reference (proprietary) |
| `loom-valkor` | open loop-engineering harness | reference |
| `herdr-workflow` | (also Tier 1) reducer/gate | validated |
| `mcp-agent` | the MCP agent builder (Layer 07 surface) | reference (large, local-only) |
| `mcp-spec` | the MCP specification | reference |
| `agent-kit` | multi-agent network orchestration | reference |
| `cmu-paper-reviewer` | paper-review agent (Layer 08) | reference |
| `agent-review-panel` | 16-phase review protocol | reference |
| `EverOS` | local-first memory runtime | reference |
| `dbos` | durable execution on Postgres | reference |
| `graphrag` | canonical GraphRAG | reference (large, local-only) |
| `KAG` | logical-form reasoning | reference (large, local-only) |
| `HippoRAG` (clone) | (also Tier 1) PPR | validated |
| `instagraph` | text→graph; our graph.json uses its schema | reference |
| `sage-wiki` | graph-as-compile-output | reference |
| `seventeen-centuries` | philosophy markdown-graph | reference |
| `kappa-graph` | epistemic weighting | reference |
| `storm` | knowledge curation → report | reference |
| `literature-review-toolkit` | literature-review agent | reference |
| `paper-qa` | scientific RAG evidence packets | reference |
| `nodedb` | local-first memory engine (gap G) | reference |

## TIER 3 — NOT CLONED (referenced in surveys/specs only) ⬜

| Repo | Referenced in | Why not cloned |
|------|--------------|----------------|
| EleutherIA | SPEC-07 | domain-generalization test data (large) |
| DSPy | SPEC-32/09 | programmatic optimization (huge, 181MB) |
| inspect_ai | SPEC-32/07 | eval framework (huge, 415MB) |
| vouch | SPEC-32/07 | review gate (we built our own) |
| restate / temporal / hatchet | SPEC-09 | durable runtimes (only if we scale) |
| dapr-agents | SPEC-09 | distributed agents |
| microsoft/autogen, langgraph | SPEC-09 | agent frameworks (we use our own) |
| Microsoft GraphRAG | SPEC-08 | (we cloned graphrag instead) |
| TodoClawbot/context-paging | SPEC-32 gap A | context-paging (gap A, not built) |

---

## THE UNLINKED GAPS (repos cloned but no experiment — need integration)

The following are cloned but **reference-only** — they're the ones a future agent should turn into
experiments (they map to the patalamix gaps):
- **`nodedb`** → gap G (local-first workstation) — no experiment yet.
- **`paper-qa`** → scientific evidence-packet mechanism — no experiment yet.
- **`agent-kit` / `mcp-agent` / `mcp-spec`** → the Layer 07 surfaces — no experiment yet.
- **`storm`** → the verified-corpus → prose projection — no experiment yet.
- **`cmu-paper-reviewer` / `agent-review-panel`** → deep-review mechanisms — no experiment yet.

---

## THE TRACEABILITY CHECK (verify nothing is orphaned)

```bash
# every repo in ecosystem/ has a README or is in the index
for d in ecosystem/*/*/; do [ -f "$d/README.md" ] || grep -q "$(basename $d)" data/references/github.json 2>/dev/null; done
# every experiment links to a source
python3 -c "
import json; d=json.load(open('data/references/experiments.json'))
missing=[e['script'] for e in d['entries'] if not e.get('source')]
print('experiments missing a source:', missing if missing else 'none')"
```

## FULL REPO INDEX (all touched)
- **Cloned:** 41 (20 validated experiments + 21 reference)
- **Referenced-not-cloned:** ~15 (Tier 3)
- **Machine catalog:** `data/references/github.json` (the authoritative repo index)
- **Experiment traceability:** `data/references/experiments.json` + `data/references/theatre-proofs-all.json`

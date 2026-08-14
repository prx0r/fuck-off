# EXPERIMENT REPORT — third-party repo experiments on the Doyle corpus

*2026-08-14. Hands-on experiments running each cloned repo's core patterns against our real data
(graph, argument, canonical DAG). Purpose: see how other people build epistemic/agent systems and what
we can adopt. All reproducible via `scripts/experiment-*.py`.*

---

## 1. herdr-workflow — adversarial review state machine ⭐ (most aligned)

**Source:** `ecosystem/agent-runtime/herdr-workflow` (Rust; not built — read the 1386-line spec)
**Experiment:** `scripts/experiment-herdr-review.py`

**What it is:** agents propose authenticated reports about immutable artifacts; committed events +
deterministic **reducers** advance state; only a human authorizes publication. The stage contract has
`roles`, `permissions`, `reducer`, `completion_predicate`, `invalidation_rules`.

**Result on our data:** the reducer correctly keeps corroborated physics claims (I1, I4, I6) in `ALIGNED`
while the machine-proposed thesis claims (I2, I3, I5) stay in `CORRECTION_REQUIRED` — they can't promote
without stronger evidence. This is our SPEC-02 invariant as executable state.

**Adopt:** the reducer/ReviewPhase/FindingStatus state machine → our Layer 05 (Review & Gate).

## 2. RKA — blast-radius staleness propagation ⭐ (the killer idea)

**Source:** `ecosystem/epistemic/rka` (SQL + MCP bridge; local-only)
**Experiment:** `scripts/experiment-rka-staleness.py`

**What it is:** a research-workflow system whose `review_queue` has flags like `stale_dependency`,
`unsupported_link`, `stale_theme`. The key idea: "claim changed → derived knowledge becomes stale →
review queue."

**Result on our DAG:** retracting PHYSICS flags **8 downstream layers** (FREE_WILL, VALUE, SYNTHESIS,
ESSAY, ...) as `stale_dependency`; retracting INDETERMINISM flags 5. The graph becomes **self-maintaining**.

**Adopt:** blast-radius walker → Layer 03 (Factory) — the executable form of `authority(projection)
<= authority(parent)`. RKA also has openalex/crossref/arxiv/semantic-scholar backends = our import_* adapters.

## 3. Kappa Graph — epistemic grounding (support vs contradiction)

**Source:** `ecosystem/epistemic/kappa-graph` (FUSE over graph; local-only)
**Experiment:** already in `data/graph/evidence-weights.json` (Kappa-style probe)

**What it is:** separates retrieval from **epistemic strength**; concepts accumulate supporting +
contradicting evidence; disagreement retained; computes grounding/diversity.

**Result on our data:** grounded physics/info concepts = high support, **zero contradiction**; thesis
concepts (free_will, value) = pure contradiction, zero support. Confirms the epistemic split is
data-driven.

**Adopt:** `calculate_type_grounding_contribution` + support/contradiction accumulation → Layer 02.

## 4. nano-graphrag — deterministic graph serialization

**Source:** `ecosystem/retrieval/nano-graphrag` (1100-line reference, tracked)
**Experiment:** `scripts/experiment-nano-stable-graph.py`

**What it is:** a minimal GraphRAG. Its reusable, no-API-key parts: `stable_largest_connected_component`
+ `_stabilize_graph` (deterministic node/edge ordering) + GraphML persistence.

**Result on our graph:** determinism confirmed (identical after re-stabilize). Our concept graph has
**19 components** (largest 36 nodes) — a real structural insight. Wrote `concept-lcc.graphml`.

**Adopt:** stable-LCC + GraphML export for reproducible graph artifacts (AGENTS.md axiom).

## 5. arcan — event-sourced agent kernel

**Source:** `ecosystem/agent-runtime/arcan` (Rust, 4.7M, tracked)
**Status:** architecture read only (no cargo to build). Tiny agent kernel, event sourcing.

## 6. SYNTHESIS — the unified epistemic pipeline ⭐

**Experiment:** `scripts/experiment-unified-epistemic.py`

Combines all three patterns on real data:
```
kappa  (grounding: CORROBORATED/CONTESTED/CONTRADICTED)
  -> herdr (review phase: ALIGNED/REVIEWING/CORRECTION_REQUIRED)
  -> RKA  (staleness blast-radius on the canonical DAG)
```
Physics floor → ALIGNED; free-will thesis → CORRECTION_REQUIRED; any physics retraction → FREE_WILL/
VALUE flagged stale → review_queue. **This is the executable epistemic-promotion engine our vision
calls for, built from herdr + RKA + kappa patterns.**

---

## What we should ADOPT (priority)
| Pattern | Source | Layer |
|---------|--------|-------|
| Reducer/ReviewPhase state machine | herdr | 05 Review & Gate |
| Blast-radius staleness + review_queue | RKA | 03 Factory |
| Grounding/contradiction accumulation | Kappa | 02 Epistemic |
| Stable-LCC + GraphML determinism | nano-graphrag | 06 Retrieval |
| import_* adapters (openalex/crossref/arxiv) | RKA backends | 01 Corpus |

## Cloned status
- **Tracked:** herdr-workflow, arcan, nano-graphrag (+ loom-valkor note)
- **Local-only (gitignored):** RKA (30M), Kappa (49M), ghuntley/loom (proprietary), maestro (sqlite secrets)

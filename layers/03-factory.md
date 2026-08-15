# LAYER 03 — FACTORY (compiler)
*Spine (Chunk 4). The derivational DAG compiler (physics→…→value).*

## 1. What it is
The layer that encodes the thesis as a directed dependency chain (CANONICAL-DAG): PHYSICS → INFORMATION → INDETERMINISM → FREE_WILL → VALUE.

## 2. Purpose
Turn co-occurrence into derivation — an auditable "what supports what" chain, not a term map.

## 3. Data
- `data/graph/canonical-dag.yaml` — the derivational DAG (canonical-dag, validated no-cycles/refs-resolve)

## 4. Processes
```
DAG define → map layers→works → validate-dag (no cycles, refs resolve) → emit derives_from edges
```

## 5. Implementations
- Spec: `specs/SPEC-01-canonical-dag.md`

## 6. Docs
- `specs/SPEC-01-canonical-dag.md`

## 7. Current state
`VALIDATED` (see `STATE.yaml`). `lib/staleness.py` (RKA blast-radius) + `data/graph/canonical-dag.yaml`
VALIDATED. Counterfactual engine DISCOVERED/PROTOTYPED.

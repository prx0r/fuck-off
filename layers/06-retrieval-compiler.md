# LAYER 06 — RETRIEVAL COMPILER
*Spine (Chunk 7). Compiled agent bundles + search.*

## 1. What it is
The layer that compiles the canonical graph into immutable, addressable read artifacts (per SPEC-00):
per-entity JSON/Markdown/bundles pushed to R2, served from the edge.

## 2. Purpose
"One agent question = one request." Materialized context bundles, incremental hashes, inverted indexes.

## 3. Data
- (to build) compiled bundles per entity/concept
- Parquet bulk exports

## 4. Processes
```
projection compiler → per-entity artifacts → R2 immutable → edge cache
```

## 5. Implementations
- Spec: `specs/SPEC-00-INFRA-BUILD.md`

## 6. Docs
- `specs/SPEC-00-INFRA-BUILD.md` (§15 compiled agent views)

## 7. Current state
`NOT_STARTED`.

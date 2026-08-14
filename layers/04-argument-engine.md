# LAYER 04 — ARGUMENT ENGINE
*Spine (Chunk 5). Claims → arguments → evidence (AIF).*

## 1. What it is
The argument graph — AIF's three node types (Info / Inference / Conflict) replacing flat edges. This
is the differentiator: "challenged_by", "reframed_by", "evidence", "depends_on" instead of "related".

## 2. Purpose
Represent the two-stage free-will argument (and the compatibilist conflict) as a resolvable argument
chain, each node anchored to a real passage.

## 3. Data
- (to build) `data/graph/argument.json`

## 4. Processes
```
hand-curate argument skeleton → anchor each node to evidence_quote + passage_ids → emit argument.json
```

## 5. Implementations
- Spec: `specs/SPEC-03-argument-graph.md`

## 6. Docs
- `specs/SPEC-03-argument-graph.md`
- `docs/vision/VISION.md` (the argument layer = the moat)

## 7. Current state
`NOT_STARTED`.

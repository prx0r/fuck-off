# LAYER 02 — EPISTEMIC GRAPH

*Part of the `VISION-CHUNK-LAYER-MAP.md` spine (Chunk 3). The concept/entity/relation knowledge graph.*

## 1. What it is
The knowledge graph: concepts, entities, and their relations, each carrying an epistemic ceiling.

## 2. Purpose
Represent the intellectual structure of the corpus as a queryable graph — with honest epistemic
status, not just term co-occurrence.

## 3. Data
- `data/graph/graph.json` — 490 nodes / 6578 edges (instagraph schema)
- `data/graph/doc_graph.gexf` — Gephi export
- `data/graph/concepts.jsonl` · `works.jsonl`

## 4. Processes
```
corpus.jsonl → concept/author lexicon match → co-occurrence edges → theme membership → graph.json
```

## 5. Implementations
- `scripts/build-graph.py`

## 6. Docs
- `docs/03-graph.md`
- `specs/SPEC-01-canonical-dag.md` (the DAG upgrade)

## 7. Current state
`PARTIAL` (see `STATE.yaml`). Built, but edges are `co_occurs_with` (statistical). Needs: epistemic
ceilings (SPEC-02) + typed relations (SPEC-03).

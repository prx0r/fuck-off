# 03 — GRAPH (the knowledge graph)

*The output knowledge graph. Ground truth verified 2026-08-14.*

## Current graph (deterministic, offline)

**490 nodes, 6578 edges**, built from the 425-doc clean corpus.

| Node type | Count |
|-----------|-------|
| work | 425 |
| concept | 31 |
| author | 18 |
| theme | 11 |
| school | 3 |
| problem | 2 |

## Edge relationships (current)

| Relationship | Between | Notes |
|--------------|---------|-------|
| `discusses` | doc → concept | term co-occurrence |
| `authored_by` | doc → author | lexicon match |
| `co_occurs_with` | concept → concept | **statistical — the main limitation** |
| `belongs_to` | concept → theme | from ontology |

## Schema

instagraph `KnowledgeGraph` format: `{metadata, nodes:[{id,label,type,color,properties}], edges:[{from,to,relationship,direction,properties}]}`. Node colors: concept #aec6ff, author #ffb3ba, work #b5ead7, school #ffd1a1, problem #ffc3e0, theme #c1f0c1.

## Files

```
data/graph/
  graph.json         primary (instagraph schema)
  doc_graph.gexf     Gephi import
  concepts.jsonl     concept records
  works.jsonl        document records
```

## Known limitation / next step

Edges are `co_occurs_with` (statistical). The next upgrade is **typed relations** (negates,
presupposes, is_cause_of, tensions_with, ...) per `04-ontology.md`, likely via LLM tagging
(darshana-graph `tag_corpus.py` pattern). Every typed edge must carry a verbatim `evidence_quote`.

## Related
- Build: `scripts/build-graph.py`
- Ontology: `04-ontology.md`
- Performance: `05-performance.md`

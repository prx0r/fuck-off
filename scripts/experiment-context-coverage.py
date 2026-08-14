#!/usr/bin/env python3
"""experiment-context-coverage.py — stress-test bounded-context across ALL concepts.

For each of the 31 concepts in the graph, retrieve a bounded context bundle from the main graph
(neighbors + evidence) and report coverage. This measures how many concepts produce a useful bundle
vs empty. Writes data/graph/context-coverage.json.
"""
import json, os

GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
CORPUS = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
OUT = "/mnt/HC_Volume_106427611/ip-graph/data/graph/context-coverage.json"

g = json.load(open(GRAPH))
concepts = [n for n in g["nodes"] if n["type"] == "concept"]
concept_ids = {n["id"] for n in concepts}

# adjacency from edges
neighbors = {cid: set() for cid in concept_ids}
edge_type = {}
for e in g["edges"]:
    f, t = e["from"], e["to"]
    if f in concept_ids and t in concept_ids:
        neighbors[f].add(t); neighbors[t].add(f)
        edge_type.setdefault((f, t), set()).add(e["relationship"])

# corpus concept presence for grounding
corpus_text = {}
for l in open(CORPUS):
    r = json.loads(l); corpus_text[r["docname"]] = r["text"].lower()

def concept_in_corpus(cid):
    name = cid.split(":")[-1].replace("_", " ")
    hits = [doc for doc, t in corpus_text.items() if name in t]
    return hits

rows = []
for c in concepts:
    cid = c["id"]; name = c["label"]
    nb = neighbors.get(cid, set())
    n_edges = len(nb)
    # distinct relations from this concept
    rels = set()
    for (f, t), rs in edge_type.items():
        if f == cid or t == cid: rels |= rs
    # grounding in corpus
    grounding_docs = concept_in_corpus(cid)
    ceiling = c["properties"].get("epistemic_ceiling", "?")
    rows.append({
        "id": cid, "label": name, "neighbors": len(nb),
        "relations": sorted(rels), "grounding_docs": len(grounding_docs),
        "epistemic_ceiling": ceiling,
        "bundle_usable": len(nb) > 0 and len(grounding_docs) > 0,
    })

json.dump({"concepts": len(rows), "rows": rows}, open(OUT, "w"), indent=1)

usable = sum(1 for r in rows if r["bundle_usable"])
print("=== BOUNDED-CONTEXT COVERAGE ACROSS ALL CONCEPTS ===")
print(f"concepts: {len(rows)}, usable bundles: {usable} ({100*usable/len(rows):.0f}%)\n")
print(f"{'concept':18s} {'nb':>3s} {'ground':>5s} {'ceiling':32s} usable")
for r in sorted(rows, key=lambda x: -x["neighbors"]):
    print(f"{r['label']:18s} {r['neighbors']:3d} {r['grounding_docs']:5d} {r['epistemic_ceiling']:32s} {'Y' if r['bundle_usable'] else 'N'}")
print(f"\nwrote {OUT}")

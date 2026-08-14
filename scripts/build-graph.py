#!/usr/bin/env python3
"""Rebuild the graph from the CLEAN corpus.jsonl (425 records, no error pages)."""
import os, re, json
from collections import Counter
import networkx as nx

JSONL = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
OUT_DIR = "/mnt/HC_Volume_106427611/ip-graph/data/graph"

CONCEPT_LEXICON = {
    "free will": ("free_will", "concept", ["free_will", "determinism", "mind"]),
    "freewill": ("free_will", "concept", ["free_will", "determinism", "mind"]),
    "determinism": ("determinism", "concept", ["determinism", "causality", "free_will"]),
    "indeterminism": ("indeterminism", "concept", ["chance", "quantum", "free_will"]),
    "causality": ("causality", "concept", ["causality", "determinism"]),
    "entropy": ("entropy", "concept", ["entropy", "information", "life"]),
    "information": ("information", "concept", ["information", "knowledge"]),
    "consciousness": ("consciousness", "concept", ["mind", "knowledge"]),
    "qualia": ("qualia", "concept", ["mind"]),
    "quantum": ("quantum_mechanics", "concept", ["quantum"]),
    "wave function": ("wave_function", "concept", ["quantum"]),
    "entanglement": ("entanglement", "concept", ["quantum"]),
    "measurement": ("measurement", "concept", ["quantum"]),
    "superposition": ("superposition", "concept", ["quantum"]),
    "probability": ("probability", "concept", ["chance", "quantum"]),
    "randomness": ("randomness", "concept", ["chance", "determinism"]),
    "chance": ("chance", "concept", ["chance"]),
    "knowledge": ("knowledge", "concept", ["knowledge"]),
    "belief": ("belief", "concept", ["knowledge"]),
    "truth": ("truth", "concept", ["knowledge"]),
    "mind": ("mind", "concept", ["mind"]),
    "mind-body": ("mind_body", "concept", ["mind"]),
    "agency": ("agency", "concept", ["free_will", "mind"]),
    "responsibility": ("responsibility", "concept", ["free_will", "value"]),
    "compatibilism": ("compatibilism", "school", ["free_will", "determinism"]),
    "libertarianism": ("libertarianism", "school", ["free_will", "determinism"]),
    "incompatibilism": ("incompatibilism", "school", ["free_will", "determinism"]),
    "arrow of time": ("arrow_of_time", "concept", ["entropy", "chance"]),
    "second law": ("second_law", "concept", ["entropy", "information"]),
    "information theory": ("information_theory", "concept", ["information"]),
    "computation": ("computation", "concept", ["information", "mind"]),
    "life": ("life", "concept", ["life"]),
    "evolution": ("evolution", "concept", ["life"]),
    "value": ("value", "concept", ["value"]),
    "morality": ("morality", "concept", ["value"]),
    "measurement problem": ("measurement_problem", "problem", ["quantum"]),
    "mind body problem": ("mind_body_problem", "problem", ["mind"]),
}
AUTHORS = {
    "einstein": ("author", ["quantum", "information"]), "bell": ("author", ["quantum"]),
    "bohr": ("author", ["quantum"]), "planck": ("author", ["quantum", "entropy"]),
    "schr": ("author", ["quantum"]), "wheeler": ("author", ["quantum", "information"]),
    "dennett": ("author", ["free_will", "mind"]), "kane": ("author", ["free_will"]),
    "sperry": ("author", ["mind", "free_will"]), "deacon": ("author", ["life", "information"]),
    "landauer": ("author", ["information"]), "shannon": ("author", ["information"]),
    "turing": ("author", ["information", "mind"]), "godel": ("author", ["knowledge"]),
    "boltzmann": ("author", ["entropy"]), "gibbs": ("author", ["entropy"]),
    "laplace": ("author", ["determinism", "chance"]), "leibniz": ("author", ["determinism", "free_will"]),
}
def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
def find_concepts(text):
    low = norm(text); found = Counter()
    for phrase, (cid, _, _) in CONCEPT_LEXICON.items():
        p = norm(phrase)   # normalize the lexicon key too (mind-body -> mind body)
        if p and p in low: found[cid] += low.count(p)
    return found
def find_authors(text):
    low = norm(text); return {a for a in AUTHORS if a in low}

docs = []
for line in open(JSONL):
    r = json.loads(line)
    text = r["text"]; section = r["section"]; title = r["title"]
    docs.append({"path": r["id"], "section": section, "title": title, "text": text,
                 "concepts": find_concepts(text), "authors": find_authors(text)})

CG = nx.Graph()
for d in docs:
    cs = list(d["concepts"].keys())
    for i in range(len(cs)):
        for j in range(i+1, len(cs)):
            if CG.has_edge(cs[i], cs[j]): CG[cs[i]][cs[j]]["weight"] += 1
            else: CG.add_edge(cs[i], cs[j], weight=1)

TYPE_COLOR = {"concept": "#aec6ff", "author": "#ffb3ba", "work": "#b5ead7",
              "school": "#ffd1a1", "problem": "#ffc3e0", "theme": "#c1f0c1"}
nodes = []; node_ids = {}
def add_node(nid, label, ntype, **props):
    if nid not in node_ids:
        node_ids[nid] = len(nodes); nodes.append({"id": nid, "label": label, "type": ntype, "color": TYPE_COLOR.get(ntype, "#cccccc"), "properties": props})

for cid in set(c for _, (c, cat, themes) in CONCEPT_LEXICON.items()):
    cat = next(cat for _, (cc, cat, _) in CONCEPT_LEXICON.items() if cc == cid)
    themes = next(t for _, (cc, _, t) in CONCEPT_LEXICON.items() if cc == cid)
    add_node(f"ip:concept:{cid}", cid.replace("_", " ").title(), cat, themes=themes)
for name, (cat, themes) in AUTHORS.items():
    add_node(f"ip:author:{name}", name.title(), cat, themes=themes)
for d in docs:
    add_node(f"ip:doc:{d['path']}", d["title"], "work", section=d["section"])

edges = []
for d in docs:
    for cid in d["concepts"]:
        edges.append({"from": f"ip:doc:{d['path']}", "to": f"ip:concept:{cid}", "relationship": "discusses", "direction": "directed", "properties": {}})
    for an in d["authors"]:
        edges.append({"from": f"ip:doc:{d['path']}", "to": f"ip:author:{an}", "relationship": "authored_by", "direction": "directed", "properties": {}})
for a, b, data in CG.edges(data=True):
    edges.append({"from": f"ip:concept:{a}", "to": f"ip:concept:{b}", "relationship": "co_occurs_with", "direction": "undirected", "properties": {"weight": data["weight"]}})
themes = sorted(set(t for _, (_, _, ts) in CONCEPT_LEXICON.items() for t in ts))
for theme in themes:
    add_node(f"ip:theme:{theme}", theme.replace("_", " ").title(), "theme")
    for cid, (_, _, ts) in CONCEPT_LEXICON.items():
        if theme in ts:
            edges.append({"from": f"ip:concept:{cid}", "to": f"ip:theme:{theme}", "relationship": "belongs_to", "direction": "directed", "properties": {}})

graph_out = {"metadata": {"createdDate": "2026-08-14", "lastUpdated": "2026-08-14", "description": "IP knowledge graph (clean corpus)"}, "nodes": nodes, "edges": edges}
json.dump(graph_out, open(os.path.join(OUT_DIR, "graph.json"), "w"), indent=1)

G = nx.Graph()
for d in docs:
    G.add_node(d["path"], title=d["title"], section=d["section"])
ids = list(G.nodes)
for i, a in enumerate(ids):
    for b in ids[i+1:]:
        shared = set(G.nodes[a].get("concepts", [])) & set(G.nodes[b].get("concepts", []))
        if not shared:
            ca = set(docs[[d["path"] for d in docs].index(a)]["concepts"])
            cb = set(docs[[d["path"] for d in docs].index(b)]["concepts"])
            shared = ca & cb
        if shared: G.add_edge(a, b, weight=len(shared))
G2 = nx.Graph()
for n, d in G.nodes(data=True):
    G2.add_node(n, **{k: (",".join(v) if isinstance(v, (list, set)) else v) for k, v in d.items()})
for a, b, d in G.edges(data=True):
    G2.add_edge(a, b, **{k: (",".join(v) if isinstance(v, (list, set)) else v) for k, v in d.items()})
nx.write_gexf(G2, os.path.join(OUT_DIR, "doc_graph.gexf"))

print(f"=== CLEAN GRAPH: {len(nodes)} nodes, {len(edges)} edges, {len(docs)} docs ===")
tc = Counter()
for d in docs:
    for c in d["concepts"]: tc[c] += 1
for c, n in tc.most_common(15):
    print(f"  {c:20s} {n}")

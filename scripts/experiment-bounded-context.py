#!/usr/bin/env python3
"""experiment-bounded-context.py — test PathRAG-style bounded context (SPEC-08 C).

Given a query concept, build a bounded context bundle:
  - the reasoning path through the argument graph (premises -> conclusion)
  - the evidence quotes + supporting works
  - capped to token_budget
This is the "one agent question = one request" retrieval primitive.
"""
import os, sys, json

GRAPH = "/mnt/HC_Volume_106427611/ip-graph/data/graph/graph.json"
ARGS = "/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"
CORPUS = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"

g = json.load(open(GRAPH))
arg = json.load(open(ARGS))

# build label + evidence lookup
node_label = {}
for n in g["nodes"]:
    node_label[n["id"]] = n["label"]

# corpus: docname -> short text snippet (first 400 chars) for evidence grounding
snippet = {}
for l in open(CORPUS):
    r = json.loads(l); snippet[r["docname"]] = r["text"][:400].replace("\n", " ")

def context_for(concept, token_budget=800):
    """Bounded context bundle for a concept via the argument graph path."""
    parts = [f"## {concept.upper()}\n"]
    used = 0
    by_id = {n["id"]: n for n in arg["information_nodes"]}
    # map inferences: premise -> conclusion
    premise_to_concl = {}
    for f in arg["inference_nodes"]:
        for p in f.get("premise_ids", []):
            premise_to_concl[p] = f["conclusion_id"]
    # seed: info nodes whose text/evidence matches the concept, OR that are reachable
    concept_look = concept.replace("_", " ")   # free_will -> free will
    def node_matches(n):
        hay = (n["text"] + " " + n.get("evidence_quote", "")).lower()
        return concept_look in hay or concept in hay
    seeds = [n for n in arg["information_nodes"] if node_matches(n)]
    # expand: follow the chain forward from any seed
    visited = set()
    chain = []
    for s in seeds:
        cur = s["id"]
        steps = 0
        while cur in premise_to_concl and cur not in visited and steps < 5:
            visited.add(cur); chain.append(cur); cur = premise_to_concl[cur]; steps += 1
        if cur not in visited:
            visited.add(cur); chain.append(cur)
    for nid in chain:
        n = by_id.get(nid)
        if not n: continue
        line = f"[{n['id']}] {n['text']}  (ceiling: {n['epistemic_ceiling']})\n  evidence: {n.get('evidence_quote','')}\n"
        if used + len(line.split()) > token_budget: break
        parts.append(line); used += len(line.split())
        for ref in n.get("source_refs", []):
            snip = snippet.get(ref, "")
            if snip and used + 40 < token_budget:
                parts.append(f"  -> {ref}: {snip[:120]}...\n"); used += 20
    for c in arg["conflict_nodes"]:
        if concept.lower() in (c.get("text","")+c.get("evidence_quote","")).lower():
            line = f"[{c['id']}] CONFLICT: {c['text']}  (vs {c.get('a_id')}/{c.get('b_id')})\n"
            if used + len(line.split()) < token_budget:
                parts.append(line); used += len(line.split())
    parts.append(f"\n_(~{used} tokens, budget {token_budget})_")
    return "".join(parts)

print("=== BOUNDED CONTEXT TEST (PathRAG-style) ===")
for concept in ["free_will", "information", "determinism"]:
    print(f"\n{'='*70}\n{context_for(concept, 500)}")

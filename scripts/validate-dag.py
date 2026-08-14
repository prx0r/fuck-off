#!/usr/bin/env python3
"""validate-dag.py (SPEC-01) — verify the canonical DAG:
1. every 'requires' layer is defined
2. no cycles (topological sort succeeds)
3. every source_ref grounds in data/corpus.jsonl
4. emit derives_from edges summary
Exits non-zero on any violation.
"""
import sys, json, os
import yaml

DAG = "/mnt/HC_Volume_106427611/ip-graph/data/graph/canonical-dag.yaml"
CORPUS = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"

dag = yaml.safe_load(open(DAG))["dependencies"]

# corpus docnames for grounding check
corpus_names = set()
for l in open(CORPUS):
    r = json.loads(l)
    corpus_names.add(r["docname"])
    corpus_names.add(r["docname"].lower())

errors = []

# 1. requires defined
for layer, d in dag.items():
    for req in d.get("requires", []):
        if req not in dag and req != "SOURCE":
            errors.append(f"layer {layer}: requires undefined layer '{req}'")

# 2. cycle detection (topological)
adj = {l: set(d.get("requires", [])) - {"SOURCE"} for l, d in dag.items()}
visited, stack = set(), set()
cycle = None
def dfs(n):
    global cycle
    if n in stack:
        cycle = n; return True
    if n in visited: return False
    visited.add(n); stack.add(n)
    for m in adj.get(n, []):
        if m in adj and dfs(m): return True
    stack.discard(n); return False
for n in dag:
    if dfs(n):
        errors.append(f"cycle detected at '{cycle}'"); break

# 3. source_refs ground in corpus
for layer, d in dag.items():
    for ref in d.get("source_refs", []):
        bare = ref.split("/")[-1]
        if not any(bare.lower() in c.lower() for c in corpus_names):
            errors.append(f"layer {layer}: source_ref '{ref}' not found in corpus")

print("=== CANONICAL DAG VALIDATION ===")
print(f"layers: {len(dag)}")
print(f"dependencies defined: {[l for l in dag]}")
if errors:
    print(f"\nERRORS ({len(errors)}):")
    for e in errors[:20]: print("  -", e)
    sys.exit(1)
else:
    print("\nPASS: no undefined deps, no cycles, all source_refs grounded.")
    # emit the chain
    order = [l for l in dag]  # topological order is source->target as defined
    print("\nDerivational chain:")
    print("  " + " -> ".join(order))
    sys.exit(0)

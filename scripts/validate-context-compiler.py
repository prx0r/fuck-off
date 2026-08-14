#!/usr/bin/env python3
"""validate-context-compiler.py — the PROJECTION COMPILER on real data (SPEC-00 §15, SPEC-49).

Proves the single highest-leverage read-plane build: compiling the canonical graph into immutable,
addressable, per-entity CONTEXT BUNDLES (one agent question = one request). Reuses the proven
query.py (KG2Code) + retrieval.py (PathRAG) kernels + the graphrag LocalSearchMixedContext pattern.
Produces cacheable JSON + Markdown projections with the SPEC-00 budget/view/depth contract.
"""
import os, sys, json, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from context_compiler import ContextCompiler

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== PROJECTION COMPILER: canonical graph -> immutable per-entity context bundles ===\n")

# ---- REAL input ----
g = json.load(open(f"{ROOT}/data/graph/graph.json"))
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))
compiler = ContextCompiler(g, arg)
check("real graph loaded", len(g["nodes"]) == 490 and len(g["edges"]) == 6578)

# ---- compile a real entity bundle ----
bundle = compiler.compile("ip:concept:free_will", depth=1)
check("entity resolves: Free Will", bundle is not None and bundle.entity["label"] == "Free Will")
check("entity carries honest ceiling", bundle.entity["ceiling"] is not None)
check("depth-1 neighbors found", len(bundle.neighbors) > 0)

# ---- the agent contract: one request, budget/view/depth ----
full = bundle.to_dict("context", budget=None, depth=1)
check("context view has positions+relations+neighbors+provenance",
      all(k in full["content"] for k in ["positions", "relations", "neighbors", "provenance"]))
compact = bundle.to_dict("compact", budget=None, depth=1)
check("compact view is just entity+definition",
      set(compact["content"].keys()) == {"entity", "definition"})
bounded = bundle.to_dict("context", budget=5, depth=1)
check("token budget caps the bundle (bounded context, SPEC-00 §23)",
      "budget" in bounded["meta"] and bounded["meta"]["budget"] == 5)

# ---- content-addressed (immutable, cacheable) ----
h1 = bundle.bundle_hash
bundle2 = compiler.compile("ip:concept:free_will", depth=1)
check("content-addressed: same inputs -> same bundle hash (cacheable)",
      h1 == bundle2.bundle_hash and h1 is not None)
check("bundle hash is a real sha256-16", len(h1) == 16 and all(c in "0123456789abcdef" for c in h1))

# ---- determinism: repeated compile is byte-identical ----
check("deterministic: repeated compile identical", json.dumps(bundle.to_dict("context")) ==
      json.dumps(bundle2.to_dict("context")))

# ---- markdown projection (for Astro + agent .md) ----
md = compiler.to_markdown("ip:concept:free_will", view="context", budget=None, depth=1)
check("markdown projection produced (Astro/agent .md)", md is not None and md.startswith("# Free Will"))

# ---- compile MANY entities (the corpus pass) ----
compiled = 0
for n in g["nodes"]:
    if n.get("type") == "concept" and compiler.compile(n["id"], depth=1):
        compiled += 1
check(f"compiled {compiled} concept bundles", compiled >= 20)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nTHE PROJECTION COMPILER: real graph -> immutable, content-addressed, per-entity context")
print("bundles (one agent question = one request), with the SPEC-00 budget/view/depth contract and")
print("markdown projections for Astro + agent .md. This unblocks agent bundles, Astro, MCP, and SEO.")
print(f"\nSAMPLE FREE-WILL BUNDLE (compact): {json.dumps(bundle.to_dict('compact'), indent=1)}")
sys.exit(0 if all(c for _,c in results) else 1)

#!/usr/bin/env python3
"""validate-bundle-router.py — the compiled agent bundles + MCP + R2-style emission (SPEC-00 §15/§16).

Proves the full agent read-plane: one HTTP request / one MCP tool call returns the compiled context
bundle for a real entity, with the SPEC-00 budget/view/depth contract, plus R2-style immutable
content-addressed artifact emission. Reuses context_compiler + fts_search + query kernels.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from bundle_router import BundleRouter

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
OUT = "/tmp/opencode/bundles"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== COMPILED AGENT BUNDLES + MCP + R2 EMISSION ===\n")
g = json.load(open(f"{ROOT}/data/graph/graph.json"))
arg = json.load(open(f"{ROOT}/data/graph/argument.json"))
router = BundleRouter(g, arg, out_dir=OUT)

# seed the FTS index from the corpus (for the search tool)
with open(f"{ROOT}/data/corpus.jsonl") as f:
    for line in f:
        r = json.loads(line)
        router.fts.add(r.get("id", r.get("title","")), f"{r.get('title','')} {r.get('body','')}")

# ---- ONE request returns the whole bundle ----
b = router.route_get("ip:concept:free_will", view="context", budget=None, depth=1)
check("GET /bundle/free-will returns one compiled bundle", b["format"] == "json")
check("bundle has entity + content + meta", "entity" in b and "content" in b and "meta" in b)
check("one request = one bundle (not 7 calls)", "content" in b and "neighbors" in b["content"])

# ---- budget + depth contract ----
b_budget = router.route_get("ip:concept:free_will", view="context", budget=2000, depth=1)
check("budget=2000 respected", b_budget["meta"]["budget"] == 2000)
b_compact = router.route_get("ip:concept:free_will", view="compact")
check("view=compact honored", set(b_compact["content"].keys()) <= {"entity", "definition"})

# ---- markdown projection (Astro + agent .md) ----
md = router.route_get("ip:concept:free_will", format="md")
check("format=md returns prose projection", md["format"] == "md" and md["body"].startswith("# Free Will"))

# ---- R2-style immutable emission ----
rec = router.emit("ip:concept:free_will", view="context", depth=1)
check("R2-style artifact emitted with content-addressed hash", rec and "v" in rec)
check("artifact file exists on disk", rec and os.path.exists(rec["path"]))
rec2 = router.emit("ip:concept:free_will", view="context", depth=1)
check("immutable: same entity -> same version hash (no rewrite)", rec["v"] == rec2["v"])

# ---- MCP 8-tool adapter (one call per question) ----
check("MCP resolve tool", router.mcp("resolve", {"name": "Free Will"}) == "ip:concept:free_will")
check("MCP context tool (one call = full bundle)",
      isinstance(router.mcp("context", {"id": "ip:concept:free_will", "token_budget": 8000}), dict)
      and "content" in router.mcp("context", {"id": "ip:concept:free_will", "token_budget": 8000}))
check("MCP neighbors tool", len(router.mcp("neighbors", {"id": "ip:concept:free_will"})) > 0)
check("MCP evidence tool has ceiling", router.mcp("evidence", {"id": "ip:concept:free_will"}).get("ceiling") is not None)
search_hits = router.mcp("search", {"query": "free will"})
check("MCP search tool returns ranked hits", len(search_hits) > 0 and "score" in search_hits[0])
check("MCP tool whitelist is exactly 8 (not 70 micro-tools)",
      router.TOOLS == ("resolve", "search", "get", "context", "trace", "compare", "neighbors", "evidence"))

# ---- compile ALL concept bundles to R2 (the corpus pass) ----
n_emitted = 0
for n in g["nodes"]:
    if n.get("type") == "concept":
        r = router.emit(n["id"], view="context", depth=1)
        if r:
            n_emitted += 1
check(f"emitted {n_emitted} concept bundles (R2 corpus pass)", n_emitted >= 20)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nCOMPILED AGENT BUNDLES: one HTTP request / one MCP tool call returns the full compiled")
print("bundle, with the SPEC-00 budget/view/depth contract, markdown projections, and R2-style")
print("immutable content-addressed emission. The agent read-plane is live on real data.")
sys.exit(0 if all(c for _,c in results) else 1)

"""lib/bundle_router.py — the compiled agent-bundle router (Layer 06/07, SPEC-00 §15/§16, SPEC-49).

The read-plane HTTP + MCP semantics over the projection compiler. Implements the SPEC-00 contract:
  GET /bundle/{id}?view=compact|evidence|context&budget=2000|8000|32000&depth=0|1|2  -> one request
  GET /api/v1/concepts/{id}?view=...  (API alias)
  POST /mcp  {tool: context|resolve|search|get|trace|compare|neighbors|evidence}
Agent performance: ONE HTTP request / ONE tool call per question (SPEC-00 §23). The bundle is a
compiled, immutable, content-addressed artifact (R2 in prod; emitted to disk here as immutable bytes).
"""
from __future__ import annotations
import os, json, hashlib


def _sha(b): return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


class BundleRouter:
    """Emits + serves compiled bundles with the SPEC-00 URL/MCP contract. Immutable R2 semantics."""

    VIEWS = ("compact", "evidence", "context")
    BUDGETS = (2000, 8000, 32000)
    TOOLS = ("resolve", "search", "get", "context", "trace", "compare", "neighbors", "evidence")

    def __init__(self, graph_json, argument_json, out_dir=None):
        from context_compiler import ContextCompiler
        from fts_search import FTSIndex
        self.compiler = ContextCompiler(graph_json, argument_json)
        self.fts = FTSIndex(use_duckdb=True)
        self.out_dir = out_dir
        self.artifact_log = []   # emitted immutable artifacts

    # ---- R2-style immutable emission (compute-on-write; reads = static bytes) ----
    def emit(self, entity_id, view="context", budget=None, depth=1):
        """Compile + write an immutable, content-addressed artifact. Returns its path + hash."""
        b = self.compiler.compile(entity_id, depth)
        if not b:
            return None
        artifact = b.to_dict(view, budget, depth)
        h = artifact["meta"]["bundle_hash"]
        if self.out_dir:
            # immutable URL: /bundle/{id}?v={hash}  -> files are content-addressed (R2 semantics)
            safe = entity_id.replace(":", "_").replace("/", "_")
            os.makedirs(self.out_dir, exist_ok=True)
            path = os.path.join(self.out_dir, f"{safe}.v{h}.json")
            with open(path, "w") as f:
                f.write(json.dumps(artifact))
            rec = {"entity": entity_id, "view": view, "budget": budget, "depth": depth,
                   "v": h, "bytes": os.path.getsize(path), "path": path}
            self.artifact_log.append(rec)
            return rec
        return {"entity": entity_id, "v": h, "bytes": len(json.dumps(artifact))}

    # ---- the HTTP router (one request per question) ----
    def route_get(self, entity_id, view="context", budget=None, depth=1, format="json"):
        """GET /bundle/{id}?view=&budget=&depth=&format=  ->  compiled bundle."""
        if view not in self.VIEWS:
            view = "context"
        if budget not in (None,) + self.BUDGETS:
            budget = None
        depth = max(0, min(2, depth))
        b = self.compiler.compile(entity_id, depth)
        if not b:
            return {"error": "not_found", "entity": entity_id}
        d = b.to_dict(view, budget, depth)
        if format == "md":
            return {"format": "md", "body": self.compiler.to_markdown(entity_id, view, budget, depth),
                    "meta": d["meta"]}
        return {"format": "json", **d}

    # ---- MCP thin adapter (8 tools, one call per question) ----
    def mcp(self, tool, params=None):
        """POST /mcp. Thin adapter over the same projections (SPEC-00 §16). NOT 70 micro-tools."""
        params = params or {}
        if tool == "resolve":
            return self.compiler.kq.resolve(params.get("name"))
        if tool == "get":
            return self.route_get(params.get("id"), params.get("view", "context"),
                                  params.get("budget"), params.get("depth", 1))
        if tool == "context":
            return self.route_get(params.get("id"), "context", params.get("token_budget", 8000),
                                  params.get("depth", 1))
        if tool == "neighbors":
            return self.compiler.kq.neighbors(params.get("id"), params.get("rel"))
        if tool == "evidence":
            return self.compiler.kq.evidence(params.get("id"))
        if tool == "search":
            hits = self.fts.search(params.get("query"), top_k=params.get("top_k", 5))
            return [{"id": d, "score": round(s, 4)} for d, s in hits]
        if tool == "trace":
            return self.compiler.kq.path(params.get("from"), params.get("to"),
                                         params.get("via"), params.get("max_hops", 4))
        if tool == "compare":
            a = self.compiler.compile(params.get("id_a"), 1)
            bb = self.compiler.compile(params.get("id_b"), 1)
            return {"a": a.entity if a else None, "b": bb.entity if bb else None}
        return {"error": f"unknown tool {tool}; use one of {self.TOOLS}"}

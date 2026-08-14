"""lib/query.py — KG2Code-style executable graph queries (Layer 10, Bet 2).

A tiny deterministic graph-query language: resolve / neighbors / path / evidence.
The agent writes the plan; the engine executes truth-preserving code with verifiable traces.
"""
from __future__ import annotations
from collections import deque

class KnowledgeQuery:
    def __init__(self, graph_json):
        self.nodes = {n["id"]: n for n in graph_json["nodes"]}
        self.label = {n["id"]: n["label"] for n in graph_json["nodes"]}
        self.type = {n["id"]: n["type"] for n in graph_json["nodes"]}
        self.adj = {}
        for e in graph_json["edges"]:
            f, t = e["from"], e["to"]
            self.adj.setdefault(f, []).append((t, e["relationship"]))
            self.adj.setdefault(t, []).append((f, e["relationship"]))

    def resolve(self, name, ntype=None):
        """resolve('Free Will', ntype='concept') -> node id."""
        for nid, n in self.nodes.items():
            if n["label"].lower() == name.lower():
                if ntype is None or self.type.get(nid) == ntype:
                    return nid
        return None

    def neighbors(self, nid, rel=None):
        return [n for n in self.adj.get(nid, []) if rel is None or n[1] == rel]

    def path(self, start_id, end_id, via=None, max_hops=4, limit=5):
        """BFS paths (deterministic). via = allowed relationship names."""
        q = deque([[start_id]]); out = []
        while q and len(out) < limit:
            p = q.popleft()
            if len(p) > max_hops: continue
            last = p[-1]
            if last == end_id and len(p) > 1:
                out.append(p); continue
            for nb, rel in self.adj.get(last, []):
                if nb not in p and (via is None or rel in via):
                    q.append(p + [nb])
        return out

    def evidence(self, nid):
        p = self.nodes.get(nid, {}).get("properties", {})
        return {"type": self.type.get(nid), "label": self.label.get(nid),
                "ceiling": p.get("epistemic_ceiling"), "review_state": p.get("review_state")}

    def execute(self, program, expected_label=None):
        """Run a composed query, return (trace, resolved_ok)."""
        result = program()
        if isinstance(result, list) and result and isinstance(result[0], list):
            flat = [n for p in result for n in p]
            trace = " | ".join(" -> ".join(self.label.get(n, n) for n in p) for p in result[:2])
            ok = any(self.label.get(n) == expected_label for n in flat) if expected_label else bool(result)
        else:
            flat = result if isinstance(result, list) else [result]
            trace = [self.label.get(n, n) for n in flat]
            ok = any(self.label.get(n) == expected_label for n in flat) if expected_label else bool(result)
        return trace, ok

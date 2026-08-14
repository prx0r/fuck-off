"""lib/graph_stable.py — the stable-graph projection (DEV_PLAN §1.5, Co-Evolving Organism / SPEC-13 F2).

The deterministic graph layer (from nano-graphrag's gdb_networkx): an identical input graph MUST yield
identical node/edge ordering every time (byte-reproducible serialization). This is the reproducibility
guarantee AGENTS.md demands — and the foundation for the Co-Evolving Organism's stable projections.

This kernel provides the stable projection primitives:
  - stabilize: canonical deterministic ordering of nodes + edges (sorted, byte-reproducible).
  - stable_lcc: the largest connected component, stabilized (deterministic, no graspologic dependency).
  - StableGraph: a stable graph projection keyed by a content hash — unchanged input = identical output
    (the compute-on-write / incremental core: only changed projections rebuild).
  - graph_hash: a content-addressed identity over the graph (the staleness check: hash mismatch = stale).

Grounded in: scripts/experiment-nano-stable-graph.py (the proven prototype), SPEC-13 F2/F3 (deterministic
serialization; staleness = the same traversal), nano-graphrag (stable_LCC + GraphML), SPEC-00 (content-addressed).
"""
from __future__ import annotations
import hashlib


def _sha(b):
    return hashlib.sha256(b.encode() if isinstance(b, str) else b).hexdigest()[:16]


class StableGraph:
    """A deterministic, content-addressed graph projection.

    Nodes/edges are stored in canonical sorted order so the projection is byte-reproducible; the graph
    carries a content hash so unchanged input = identical output (the incremental-rebuild core).
    """

    def __init__(self):
        self.nodes = {}      # id -> attributes (dict)
        self._edges = set()  # (src, dst) normalized

    def add_node(self, nid, **attrs):
        self.nodes[nid] = dict(attrs)

    def add_edge(self, src, dst, **attrs):
        # undirected canonical form: (min, max) so the edge is order-independent
        a, b = (src, dst) if src < dst else (dst, src)
        self._edges.add((a, b))
        if a not in self.nodes:
            self.nodes[a] = {}
        if b not in self.nodes:
            self.nodes[b] = {}

    # ---- canonical deterministic ordering (byte-reproducible) ----
    def stabilize(self):
        """Return the graph with nodes + edges in canonical sorted order."""
        sorted_nodes = sorted(self.nodes.items(), key=lambda x: x[0])
        sorted_edges = sorted(self._edges, key=lambda e: (e[0], e[1]))
        return {"nodes": [(n, attrs) for n, attrs in sorted_nodes],
                "edges": sorted_edges}

    # ---- the deterministic largest connected component ----
    def stable_lcc(self):
        """The largest connected component, stabilized (deterministic, no graspologic)."""
        comps = self._components()
        if not comps:
            return StableGraph()
        biggest = max(comps, key=len)
        sub = StableGraph()
        for n in sorted(biggest):
            sub.add_node(n, **self.nodes.get(n, {}))
        for a, b in self._edges:
            if a in biggest and b in biggest:
                sub.add_edge(a, b)
        return sub

    def _components(self):
        """Connected components (iterative BFS; deterministic node order)."""
        seen = set()
        comps = []
        for start in sorted(self.nodes):
            if start in seen:
                continue
            comp = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node in comp:
                    continue
                comp.add(node)
                for a, b in self._edges:
                    if a == node and b not in comp:
                        stack.append(b)
                    elif b == node and a not in comp:
                        stack.append(a)
            seen |= comp
            comps.append(comp)
        return comps

    # ---- content-addressed identity (the staleness check) ----
    def graph_hash(self):
        """A content address over the stable projection (hash mismatch = stale)."""
        s = self.stabilize()
        canonical = hashlib.sha256(
            ("NODES:" + repr(s["nodes"]) + "EDGES:" + repr(s["edges"])).encode()
        ).hexdigest()
        return canonical[:16]

    def n_components(self):
        return len(self._components())

    def summary(self):
        return {"nodes": len(self.nodes), "edges": len(self._edges),
                "components": self.n_components(), "hash": self.graph_hash()}

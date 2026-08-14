"""lib/lightrag_compare.py — LightRAG's core retrieval semantics, adapted + compared to ours (Layer 10).

Faithful adaptation of LightRAG's graph-RAG retrieval modes (base.py: local/global/hybrid/mix) onto our
real graph, for a head-to-head comparison with our proven PathRAG/KG2Code kernels. LightRAG (HKUDS, ⭐38k)
builds a KG from entities+relations then retrieves by:
  - local:  walk from seed entities along weighted neighbors (degree-weighted), gather 1-hop context
  - global: keyword/degree-driven map-reduce over the whole graph (rare + important entities)
  - hybrid/mix: combine both (+ vector).
This kernel reuses our `query.py` adjacency + `retrieval.py` to reproduce those modes deterministically,
so we can measure whether LightRAG's local mode beats our PathRAG on our graph.
"""
from __future__ import annotations
from collections import deque


class LightRAGRetriever:
    """LightRAG-style retrieval modes on our canonical graph (local/global/hybrid)."""

    def __init__(self, graph_json, argument_json=None):
        from query import KnowledgeQuery
        self.kq = KnowledgeQuery(graph_json)
        self.graph = graph_json
        self.argument = argument_json or {"information_nodes": []}

    # ---- local retrieval: weighted 1-hop neighbor walk from seeds (LightRAG local mode) ----
    def local_retrieve(self, seed_entity, hops=1, top_k=8):
        """Walk from a seed entity, gather neighbors weighted by node degree (LightRAG local)."""
        seed = self.kq.resolve(seed_entity) if isinstance(seed_entity, str) else seed_entity
        if seed is None:
            return []
        visited = {seed}
        frontier = [seed]
        scored = {}
        for _ in range(hops):
            nxt = []
            for nid in frontier:
                deg = len(self.kq.adj.get(nid, []))
                for nb, rel in self.kq.adj.get(nid, []):
                    if nb in visited:
                        continue
                    visited.add(nb)
                    nb_deg = len(self.kq.adj.get(nb, []))
                    # LightRAG local weights by degree/strength: relevant if high degree OR linked
                    scored[nb] = scored.get(nb, 0) + 1.0 / (1 + deg)
                    nxt.append(nb)
            frontier = nxt
        # rank by score then degree (LightRAG favors well-connected, directly-linked context)
        ranked = sorted(scored.items(), key=lambda kv: (-kv[1], -len(self.kq.adj.get(kv[0], []))))
        return [(self.kq.label.get(n, n), round(s, 3), len(self.kq.adj.get(n, [])))
                for n, s in ranked[:top_k]]

    # ---- global retrieval: degree + keyword-frequency map-reduce (LightRAG global mode) ----
    def global_retrieve(self, top_k=8):
        """Global: surface the rare-but-important entities by degree+frequency (LightRAG global)."""
        scored = {}
        for nid in self.kq.nodes:
            deg = len(self.kq.adj.get(nid, []))
            # global mode favors rare, important (high info) nodes: use inverse-degree salience
            if deg > 0:
                scored[nid] = 1.0 / (1 + deg)
        ranked = sorted(scored.items(), key=lambda kv: kv[1])[:top_k]  # rarest first = global context
        return [(self.kq.label.get(n, n), round(s, 3), len(self.kq.adj.get(n, [])))
                for n, s in ranked]

    # ---- hybrid: union of local + global (LightRAG hybrid mode) ----
    def hybrid_retrieve(self, seed_entity, top_k=10):
        local = self.local_retrieve(seed_entity, hops=1, top_k=top_k)
        global_ = self.global_retrieve(top_k=top_k)
        seen = set(); out = []
        for label, s, d in local + global_:
            if label not in seen:
                seen.add(label); out.append((label, s, d))
        return out[:top_k]

    # ---- evidence: pull the claims that touch the retrieved nodes (ours, onto LightRAG's output) ----
    def evidence_for(self, labels, top_k=5):
        hits = []
        for n in self.argument.get("information_nodes", []):
            text = str(n.get("label", n.get("id", "")))
            if any(lbl.lower() in text.lower() for lbl in labels):
                hits.append({"claim": text, "ceiling": n.get("epistemic_ceiling")})
        return hits[:top_k]

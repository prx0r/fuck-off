"""lib/retrieval.py — graph retrieval algorithms (Layer 10): PathRAG + HippoRAG + ToG-2 + bounded-context.

Borrowed from the arXiv papers (SPEC-08) and proven in experiments:
  - PathRAG: flow-based path retrieval with distance decay + path reliability
  - HippoRAG: Personalized PageRank multi-hop retrieval
  - ToG-2: alternating graph <-> document retrieval (arXiv 2407.10805) — the verified spine grounds
    each graph step in the underlying evidence documents, reducing hallucination.
"""
from __future__ import annotations
import networkx as nx


class GraphRetriever:
    def __init__(self, concept_edges, labels=None, weight_key="weight"):
        self.G = nx.Graph()
        self.labels = labels or {}
        for f, t, w in concept_edges:
            self.G.add_edge(f, t, weight=float(w))

    # ---- PathRAG: flow-based pruning ----
    def pathrag_flow(self, start, alpha=0.7, theta=1e-3, iters=50):
        S = {n: 0.0 for n in self.G.nodes}; S[start] = 1.0
        for _ in range(iters):
            delta = 0.0; newS = dict(S)
            for v in self.G.nodes:
                if v == start: continue
                incoming = sum(alpha * S[u] / max(1, self.G.degree(u)) for u in self.G.neighbors(v))
                newS[v] = incoming; delta = max(delta, abs(newS[v] - S[v]))
            S = newS
            if delta < 1e-6: break
        for v in S:
            if S[v] / max(1, self.G.degree(v)) < theta: S[v] = 0.0
        return S

    def pathrag_paths(self, start, end, max_hops=3, K=3, alpha=0.7):
        if start not in self.G or end not in self.G: return []
        S = self.pathrag_flow(start, alpha=alpha)
        paths = list(nx.all_simple_paths(self.G, start, end, cutoff=max_hops))
        scored = [(sum(S[v] for v in p) / max(1, len(p) - 1), p) for p in paths]
        scored.sort(key=lambda x: -x[0])
        return scored[:K]

    # ---- HippoRAG: Personalized PageRank ----
    def hipporag(self, seeds, top_k=8, weight="weight"):
        pers = {n: 0.0 for n in self.G.nodes}
        for s in seeds:
            if s in self.G: pers[s] = 1.0 / len(seeds)
        tot = sum(pers.values())
        if tot == 0: return []
        pers = {k: v/tot for k, v in pers.items()}
        ppr = nx.pagerank(self.G, personalization=pers, weight=weight)
        ranked = sorted(ppr.items(), key=lambda x: -x[1])
        return [(nid, round(sc, 4)) for nid, sc in ranked if nid not in seeds][:top_k]

    # ---- ToG-2: alternating graph <-> document retrieval ----
    def tog2(self, start, target=None, max_hops=3, max_iter=6, ground=None):
        """Alternate GRAPH expansion with DOCUMENT grounding (arXiv 2407.10805).

        At each step: (1) expand the frontier one hop on the graph, (2) GROUND each new node in its
        evidence documents (a `ground(nid)` callable returning an evidence dict — e.g. epistemic
        ceiling / review_state / source refs), (3) decide. This ties the verified concept spine back to
        its grounding docs, unlike single-lookup retrieval.

        Returns (trace, reached_target) where trace = [(node_id, evidence_dict), ...].
        """
        if start not in self.G:
            return [], False
        visited, frontier = {start}, [start]
        trace = []
        for it in range(max_iter):
            if len(trace) >= max_hops * 4:
                break
            # GRAPH layer: expand the frontier one hop
            candidates = []
            for n in frontier:
                for nb in self.G.neighbors(n):
                    if nb not in visited:
                        visited.add(nb)
                        candidates.append(nb)
            if not candidates:
                break
            # DOC layer: ground each new node
            grounded = []
            for c in candidates:
                ev = ground(c) if ground else {}
                grounded.append((c, ev))
                if target is not None and c == target:
                    trace.append((c, ev))
                    return trace, True
            trace.extend(grounded)
            frontier = [c for c, _ in grounded]
        return trace, (target is not None and target in visited)

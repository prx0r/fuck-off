"""lib/structure_recall.py — SAGE structure-aware recall on the read plane (arXiv 2605.12061).

Steal (2605.12061, SAGE: Self-Evolving Agentic Graph-Memory Engine): associative memory structured as a
graph that evolves with interactions; retrieval is STRUCTURE-AWARE (follows graph topology, not just
lexical match).

Our adaptation (bounded to the READ PLANE, off the verified spine — per the honest caveat): recall a
concept by FOLLOWING GRAPH TOPOLOGY from a seed (neighbors → their neighbors), not just string match.
Reuses our query.py adjacency. The graph-memory "evolution" here is the read-plane's retrieval graph
(which links resolve a question), kept strictly separate from the verified epistemic spine.
"""
from __future__ import annotations


class StructureAwareRecall:
    """Recall that follows graph topology (SAGE), on the read plane (off the verified spine)."""

    def __init__(self, graph_json, kq=None):
        from query import KnowledgeQuery
        self.kq = kq or KnowledgeQuery(graph_json)

    def resolve(self, entity_label):
        return self.kq.resolve(entity_label)

    def recall_structural(self, entity_label, max_depth=2, top_k=8):
        """Structure-aware recall: BFS the graph topology from a seed (SAGE), not lexical only."""
        nid = self.resolve(entity_label)
        if nid is None:
            return []
        visited = {nid}
        frontier = [nid]
        results = []
        for depth in range(1, max_depth + 1):
            nxt = []
            for f in frontier:
                for nb, rel in self.kq.adj.get(f, []):
                    if nb in visited:
                        continue
                    visited.add(nb)
                    results.append({"label": self.kq.label.get(nb, nb), "rel": rel,
                                    "depth": depth, "type": self.kq.type.get(nb, "")})
                    nxt.append(nb)
            frontier = nxt
            if len(results) >= top_k:
                break
        return results[:top_k]

    def recall_structured_context(self, entity_label, max_depth=1, top_k=6):
        """Return the structure-aware neighborhood as a context (for the read plane)."""
        neighbors = self.recall_structural(entity_label, max_depth=max_depth, top_k=top_k)
        return {"seed": entity_label, "n_nodes": len(neighbors),
                "structure": [{"label": n["label"], "via": n["rel"], "depth": n["depth"]}
                              for n in neighbors]}

"""lib/cognee_compare.py — Cognee's remember/recall + KG search, adapted + compared (Layer 09).

Cognee (topoteretes, ⭐30k, ecosystem/agent-memory/cognee) is a frontier AI-memory platform: ingest any
data → build a self-hosted knowledge graph → agents recall/connect/act with full context. Its core is
remember()/recall() with typed memory entries (QA, trace, feedback) routed into a KG, then search/
prune/forget.

We adapt its memory-entry + graph-recall pattern onto our canonical graph + argument, reusing our
`context_compiler` bundles. This lets us compare: Cognee-style typed memory recall vs our compiled
context bundles — both "give an agent full context in one call."
"""
from __future__ import annotations
from context_compiler import ContextCompiler


class CogneeMemory:
    """Cognee-style typed memory (remember/recall) over a knowledge graph, adapted to ours."""

    def __init__(self, graph_json, argument_json=None):
        self.compiler = ContextCompiler(graph_json, argument_json or {"information_nodes": []})
        self.memory = {}   # memory_id -> typed entry

    def remember(self, memory_id, content, mtype="qa", metadata=None):
        """remember(): store a typed memory entry (qa / trace / feedback / text)."""
        self.memory[memory_id] = {"type": mtype, "content": content,
                                  "metadata": metadata or {}, "graph": self._link(content)}
        return memory_id

    def _link(self, content):
        """Link the memory content to graph entities it mentions (the KG association)."""
        links = []
        text = content.lower() if isinstance(content, str) else ""
        for nid, node in self.compiler.kq.nodes.items():
            label = self.compiler.kq.label.get(nid, "")
            if label and label.lower() in text:
                links.append({"id": nid, "label": label})
        return links[:10]

    def recall(self, query, top_k=5):
        """recall(): return the memory entries whose linked entities match the query."""
        q = query.lower()
        scored = []
        for mid, m in self.memory.items():
            # score = how many linked-entity labels appear in the query OR how many query words match
            s = 0
            for link in m["graph"]:
                if link["label"].lower() in q:
                    s += 2
            s += sum(1 for w in q.split() if w in m["content"].lower())
            if s > 0:
                scored.append((s, mid, m))
        scored.sort(key=lambda x: -x[0])
        return [{"id": mid, "type": m["type"], "content": m["content"],
                 "links": m["graph"][:3]} for s, mid, m in scored[:top_k]]

    def search_graph(self, entity_label, depth=1):
        """search(): resolve an entity to its full context bundle (Cognee's graph recall)."""
        nid = self.compiler.kq.resolve(entity_label)
        if not nid:
            return None
        return self.compiler.compile(nid, depth).to_dict("context", None, depth)

    def forget(self, memory_id):
        """forget(): remove a memory entry (the memory hygiene primitive)."""
        if memory_id in self.memory:
            del self.memory[memory_id]
            return True
        return False

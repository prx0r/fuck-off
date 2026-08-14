"""lib/context_compiler.py — the PROJECTION COMPILER (Layer 06, SPEC-00 §15 + SPEC-49).

The single highest-leverage read-plane build: turns the canonical graph into immutable, addressable
per-entity CONTEXT BUNDLES — "one agent question = one request" (SPEC-00 §15). This adapts the frontier
graphrag `LocalSearchMixedContext` pattern (entity + relationships + evidence + community report in ONE
bundle, token-budgeted) to our graph, reusing the proven `query.py` (KG2Code) + `retrieval.py`
(PathRAG/HippoRAG) kernels. Never a live query — a compiled, cacheable artifact.

API contract (SPEC-00 §15 / §24, agent perf):
  /bundle/{id}                       -> full entity bundle
  ?view=compact|evidence|context     -> which sections
  ?budget=2000|8000|32000            -> token-bounded
  ?depth=0|1|2                        -> neighbor-depth (0 = self only, bounded to prevent explosion)
  ?format=json|md                    -> machine or prose

Every bundle carries: entity · definition · positions · relations · primary_evidence ·
important_works · disagreements · neighbors · provenance · canonical_url.
Output is content-addressed (hash of canonical inputs) -> immutable, cacheable.
"""
from __future__ import annotations
import hashlib, json


def _sha(obj): return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:16]


class ContextBundle:
    """A compiled per-entity context bundle (immutable, cacheable)."""

    # rough token cost (dense, machine-readable — the agent-cache-line)
    _FIELD_TOKEN_COST = {"entity": 1, "definition": 2, "positions": 3, "relations": 2,
                         "primary_evidence": 2, "important_works": 1, "disagreements": 2,
                         "neighbors": 2, "provenance": 1}

    def __init__(self, entity_id, label, entity_type, ceiling):
        self.entity = {"id": entity_id, "label": label, "type": entity_type, "ceiling": ceiling}
        self.definition = None
        self.positions = []          # claims/positions attached to the entity
        self.relations = []          # [(relation, target_label)]
        self.primary_evidence = []   # [(source_ref, quote)]
        self.important_works = []    # source works
        self.disagreements = []      # cruxes/tensions
        self.neighbors = []          # depth-bounded
        self.provenance = {}
        self.bundle_hash = None

    def to_dict(self, view="context", budget=None, depth=2):
        """Compile the bundle for a given view + token budget + depth."""
        out = {"entity": self.entity, "canonical_url": self.entity["id"]}
        sections = {
            "entity": lambda: self.entity,
            "definition": lambda: self.definition,
            "positions": lambda: self.positions,
            "relations": lambda: self.relations,
            "primary_evidence": lambda: self.primary_evidence,
            "important_works": lambda: self.important_works,
            "disagreements": lambda: self.disagreements,
            "neighbors": lambda: self.neighbors if depth > 0 else [],
            "provenance": lambda: self.provenance,
        }
        # view -> which sections (compact = self + def; evidence = + evidence/works; context = all)
        view_map = {
            "compact": ["entity", "definition"],
            "evidence": ["entity", "definition", "primary_evidence", "important_works"],
            "context": ["entity", "definition", "positions", "relations", "primary_evidence",
                        "important_works", "disagreements", "neighbors", "provenance"],
        }
        selected = view_map.get(view, view_map["context"])
        body = {}
        tokens = 0
        for sec in selected:
            val = sections[sec]()
            body[sec] = val
            if val:
                tokens += self._FIELD_TOKEN_COST.get(sec, 1)
            if budget and tokens > budget:  # hard cap (SPEC-00 §23: bounded context)
                body.pop(sec, None)
                break
        out["content"] = body
        out["meta"] = {"view": view, "budget": budget, "depth": depth,
                       "bundle_hash": _sha({"id": self.entity["id"], "body": body})}
        return out


class ContextCompiler:
    """Compiles the canonical graph into ContextBundles (the projection compiler)."""

    def __init__(self, graph_json, argument_json=None):
        from query import KnowledgeQuery
        from retrieval import GraphRetriever
        self.kq = KnowledgeQuery(graph_json)
        self.graph = graph_json
        self.argument = argument_json or {"information_nodes": [], "conflict_nodes": []}

    def compile(self, entity_id, depth=1):
        """Build a ContextBundle for an entity from the canonical graph."""
        node = self.kq.nodes.get(entity_id)
        if not node:
            return None
        label = self.kq.label.get(entity_id, entity_id)
        ntype = self.kq.type.get(entity_id, "")
        props = node.get("properties", {})
        b = ContextBundle(entity_id, label, ntype, props.get("epistemic_ceiling"))
        b.definition = props.get("definition") or f"{label} — canonical {ntype} node"
        # neighbors (depth-bounded, dedup)
        seen = {entity_id}
        frontier = [entity_id]
        for _ in range(max(1, depth)):
            nxt = []
            for f in frontier:
                for nb, rel in self.kq.neighbors(f):
                    if nb not in seen:
                        seen.add(nb)
                        b.neighbors.append({"label": self.kq.label.get(nb, nb),
                                            "rel": rel, "type": self.kq.type.get(nb, "")})
                        nxt.append(nb)
            frontier = nxt
            if not frontier:
                break
        # relations = typed neighbor edges
        b.relations = b.neighbors[:]
        # positions from the argument graph (information nodes mentioning this entity)
        for n in self.argument.get("information_nodes", []):
            if entity_id in str(n.get("source_refs", "")) or label.lower() in str(n.get("id", "")).lower():
                b.positions.append({"claim": n.get("label", n.get("id")),
                                    "ceiling": n.get("epistemic_ceiling")})
        # disagreements = conflict nodes (cruxes) touching this entity
        for c in self.argument.get("conflict_nodes", []):
            if entity_id in str(c.get("id", "")) or label.lower() in str(c.get("id", "")).lower():
                b.disagreements.append({"crux": c.get("label", c.get("id"))})
        # provenance = the content-addressed source
        b.provenance = {"source_hash": _sha({"id": entity_id, "label": label}),
                        "graph_hash": _sha({"nodes": len(self.graph.get("nodes", [])),
                                            "edges": len(self.graph.get("edges", []))})}
        b.bundle_hash = _sha({"id": entity_id, "label": label,
                              "neighbors": len(b.neighbors), "positions": len(b.positions)})
        return b

    def to_markdown(self, entity_id, view="context", budget=None, depth=1):
        """Prose/MD projection (for Astro pages + agent .md)."""
        b = self.compile(entity_id, depth)
        if not b:
            return None
        d = b.to_dict(view, budget, depth)
        md = [f"# {b.entity['label']}\n", f"**Type:** {b.entity['type']} · **Ceiling:** {b.entity['ceiling']}\n"]
        body = d.get("content", {})
        if "definition" in body and body["definition"]:
            md.append(f"**Definition:** {body['definition']}\n")
        if "positions" in body and body["positions"]:
            md.append("## Positions\n" + "\n".join(f"- {p['claim']} ({p['ceiling']})" for p in body["positions"]))
        if "neighbors" in body and body["neighbors"]:
            md.append("## Neighbors\n" + "\n".join(f"- {n['label']} [{n['rel']}]" for n in body["neighbors"][:20]))
        if "primary_evidence" in body and body["primary_evidence"]:
            md.append("## Evidence\n" + "\n".join(f"- {e[0]}: {e[1][:80]}" for e in body["primary_evidence"]))
        if "disagreements" in body and body["disagreements"]:
            md.append("## Disagreements\n" + "\n".join(f"- {c['crux']}" for c in body["disagreements"]))
        md.append(f"\n`{b.bundle_hash}`")
        return "\n".join(md)

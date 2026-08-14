# ALGORITHMS — granular findings from reading the arXiv papers

*2026-08-14. I read the actual papers (not just surveys) and implemented their core algorithms against
our real graph. This is the granular, implementable knowledge. Every experiment is reproducible via
`scripts/experiment-*.py`.*

---

## 1. PathRAG (arXiv 2502.14902) — flow-based path retrieval ⭐ IMPLEMENTED

**The insight:** graph-RAG's problem is *redundancy*, not insufficiency. Retrieve **key relational
paths**, not node piles. Use **flow-based pruning** with distance awareness.

**Algorithm (`experiment-pathrag.py`):**
1. **Node retrieval** — extract keywords, dense-match top-N nodes (N=40 in paper)
2. **Flow-based pruning** (eq.2): resource propagation with decay
   ```
   S(vi) = Σ_{vj∈N(·,vi)} α·S(vj)/|N(vj,·)|,   α=0.7
   ```
   Early-stop when `S(vi)/|N(vi)| < θ` (θ small)
3. **Path reliability** (eq.4): `S(P) = (1/|E_P|)·Σ_{vi∈V_P} S(vi)`
4. **Path prompting** (eq.6): place paths in **ascending reliability** — most reliable LAST (the
   "golden memory" region), query first. Addresses LLM "lost in the middle."
5. **Complexity:** O(N²/((1-α)·θ)) — cheap since N<<|V|

**Result on our graph:** retrieves sensible relational paths (Quantum→Indeterminism→FreeWill,
Entropy→Information). Token-efficient (pruned, not full piles).

## 2. HippoRAG (arXiv 2405.14831) — Personalized PageRank ⭐ IMPLEMENTED

**The insight:** hippocampal indexing theory. LLM extracts query entities → **Personalized PageRank**
over the KG (the personalization = query entities) → top-ranked nodes = retrieved passages.

**Algorithm (`experiment-hipporag.py`):**
1. LLM extracts query entities (our: query concepts)
2. PPR with `personalization = seed concepts`, `weight = co-occurrence`
3. Top-k ranked nodes = multi-hop retrieval in ONE step

**Result on our graph:** PPR surfaces indirectly-related concepts in one step (no iterative retrieval).
**Finding/bias:** high-degree hub nodes (Value, Information) rank too high — PPR is structure-dominated,
not query-specific. The paper weights PPR with relevance; our small dense graph needs that correction.

## 3. KG2Code (arXiv 2607.22652) — executable graph queries ⭐ IMPLEMENTED (Bet 2)

**The insight:** transform the KG into **executable code**. KGQA becomes code generation → verifiable
reasoning traces + executable code, mitigating hallucination.

**Algorithm (`experiment-kg2code.py`):** a tiny deterministic graph-query language:
```
resolve('Free Will') -> node id
neighbors(nid, rel=...) -> [(node, rel)]
path(from, to, via=[rels], max_hops) -> [node-sequences]  (BFS, deterministic)
evidence(nid) -> {ceiling, review_state}
```
The agent writes the PLAN; the engine executes TRUTH-PRESERVING code with a **verifiable trace**.

**Result on our graph:** verified trace `Quantum Mechanics -> Free Will` resolves correctly. This is
our agent-query frontier (vs 40 MCP tools).

## 4. ToG-2 (arXiv 2407.10805) — alternating graph+context retrieval

**The insight:** tightly-couple graph retrieval + context retrieval. Use the KG to link documents via
entities; use documents as entity contexts. **Alternate** between graph and context retrieval to deepen
reasoning.

**For us:** our `trace()`/`investigate()` agent op should interleave graph-walking (concepts) with
reading the grounding documents (evidence). Adopt the alternation loop into Layer 06.

## 5. SubgraphRAG (arXiv 2503.09287) — smallest useful subgraph

**The insight:** retrieve the **smallest useful graph** for the query, not large neighborhoods.
GNN-free, subgraph selection by query relevance.

**For us:** validates our "one agent question = one bounded request" doctrine. Combine with our
bounded-context experiment.

## 6. G-reasoner / GFM-RAG (arXiv 2509.24276) — graph foundation model

**The insight:** a **pretrained graph foundation model** (34M params) for RAG retrieval, bringing
external graphs into a standardized interface. `export_gfm_graph()`.

**For us:** once our graph is bigger, a learned retriever could beat PPR. For now (490 nodes) it's
overkill — but `export_gfm_graph()` is the interop path.

## 7. HyperGraphRAG (arXiv 2505.07426) — higher-order relations (Bet 1)

**The insight:** relations don't have only 2 endpoints. Represent **n-ary/hypergraph** structure.

**For us:** our Argument object (premises+conclusion+defeaters) is naturally hypergraphic. Don't
flatten it; project to property/hypergraph/xAIF/RDF as needed.

---

## What to ADOPT into our engine (with the experiment as proof)
| Algorithm | Experiment | Adopt into Layer |
|-----------|-----------|------------------|
| PathRAG flow-pruning + path prompting | `experiment-pathrag.py` | 06 Retrieval (bounded paths) |
| HippoRAG PPR (with hub-bias correction) | `experiment-hipporag.py` | 06 Retrieval (associative) |
| KG2Code executable query DSL | `experiment-kg2code.py` | 06 Retrieval + Layer 07 (MCP) |
| ToG-2 alternating graph↔context | (read) | 06 trace()/investigate() |
| HyperGraphRAG hypergraph Argument | (read) | 04 Argument Engine (don't flatten) |

## Validation
All 8 gates still pass after adding these experiments (`scripts/run-tests.py`).

Yes. Going deeper changed my view again. The interesting frontier is no longer merely “GraphRAG.” There are several **different architectures converging on something close to the generalized Pāṭala idea**:

```text
raw evidence
     ↓
compiled knowledge structure
     ↓
typed / temporal / epistemic graph
     ↓
learned or agentic graph retrieval
     ↓
bounded evidence assembly
     ↓
verifiable reasoning
     ↓
self-correction / supersession
```

Below are the repos and papers I would actually investigate. I searched through current work up to **August 2026**, including smaller implementations and research repos rather than only famous frameworks.

# 1. G-reasoner / GFM-RAG — possibly the most important new architecture

**GitHub**

[https://github.com/RManLuo/gfm-rag](https://github.com/RManLuo/gfm-rag)

**Paper**

[https://arxiv.org/abs/2509.24276](https://arxiv.org/abs/2509.24276)

This is substantially more interesting than another LLM-driven GraphRAG pipeline. The authors train an actual **graph foundation model** that can operate over heterogeneous graph structures and generalize to unseen KGs. The 2026 G-reasoner version introduces `QuadGraph`, a four-layer common representation, plus a 34M-parameter graph model. Their repository already ships pretrained GFM-RAG and G-reasoner checkpoints and allows you to bring your own graph using a simple `nodes.csv / relations.csv / edges.csv` interface. ([GitHub][1])

This means your future architecture could become:

```text
PĀṬALA canonical graph
        ↓
QuadGraph adapter
        ↓
G-reasoner
        ↓
query-conditioned graph retrieval
```

rather than hand-writing every traversal heuristic.

**What to steal**

* universal graph-index abstraction
* pretrained graph retriever
* graph → reasoning-path scoring
* cross-graph transfer
* training/evaluation infrastructure

**Action:** **clone immediately**. This should become an experimental retrieval backend for Pāṭala.

---

# 2. Reasoning on Graphs — generate graph-valid plans before answering

[https://github.com/RManLuo/reasoning-on-graphs](https://github.com/RManLuo/reasoning-on-graphs)

This earlier ICLR architecture from the same researcher is surprisingly relevant because its decomposition is better than typical GraphRAG:

```text
question
   ↓
PLAN
relation path
   ↓
RETRIEVE
actual paths satisfying plan
   ↓
REASON
```

The important idea is that the LLM doesn't free-associate its way through arbitrary context. It first generates a **graph-grounded plan**, then the graph determines whether that path actually exists. ([GitHub][2])

For Pāṭala:

```text
question:
"What does Utpaladeva's argument require?"

planner:
Claim
 → presupposes
 → Claim
 → supported_by
 → Passage

executor:
resolve actual path

LLM:
interpret returned structure
```

This is much closer to rigorous philosophical retrieval than “retrieve top 20 similar chunks.”

**Action:** clone. The plan/retrieve/reason separation is worth copying almost directly.

---

# 3. Think-on-Graph 2.0 — alternating graph and document reasoning

**GitHub**

[https://github.com/IDEA-FinAI/ToG-2](https://github.com/IDEA-FinAI/ToG-2)

**Paper**

[https://arxiv.org/abs/2407.10805](https://arxiv.org/abs/2407.10805)

ToG-2 is important because it rejects an artificial choice between:

```text
knowledge graph
OR
documents
```

Instead it alternates between them:

```text
entity
  ↓
graph relation
  ↓
new entity
  ↓
retrieve its textual evidence
  ↓
text reveals next clue
  ↓
graph exploration
  ↓
...
```

It uses bounded depth/width, relation pruning, topic pruning, clue queries and self-consistency thresholds. ([GitHub][3])

This is basically the right retrieval pattern for scholarship.

Your graph tells the agent **where to look**.

Your passage layer tells the agent **what is actually evidenced**.

**Action:** clone. Mine `search.py`, pruning and alternating traversal.

---

# 4. Original Think-on-Graph — graph exploration as an agent action

[https://github.com/IDEA-FinAI/ToG](https://github.com/IDEA-FinAI/ToG)

Paper:

[https://arxiv.org/abs/2307.07697](https://arxiv.org/abs/2307.07697)

The original ToG implements LLM-driven beam search over a KG. Rather than dumping a subgraph into context, the LLM evaluates candidate relations/entities iteratively. ([GitHub][4])

Conceptually:

```text
frontier
    ↓
score candidate relations
    ↓
expand promising branches
    ↓
stop when sufficient
```

Keep this around mainly as a **minimal reference implementation** because ToG-2 is more relevant.

---

# 5. FastToG — graph communities as search units

[https://github.com/sherlockl01/FastToG](https://github.com/sherlockl01/FastToG)

FastToG asks a good scaling question: traversing huge dense graphs node-by-node gets expensive, so why not reason **community by community**? The implementation accompanies the AAAI 2025 work and focuses on widening/deepening KG reasoning while controlling retrieval cost. ([GitHub][5])

This could become valuable once Pāṭala has:

```text
10m passages
1m claims
20m evidence links
```

You could traverse:

```text
Pratyabhijñā arguments
    ↓
recognition cluster
    ↓
memory cluster
    ↓
Buddhist objection cluster
```

before resolving individual claims.

**Action:** clone for later-scale retrieval.

---

# 6. HyperGraphRAG — relations don't necessarily have only two endpoints

[https://github.com/LHRLAB/HyperGraphRAG](https://github.com/LHRLAB/HyperGraphRAG)

HyperGraphRAG was published at NeurIPS 2025 and represents knowledge using hyperedges rather than only pairwise graph edges. ([GitHub][6])

This matters more for Pāṭala than it initially sounds.

Normal graph:

```text
Claim A ─supports→ Claim B
```

But scholarly evidence often looks like:

```text
        ┌ Evidence passage
        │
Claim A ┼ interpretive condition
        │
        ├ source edition
        │
        └ scope qualifier
```

Likewise an argument:

[
P_1, P_2, P_3 \Rightarrow C
]

is intrinsically a relation among **multiple premises and one conclusion**.

A hypergraph can encode the argument object itself:

```text
ARGUMENT H17
├── premise P1
├── premise P2
├── premise P3
├── defeater D4
└── conclusion C1
```

rather than destroying that structure into arbitrary pairwise edges.

**Action:** clone and benchmark hypergraph representation for your argument layer.

---

# 7. Hyper-RAG — hypergraphs applied to scientific evidence

[https://github.com/iMoonLab/Hyper-RAG](https://github.com/iMoonLab/Hyper-RAG)

This is particularly relevant to your scientific vertical. It uses hypergraph-driven retrieval to capture beyond-pairwise relationships and reports results in a medical/neurology setting; the associated work was published in Nature Communications in 2026. ([GitHub][7])

Don't adopt the medical architecture wholesale.

Study how they encode:

```text
multi-factor scientific relation
→ hyperedge
→ retrieval
```

because scientific evidence often cannot faithfully be represented as binary predicates.

---

# 8. PathRAG — retrieve reasoning paths, not piles of nodes

**GitHub**

[https://github.com/BUPT-GAMMA/PathRAG](https://github.com/BUPT-GAMMA/PathRAG)

**Paper**

[https://arxiv.org/abs/2502.14902](https://arxiv.org/abs/2502.14902)

PathRAG's key observation is excellent:

> Graph retrieval's problem is frequently **too much information**, not too little.

It uses flow-based pruning to identify important relational paths and then serializes those paths into prompts. ([GitHub][8])

That's extremely compatible with your proposed:

```text
?depth=
?budget=
?select=
```

API.

Instead of:

```text
retrieve 300 nodes
```

compile:

```text
Utpaladeva
 → makes_claim
 C17
 → challenged_by
 BuddhistArgument29
 → supported_by
 DharmakirtiPassage183
```

Five objects.

Possibly 300 tokens.

**Action:** clone. Very high value.

---

# 9. SubgraphRAG — retrieve the smallest useful graph

[https://github.com/Graph-COM/SubgraphRAG](https://github.com/Graph-COM/SubgraphRAG)

This ICLR 2025 implementation explicitly splits:

```text
retrieve/
reason/
```

and retrieves query-relevant subgraphs before passing information to the LLM. ([GitHub][9])

I'd use it to design a generalized operation:

```python
patala_subgraph(
    query,
    token_budget=4000,
    max_nodes=32,
    max_edges=48
)
```

That may eventually become more important than generic vector search.

---

# 10. HippoRAG 2 — associative memory rather than database lookup

[https://github.com/OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG)

HippoRAG is worth a much deeper code read than I previously implied.

It combines graph memory with Personalized PageRank and is explicitly inspired by human associative memory. HippoRAG 2 focuses on factual memory, multi-hop association and integration/sense-making of larger contexts while keeping online retrieval relatively inexpensive. ([GitHub][10])

The thing to borrow is not their entire KG.

It's:

```text
query seeds
     ↓
activation
     ↓
spreading through graph
     ↓
Personalized PageRank
     ↓
evidence ranking
```

This could become one retrieval strategy behind Pāṭala.

---

# 11. fast-graphrag — smaller, production-minded HippoRAG-like architecture

[https://github.com/circlemind-ai/fast-graphrag](https://github.com/circlemind-ai/fast-graphrag)

This is one of the personal/startup-scale projects I'd clone.

It supports incremental updates, dynamic ontology adaptation, asynchronous pipelines, and uses Personalized PageRank for graph exploration. The maintainers report much lower indexing cost than Microsoft's GraphRAG on their toy comparison. ([GitHub][11])

More importantly, it is much easier to read than Microsoft GraphRAG.

**Action:** clone before Microsoft GraphRAG if you're trying to learn implementation patterns.

---

# 12. nano-graphrag — approximately 1,100 lines of GraphRAG

[https://github.com/gusye1234/nano-graphrag](https://github.com/gusye1234/nano-graphrag)

This is precisely the sort of “smart person's stripped-down fork” you asked me to find.

The author explicitly rebuilt GraphRAG because the Microsoft implementation was difficult to hack. It keeps the essential graph/community machinery in roughly 1,100 lines excluding tests/prompts and exposes replaceable KV, vector and graph storage interfaces. It also supports content-hash-based incremental insertion. ([GitHub][12])

It became upstream inspiration for several subsequent GraphRAG implementations, including LightRAG and fast-graphrag. ([GitHub][12])

**This is a great code-reading repo.**

Do not build GraphRAG internals without first understanding this.

---

# 13. LightRAG — worth stealing its dual-level retrieval, not its worldview

[https://github.com/HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)

LightRAG has become a large project, but its core conceptual move remains useful: maintain lightweight graph indexes and use entity/relationship-level retrieval rather than Microsoft's expensive hierarchical community pipeline. The project now supports multiple chunking strategies, multimodal parsing, role-specific models, tracing/evaluation and numerous storage backends. ([GitHub][13])

The fork/history is instructive:

```text
Microsoft GraphRAG
       ↓ simplify
nano-graphrag
       ↓ rethink retrieval
LightRAG
       ↓
large ecosystem
```

I wouldn't make it your canonical graph layer.

I would compare your projection compiler's retrieval against it.

---

# 14. KAG / OpenSPG — ontology + logic + retrieval

[https://github.com/OpenSPG/KAG](https://github.com/OpenSPG/KAG)

KAG is underappreciated in Western GraphRAG discussions.

It explicitly tries to solve the noise created by generic OpenIE graph extraction through:

```text
schema / semantic knowledge
+
original text indexing
+
logical-form guided reasoning
+
knowledge alignment
```

Its architecture is divided into a KG builder and solver, with logical symbolic guidance over retrieval rather than pure embedding similarity. ([GitHub][14])

This is highly relevant because Pāṭala already has a controlled ontology.

You don't want:

```text
LLM invent relation names endlessly
```

You want:

```text
closed/controlled epistemic vocabulary
+
open evidence
```

**Action:** serious code read.

---

# 15. GFM-RAG vs KAG vs ToG is an important architectural comparison

I would actually benchmark all three:

```text
                 PĀṬALA GRAPH
                      │
       ┌──────────────┼───────────────┐
       │              │               │
       ▼              ▼               ▼
    ToG-2           KAG          G-reasoner
 agent search   symbolic search   learned GNN
       │              │               │
       └──────────────┼───────────────┘
                      ▼
                 same queries
```

They represent three distinct philosophies:

```text
ToG       LLM decides traversal
KAG       logic/schema guides traversal
GFM       graph model learns traversal
```

That is exactly the sort of thing your generalized engine should support as interchangeable retrieval policies. ([GitHub][1])

---

# 16. Graphiti — temporal truth and provenance

[https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)

Graphiti deserves a deeper look than ordinary agent-memory frameworks.

Its model explicitly separates:

```text
Entities
Facts/relationships
Episodes
Ontology
```

and relationships have temporal validity. Crucially, every derived graph fact can trace back to the episode/raw information from which it originated. It performs incremental updates rather than rebuilding the whole graph. ([GitHub][15])

For Pāṭala this maps beautifully:

```text
EPISODE
scholar review / ingestion / agent run

          ↓ derives

ASSERTION
"X supports Y"

valid_from
superseded_by
source
```

I'd borrow Graphiti's temporal model almost verbatim conceptually.

Not necessarily its Neo4j storage.

---

# 17. AriGraph — semantic memory + episodic memory + world model

**GitHub**

[https://github.com/AIRI-Institute/AriGraph](https://github.com/AIRI-Institute/AriGraph)

**Paper**

[https://arxiv.org/abs/2407.04363](https://arxiv.org/abs/2407.04363)

AriGraph is one of the more ambitious agent-memory designs.

Instead of treating the graph solely as static facts, it combines:

```text
semantic graph
+
episodic vertices/edges
```

so an agent can reason about both:

```text
what is generally true
```

and:

```text
what happened during a specific experience
```

It uses this graph as a continuously learned world model. ([GitHub][16])

For scholarly agents, that implies:

```text
SEMANTIC
Claim A opposes Claim B

EPISODIC
Agent 7 inspected manuscript M at run 193
Scholar X rejected interpretation during review R7
```

That distinction is extremely valuable.

**Action:** clone.

---

# 18. Neo4j Agent Memory — particularly useful new 2026 project

[https://github.com/neo4j-labs/agent-memory](https://github.com/neo4j-labs/agent-memory)

This is only a Labs project rather than a stable Neo4j product, which makes it more interesting to code-read.

It explicitly separates:

```text
short-term memory
long-term graph memory
reasoning memory
```

and stores reasoning traces, tool calls and causal relationships alongside extracted entities. It includes a full example built from 299 podcast episodes with specialized agent tools and graph exploration. ([GitHub][17])

The idea worth stealing:

> **reasoning traces should themselves become first-class graph objects.**

For Pāṭala:

```text
AgentRun
├─ Query
├─ RetrievalTrace
├─ EvidenceSelected
├─ ClaimGenerated
├─ Validation
└─ FinalDecision
```

This gives you a graph of **how knowledge was produced**, not only the result.

---

# 19. create-context-graph — ontology-to-full-stack generator

[https://github.com/neo4j-labs/create-context-graph](https://github.com/neo4j-labs/create-context-graph)

This is interesting mainly as a development tool.

It can generate domain-specific context-graph apps from an ontology/domain definition and includes web UI, graph memory, reasoning traces and optional MCP integration. ([GitHub][18])

I wouldn't build Pāṭala on it.

But it gives you a clever idea:

```text
ontology schema
     ↓
code generation
     ↓
API
MCP
UI
validators
```

Your own ontology/compiler could eventually generate substantial infrastructure automatically.

---

# 20. Cognee — memory control plane

[https://github.com/topoteretes/cognee](https://github.com/topoteretes/cognee)

Cognee has become much larger, but architecturally it contains valuable abstractions:

```text
remember
recall
forget
improve
```

underneath which it manages graph + vectors + relational storage, ontology grounding, temporal extraction, feedback and multiple retrieval modes. ([GitHub][19])

Its integration repo is also worth scanning:

[https://github.com/topoteretes/cognee-integrations](https://github.com/topoteretes/cognee-integrations)

because it demonstrates how one memory substrate gets exposed to many agent frameworks without coupling the underlying data model to them. ([GitHub][20])

That's exactly how you should think about:

```text
Hermes
Claude Code
OpenAI agents
MCP
web app

              ↓

same Pāṭala knowledge engine
```

---

# 21. AgenticMemory — bizarrely relevant personal Rust project

[https://github.com/agentralabs/agentic-memory](https://github.com/agentralabs/agentic-memory)

This is one of the more interesting personal/small-team finds.

It stores a cognitive graph in a portable binary file with:

```text
facts
decisions
inferences
corrections
skills
episodes
```

and explicitly supports supersession instead of mutation. It uses append-only storage with BLAKE3 integrity chains, multiple indexes—temporal, semantic, causal, entity and procedural—and an MCP server. ([GitHub][21])

Some of its marketing claims should obviously be treated skeptically until benchmarked, but the architecture is very relevant.

Especially:

```text
Correction
    ↓
SUPERSEDES
    ↓
Fact
```

and:

```text
Decision
← caused_by ← Fact
← inferred_from ← Observation
```

That's basically provenance-aware epistemic memory.

**Action:** definitely clone and code-read the Rust storage layer.

---

# 22. OriginTrail DKG V10 — shared multi-agent knowledge with promotion levels

[https://github.com/OriginTrail/dkg](https://github.com/OriginTrail/dkg)

I previously dismissed the blockchain aspect as unnecessary, and I still would not adopt the chain infrastructure.

But the latest architecture contains a very interesting **multi-level memory promotion model**. Knowledge starts in cheaper/private layers and can be promoted as it becomes more trusted or collaboratively verified. Context graphs have scoped governance and verifiable provenance. ([GitHub][22])

That's highly analogous to what Pāṭala wants:

```text
candidate
 ↓
agent validated
 ↓
peer reviewed
 ↓
scholar adjudicated
 ↓
canonical
```

Mine the **promotion semantics**, ignore the blockchain dependency.

---

# 23. LLM-Wiki — this may be closer to your optimized architecture than GraphRAG

**Paper**

[https://arxiv.org/abs/2605.25480](https://arxiv.org/abs/2605.25480)

This is one of the biggest findings.

Rather than building another vector index or static KG, LLM-Wiki treats external knowledge as a **compiled, composable and self-evolving structure**.

Documents become interlinked Wiki pages. Agents receive primitive operations like:

```text
search
read
follow-link
```

and navigate iteratively until evidence is sufficient.

Even more interesting: it maintains an **Error Book** so the compiled knowledge representation can correct structural or semantic problems over time. It reported gains over HippoRAG 2, LightRAG and GraphRAG on multi-hop benchmarks. ([arXiv][23])

That's astonishingly close to what we independently converged on:

```text
RAW SOURCE
     ↓
COMPILE ON WRITE
     ↓
INTERLINKED KNOWLEDGE ARTIFACTS
     ↓
AGENT NAVIGATION
```

### Important caveat

I could verify the paper, but I **could not verify an official authors' implementation repository** from my searches. I would not pretend one exists.

However, there is already an ecosystem forming around the idea:

[https://github.com/gavischneider/awesome-llm-wiki](https://github.com/gavischneider/awesome-llm-wiki)

([GitHub][24])

and an AWS sample implementation:

[https://github.com/aws-samples/sample-kiro-llm-wiki](https://github.com/aws-samples/sample-kiro-llm-wiki)

which explicitly implements the “incremental compilation, not RAG” pattern. ([GitHub][25])

---

# 24. Oshayr/LLM-Wiki — personal implementation

[https://github.com/Oshayr/LLM-Wiki](https://github.com/Oshayr/LLM-Wiki)

This is exactly the sort of personal project worth mining.

It implements an autonomous knowledge base that captures research and decisions, creates interlinked pages, uses semantic + text search, backlinks, transclusion and research-on-miss. ([GitHub][26])

Don't confuse it with the research paper's official implementation.

But study:

```text
automatic capture
backlinks
research-on-miss
transclusion
structured frontmatter queries
```

Those are excellent human+agent knowledge-interface ideas.

---

# 25. The LLM-Wiki research ecosystem itself

[https://github.com/gavischneider/awesome-llm-wiki](https://github.com/gavischneider/awesome-llm-wiki)

This surfaced additional work around:

```text
compiled knowledge
structural repair
self-evolving knowledge
cross-source comparison
```

including work on agent-compiled knowledge refinement and persistent structural decay. ([GitHub][24])

I'd clone this repository not for code but as a **research feed**.

---

# 26. KG2Code — possibly a profound idea for Pāṭala agents

**Paper**

[https://arxiv.org/abs/2607.22652](https://arxiv.org/abs/2607.22652)

This is extremely recent—July 2026.

Instead of turning a graph into natural-language descriptions, KG2Code transforms KG structure into **executable code representations** and asks an LLM to generate executable programs that query/reason over the graph. This preserves structural semantics and produces verifiable execution traces. ([arXiv][27])

Conceptually:

```text
QUESTION
"What evidence defeats claim C?"

        ↓ LLM

result = graph.claim("C") \
              .incoming("defeats") \
              .where(confidence > .8) \
              .evidence()

        ↓ execute

deterministic result
```

I think this could be huge for Pāṭala.

Instead of an agent trying to reason over serialized JSON:

```text
LLM writes a constrained query/program
              ↓
Pāṭala executes it
              ↓
results are deterministic
```

That aligns with what we want for MCP too.

**Caveat:** the paper says code/data are on GitHub, but I couldn't confidently identify the official repository in the search results, so I'm not going to invent a URL. ([arXiv][27])

Keep this one on a watch list.

---

# 27. This 2026 finding strongly supports deterministic graph execution

A recent industrial study reaches a result that matters strategically:

[https://arxiv.org/abs/2605.26874](https://arxiv.org/abs/2605.26874)

In its operational benchmark, deterministic handlers over a typed KG substantially outperformed giving the same information to an LLM-oriented data layer; the authors' central thesis is essentially that **the data representation can be more important than the orchestration layer**. ([arXiv][28])

This reinforces your design:

```text
DON'T:

raw information
→ LLM figures everything out

DO:

raw information
→ typed structure
→ deterministic graph operations
→ LLM interprets results
```

---

# 28. KORAL — two graphs: reality and literature

Paper:

[https://arxiv.org/abs/2602.10246](https://arxiv.org/abs/2602.10246)

GitHub:

[https://github.com/Damrl-lab/KORAL](https://github.com/Damrl-lab/KORAL)

This is a genuinely interesting scientific architecture.

KORAL keeps:

```text
DATA KG
observed telemetry

        +

LITERATURE KG
scientific/expert knowledge
```

and reasons across both to produce explanations and recommendations. ([arXiv][29])

For a scientific Pāṭala:

```text
EMPIRICAL GRAPH
experiments
measurements
datasets
results

        +

LITERATURE GRAPH
claims
papers
theories
arguments
reviews
```

That separation is excellent.

**Action:** clone.

---

# 29. CodeScientist — KG-based agents actually doing scientific investigation

[https://github.com/allenai/codescientist](https://github.com/allenai/codescientist)

This AllenAI project is experimenting with automated scientific discovery through executable experiments. One of its experiments explicitly compares a knowledge-graph-based scientific agent with a ReAct baseline in DiscoveryWorld. ([GitHub][30])

It isn't a general-purpose epistemic engine.

But it matters because it lets you see what happens when:

```text
graph knowledge
+
hypothesis
+
experiment
+
observation
```

actually enters an agent loop.

Useful future benchmark for your scientific layer.

---

# 30. ScienceAgentBench — don't invent scientific-agent evaluation

[https://github.com/OSU-NLP-Group/ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench)

This benchmark provides 102 validated scientific tasks derived from 44 peer-reviewed papers across several disciplines, with executable program outputs and expert validation. ([GitHub][31])

Eventually compare:

```text
normal science agent

vs

science agent + Pāṭala epistemic graph
```

If Pāṭala doesn't improve real scientific tasks, rethink assumptions.

---

# 31. TechGraphRAG — evidence sufficiency as a first-class gate

Paper:

[https://arxiv.org/abs/2606.01613](https://arxiv.org/abs/2606.01613)

This June 2026 system is particularly relevant to your **review/gate** ideas.

It uses a 13-step pipeline including:

```text
intent classification
↓
retrieval
↓
evidence sufficiency scoring
↓
external academic search
↓
search → vet loops
↓
KG traversal
↓
citation verification
↓
quality check
↓
regenerate if needed
```

and includes a 100-point multidimensional evidence-sufficiency rubric. ([arXiv][32])

This is exactly the direction your scholar agents should evolve:

```text
agent cannot simply say "done"

EvidenceGate.evaluate(result)
       ↓
insufficient
       ↓
research again
```

I could verify the paper, but not a canonical GitHub repository from the searches I ran, so treat this as **architecture research rather than code to clone**.

---

# 32. TrustGraph — deterministic “context engineering”

[https://github.com/trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)

The interesting part is not the platform. It's their explicit stance that context should be a traceable graph artifact rather than mysterious vector-search output.

They maintain provenance at the node/edge level and expose the exact paths selected for generation. ([GitHub][33])

Your corresponding object should probably be:

```json
{
  "context_id": "...",
  "query": "...",
  "selected_claims": [...],
  "selected_edges": [...],
  "selected_evidence": [...],
  "retrieval_method": "...",
  "reasoning_paths": [...]
}
```

Meaning **context itself becomes citable/auditable**.

I really like that.

---

# 33. Microsoft GraphRAG — useful as reference, not foundation

[https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag)

Microsoft GraphRAG still matters because it popularized:

```text
TextUnits
→ entity/relationship extraction
→ Leiden communities
→ hierarchical community summaries
→ local/global retrieval
```

and its current architecture explicitly abstracts the knowledge model from storage. ([GitHub][34])

But the project itself warns that indexing can consume substantial LLM resources. ([GitHub][35])

For your use case:

**read it. Benchmark against it. Don't architect around it.**

---

# 34. GraphRAG meta-implementation — extremely useful for benchmarking algorithms

[https://github.com/JayLZhou/GraphRAG](https://github.com/JayLZhou/GraphRAG)

This repo is underappreciated.

It implements many competing RAG approaches under one experimental framework, including methods such as:

```text
DALK
GraphRAG Local
GraphRAG Global
HippoRAG
KGP
LightRAG
RAPTOR
...
```

([GitHub][36])

That's perfect for you.

Rather than wiring ten repositories independently:

```text
Pāṭala corpus
    ↓
same benchmark
    ↓
multiple retrieval methods
```

Use this project as the experimental harness.

**Action: clone immediately.**

---

# 35. GraphRAG MCP research server — somebody already compiled much of this research

[https://github.com/lyndonkl/graphragmcp](https://github.com/lyndonkl/graphragmcp)

This is a niche personal project explicitly containing a structured research base about graph construction, embedding fusion, retrieval methods, architecture choices, RDF/property graphs/hypergraphs and GraphRAG patterns, exposed via MCP. ([GitHub][37])

This may be worth **feeding directly to your coding/research agents**.

Rather than every agent rediscovering GraphRAG architecture:

```text
Hermes
  ↓
GraphRAG research MCP
```

Could save time.

---

# 36. There is a huge graph-reasoning bibliography already curated

[https://github.com/ngl567/KGR-Survey](https://github.com/ngl567/KGR-Survey)

It catalogs task-oriented KG reasoning systems including ToG, KG-Agent, KnowledgeNavigator and many others. ([GitHub][38])

Clone it primarily to use as a **paper-discovery index**.

---

# 37. And the agent-memory literature has its own good tracker

[https://github.com/Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)

This includes graph memory, episodic memory, temporal memory and personalized-agent memory systems such as AriGraph and many less famous approaches. ([GitHub][39])

Again: research feed, not implementation.

---

# SPEC-08 — GRAPH REASONING SURVEY (arXiv architectures for graph retrieval)

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/arxivgraph`
**Scope:** 37 graph-reasoning/GraphRAG architectures (G-reasoner, ToG-2, PathRAG, SubgraphRAG,
HyperGraphRAG, HippoRAG, Graphiti, AriGraph, KAG, KG2Code, LLM-Wiki, KORAL, ...). Key conclusions:
(1) do NOT choose one GraphRAG algorithm — build a stable epistemic graph with **pluggable retrieval**;
(2) the 4 things to pinch: GFM-RAG graph abstraction, ToG-2 alternating text↔graph search, PathRAG/
SubgraphRAG bounded context, Graphiti/AriGraph epistemic-vs-event separation; (3) two bets: support
hypergraphs internally, and let agents write executable graph queries (KG2Code) not 40 MCP tools.

---



I think there are now **eight technologies worth explicitly supporting as interchangeable layers**.

```text
                         PĀṬALA
                            │
                    CANONICAL OBJECTS
                            │
     ┌──────────────────────┼───────────────────────┐
     │                      │                       │
 PASSAGES                CLAIM GRAPH             EPISODES
     │                      │                       │
 provenance             arguments               agent runs
 evidence               relations               reviews
     │                      │                       │
     └──────────────────────┼───────────────────────┘
                            │
                     GRAPH COMPILER
                            │
         ┌──────────────────┼───────────────────┐
         │                  │                   │
      property           hypergraph          QuadGraph
       graph
         │                  │                   │
         ▼                  ▼                   ▼
      ToG-2            HyperGraphRAG        G-reasoner
         │
         ├──── PathRAG
         ├──── SubgraphRAG
         ├──── HippoRAG
         └──── deterministic query/code
                            │
                            ▼
                    CONTEXT ARTIFACT
                            │
                    evidence + paths
                            │
                            ▼
                           LLM
```

The key point:

> **Do not choose one GraphRAG algorithm.**

Build a stable canonical epistemic graph and make retrieval strategies pluggable.

---

# The four things I would actually pinch now

### **A. GFM-RAG's graph abstraction**

[https://github.com/RManLuo/gfm-rag](https://github.com/RManLuo/gfm-rag)

Build:

```text
export_gfm_graph()
```

and benchmark the pretrained 34M G-reasoner on Pāṭala retrieval. It supports bringing external graph representations into its standardized interface. ([GitHub][1])

### **B. ToG-2's text↔graph alternating search**

[https://github.com/IDEA-FinAI/ToG-2](https://github.com/IDEA-FinAI/ToG-2)

Build this into your agent `trace()` / `investigate()` operation. ([GitHub][3])

### **C. PathRAG/SubgraphRAG's bounded context construction**

[https://github.com/BUPT-GAMMA/PathRAG](https://github.com/BUPT-GAMMA/PathRAG)

[https://github.com/Graph-COM/SubgraphRAG](https://github.com/Graph-COM/SubgraphRAG)

These directly inform `patala_context(... token_budget=N)`. ([arXiv][40])

### **D. Graphiti/AriGraph's distinction between epistemic graph and event history**

[https://github.com/getzep/graphiti](https://github.com/getzep/graphiti)

[https://github.com/AIRI-Institute/AriGraph](https://github.com/AIRI-Institute/AriGraph)

Your append-only review and agent-run system should not be jammed into the same semantic objects as claims. ([GitHub][15])

---

# And two slightly radical bets

## Bet 1 — Pāṭala should support hypergraphs internally

Not necessarily as canonical storage.

But your **Argument** object should not be flattened prematurely.

```text
Argument
{
   premises: [P1,P2,P3],
   conclusion: C,
   assumptions: [A1],
   defeaters: [D1]
}
```

can project into:

```text
property graph
hypergraph
xAIF
RDF
```

HyperGraphRAG is strong evidence that higher-order relational representations are becoming technically useful rather than merely mathematically elegant. ([GitHub][6])

---

## Bet 2 — eventually agents should write executable graph queries, not reason over JSON

KG2Code points toward something I think is extremely important. ([arXiv][27])

Instead of MCP giving an agent:

```text
40 specialist tools
```

give it a tiny graph language:

```text
resolve(...)
search(...)
neighbors(...)
path(...)
filter(...)
evidence(...)
```

Then let the model compose:

```text
path(
  from=claim("IPK-1.5.11"),
  via=["opposed_by", "supported_by"],
  to=passage("*")
)
.filter(review_status="accepted")
.limit(12)
```

The program executes deterministically.

The agent is responsible for **planning**.

Pāṭala is responsible for **truth-preserving execution**.

That separation looks increasingly like the frontier.

---

# My revised clone list

If you want maximum information gain and minimal duplicated work, I would now clone in this order:

```text
01  https://github.com/RManLuo/gfm-rag
02  https://github.com/RManLuo/reasoning-on-graphs
03  https://github.com/IDEA-FinAI/ToG-2
04  https://github.com/BUPT-GAMMA/PathRAG
05  https://github.com/Graph-COM/SubgraphRAG
06  https://github.com/OSU-NLP-Group/HippoRAG
07  https://github.com/LHRLAB/HyperGraphRAG
08  https://github.com/getzep/graphiti
09  https://github.com/AIRI-Institute/AriGraph
10  https://github.com/agentralabs/agentic-memory
11  https://github.com/neo4j-labs/agent-memory
12  https://github.com/OpenSPG/KAG
13  https://github.com/gusye1234/nano-graphrag
14  https://github.com/circlemind-ai/fast-graphrag
15  https://github.com/JayLZhou/GraphRAG
16  https://github.com/trustgraph-ai/trustgraph
17  https://github.com/lyndonkl/graphragmcp
18  https://github.com/Oshayr/LLM-Wiki
19  https://github.com/aws-samples/sample-kiro-llm-wiki
20  https://github.com/Damrl-lab/KORAL
```

And keep these papers beside them:

```text
https://arxiv.org/abs/2509.24276  G-reasoner
https://arxiv.org/abs/2407.10805  ToG-2
https://arxiv.org/abs/2502.14902  PathRAG
https://arxiv.org/abs/2407.04363  AriGraph
https://arxiv.org/abs/2605.25480  LLM-Wiki
https://arxiv.org/abs/2607.22652  KG2Code
https://arxiv.org/abs/2602.10246  KORAL
https://arxiv.org/abs/2606.01613  TechGraphRAG
```

The three I think we **underestimated before** are **G-reasoner**, **LLM-Wiki**, and **KG2Code**. Taken together they point toward a stronger architecture than conventional GraphRAG:

> **compile knowledge once → represent it structurally → learn/search the graph efficiently → let agents navigate via small deterministic operations → retain provenance and self-correction as first-class state.**

That is remarkably close to the optimized generalized Pāṭala architecture you're converging on.

[1]: https://github.com/RManLuo/gfm-rag?utm_source=chatgpt.com "GitHub - RManLuo/gfm-rag: [NeurIPS'25, ICLR'26] Graph Foundation Model for Retrieval Augmented Generation · GitHub"
[2]: https://github.com/RManLuo/reasoning-on-graphs?utm_source=chatgpt.com "GitHub - RManLuo/reasoning-on-graphs: Official Implementation of ICLR 2024 paper: \"Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning\" · GitHub"
[3]: https://github.com/IDEA-FinAI/ToG-2?utm_source=chatgpt.com "GitHub - DataArcTech/ToG-2 · GitHub"
[4]: https://github.com/IDEA-FinAI/ToG?utm_source=chatgpt.com "GitHub - DataArcTech/ToG: This is the official github repo of Think-on-Graph (ICLR 2024). If you are interested in our work or willing to join our research team in Shenzhen, please feel free to contact us by email (xuchengjin@idea.edu.cn) · GitHub"
[5]: https://github.com/sherlockl01/FastToG?utm_source=chatgpt.com "GitHub - sherlockl01/FastToG: Code implement for FastToG · GitHub"
[6]: https://github.com/LHRLAB/HyperGraphRAG?utm_source=chatgpt.com "GitHub - LHRLAB/HyperGraphRAG: [NeurIPS 2025] Official resources of \"HyperGraphRAG: Retrieval-Augmented Generation via Hypergraph-Structured Knowledge Representation\". · GitHub"
[7]: https://github.com/iMoonLab/Hyper-RAG?utm_source=chatgpt.com "GitHub - iMoonLab/Hyper-RAG: \"Hyper-RAG: Combating LLM Hallucinations using Hypergraph-Driven Retrieval-Augmented Generation\" by Yifan Feng, Hao Hu, Shihui Ying, Xingliang Hou, Shiquan Liu, Mingyuan Yang, Junchang Li, Shaoyi Du, Nanning Zheng, Han Hu, and Yue Gao. · GitHub"
[8]: https://github.com/bupt-gamma/pathrag?utm_source=chatgpt.com "GitHub - BUPT-GAMMA/PathRAG · GitHub"
[9]: https://github.com/Graph-COM/SubgraphRAG?utm_source=chatgpt.com "GitHub - Graph-COM/SubgraphRAG: [ICLR 2025] Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation · GitHub"
[10]: https://github.com/osu-nlp-group/hipporag?utm_source=chatgpt.com "GitHub - OSU-NLP-Group/HippoRAG: [NeurIPS'24] HippoRAG is a novel RAG framework inspired by human long-term memory that enables LLMs to continuously integrate knowledge across external documents. RAG + Knowledge Graphs + Personalized PageRank. · GitHub"
[11]: https://github.com/circlemind-ai/fast-graphrag?utm_source=chatgpt.com "GitHub - circlemind-ai/fast-graphrag: RAG that intelligently adapts to your use case, data, and queries · GitHub"
[12]: https://github.com/gusye1234/nano-graphrag?utm_source=chatgpt.com "GitHub - gusye1234/nano-graphrag: A simple, easy-to-hack GraphRAG implementation · GitHub"
[13]: https://github.com/hkuds/lightrag?utm_source=chatgpt.com "GitHub - HKUDS/LightRAG: [EMNLP2025] \"LightRAG: Simple and Fast Retrieval-Augmented Generation\" · GitHub"
[14]: https://github.com/openspg/kag?utm_source=chatgpt.com "GitHub - OpenSPG/KAG: KAG is a logical form-guided reasoning and retrieval framework based on OpenSPG engine and LLMs. It is used to build logical reasoning and factual Q&A solutions for professional domain knowledge bases. It can effectively overcome the shortcomings of the traditional RAG vector similarity calculation model. · GitHub"
[15]: https://github.com/getzep/graphiti?utm_source=chatgpt.com "GitHub - getzep/graphiti: Build Real-Time Knowledge Graphs for AI Agents · GitHub"
[16]: https://github.com/airi-institute/arigraph?utm_source=chatgpt.com "GitHub - AIRI-Institute/AriGraph · GitHub"
[17]: https://github.com/neo4j-labs/agent-memory?utm_source=chatgpt.com "GitHub - neo4j-labs/agent-memory: A graph-native memory system for AI agents and context graphs. Store conversations, build knowledge graphs, and let your agents learn from their own reasoning — all backed by Neo4j. · GitHub"
[18]: https://github.com/neo4j-labs/create-context-graph?utm_source=chatgpt.com "GitHub - neo4j-labs/create-context-graph: AI agents with graph based reasoning memory, scaffolded in seconds · GitHub"
[19]: https://github.com/topoteretes/cognee?utm_source=chatgpt.com "GitHub - topoteretes/cognee: Memory control plane for AI Agents in 6 lines of code · GitHub"
[20]: https://github.com/topoteretes/cognee-integrations?utm_source=chatgpt.com "GitHub - topoteretes/cognee-integrations · GitHub"
[21]: https://github.com/agentralabs/agentic-memory?utm_source=chatgpt.com "GitHub - agentralabs/agentic-memory: Persistent cognitive graph memory for AI agents — facts, decisions, reasoning chains, corrections. 16 query types, sub-millisecond. Rust core + Python SDK + MCP server. · GitHub"
[22]: https://github.com/OriginTrail/dkg?utm_source=chatgpt.com "GitHub - OriginTrail/dkg: OriginTrail Decentralized Knowledge Graph (DKG) is a decentralized knowledge infrastructure for multi-agent AI memory — enabling agents to publish, verify, and query shared knowledge as cryptographically verifiable graph assets across a peer-to-peer network. · GitHub"
[23]: https://arxiv.org/abs/2605.25480?utm_source=chatgpt.com "Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki"
[24]: https://github.com/gavischneider/awesome-llm-wiki?utm_source=chatgpt.com "GitHub - gavischneider/awesome-llm-wiki: A curated list of foundational blueprints, functional frameworks, and technical guides for building compounding, AI-compiled knowledge bases. · GitHub"
[25]: https://github.com/aws-samples/sample-kiro-llm-wiki?utm_source=chatgpt.com "GitHub - aws-samples/sample-kiro-llm-wiki · GitHub"
[26]: https://github.com/Oshayr/LLM-Wiki?utm_source=chatgpt.com "GitHub - Oshayr/LLM-Wiki: Autonomous knowledge base plugin for Claude Code - captures reserch, ideas, and decisions into an interlinked wiki with reserch-on-miss, semantic search, and a Wikipedia-style web UI. Knowledge compounds as you work. · GitHub"
[27]: https://arxiv.org/abs/2607.22652?utm_source=chatgpt.com "KG2Code: Bridging Knowledge Graphs and Large Language Models via Executable Code for Question Answering"
[28]: https://arxiv.org/abs/2605.26874?utm_source=chatgpt.com "Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations"
[29]: https://arxiv.org/abs/2602.10246?utm_source=chatgpt.com "KORAL: Knowledge Graph Guided LLM Reasoning for SSD Operational Analysis"
[30]: https://github.com/allenai/codescientist?utm_source=chatgpt.com "GitHub - allenai/codescientist: CodeScientist: An automated scientific discovery system for code-based experiments · GitHub"
[31]: https://github.com/OSU-NLP-Group/ScienceAgentBench?utm_source=chatgpt.com "GitHub - OSU-NLP-Group/ScienceAgentBench: [ICLR'25] ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery · GitHub"
[32]: https://arxiv.org/abs/2606.01613?utm_source=chatgpt.com "TechGraphRAG: An Agentic Graph-Augmented RAG Framework for Technical Literature Reasoning"
[33]: https://github.com/trustgraph-ai/trustgraph?utm_source=chatgpt.com "GitHub - trustgraph-ai/trustgraph: The deterministic context engineering platform for open source AI. Connect open models and ontologies with context graph harnesses to build explainable, reliable agents. · GitHub"
[34]: https://github.com/microsoft/graphrag/blob/main/docs/index.md?utm_source=chatgpt.com "graphrag/docs/index.md at main · microsoft/graphrag · GitHub"
[35]: https://github.com/microsoft/graphrag/blob/main/docs/get_started.md?utm_source=chatgpt.com "graphrag/docs/get_started.md at main · microsoft/graphrag · GitHub"
[36]: https://github.com/jaylzhou/graphrag?utm_source=chatgpt.com "GitHub - JayLZhou/GraphRAG: In-depth study of the graphrag · GitHub"
[37]: https://github.com/lyndonkl/graphragmcp?utm_source=chatgpt.com "GitHub - lyndonkl/graphragmcp: A comprehensive Model Context Protocol (MCP) server providing structured access to knowledge about **Knowledge Graph Construction & Retrieval Strategies for LLM Reasoning**. This server enables AI agents to access detailed research findings, implementation patterns, and best practices for building graph-enhanced RAG systems. · GitHub"
[38]: https://github.com/ngl567/KGR-Survey?utm_source=chatgpt.com "GitHub - ngl567/KGR-Survey: A Survey of Task-Oriented Knowledge Graph Reasoning: Status, Applications, and Prospects · GitHub"
[39]: https://github.com/Shichun-Liu/Agent-Memory-Paper-List?utm_source=chatgpt.com "GitHub - Shichun-Liu/Agent-Memory-Paper-List: The paper list of \"Memory in the Age of AI Agents: A Survey\" · GitHub"
[40]: https://arxiv.org/abs/2502.14902?utm_source=chatgpt.com "PathRAG: Pruning Graph-based Retrieval Augmented Generation with Relational Paths"

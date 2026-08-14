# ECOSYSTEM — the reference index (repos · datasets · arxiv · agent infra)

*2026-08-14. The consolidated, agent-navigable index of everything in the open ecosystem we should
steal, ingest, or benchmark. Each entry: what it is (1 line) + why it matters to us. Full detail in the
linked SPEC. Organized by the three survey docs. For future agents: read this to know WHAT exists and
WHY before cloning/building.*

---

## How this is organized

| Source | Spec | Focus |
|--------|------|-------|
| Ecosystem survey | `SPEC-07` | repos/datasets/benchmarks (R2 `gitclone`) |
| Graph-reasoning survey | `SPEC-08` | arXiv GraphRAG architectures (R2 `arxivgraph`) |
| Agent-orchestration survey | `SPEC-09` | runtimes/protocols/universal schema (R2 `agenticref`) |
| Frontier-agent survey | `SPEC-10` | people/labs to track (R2 `frontieragent`) |
| Agent-memory survey | `SPEC-11` | self-evolving systems (R2 `githubagent`) |

**Recommended clone order** and **recommended ingest order** are in each spec's final section.

---

## 1. TIER-0 CLONES — steal architecture/code first (SPEC-07)

| Repo | What it is | Why it matters | Priority |
|------|-----------|----------------|----------|
| **RKA** | research-workflow-as-state (literature→claims→evidence→RQ); supersession/staleness propagation | closest to our architecture; "claim changed → derived knowledge stale → review queue" | CLONE+READ |
| **Kappa Graph** | epistemic weighting: supporting vs contradicting evidence, disagreement retained, grounding+diversity | matches our epistemic-envelope idea; mine its accumulation logic | CLONE |
| **Vouch** | git-native review gate: agents propose, humans approve, claims cite sources, append-only audit | don't rebuild the write/review gate | CLONE |
| **Eigenius** | typed knowledge classes (Declared/Observed/Derived/Verified) | extends our epistemic ladder (how something is KNOWN) | CLONE |
| **sage-wiki** | graph as compile output, not a second DB to sync | confirms our SPEC-00 compiler model | CLONE (pattern) |
| **graphify** | extract→canonicalize→reconcile→typed graph | entity-reconciliation tests to compare | CLONE |
| **obra/knowledge-graph** | query an Obsidian vault as a KG | agent interface design | CLONE |
| **DocGraph** | SQLite KG + drift audits (stale/superseded docs) | governance layer (drift = staleness) | CLONE |

## 2. STRUCTURED DATA TO INGEST (SPEC-07)

| Dataset | What it is | Why |
|---------|-----------|-----|
| **SciFact** | scientific claim↔evidence gold | test claim/evidence machinery |
| **ARG Tech xAIF** | argument graphs (QT30 ~20k utterances) | the single most important argument dataset |
| **EleutherIA** | free-will philosophy KG (~19k nodes/69k passages) | domain generalization test |
| **FactKG** | 108k claims with reasoning structures | claim graph benchmark |
| **ExplaGraphs** | argument→explanation graph | explanation decomposition |
| **MSVEC** | multi-domain scientific claims | cross-domain generalization |
| **FACTors** | 118k fact-check claims | real-world claims |
| **OpenAlex / S2ORC / peS2o** | bibliography/corpus infrastructure | don't build this yourself |

## 3. arXiv GRAPH-REASONING ARCHITECTURES (SPEC-08)

| Arch | What it is | Our status | Pinch |
|------|-----------|-----------|-------|
| **G-reasoner/GFM-RAG** | graph foundation model for RAG | GAP | `export_gfm_graph()` + benchmark |
| **Reasoning-on-Graphs** | graph-valid plan before answering | GAP | argument-engine planning |
| **ToG-2** | alternating text↔graph search | GAP | `trace()`/`investigate()` |
| **FastToG** | graph communities as search units | GAP | bound retrieval |
| **HyperGraphRAG** | higher-order relations (hypergraph) | **BET** | keep Argument non-flat |
| **PathRAG** | retrieve reasoning paths, bounded token | GAP | `context(token_budget=N)` |
| **SubgraphRAG** | retrieve smallest useful graph | **VALIDATES** | our bounded-request doctrine |
| **HippoRAG** | PPR over KG for associative memory | GAP | retrieval |
| **LightRAG** | dual-level retrieval | **VALIDATES** | compile once |
| **KAG/OpenSPG** | ontology+logic+retrieval | GAP | DAG as logical form |
| **Graphiti** | epistemic graph vs temporal events | GAP | separate review from claims |
| **AriGraph** | semantic+episodic memory | GAP | claims vs agent-runs |
| **KG2Code** | agents write executable graph queries | **BET** | `path(from,via,to).filter()` |
| **LLM-Wiki** | graph-as-compiled-wiki | **VALIDATES** | compiler model |
| **KORAL** | two graphs: reality vs literature | GAP | evidence vs interpretation |
| **TechGraphRAG** | evidence sufficiency gate | GAP | ceilings gate retrieval |

## 4. AGENT ORCHESTRATION (SPEC-09)

### Runtimes (pick when single-host boundary hurts)
| Runtime | What it is | Ranking (for us) |
|---------|-----------|------------------|
| **Restate** | distributed stateful actors + durable calls | 1 (best fit) |
| **DBOS** | durable execution on Postgres | 2 (we use Postgres) |
| **Temporal** | mature durable execution | 3 (more infra) |
| **Hatchet** | queue/scheduling ergonomics | 4 |

### Today (keep cheap, no new infra)
`Hermes Kanban` + `SQLite (Task/Run/Event)` + `MCP capabilities` + `git worktrees` = the local
control plane. Only add a distributed runtime when the single-host boundary hurts.

### Protocols
| Protocol | What it is | Why |
|----------|-----------|-----|
| **MCP** | agent ↔ capability | the capability interface |
| **A2A** | agent ↔ agent/service | cross-agent |
| **MCP Gateway** | tool explosion control plane | tool orchestration |
| **GitSkills** | enormous dataset of skills | ingest candidate |

### The universal schema (the big idea)
```
PROJECT → KNOWLEDGE(Source/Passage/Entity/Claim/Argument/Evidence/Review)
        → WORK(Task/Run/Step/Event)
        → EXECUTORS(Agent/Skill/Tool/Runtime)
        → OUTPUT(Artifact/Proposal/Validation/Decision)
```
Full end-to-end provenance: `Task → Run → Agent → Artifact → Proposal → Review → Decision →
(Supersede)`. **This matches our epistemic envelope** (Review/Decision/Supersede = our review chain).

---

## 5. What to build next (the adapters — SPEC-07 §biggest opportunity)

```text
import_openalex()  import_s2orc()  import_scifact()  import_xaif()  import_eleutheria()
  → ExternalRecord → CanonicalCandidate → Validation → Proposal → AcceptedObject
```
This is the **generalization test**: if Doyle + EleutherIA + SciFact + xAIF all enter the same engine,
the abstraction is real.

---

## 6. PEOPLE/LABS TO TRACK (SPEC-10 — the frontier-agent watchlist)

The strategic implication: **persistent verified state (truth/evidence/execution-history/skills/
review) becomes the durable intelligence — models are disposable compute.** We are building that
substrate. See `specs/SPEC-10-FRONTIER-AGENT-SURVEY.md` for full detail.

| Watch | Why |
|-------|-----|
| Jeff Clune / Sakana AI | open-ended/self-improving systems |
| Jenny Zhang | DGM → Hyperagents |
| Jiayi Pan | learned parallelism + coding-agent training |
| Shunyu Yao / Princeton | agent reasoning + real-world eval |
| Graham Neubig / OpenHands | production-grade agents |
| Charles Packer / Letta | agent memory as OS |
| Muhan Zhang | graph learning → agent memory |
| Omar Khattab / DSPy | optimizable LM programs |
| METR | agent evaluation lab |
| Prime Intellect | RL-train agents in real environments |

**Labs:** Sakana, Prime Intellect, OpenHands, Berkeley systems, Princeton, METR, Letta, Stanford NLP,
graph-foundation-model groups, Nous Research. Allocation: 40% open-endedness, 25% agent-RL, 20%
graph-memory, 15% practical implementation.

### The convergence (why our work matters)
```
2024: LLM + prompt + vectordb + tools = agent
NOW:   foundation model → learned computation policy → spawn agents/tools/graph-memory
        → trajectory → deterministic environment → verifier → experience archive
        → skills/memory/architecture → SELF-IMPROVEMENT
```
We are building the **persistent verified state** those systems need.

---

## 7. AGENT-MEMORY / SELF-EVOLVING SYSTEMS (SPEC-11)

These cover much of the agent plumbing we'd want. **What remains distinctly ours: the epistemic kernel
+ rigorous promotion path (agent output → evidence → review → canonical knowledge).**

| Repo | Why |
|------|-----|
| EvoScientist | self-evolving AI scientists — study deepest |
| Neo.mjs (neomjs/neo) | agent OS / software organism |
| neo4j-labs/meta-knowledge-graph | self-improving memory, lifecycle hooks |
| MemOS / MemRL | self-evolving memory OS + runtime RL |
| Memento-Skills / CoEvoSkills / MemSkill / SkillRL | skill self-evolution |
| A-MEM / MemoryGraph / agent-memory-mcp | graph-memory MCP servers |

Full list + tier tagging: `docs/GITHUB-INDEX.md` (`agent-memory` category) + `data/references/github.json`.

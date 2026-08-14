# SPEC-11 — AGENT MEMORY / SELF-EVOLVING SYSTEMS SURVEY

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/githubagent`
**Scope:** agent-memory + self-evolving systems (EvoScientist, Neo.mjs, MemOS, MemRL, MemSkill,
SkillRL, Neo4j meta-knowledge-graph, A-MEM, MemoryGraph, agent-memory-mcp, ...). Key insight: these
already cover much of the agent plumbing we'd want — **what remains distinctly ours is the epistemic
kernel + rigorous promotion path (agent output → evidence → review → canonical knowledge)**.

---

Yes. I went hunting for projects that are **actually fusing several frontier ideas at once**—persistent graphs, self-evolving skills, executable agents, memory, verification, MCP, scheduling, multi-agent execution—not just papers with a toy script.

A few are much more ambitious than I expected.

## 1. EvoScientist — closest existing thing to the integrated research organism

[https://github.com/EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist)

This is probably the **most directly relevant repo I found for your current direction**.

It is not merely an “AI scientist” demo. The current implementation has six specialized subagents, persistent self-evolving memory that links observations into a knowledge graph, automatically proposed reusable skills, scheduled unattended work, adaptive tool selection, MCP integration, multiple model providers, human approval gates, LangGraph persistence, CLI/TUI/Web interfaces, and an explicit scientific pipeline of intake → planning → execution → evaluation → writing → verification. ([GitHub][1])

Its June–August 2026 releases are particularly interesting: it added graph memory relationships such as **complements / contradicts / supersedes**, cron-style autonomous tasks, `AutoSkills` generated from memory clusters, unified HITL approval for asynchronous subagents, and expert skills that can be invited into sessions as panels or background workers. ([GitHub][1])

Conceptually:

```text
research task
   ↓
planner
   ↓
research / code / debug / analyze workers
   ↓
observations
   ↓
persistent memory graph
   ↓
repeated patterns
   ↓
AutoSkill proposal
   ↓
human review
   ↓
future research capability
```

That is remarkably close to your intended system.

### What I'd actually pinch

Do a serious read of:

```text
memory lifecycle
AutoSkills compiler
scheduled jobs
async subagent handling
approval propagation
dynamic tool selection
LangGraph checkpoint recovery
CLI/Web common gateway
```

And compare all of those against Hermes rather than automatically replacing Hermes.

**Priority: #1 clone.**

---

# 2. Neo.mjs Agent OS — the most extreme “software organism” implementation I found

[https://github.com/neomjs/neo](https://github.com/neomjs/neo)

This one is wild.

The project describes and operates a cross-model AI engineering system around its own codebase using:

* persistent Memory Core
* knowledge-base MCP
* Active Hybrid GraphRAG
* multiple model families
* cross-model review
* an orchestrator
* “DreamService” background consolidation/self-improvement
* self-healing loops
* per-project isolation

and claims hundreds of merged PRs per month produced through this system. ([GitHub][2])

The interesting idea isn't whether every claim in their README generalizes.

It's the **organizational architecture**:

```text
               persistent brain
                    │
        ┌───────────┼────────────┐
        ▼           ▼            ▼
     Claude       Gemini        GPT
        │           │            │
        └────── cross-review ─────┘
                    │
                artifacts
                    │
                    ▼
              verification
                    │
                    ▼
               repository
                    │
                    ▼
              DreamService
                    │
          memory consolidation
                    │
                    └──→ next cycle
```

They've taken the “agent institution” idea further than most research demos.

### For your system

Read their:

```text
ADRs
Agent OS topology
Memory Core
GraphRAG architecture
DreamService
cross-model review
tenant/project isolation
```

Not because you should copy Neo.mjs, but because this is essentially a live experiment in:

> **what happens when the repository is permanently inhabited by agents instead of agents being invoked episodically?**

**Priority: very high architecture mine.**

---

# 3. Neo4j Meta Knowledge Graph — coding agents + lifecycle hooks + graph memory + evolution

[https://github.com/neo4j-labs/meta-knowledge-graph](https://github.com/neo4j-labs/meta-knowledge-graph)

This is one of the strongest newer finds.

It is explicitly **harness agnostic**. Claude Code, Codex or another agent can use the same underlying graph memory through lifecycle hooks and MCP. Sessions are captured; durable learnings are extracted afterward; observations form an append-only episodic timeline; useful context is injected into future sessions. ([GitHub][3])

Architecture:

```text
Claude / Codex / whatever
          │
     lifecycle hooks
          │
          ▼
      observations
          │
          ├──── episodic timeline
          │
          ▼
      LLM extraction
          │
          ▼
       learnings
          │
          ▼
    knowledge graph
          │
        MCP
          │
          └──→ future agents
```

It even retains version history when consolidated system-prompt knowledge changes. ([GitHub][3])

This is highly relevant to your:

```text
agents ≠ canonical state
```

principle.

Agents remain replaceable harnesses.

Memory survives them.

**Clone it.**

---

# 4. Neo4j Agent Memory + TCK — unusually serious multi-agent interoperability experiment

Core:

[https://github.com/neo4j-labs/agent-memory](https://github.com/neo4j-labs/agent-memory)

TCK/demos:

[https://github.com/neo4j-labs/agent-memory-tck](https://github.com/neo4j-labs/agent-memory-tck)

This is more interesting than it sounds.

The TCK includes a multi-agent example where six agents implemented in **five languages and several different frameworks** share the same graph memory:

```text
PydanticAI
Vercel AI SDK
Go custom client
LangGraph
Semantic Kernel
R/ellmer
```

with roles including research, enrichment, orchestration, validation and statistics. ([GitHub][4])

That is almost a proof of the architecture I recommended:

```text
DO NOT:

make framework X your architecture

DO:

canonical external substrate
      ↑
framework adapters
```

This repo is therefore useful not merely for Neo4j.

Steal their **technology compliance kit idea**.

Imagine:

```text
PĀṬALA AGENT TCK

does this runtime support:
✓ resolve
✓ context
✓ propose
✓ run events
✓ approval
✓ artifacts
✓ provenance
✓ cancellation
✓ resume
```

Then Hermes, Codex, PydanticAI, a Rust worker, or some future GPT-8 harness can all be tested against the same contract.

That's excellent.

---

# 5. MemOS — memory OS + Hermes integration + skills + world models

[https://github.com/MemTensor/MemOS](https://github.com/MemTensor/MemOS)

This has evolved well beyond a memory library.

Current MemOS explicitly supports Hermes Agent and describes a tiered local memory architecture containing:

```text
L1 trace
L2 policy
L3 world model
crystallized skills
```

with feedback-driven evolution, graph-structured memory, multimodal/tool memory, asynchronous scheduling, MCP, memory correction and multi-agent sharing. ([GitHub][5])

This is very relevant because **you already use Hermes**.

Rather than implementing sophisticated general agent memory inside Pāṭala, I would test:

```text
Hermes
  +
MemOS
  +
Pāṭala epistemic store
```

and establish the boundary experimentally.

Likely:

```text
MemOS owns
───────────
working experience
procedural memory
tool-use patterns
agent preferences
skills

Pāṭala owns
───────────
claims
evidence
arguments
canonical sources
review
scholarly decisions
```

Don't duplicate both.

**Very high-value experiment.**

---

# 6. Memento-Skills — agent literally redesigns its own agent skills

[https://github.com/Memento-Teams/Memento-Skills](https://github.com/Memento-Teams/Memento-Skills)

This is much closer to Sakana-style deployment-time evolution.

The agent has a skill router and skill library. When given a problem it either selects an existing executable skill or generates one, executes it, reflects on the result, and then either reinforces the skill's utility or rewrites the underlying skill package. ([GitHub][6])

That's:

```text
task
 ↓
retrieve/generate skill
 ↓
execute
 ↓
outcome
 ↓
reflect
 ↓
update skill
 ↓
future task
```

This is the important distinction from static `SKILL.md` collections:

> **skills are runtime-evolving artifacts.**

For Pāṭala, however, I would add one missing component:

```text
skill modification
      ↓
PROPOSAL
      ↓
benchmark
      ↓
review
      ↓
promote
```

rather than allowing silent mutation.

So:

**Memento evolution + Vouch/Pāṭala gate** is stronger than either alone.

---

# 7. CoEvoSkills — skill and verifier co-evolve together

[https://github.com/Zhang-Henry/CoEvoSkills](https://github.com/Zhang-Henry/CoEvoSkills)

This is one of the most Pāṭala-compatible research implementations.

Instead of self-improvement being:

```text
agent writes skill
→ trusts itself
```

there are two evolving systems:

```text
Skill Generator
      ↕
Surrogate Verifier
```

The verifier independently evolves test assertions, while ground-truth evaluation is information-isolated and returns only opaque pass/fail where needed. ([GitHub][7])

This is **much more sophisticated**.

You could apply the same pattern to scholarship:

```text
TRANSLATION EVOLVER
       ↕
TRANSLATION VERIFIER

ARGUMENT EXTRACTOR
       ↕
ARGUMENT VERIFIER

EVIDENCE RETRIEVER
       ↕
EVIDENCE-SUFFICIENCY VERIFIER
```

The verifier itself improves.

That could be huge.

**Clone + adapt conceptually.**

---

# 8. MemSkill — memory policy learns how to remember

[https://github.com/ViktorAxelsen/MemSkill](https://github.com/ViktorAxelsen/MemSkill)

MemSkill is not mainly learning facts. It learns **meta-memory skills**:

> what should be remembered, what should be ignored, and how memory should be constructed.

It maintains an evolving skill bank and mines difficult cases to generate/refine memory strategies. It also has checkpointed training and high-throughput parallel evaluation infrastructure. ([Cloudflare Docs][8])

That's a useful distinction:

```text
MEMORY
"Claim X failed because source Y was missing."

META-MEMORY
"When translation tasks contain ambiguous compounds,
retain competing parse evidence before summarizing."
```

Pāṭala could eventually learn the second type from its execution history.

I'd keep this as a **research experiment**, not a production dependency.

---

# 9. MemRL — runtime learning without modifying weights

[https://github.com/MemTensor/MemRL](https://github.com/MemTensor/MemRL)

This is closely connected to MemOS but more research-y.

MemRL treats episodic memories as candidate strategies whose utility can be learned from environment feedback. Its two-stage retrieval attempts to filter semantically similar but low-value memories and favor experiences that actually produced successful outcomes. ([GitHub][9])

The useful idea is:

```text
similar experience ≠ useful experience
```

Rank memory by something closer to:

[
R(m\mid q)
==========

semantic(q,m)
\times
utility(m)
]

rather than cosine similarity alone.

For Pāṭala:

```text
past translation strategy
├─ semantic relevance
├─ verifier score
├─ review acceptance
├─ transfer success
└─ freshness
```

That's much stronger retrieval.

---

# 10. SkillRL — trajectories → hierarchical skills → RL

[https://github.com/aiming-lab/SkillRL](https://github.com/aiming-lab/SkillRL)

SkillRL takes successful/raw experiences and abstracts reusable strategies into a hierarchical skill library, then uses those skills in recursive RL training. The repo includes training code, SFT data generation and released checkpoints. ([GitHub][10])

This closes a loop I think you'll eventually want:

```text
Pāṭala runs
      ↓
verified trajectories
      ↓
skill extraction
      ↓
skill library
      ↓
SFT/RL environment
      ↓
new agent
      ↓
Pāṭala runs
```

Your execution logs therefore shouldn't be regarded as mere debugging.

They're **future training data**.

---

# 11. Skill Self-Play — Alibaba/Qwen taking the idea seriously

[https://github.com/Qwen-Applications/skill-self-play](https://github.com/Qwen-Applications/skill-self-play)

This is interesting because it's a major model team implementing a similar principle.

Skill Self-Play combines:

* evolving skill libraries
* skill-routed task generation
* automatic validity checks
* frontier curriculum creation
* feedback-based skill evolution

and uses the skill system for training while leaving the resulting solver prompt-only at inference. ([Cloudflare Docs][11])

That reinforces an important architectural separation:

```text
AGENT PRODUCTION SYSTEM
can be enormously complicated

DEPLOYED MODEL
can remain relatively simple
```

Thus your Pāṭala infrastructure could eventually serve as a **training/evolution environment** without becoming baggage every deployed model must carry.

---

# 12. Evolving Memory / Cognitive Trajectory Engine — strange but conceptually rich personal project

[https://github.com/EvolvingAgentsLabs/evolving-memory](https://github.com/EvolvingAgentsLabs/evolving-memory)

This is precisely the kind of weird ambitious personal repo worth reading.

It captures complete agent execution trajectories into a topological graph and periodically consolidates them through bio-inspired “dream cycles.” It also experiments with an agent instruction-set architecture where models emit structured opcodes rather than arbitrary JSON. ([GitHub][12])

I would treat the neuroscience terminology cautiously.

But two engineering ideas are interesting:

### Agent trajectories as graph objects

```text
Action
→ Observation
→ Decision
→ Tool
→ Result
→ Reflection
```

### Agent ISA

Instead of freeform:

```json
{"tool": "...", "args": "..."}
```

have a tiny executable operation language.

That links directly to the **KG2Code** paper we found previously.

Worth code-reading.

---

# 13. EvoMap Evolver — distributed reusable “genes” for coding agents

Claude Code:

[https://github.com/EvoMap/evolver-claude-code-plugin](https://github.com/EvoMap/evolver-claude-code-plugin)

Other harness:

[https://github.com/EvoMap/evolver-antigravity-plugin](https://github.com/EvoMap/evolver-antigravity-plugin)

This is interesting because it attempts to turn agent improvements into portable artifacts called genes/capsules, with local persistent evolution memory and an MCP bridge to a network where proven patterns can be reused. ([GitHub][13])

Conceptually:

```text
Agent A
 discovers strategy
       ↓
Gene
       ↓
validation
       ↓
network
       ↓
Agent B
 reuses strategy
```

Now translate this into Pāṭala:

```text
Scholar Agent A
discovers robust procedure for
checking Sanskrit bahuvrīhi ambiguity

       ↓

Skill artifact
       ↓
evaluation/review
       ↓
skill registry
       ↓
all translation agents
```

You don't need EvoMap itself.

But **verified skill portability** is almost certainly part of your endgame.

---

# 14. `self-evolving-agent` — tiny personal repo with a surprisingly correct governance model

[https://github.com/RangeKing/self-evolving-agent](https://github.com/RangeKing/self-evolving-agent)

Only a small repo, but it makes the right distinction between:

```text
logging failure
```

and:

```text
capability management
```

It keeps capability records, curricula, evaluation, transfer checks and promotion review. It includes model-in-the-loop benchmark scripts and explicit promotion gates. ([Cloudflare Docs][14])

That resembles what you want:

```text
WeakCapability
       ↓
LearningAgenda
       ↓
training tasks
       ↓
evaluation
       ↓
transfer test
       ↓
promotion
```

Excellent personal project to mine for your skill-governance schema.

---

# 15. Self-Evolving-Skill — another tiny repo with five-gate knowledge governance

[https://github.com/191341025/Self-Evolving-Skill](https://github.com/191341025/Self-Evolving-Skill)

This one has explicit confidence decay, hard/soft feedback, knowledge routing, selective injection, validation gates and detailed evolution logs. The author reports iterative experiments against real database tasks rather than only toy prompts. ([GitHub][15])

Again, don't trust its formulas automatically.

But inspect:

```text
Five-Gate governance
confidence decay
rejection criteria
knowledge snapshots
evolution logs
```

It's another independent convergence toward:

> **self-evolution requires governance, not merely reflection.**

That is very supportive of your Pāṭala review-gate direction.

---

# 16. A-MEM MCP — self-evolving graph memory specifically for coding agents

[https://github.com/DiaaAj/a-mem-mcp](https://github.com/DiaaAj/a-mem-mcp)

This one is clean and simple enough to read rapidly.

New memories are:

```text
analyzed
→ linked
→ related memories updated
→ stored
```

forming an evolving Zettelkasten-like graph. Retrieval starts broad using lightweight metadata and lets the agent drill into selected memories, which explicitly reduces context usage. ([GitHub][16])

That `peek → drill` interface is excellent:

```text
search_memories()
   ↓
tiny records only

read_memory(id)
   ↓
full content
```

Exactly the progressive-disclosure principle we've now seen in:

* graph retrieval
* MCP capability discovery
* knowledge projection
* agent memory

This one is worth copying at the interface level.

---

# 17. MemoryGraph — temporal graph memory implemented as an MCP service

[https://github.com/memory-graph/memory-graph](https://github.com/memory-graph/memory-graph)

Very useful small project.

It gives coding agents persistent graph memory with bitemporal-like fields:

```text
valid_from
valid_until
recorded_at
invalidated_by
```

and supports querying what was known at a historical point and how relationships evolved over time. ([GitHub][17])

For your general kernel:

```text
transaction time:
when Pāṭala learned it

valid time:
when the assertion claims it was true
```

Those are genuinely different.

That's especially relevant for historical/scientific data.

Clone.

---

# 18. agent-memory-mcp — almost a mini Pāṭala for coding knowledge

[https://github.com/ipiton/agent-memory-mcp](https://github.com/ipiton/agent-memory-mcp)

This underrated repo combines:

* episodic/semantic/procedural/working memories
* semantic + keyword retrieval
* automatic session capture
* documentation RAG
* duplicate/conflict/staleness detection
* review inbox
* temporal validity
* explicit supersession chains
* MCP + HTTP

([GitHub][18])

That's an unusually comprehensive small implementation.

Its `steward_inbox` is particularly relevant:

```text
candidate issue
    ↓
merge
mark_outdated
promote
verify
suppress
defer
```

That's basically a **memory adjudication queue**.

For Pāṭala:

```text
review inbox
    ↓
merge entity
supersede claim
verify evidence
reject relation
request scholar
```

Steal that interaction model.

---

# 19. MemOS + Hermes specifically deserves a prototype

This one is important enough to reiterate.

MemOS already ships a Hermes-oriented local plugin with hybrid retrieval, deduplication, tiered skill evolution and cross-agent memory capabilities. ([GitHub][5])

So before you write:

```text
patala-agent-memory/
```

test:

```text
Hermes
│
├─ MemOS
│    └─ experiential/procedural memory
│
└─ Pāṭala MCP
     └─ canonical epistemic knowledge
```

That's potentially an enormous amount of avoided work.

---

# 20. The most extreme embodied analogue: ABot-AgentOS

[https://github.com/amap-cvlab/ABot-AgentOS](https://github.com/amap-cvlab/ABot-AgentOS)

Code isn't fully released yet, so **don't clone expecting a complete implementation**. The repo currently says the source/resources are being prepared. ([GitHub][19])

But the architecture is significant because it combines almost everything:

```text
foundation models
edge/cloud routing
agent harness
context management
skills
tools
verification
multimodal graph memory
skill evolution
training
RL
benchmark environments
```

and uses failure-driven evolution assets. ([GitHub][19])

That's robotics, but structurally:

```text
PERCEPTION
   ↓
REASON
   ↓
ACTION
   ↓
VERIFY
   ↓
MEMORY
   ↓
EVOLVE SKILL
   ↓
TRAIN
```

is exactly the same loop as:

```text
SOURCE
   ↓
REASON
   ↓
PRODUCE CLAIM/TRANSLATION
   ↓
VERIFY
   ↓
MEMORY
   ↓
EVOLVE SKILL
   ↓
TRAIN
```

Keep watching it.

---

# 21. `production-ai-stack` — one engineer's integration map

[https://github.com/h9-tec/production-ai-stack](https://github.com/h9-tec/production-ai-stack)

Not novel research, but useful because it's one person's concrete opinionated synthesis of the ecosystem.

Its recommendation is essentially:

```text
PydanticAI     agent logic
LangGraph      stateful orchestration
Temporal       high-stakes durability
MCP            protocol
Graphiti/etc   external memory
real sandbox   code execution
```

rather than expecting one framework to own everything. ([GitHub][20])

That is independently converging on the layered architecture we arrived at.

Pattern mine; don't treat it as authority.

---

# The project I think you should study deepest: EvoScientist

If the question is:

> **“Who has actually assembled most of the pieces we have been discussing into one working system?”**

it's currently:

### EvoScientist

[https://github.com/EvoScientist/EvoScientist](https://github.com/EvoScientist/EvoScientist)

because it already combines:

```text
multi-agent research
scientific workflow
execution
memory
knowledge graph
self-generated skills
skill review
MCP
adaptive tools
scheduled autonomous work
context management
human approval
persistent LangGraph state
multiple models
Web/CLI interfaces
```

([GitHub][1])

And it's actively shipping, with 642 commits visible in the repo when I checked. ([GitHub][1])

**I would absolutely clone this before designing your scientific-agent architecture further.**

---

# But Neo.mjs is conceptually crazier

If you ask:

> “Who is closest to actually running an AI organization permanently on top of a codebase?”

then:

[https://github.com/neomjs/neo](https://github.com/neomjs/neo)

is probably the weirdest serious example I found. Its stated topology combines a knowledge base, memory core, graph retrieval, orchestration, several model families, peer review and recurring consolidation. ([GitHub][21])

Read this less as software to reuse and more as a **living systems experiment**.

---

# The combination I would prototype

Rather than implementing your own version of every frontier paper, I would now prototype:

```text
                        HERMES
                           │
                    canonical tasks
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
             Codex       Claude   Research worker
                │          │          │
                └──────────┼──────────┘
                           │
                       TASK RUNS
                           │
                           ▼
                  execution event log
                           │
             ┌─────────────┼─────────────┐
             │                           │
             ▼                           ▼
          MemOS                       Pāṭala
     experiential memory         epistemic truth
     procedural memory           claims/evidence
     skill strategies            arguments/reviews
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
                      MCP gateway
                           │
                lazy capability discovery
                           │
                           ▼
                       AGENT
                           │
                           ▼
                       Artifact
                           │
                           ▼
                      Proposal
                           │
                   Vouch-like gate
                           │
                       verifier
                           │
                         review
                           │
                    accepted state
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       skill experience          knowledge update
              │
              ▼
         Memento /
         CoEvoSkills
              │
              ▼
     candidate improved skill
              │
              ▼
        benchmark + gate
```

That is already buildable mostly from existing components.

---

# Then add the learned frontier later

Once you have enough trajectories:

```text
verified Task/Runs
      ↓
training corpus
      │
      ├── MemRL
      ├── SkillRL
      ├── MemSkill
      └── CoEvoSkills
```

And eventually:

```text
retrieval
   ↓
G-reasoner

orchestration
   ↓
Fugu/APR-like learned policy

skills
   ↓
self-evolution

agent
   ↓
RL
```

This is the distinction I would hold onto:

### **Phase 1**

Build the **institution**.

### **Phase 2**

Accumulate high-quality verified trajectories.

### **Phase 3**

Learn policies from the institution's history.

Don't start with self-improvement.

Start by creating the structure that makes successful and failed improvement **measurable**.

---

# SPEC-11 — AGENT MEMORY / SELF-EVOLVING SYSTEMS SURVEY

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/githubagent`
**Scope:** agent-memory + self-evolving systems (EvoScientist, Neo.mjs, MemOS, MemRL, MemSkill,
SkillRL, Neo4j meta-knowledge-graph, A-MEM, MemoryGraph, agent-memory-mcp, ...). Key insight: these
already cover much of the agent plumbing we'd want — **what remains distinctly ours is the epistemic
kernel + rigorous promotion path (agent output → evidence → review → canonical knowledge)**. Clone
shortlist + two research-index repos are in the final section.

---



# My new clone shortlist

If you're making another `/clones/frontier-agent-os/`, I'd now put these first:

```text
01 https://github.com/EvoScientist/EvoScientist

02 https://github.com/neomjs/neo

03 https://github.com/neo4j-labs/meta-knowledge-graph

04 https://github.com/neo4j-labs/agent-memory
05 https://github.com/neo4j-labs/agent-memory-tck

06 https://github.com/MemTensor/MemOS
07 https://github.com/MemTensor/MemRL

08 https://github.com/Memento-Teams/Memento-Skills

09 https://github.com/Zhang-Henry/CoEvoSkills

10 https://github.com/ViktorAxelsen/MemSkill

11 https://github.com/aiming-lab/SkillRL

12 https://github.com/Qwen-Applications/skill-self-play

13 https://github.com/EvolvingAgentsLabs/evolving-memory

14 https://github.com/EvoMap/evolver-claude-code-plugin

15 https://github.com/RangeKing/self-evolving-agent

16 https://github.com/191341025/Self-Evolving-Skill

17 https://github.com/DiaaAj/a-mem-mcp

18 https://github.com/memory-graph/memory-graph

19 https://github.com/ipiton/agent-memory-mcp

20 https://github.com/EverMind-AI/EverOS
```

And two research-index repos because they'll keep feeding you new projects:

```text
https://github.com/LuckyGirl-XU/Awesome-Agent-Dynamic-Graphs

https://github.com/DataArcTech/Awesome-Agent-Skill-Papers
```

The biggest new realization from this pass is that **EvoScientist + Neo.mjs + MemOS + Neo4j's agent-memory work already cover much more of your envisioned operating system than I'd assumed**. The part that remains distinctly Pāṭala is not generic memory/orchestration—it is the **epistemic kernel and rigorous promotion path from agent output → evidence → review → canonical knowledge**. That is where I would concentrate original engineering rather than rebuilding their agent plumbing.

[1]: https://github.com/EvoScientist/EvoScientist "GitHub - EvoScientist/EvoScientist: 🔬 Harness Vibe Research with Self-evolving AI Scientists · GitHub"
[2]: https://github.com/neomjs/neo "GitHub - neomjs/neo: Neo.mjs is a self-evolving software organism: a professional end-to-end AI engineering team whose cross-model swarm inhabits live apps via Neural Link, Active Hybrid GraphRAG, DreamService, and self-healing loops. · GitHub"
[3]: https://github.com/neo4j-labs/meta-knowledge-graph?utm_source=chatgpt.com "GitHub - neo4j-labs/meta-knowledge-graph: Self-improving, harness-agnostic memory layer for AI agents, backed by Neo4j — lifecycle hooks capture every session, MCP tools recall project memory, and an LLM extraction loop distills durable learnings and evolves the agent's system prompt. · GitHub"
[4]: https://github.com/neo4j-labs/agent-memory-tck?utm_source=chatgpt.com "GitHub - neo4j-labs/agent-memory-tck: Technology Compliance Kit (TCK) for Neo4j Agent Memory · GitHub"
[5]: https://github.com/MemTensor/MemOS?utm_source=chatgpt.com "GitHub - MemTensor/MemOS: Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings · GitHub"
[6]: https://github.com/Memento-Teams/Memento-Skills?utm_source=chatgpt.com "GitHub - Memento-Teams/Memento-Skills: Memento-Skills: Let Agents Design Agents · GitHub"
[7]: https://github.com/Zhang-Henry/CoEvoSkills?utm_source=chatgpt.com "GitHub - Zhang-Henry/CoEvoSkills: CoEvoSkills: Self-Evolving Agent Skills via Co-Evolutionary Verification · GitHub"
[8]: https://developers.cloudflare.com/workers/static-assets/?utm_source=chatgpt.com "Static Assets · Cloudflare Workers docs"
[9]: https://github.com/MemTensor/MemRL?utm_source=chatgpt.com "GitHub - MemTensor/MemRL: Paper: “MEMRL: SELF-EVOLVING AGENTS VIA RUNTIME REINFORCEMENT LEARNING ON EPISODIC MEMORY” Open-Source Code · GitHub"
[10]: https://github.com/aiming-lab/SkillRL?utm_source=chatgpt.com "GitHub - aiming-lab/SkillRL: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning · GitHub"
[11]: https://developers.cloudflare.com/workers/configuration/placement/?utm_source=chatgpt.com "Placement · Cloudflare Workers docs"
[12]: https://github.com/EvolvingAgentsLabs/evolving-memory?utm_source=chatgpt.com "GitHub - EvolvingAgentsLabs/evolving-memory · GitHub"
[13]: https://github.com/EvoMap/evolver-claude-code-plugin?utm_source=chatgpt.com "GitHub - EvoMap/evolver-claude-code-plugin: Official Claude Code plugin for Evolver — GEP-powered self-evolution for AI agents. Part of EvoMap. · GitHub"
[14]: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/?utm_source=chatgpt.com "Connect to PostgreSQL · Cloudflare Hyperdrive docs"
[15]: https://github.com/191341025/Self-Evolving-Skill?utm_source=chatgpt.com "GitHub - 191341025/Self-Evolving-Skill: A design pattern for Claude Code Skills that improve through use — more accurate, more efficient, never bloated. | 越用越准、越用越快、但不臃肿的 Skill 设计模式 · GitHub"
[16]: https://github.com/DiaaAj/a-mem-mcp?utm_source=chatgpt.com "GitHub - DiaaAj/a-mem-mcp · GitHub"
[17]: https://github.com/memory-graph/memory-graph?utm_source=chatgpt.com "GitHub - memory-graph/memory-graph: A graph DB-based MCP memory server for coding agents with intelligent relationship tracking · GitHub"
[18]: https://github.com/ipiton/agent-memory-mcp?utm_source=chatgpt.com "GitHub - ipiton/agent-memory-mcp: MCP server that gives AI agents persistent memory with semantic search · GitHub"
[19]: https://github.com/amap-cvlab/ABot-AgentOS?utm_source=chatgpt.com "GitHub - amap-cvlab/ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory · GitHub"
[20]: https://github.com/h9-tec/production-ai-stack?utm_source=chatgpt.com "GitHub - h9-tec/production-ai-stack · GitHub"
[21]: https://github.com/neomjs/neo?utm_source=chatgpt.com "GitHub - neomjs/neo: Neo.mjs is a self-evolving software organism: a professional end-to-end AI engineering team whose cross-model swarm inhabits live apps via Neural Link, Active Hybrid GraphRAG, DreamService, and self-healing loops. · GitHub"

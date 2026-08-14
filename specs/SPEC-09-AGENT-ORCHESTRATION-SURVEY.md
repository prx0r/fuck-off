# SPEC-09 — AGENT ORCHESTRATION SURVEY (runtimes, protocols, universal schema)

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/agenticref`
**Scope:** agent orchestration infra (Hermes Kanban, Restate, Temporal, DBOS, Hatchet, Pydantic AI,
LangGraph, Mastra), protocols (MCP, A2A, MCP Gateway, GitSkills), and the emerging **universal schema**
(PROJECT → KNOWLEDGE/WORK/EXECUTORS/OUTPUT with full end-to-end provenance: Task→Run→Agent→Artifact→
Proposal→Review→Decision). Key takeaways: (1) keep a cheap single-host runtime today (Hermes Kanban +
SQLite + MCP + git worktrees), choose Restate/DBOS/Temporal/Hatchet only when the single-host boundary
hurts; (2) the universal schema's Review/Decision/Supersede chain matches our epistemic envelope.

---

Yes. The agentic-infrastructure frontier fits the graph findings extremely well, and I think it clarifies the final architecture.

The central mistake in most agent frameworks is mixing **knowledge state**, **execution state**, **conversation state**, and **tool state** together. Pāṭala should keep them separate and connect them through IDs and provenance:

```text
                 EPISTEMIC PLANE
          claims / evidence / arguments
                        │
                        │ provenance
                        ▼
                 EXECUTION PLANE
      task → run → step → tool call → artifact
                        │
                        │ produced / consumed
                        ▼
                  ARTIFACT PLANE
       files / diffs / datasets / projections
                        │
                        ▼
                  REVIEW PLANE
       validation → review → accept/reject
                        │
                        ▼
                   AGENT PLANE
    Hermes / Codex / research / scholar / reviewer
```

That is much stronger than “use LangGraph.”

---

# Tier 0 — the infrastructure I would study first

## 1. Hermes Kanban — keep this as the local control plane

[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

Specific contract:

[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban-worker-lanes.md](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban-worker-lanes.md)

Hermes has converged on an unusually good distinction:

```text
Hermes Kanban = lifecycle truth
Worker lane   = executor
Reviewer      = completion gate
PR/artifact   = output
```

Workers do not own the canonical task state. The Kanban kernel records `task_runs` separately from `task_events`, including state transitions such as claim, heartbeat, crash, timeout, completion, blocking and reclaiming. ([GitHub][1])

That is exactly the distinction you need.

### Steal/retain

```text
tasks
task_runs
task_events
dependencies
comments
claims/leases
heartbeats
failure counters
review-required
workspaces
```

I would **not replace Hermes for your single-machine worker fleet**.

Instead, make Pāṭala compatible with the Hermes lifecycle.

---

# 2. Agetor — still one of the best personal projects

[https://github.com/alamops/agetor](https://github.com/alamops/agetor)

This is even more useful after the latest code/docs read.

Its schema separates **Task ≠ Run ≠ Event**. A task can accumulate multiple runs, and each run has a persistent event stream. It also gives every code task an isolated Git worktree from a pinned base SHA, preserves run history, surfaces approvals/questions structurally, and exposes the whole thing through a tiny local JSON+SSE API. ([GitHub][2])

That's excellent architecture:

```text
Task
  │
  ├── Run 1
  │    ├── event
  │    ├── event
  │    └── result
  │
  ├── Run 2
  │    └── ...
  │
  └── accepted artifact
```

This distinction is extremely important.

A task is:

> an intended piece of work.

A run is:

> one attempt at carrying it out.

An artifact is:

> something produced by that attempt.

A review is:

> a judgment about that artifact.

### Action

**Clone and inspect its SQLite migrations.**

I would probably pinch its task/run/event schema more directly than I previously suggested.

---

# 3. Temporal — strongest mature durable-execution substrate

[https://github.com/temporalio/temporal](https://github.com/temporalio/temporal)

Agent examples:

[https://github.com/temporalio/ai-cookbook](https://github.com/temporalio/ai-cookbook)

Temporal turns workflow execution into recoverable state: workflows survive failures, and nondeterministic/external operations run as activities whose results are persisted so execution can resume instead of blindly repeating work. ([GitHub][3])

The recent agent integrations make this much more directly relevant. Temporal's OpenAI Agents integration, for example, durably handles model calls, tools, MCP, approvals, sessions, child workflows and agent handoffs. ([GitHub][4])

The underlying pattern is what matters:

```text
DETERMINISTIC ORCHESTRATION

Task
 ↓
Step A
 ↓
checkpoint
 ↓
LLM activity
 ↓
checkpoint
 ↓
Tool activity
 ↓
checkpoint
 ↓
review wait
 ↓
resume tomorrow
```

### But

I **wouldn't introduce Temporal into your current single-host Pāṭala fleet yet**.

Hermes + SQLite is much lighter.

Temporal becomes interesting when:

```text
multiple machines
long-running jobs
weeks-long waits
thousands of concurrent executions
strong recovery requirements
```

### Action

Study it as the eventual distributed-runtime backend.

---

# 4. Restate — possibly a better eventual Pāṭala fit than Temporal

[https://github.com/restatedev/restate](https://github.com/restatedev/restate)

Agent examples:

[https://github.com/restatedev/ai-examples](https://github.com/restatedev/ai-examples)

This deserves very serious attention.

Restate provides durable execution, stateful services/actors, reliable RPC, queues and orchestration without forcing agent logic into one particular agent framework. Its agent examples demonstrate crash-safe model/tool calls, idempotent retries, human waits, durable sessions and multi-agent coordination. ([GitHub][5])

Its abstraction is closer to:

```text
Entity / service
     │
 durable invocation
     ↓
agent
     │
 durable invocation
     ↓
tool
```

rather than “everything is one giant workflow.”

That is interesting for Pāṭala because you naturally have durable entities:

```text
Work
Claim
Translation
Review
Task
Agent
Corpus
```

You could conceivably have:

```text
ClaimActor(C17)
ReviewActor(R93)
CorpusActor(IPVV)
```

each serializing mutations to its own durable state.

### Action

**Clone this. High priority.**

I'd benchmark Restate against Temporal before choosing a distributed runtime.

---

# 5. DBOS — extremely elegant if Postgres is already canonical

[https://github.com/dbos-inc/dbos-transact-py](https://github.com/dbos-inc/dbos-transact-py)

[https://github.com/dbos-inc/dbos-transact-ts](https://github.com/dbos-inc/dbos-transact-ts)

DBOS implements durable functions by checkpointing workflow steps in PostgreSQL. A failed process resumes from its last completed step rather than replaying everything. ([GitHub][6])

This is conceptually very attractive for you because we already converged on:

```text
Postgres = canonical structured state
```

So you could potentially get:

```text
canonical graph
+
task/run state
+
durable workflow checkpoints

       all centered on Postgres
```

rather than operating Temporal's separate distributed control infrastructure.

This would make a beautifully compact small-team architecture.

### Action

Clone and prototype.

**DBOS may actually be the most aesthetically compatible distributed runtime with optimized Pāṭala.**

---

# 6. Hatchet — excellent middle ground

[https://github.com/hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)

And especially:

[https://github.com/hatchet-dev/durable-execution-the-hard-way](https://github.com/hatchet-dev/durable-execution-the-hard-way)

Hatchet combines a Postgres-backed durable task queue, workflows, worker scheduling, rate limiting, observability and dashboards. Its authors explicitly position it between basic task queues and heavyweight durable workflow engines. ([GitHub][7])

The second repo is gold because it teaches durable execution from scratch in Go + Postgres:

```text
https://github.com/hatchet-dev/durable-execution-the-hard-way
```

Rather than accepting Temporal/DBOS magic, read that repo and understand:

```text
journal
checkpoint
step id
retry
lease
recovery
idempotency
```

([GitHub][8])

**Definitely clone that educational repo.**

---

# 7. Dapr Agents — frontier if Pāṭala becomes genuinely distributed

[https://github.com/dapr/dapr-agents](https://github.com/dapr/dapr-agents)

Dapr Agents combines durable workflows with virtual actors, pub/sub, service-to-service calls, state management, resiliency policies, tracing and multi-agent communication. It is specifically designed to distribute agents across machines while retaining durable execution. ([GitHub][9])

Architecture:

```text
Agent A actor
     │
     ├── message bus
     │
Agent B actor
     │
     └── durable workflow
              │
              ▼
           Agent C
```

This is considerably more infrastructure than you need today.

But if someday you're running:

```text
1,000 scholar workers
100 ingest workers
50 reviewers
multiple GPU workers
multi-host queues
```

then Dapr becomes relevant.

### Action

Pattern mine now; don't adopt now.

---

# 8. Inngest AgentKit — deterministic routing is the important part

[https://github.com/inngest/agent-kit](https://github.com/inngest/agent-kit)

The useful idea isn't “multi-agent network.”

It's that routing can range from fully deterministic code to LLM-driven supervision while operating over a shared typed state. Inngest then supplies fault-tolerant orchestration underneath it. ([GitHub][10])

That suggests a very good principle:

```text
use code whenever routing can be code
use LLM only where routing requires judgment
```

Example:

```text
if artifact.type == "translation"
and verification.failed:
    → translation_repair

elif scholarly_judgment_required:
    → scholar_review

else:
    → deterministic next stage
```

Don't ask an LLM:

> “Who should handle this?”

when the database already knows.

### Action

Mine the router/state model.

---

# 9. Pydantic AI — likely best Python agent-shell candidate

[https://github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)

This project has become substantially more interesting by 2026. It now combines typed agents, structured outputs, MCP, tool approval, evaluations, OTel observability, graph workflows, reusable capabilities and durable-execution integrations. ([GitHub][11])

Most interestingly, the durability abstraction is becoming **runtime-neutral**: Temporal, DBOS and Prefect are being treated as execution capabilities rather than something that should infect your agent implementation. ([GitHub][12])

That's exactly right.

You want:

```python
agent = ScholarAgent(...)
```

not:

```python
agent = TemporalScholarAgent(...)
```

The runtime belongs underneath.

### Action

This is the Python agent framework I would most seriously evaluate for new Pāṭala worker implementations.

Not because it has more features.

Because:

```text
Pydantic types
structured outputs
tools
MCP
evals
durability abstraction
```

fit your verification-heavy design.

---

# 10. mcp-agent — very good minimal orchestration philosophy

[https://github.com/lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent)

Its thesis is basically:

> use MCP + a few composable agent patterns instead of inventing giant proprietary abstractions.

It includes router, orchestrator, map-reduce, evaluator-optimizer and swarm patterns, and can run the same agent workflows durably on Temporal. ([GitHub][13])

I strongly agree with this for Pāṭala.

You probably need:

```text
router
parallel map
reduce
evaluator → optimizer
handoff
review gate
```

not a mystical “society of agents.”

**Clone this.**

---

# 11. LangGraph — benchmark target, not necessarily your foundation

[https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

LangGraph provides durable stateful graphs, human-in-the-loop inspection/modification, memory and execution tracing. ([GitHub][14])

It is mature and absolutely worth benchmarking.

But I don't think your domain model should become:

```text
Pāṭala = LangGraph state
```

because your canonical state is richer than an agent workflow state.

Use something like:

```text
LangGraph
     │
     ▼
Pāṭala tools/API
```

not:

```text
Pāṭala canonical objects
     ↓
stuffed into LangGraph checkpoints
```

---

# 12. Mastra — best TypeScript integrated app framework candidate

[https://github.com/mastra-ai/mastra](https://github.com/mastra-ai/mastra)

Mastra combines agents, graph workflows, persistent pause/resume, memory, MCP, observability and evals in a TypeScript-native package. ([GitHub][15])

If you ever want the **web/agent control surface itself** to be TypeScript end-to-end, Mastra is worth serious examination.

But since your factory/research agents are naturally Python-heavy, I would probably keep it on the API/UI side rather than make it the universal agent runtime.

---

# The protocols matter almost more than frameworks

This is where I think your stack gets very clean.

# 13. MCP = agent ↔ capability

Conceptually:

```text
AGENT
  │
  ▼
tool / data capability
```

For Pāṭala:

```text
resolve
search
context
trace
compare
evidence
review
propose
```

MCP should expose **capabilities**.

It should not be your multi-agent lifecycle.

---

# 14. A2A = agent/service ↔ agent/service

[https://github.com/a2aproject/A2A](https://github.com/a2aproject/A2A)

A2A's current spec has a particularly relevant model:

```text
Task
├── status
├── artifacts
├── history
└── context_id
```

with explicit lifecycle states such as submitted, working, completed, failed, canceled, input-required and rejected. ([GitHub][16])

This maps almost directly to the Task≠Run insight.

I would make Pāṭala's internal objects capable of exporting to A2A, **without making A2A canonical**.

Perhaps:

```text
PatalaTask
   ↓ adapter
A2A Task

PatalaArtifact
   ↓ adapter
A2A Artifact
```

Then external research agents can interoperate without understanding Hermes internals.

---

# 15. MCP Gateway — tool explosion is becoming a real frontier problem

This little Rust project is very relevant:

[https://github.com/MikkoParkkola/mcp-gateway](https://github.com/MikkoParkkola/mcp-gateway)

Instead of showing an agent hundreds of individual tools, it presents a fixed meta-tool surface and lets the agent discover capabilities lazily. It also ingests `SKILL.md` files and exposes their contents through progressive disclosure. ([GitHub][17])

That directly reinforces our graph-side discovery conclusion.

Don't do:

```text
Agent system prompt:

128 MCP tools
47 Pāṭala tools
32 upload tools
18 scholar tools
...
```

Do:

```text
discover("translation verification")
        ↓
returns:
verify_translation
compare_readings
source_passage
```

Then load only those schemas.

This is likely important for your future agent fleet.

---

# 16. MCP Gateway Registry — control plane for agents + tools + skills

[https://github.com/agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)

This is more enterprise-heavy but architecturally fascinating.

It combines:

```text
MCP server registry
agent registry
skills registry
A2A discovery
semantic capability search
access policies
auditing
```

and supports virtual MCP servers aggregating selected capabilities across many backend servers. ([GitHub][18])

You probably don't need their auth infrastructure.

But their abstraction is correct:

```text
Capability Registry

Agent
Tool
Skill
Service
```

This should influence your future Pāṭala registry.

---

# 17. GitSkills — enormous new dataset you should probably ingest

Paper, published **August 11, 2026**:

[https://arxiv.org/abs/2608.10906](https://arxiv.org/abs/2608.10906)

This is extremely timely.

GitSkills collected **3,797,117 `SKILL.md` occurrences from 282,200 GitHub repositories**, deduplicated into ~1.88M distinct contents, with metadata/frontmatter and some history packaged into SQLite. ([arXiv][19])

That means:

> don't invent your entire skill vocabulary manually.

You can mine this dataset for:

```text
common skill structures
tool dependencies
domain taxonomies
trigger patterns
duplicate skills
high-signal coding workflows
review patterns
```

This could potentially seed a Pāṭala skill registry.

Very high value.

---

# 18. Hierarchical lazy tool discovery — current research supports exactly this

Recent July 2026 paper:

[https://arxiv.org/abs/2607.11138](https://arxiv.org/abs/2607.11138)

It argues that flat tool registries cause context/tool-selection problems and proposes a rooted capability tree where only immediate child capabilities are loaded during traversal, using stack-based execution for nested contexts. ([arXiv][20])

This maps beautifully onto the **knowledge graph retrieval frontier** we just covered:

```text
GRAPH RETRIEVAL

question
 ↓
discover relevant graph region
 ↓
load bounded subgraph
```

and now:

```text
TOOL RETRIEVAL

task
 ↓
discover relevant capability region
 ↓
load bounded toolset
```

Same principle.

## This may be a general law for agent systems

[
\text{Expose only the local frontier}
]

Not the whole universe.

---

# 19. Self-healing orchestration — retries aren't enough

Paper:

[https://arxiv.org/abs/2606.01416](https://arxiv.org/abs/2606.01416)

This work distinguishes failure types such as timeout, malformed arguments, stale context, contradictory evidence and invalid intermediate output, then chooses targeted recovery actions under a budget and verifies the recovered trajectory rather than blindly retrying. ([arXiv][21])

This matters enormously.

Your worker runtime should eventually recognize:

```text
MODEL_TIMEOUT
TOOL_TIMEOUT
INVALID_SCHEMA
EVIDENCE_INSUFFICIENT
CONTRADICTION
SOURCE_BLOCKED
STALE_INPUT
TEST_FAILURE
REVIEW_REJECTED
```

Different failure:

```text
≠ generic retry
```

Instead:

```text
SOURCE_BLOCKED
  → alternate-source worker

TEST_FAILURE
  → repair worker

EVIDENCE_INSUFFICIENT
  → research expansion

REVIEW_REJECTED
  → revision task
```

This aligns perfectly with the typed epistemic graph.

---

# 20. The latest systems research says orchestration itself is becoming a performance problem

A Microsoft Azure study posted August 5, 2026 analyzed production agentic workloads and found that agent execution repeatedly alternates between model inference, CPU-side orchestration and tools, producing bursty heterogeneous demand and making CPU orchestration itself part of the critical path. ([arXiv][22])

This is useful strategically because it says:

> don't turn every microscopic operation into a separate agent/tool/network hop.

Exactly as with the optimized website:

```text
COMPUTE ONCE
BATCH
LOCALIZE
MINIMIZE ROUND TRIPS
```

For agents:

```text
bad:

agent
→ resolve
→ get node
→ get relation
→ get evidence
→ get metadata
→ get reviewer
→ get citation

good:

agent
→ context_bundle(...)
```

Agent infra and web infra converge on the **same optimization principle**.

---

# Now connect the agent frontier to the graph frontier

This is the important part.

## Layer 1 — Epistemic state

From our previous research:

```text
Pāṭala
RKA
Kappa
Vouch
DocGraph
Graphiti
Eigenius
```

Objects:

```text
Source
Passage
Claim
Evidence
Argument
Relation
Review
Decision
```

This answers:

> **What do we know, why, and how trustworthy is it?**

---

# Layer 2 — Work state

From:

```text
Hermes
Agetor
Temporal
Restate
DBOS
Hatchet
```

Objects:

```text
Task
Run
Step
Event
Attempt
Lease
Heartbeat
Failure
Checkpoint
Artifact
```

This answers:

> **What work is happening, who attempted it, and what happened?**

---

# Layer 3 — Agent capability state

From:

```text
MCP
Skills
MCP Gateway
capability registries
```

Objects:

```text
Agent
Skill
Tool
Capability
Permission
Endpoint
Model
```

This answers:

> **What can perform the work?**

---

# Layer 4 — Retrieval / reasoning

From:

```text
G-reasoner
ToG-2
PathRAG
SubgraphRAG
KAG
HippoRAG
KG2Code
```

Objects:

```text
Query
Plan
Traversal
ContextBundle
EvidenceSelection
ReasoningPath
```

This answers:

> **What knowledge does the worker need for this task?**

---

# Layer 5 — gate / review

From:

```text
Vouch
Hermes review-required
RKA
DocGraph
self-healing orchestrators
```

Objects:

```text
Proposal
Validation
Review
Defect
Revision
Acceptance
Supersession
```

This answers:

> **May this result change canonical state?**

---

# I think the universal schema is becoming visible

Something like:

```text
PROJECT
  │
  ├── KNOWLEDGE
  │      ├── Source
  │      ├── Passage
  │      ├── Entity
  │      ├── Claim
  │      ├── Argument
  │      ├── Evidence
  │      └── Review
  │
  ├── WORK
  │      ├── Task
  │      ├── Run
  │      ├── Step
  │      └── Event
  │
  ├── EXECUTORS
  │      ├── Agent
  │      ├── Skill
  │      ├── Tool
  │      └── Runtime
  │
  └── OUTPUT
         ├── Artifact
         ├── Proposal
         ├── Validation
         └── Decision
```

Then the relationships matter enormously:

```text
Task
  └── attempted_by → Run

Run
  ├── executed_by → Agent
  ├── used_skill → Skill
  ├── called_tool → Tool
  ├── read → KnowledgeObject
  └── produced → Artifact

Artifact
  └── proposed_as → Proposal

Proposal
  ├── modifies → KnowledgeObject
  └── reviewed_by → Review

Review
  └── yields → Decision

Decision
  ├── accepts → Artifact
  └── supersedes → KnowledgeObject
```

That gives you complete end-to-end provenance.

---

# An example scientific claim

Imagine an agent adds:

```text
Claim C281
```

You can eventually answer:

```text
Where did C281 come from?
```

And traverse:

```text
Claim C281
 ↑ accepted_as
Decision D82
 ↑ yielded_by
Review RV29
 ↑ reviews
Proposal P93
 ↑ produced_from
Artifact A19
 ↑ produced_by
Run R881
 ↑ attempt_of
Task T551
 ↑ assigned_to
ScholarAgent-7

R881 read:
 ├─ Paper P31
 ├─ Passage P31:182
 ├─ Claim C79
 └─ Evidence E92

R881 used:
 ├─ scifact-search
 ├─ patala-context
 └─ claim-extraction-v4

model:
Model-X

prompt version:
sha256:...
```

That is a **real audit graph**.

---

# This is where Graphiti/AriGraph become relevant

You shouldn't put that entire execution history into the semantic knowledge graph.

Instead:

```text
EPISTEMIC GRAPH
what we believe

PROVENANCE GRAPH
how it was established

EXECUTION EVENT LOG
what actually occurred
```

Join them by IDs.

That gives you clean conceptual boundaries.

---

# And this solves the docs↔state↔agents problem

This is the problem you've been circling around.

The answer isn't:

```text
agents edit docs
and docs describe state
and state somehow matches agents
```

Instead:

```text
                  CANONICAL STATE
                  Postgres/events
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
          docs         API         UI
      generated/     projection  projection
       curated
                        │
                        ▼
                      MCP
                        │
                        ▼
                     agents
```

**Docs become projections/views where possible.**

They are not the hidden operational database.

That is exactly analogous to the graph compiler architecture we found earlier.

---

# And agents themselves become worker lanes, not architecture

This is the Hermes insight I would preserve rigidly.

Don't build:

```text
ResearchAgent architecture
TranslationAgent architecture
ReviewerAgent architecture
ScholarAgent architecture
```

Build:

```text
RUNTIME
+
TASK CONTRACT
+
CAPABILITY PROFILE
```

Then:

```text
researcher =
    runtime: Hermes
    skills: [search, bibliography, evidence]
    tools: [...]
    policy: [...]

translator =
    runtime: Hermes
    skills: [...]
    tools: [...]

reviewer =
    runtime: Codex/Claude/Pydantic
    skills: [...]
```

The *agent identity* should mostly be configuration.

---

# Coding workers become replaceable adapters

Exactly like Hermes' worker-lane design:

```text
Canonical task
     │
     ├──── Hermes worker
     ├──── Codex CLI
     ├──── Claude Code
     ├──── OpenCode
     ├──── local model
     └──── human
```

All must return the same:

```text
RunResult {
   status
   summary
   artifacts
   verification
   blockers
   metadata
}
```

That prevents model/vendor lock-in.

Hermes already explicitly argues that specialist workers should remain executors under one canonical lifecycle rather than creating shadow task systems. ([GitHub][23])

---

# My ideal runtime hierarchy for you now

I would use:

```text
TODAY
───────────────────────────────

Hermes Kanban
    │
    ├── Hermes worker
    ├── CLI worker lane
    ├── research process
    └── review worker

SQLite
Task / Run / Event

Pāṭala DB
Knowledge / Evidence / Review

MCP
capabilities

Git worktrees
coding isolation
```

Very cheap.

Very comprehensible.

---

# Next stage

When the single-host boundary hurts:

```text
PĀṬALA distributed runtime
          │
          ▼
choose one:

Restate
Temporal
DBOS
Hatchet
```

My current research ranking **for your likely architecture**, not universally:

### 1. Restate

Potential best fit for distributed stateful actors/services + durable agent calls.

[https://github.com/restatedev/restate](https://github.com/restatedev/restate)

### 2. DBOS

Potentially beautiful because you're already likely to use Postgres.

[https://github.com/dbos-inc/dbos-transact-py](https://github.com/dbos-inc/dbos-transact-py)

### 3. Temporal

Strongest maturity / durability model; more infrastructure.

[https://github.com/temporalio/temporal](https://github.com/temporalio/temporal)

### 4. Hatchet

Excellent if queue/scheduling ergonomics become more important than pure durable execution.

[https://github.com/hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet)

I would actually prototype **the same Pāṭala Task→Run→Review flow on all four** before committing.

---

# My deeper clone list

These are the agent-infrastructure repos I would add alongside the graph research collection:

```text
agent-infra/

runtime/
  https://github.com/temporalio/temporal
  https://github.com/restatedev/restate
  https://github.com/dbos-inc/dbos-transact-py
  https://github.com/hatchet-dev/hatchet
  https://github.com/dapr/dapr-agents

runtime-learning/
  https://github.com/hatchet-dev/durable-execution-the-hard-way
  https://github.com/temporalio/ai-cookbook
  https://github.com/restatedev/ai-examples

orchestration/
  https://github.com/NousResearch/hermes-agent
  https://github.com/alamops/agetor
  https://github.com/inngest/agent-kit
  https://github.com/lastmile-ai/mcp-agent
  https://github.com/pydantic/pydantic-ai
  https://github.com/langchain-ai/langgraph
  https://github.com/mastra-ai/mastra

protocols/
  https://github.com/a2aproject/A2A

capability-discovery/
  https://github.com/MikkoParkkola/mcp-gateway
  https://github.com/agentic-community/mcp-gateway-registry

skills-data/
  https://arxiv.org/abs/2608.10906
```

---

# Combine that with the graph repos

Then your external-research tree becomes:

```text
research/
│
├── knowledge/
│   ├── RKA
│   ├── Kappa
│   ├── Vouch
│   ├── DocGraph
│   └── Graphiti
│
├── graph-retrieval/
│   ├── G-reasoner
│   ├── ToG-2
│   ├── PathRAG
│   ├── SubgraphRAG
│   ├── HyperGraphRAG
│   └── KAG
│
├── agent-runtime/
│   ├── Hermes
│   ├── Agetor
│   ├── Restate
│   ├── DBOS
│   ├── Temporal
│   └── Hatchet
│
├── agent-framework/
│   ├── PydanticAI
│   ├── mcp-agent
│   ├── AgentKit
│   └── LangGraph
│
├── protocols/
│   ├── MCP
│   └── A2A
│
└── capability/
    ├── MCP Gateway
    ├── MCP Registry
    └── GitSkills
```

And now I think the **endgame stack** is pretty clear:

```text
                        PĀṬALA KERNEL
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
       Epistemic Store    Work/Event Store   Artifact Store
        PostgreSQL          event-sourced          R2
             │                │                │
             └────────────────┼────────────────┘
                              │
                         Task Runtime
                              │
                 Hermes today / Restate later
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
          Worker           Worker           Worker
          Claude           Codex            Scholar
             │                │                │
             └────────────────┼────────────────┘
                              │
                         Capability Hub
                       MCP + lazy discovery
                              │
                ┌─────────────┼──────────────┐
                ▼             ▼              ▼
            graph query     sources        tools
                │
                ▼
          retrieval policies
        G-reasoner / ToG / PathRAG
                │
                ▼
          ContextArtifact
                │
                ▼
              worker
                │
                ▼
             Artifact
                │
                ▼
             Proposal
                │
                ▼
           validation gate
                │
                ▼
              review
                │
                ▼
          canonical mutation
```

The graph research and the agent-infra research are therefore **not two projects**. One solves *what agents can know and retrieve*; the other solves *how work on that knowledge executes reliably*.

The most important architectural invariant I'd adopt from all of this is:

> **Agents never own truth, workers never own lifecycle, retrieval never owns canonical knowledge, and UI/docs never own state.**

Canonical stores own truth. Everything else—agents, graphs optimized for retrieval, APIs, MCP tools, docs, websites—is a typed projection or executor around that truth.

That is a significantly stronger foundation for the generalized Pāṭala system than choosing any single “agent framework.”

[1]: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban-worker-lanes.md?utm_source=chatgpt.com "hermes-agent/website/docs/user-guide/features/kanban-worker-lanes.md at main · NousResearch/hermes-agent · GitHub"
[2]: https://github.com/alamops/agetor?utm_source=chatgpt.com "GitHub - alamops/agetor: The harness orchestrator — a local-first kanban for running Claude Code, Codex, and other CLI coding agents in parallel, each in its own git worktree. · GitHub"
[3]: https://github.com/temporalio/temporal?utm_source=chatgpt.com "GitHub - temporalio/temporal: Temporal service · GitHub"
[4]: https://github.com/temporalio/sdk-typescript/blob/main/contrib/openai-agents/README.md?utm_source=chatgpt.com "sdk-typescript/contrib/openai-agents/README.md at main · temporalio/sdk-typescript · GitHub"
[5]: https://github.com/restatedev/ai-examples?utm_source=chatgpt.com "GitHub - restatedev/ai-examples: A collection of Restate examples for AI use cases: agents, A2A, MCP, ... · GitHub"
[6]: https://github.com/dbos-inc/dbos-transact-py?utm_source=chatgpt.com "GitHub - dbos-inc/dbos-transact-py: Database-Backed Durable Python Workflows · GitHub"
[7]: https://github.com/hatchet-dev/hatchet?utm_source=chatgpt.com "GitHub - hatchet-dev/hatchet: 🪓 An orchestration engine for background tasks, AI agents, and durable workflows · GitHub"
[8]: https://github.com/hatchet-dev/durable-execution-the-hard-way?utm_source=chatgpt.com "GitHub - hatchet-dev/durable-execution-the-hard-way: Set up a durable execution engine from scratch using Postgres with no dependencies. · GitHub"
[9]: https://github.com/dapr/dapr-agents?utm_source=chatgpt.com "GitHub - dapr/dapr-agents: Build autonomous, resilient and observable AI agents with built-in workflow orchestration, security, statefulness and telemetry. · GitHub"
[10]: https://github.com/inngest/agent-kit?utm_source=chatgpt.com "GitHub - inngest/agent-kit: AgentKit: Build multi-agent networks in TypeScript with deterministic routing and rich tooling via MCP. · GitHub"
[11]: https://github.com/pydantic/pydantic-ai?utm_source=chatgpt.com "GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub"
[12]: https://github.com/pydantic/pydantic-ai/issues/5477?utm_source=chatgpt.com "First-class `RuntimeCapability` extension point for durable execution (post-v2) · Issue #5477 · pydantic/pydantic-ai · GitHub"
[13]: https://github.com/lastmile-ai/mcp-agent?utm_source=chatgpt.com "GitHub - lastmile-ai/mcp-agent: Build effective agents using Model Context Protocol and simple workflow patterns · GitHub"
[14]: https://github.com/langchain-ai/langgraph?utm_source=chatgpt.com "GitHub - langchain-ai/langgraph: Build resilient agents. · GitHub"
[15]: https://github.com/mastra-ai/mastra?utm_source=chatgpt.com "GitHub - mastra-ai/mastra: From the team behind Gatsby, Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. · GitHub"
[16]: https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto?utm_source=chatgpt.com "A2A/specification/a2a.proto at main · a2aproject/A2A · GitHub"
[17]: https://github.com/MikkoParkkola/mcp-gateway?utm_source=chatgpt.com "GitHub - MikkoParkkola/mcp-gateway: One endpoint in front of unlimited MCP servers and REST APIs. The agent sees a fixed ~15-tool surface however many you connect, so tool-list token cost stays flat (about 89% less on a 100-tool stack) and the savings climb as you add more. Single Rust binary. · GitHub"
[18]: https://github.com/agentic-community/mcp-gateway-registry?utm_source=chatgpt.com "GitHub - agentic-community/mcp-gateway-registry: Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynamic tool discovery, and unified access for both autonomous AI agents and AI coding assistants. Transform scattered MCP server chaos into governed, auditable tool access with Keycloak/Entra integration. · GitHub"
[19]: https://arxiv.org/abs/2608.10906?utm_source=chatgpt.com "GitSkills: A Dataset of Agent Skills on GitHub"
[20]: https://arxiv.org/abs/2607.11138?utm_source=chatgpt.com "A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery"
[21]: https://arxiv.org/abs/2606.01416?utm_source=chatgpt.com "Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems"
[22]: https://arxiv.org/abs/2608.04458?utm_source=chatgpt.com "Architectural Implications of Agentic AI Workflows"
[23]: https://github.com/NousResearch/hermes-agent/issues/19931?utm_source=chatgpt.com "Architecture: specialist worker lanes under Hermes Kanban orchestration · Issue #19931 · NousResearch/hermes-agent"

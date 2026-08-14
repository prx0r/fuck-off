# SPEC-12 — AGENT HARNESS SURVEY (maestro, arcan, herdr, weft, looms, ...)

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/githubagent2`
**Scope:** agent-harness repos + the "Tom will probably love" ranking. Two red-circle discoveries:
**Herdr** (agents propose immutable evidence while deterministic reducers own lifecycle — the cleanest
formulation of our epistemic promotion) and the **Dicklesworthstone flywheel** (tiny, brutally useful,
composable tools instead of an Agent OS). Plus engineering-taste tools (uv, mise, nushell). Note: the
cloned `ghuntley/loom` is proprietary/design-mine; `valkor-ai/loom` (Apache-2.0) is the open one.

---

Yes. **Loom is a much better taste signal than “find me agent frameworks.”** Huntley’s repo is interesting because it exposes the machinery: Rust workspace, explicit core state machine, provider abstraction, tool registry, persisted threads, remote execution via Kubernetes, auth/ABAC, analytics, feature flags, and a server-side LLM proxy. It is also explicitly experimental and proprietary, so it is a **design mine, not code you should transplant**.

The deeper search turned up a much stronger set of projects I had missed.

## 1. `maestro` — this is extremely Pāṭala-compatible

[https://github.com/ReinaMacCredy/maestro](https://github.com/ReinaMacCredy/maestro)

This may be the biggest miss from the previous passes.

It is a **single Rust binary** that gives Claude Code, Codex and CI a shared durable task system, verdict ledger and state store. Crucially, its canonical operational state is plain repo-local files under `.maestro/`; there is no daemon or cloud service required. ([GitHub][1])

Its philosophy is basically:

```text
human intent
     ↓
durable task
     ↓
agent attempt
     ↓
artifact
     ↓
verdict / proof
     ↓
accepted work
```

That is very close to your emerging:

```text
Task ≠ Run ≠ Artifact ≠ Review
```

I'd put this beside **Hermes + Agetor + Vouch** and compare schemas.

**Clone: absolutely.**

---

## 2. `Arcan` — tiny agent kernel, event sourcing done correctly

[https://github.com/broomva/arcan](https://github.com/broomva/arcan)

This is exactly the kind of personal architecture you asked for.

Arcan describes itself as the kernel of a “Life Agent OS” and uses:

* Rust
* event-sourced state
* typed streaming events
* replayable sessions
* append-only event repositories
* sandbox/guardrail layer
* provider abstraction
* daemon + SSE

Its crates explicitly separate runtime contracts, harness, store, provider and daemon. ([GitHub][2])

Conceptually:

```text
Command
   ↓
Runtime
   ↓
Event
   ↓
append-only log
   ↓
Reducer
   ↓
State
```

That is a much cleaner foundation than continuously mutating opaque agent JSON.

**This belongs in your Task/Run/Event research immediately.**

---

# 3. `herdr-workflow` — zero stars, potentially brilliant

[https://github.com/XiaoConstantine/herdr-workflow](https://github.com/XiaoConstantine/herdr-workflow)

This is exactly why searching personal repos matters.

The project is an **event-sourced workflow runtime for adversarially reviewed software delivery**. Its defining principle is that agents do **not** advance workflow state directly. They submit authenticated reports concerning immutable artifacts; deterministic reducers and committed events decide what state transitions occur. ([GitHub][3])

Read that again because it's remarkably Pāṭala:

```text
AGENT
 cannot mutate truth

AGENT
 proposes report

RUNTIME
 verifies artifact

EVENT
 is committed

REDUCER
 advances state
```

That is almost the cleanest implementation philosophy we've found for your gate.

It has essentially no adoption yet. Doesn't matter.

**Clone. Read the workflow spec.**

---

# 4. `agent-loom` — someone independently discovered the “missing middle”

[https://github.com/z3z1ma/agent-loom](https://github.com/z3z1ma/agent-loom)

This is not Huntley's Loom.

Its central argument is excellent:

```text
prompt → patch
```

is structurally too thin.

It instead forces:

```text
prompt
→ route
→ research/spec/plan/ticket
→ patch
→ evidence
→ critique
→ promotion
→ closure
```

with each intermediate product becoming a typed artifact. The author explicitly frames it as forcing agents to externalize assumptions, claims, constraints, evidence, critique and decisions rather than letting everything disappear into chat history. ([GitHub][4])

This is almost literally the software-engineering analogue of Pāṭala's:

```text
source
→ passage
→ proposition
→ evidence
→ argument
→ review
→ adjudication
```

**Very high-signal architecture mine.**

---

# 5. `Weft` — agent fleet as local operating system

[https://github.com/SoloJiang/weft](https://github.com/SoloJiang/weft)

This is more mature/productized than Herdr.

A Rust backend owns:

* SQLite operational state
* Git worktrees
* agent processes
* MCP bus
* permissions/questions bridge
* skill sources
* encrypted backups
* sidecar observation

while Claude Code, Codex and OpenCode remain replaceable native worker processes. ([GitHub][5])

The pattern is excellent:

```text
WEFT
owns:
tasks
worktrees
state
coordination

CODING AGENT
owns:
one execution attempt
```

Exactly our Hermes conclusion.

Don't necessarily adopt Weft.

**Study its worker-process boundary and worktree lifecycle.**

---

# 6. VTCode — surprisingly sophisticated Rust harness

[https://github.com/vinhnx/VTCode](https://github.com/vinhnx/VTCode)

This one is much more ambitious than the usual personal coding-agent clone.

It has:

* OS-native sandboxing
* provider governance
* MCP client/server
* A2A
* ATIF
* worktree isolation
* propose/verify agent separation
* durable loop state
* planning gates
* cost guardrails
* scheduled tasks

([GitHub][6])

The particularly interesting bit is:

```text
PLAN
  ↓
BUILD
  ↓
independent VERIFY
```

rather than allowing the same trajectory to both generate and certify its output.

This should sit beside CoEvoSkills/Vouch in your verifier research.

---

# 7. `Pie` — recurring agents with memory across invocations

[https://github.com/c4pt0r/pie](https://github.com/c4pt0r/pie)

Small/personal Rust rewrite of the Pi coding harness, but the interesting addition is **Loops**:

> stateful cron jobs whose memory persists across executions, feeding results into a human triage inbox.

It also deliberately preserves byte-identical request prefixes to exploit KV prefix caching efficiently with local models. ([GitHub][7])

Two genuinely useful ideas:

```text
recurring agent
       ↓
persistent state
       ↓
run
       ↓
inbox
       ↓
human triage
```

and:

```text
context design
is also
inference-performance design
```

That second one will matter increasingly with local models.

---

# 8. `Open Interpreter`'s current incarnation is fascinating

[https://github.com/openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)

I had mentally filed this under an older category. That's now wrong.

It has become a **harness emulation laboratory**. The current project can switch between behavior approximating different harnesses such as Claude Code, Kimi Code, Qwen Code, SWE-agent and others, while being implemented around an open coding-agent core. ([GitHub][8])

That creates an extremely interesting experimental question:

[
\text{performance}
==================

f(\text{model},\text{harness})
]

You could hold the model fixed and compare:

```text
same model
+
Claude-like harness

vs

same model
+
Kimi harness

vs

same model
+
Pāṭala harness
```

This is exactly how you should eventually test whether your infrastructure actually contributes something.

---

# 9. `learn-claude-code-rs` — perhaps the best executable textbook I've found

[https://github.com/wulawulu/learn-claude-code-rs](https://github.com/wulawulu/learn-claude-code-rs)

This is not groundbreaking because of one algorithm.

It's brilliant because each stage independently implements another agent primitive:

```text
01 agent loop
02 tools
03 planning
...
memory
subagents
permissions
hooks
background work
teams
worktrees
MCP
typed routing
```

as runnable Rust crates. ([GitHub][9])

For understanding Loom rather than cargo-culting Loom:

**read this first.**

It gives you a controlled diff between increasingly sophisticated harnesses.

---

# 10. And Huntley's own workshop is still mandatory

[https://github.com/ghuntley/how-to-build-a-coding-agent](https://github.com/ghuntley/how-to-build-a-coding-agent)

This is Huntley's minimalist counterpoint to Loom.

The entire lesson is basically:

```text
LLM
 ↓
tool call
 ↓
execute
 ↓
result
 ↓
LLM
```

and progressively adds file reading, listing, shell, editing and code search. ([GitHub][10])

You should keep **both** repositories visible:

```text
how-to-build-a-coding-agent
         ↓
minimum essence

loom
         ↓
what happens when you productionize
that essence extremely aggressively
```

That's useful architectural discipline.

---

# 11. Dicklesworthstone / Jeff Emanuel — you need to raid this entire account

[https://github.com/Dicklesworthstone](https://github.com/Dicklesworthstone)

This may be the strongest answer to “other genius work I would love.”

Instead of building one monolithic Agent OS, Jeff has built a **Unix ecosystem for agents**, where each small tool solves one operational problem. His current “Agentic Coding Flywheel” includes agent messaging, task graphs, cross-agent session search, procedural memory, destructive-command protection, multi-agent tmux control and other components. ([GitHub][11])

This design philosophy is worth studying by itself:

```text
not:

AGENT_OS.exe
does everything

but:

mail
task graph
search
memory
guard
orchestrator
review
```

Each independently composable.

That might actually be the right architecture for parts of your Pāṭala stack.

---

# 12. `mcp_agent_mail`

[https://github.com/Dicklesworthstone/mcp_agent_mail](https://github.com/Dicklesworthstone/mcp_agent_mail)

This is far more interesting than the name suggests.

It's essentially **asynchronous inter-agent coordination as durable infrastructure**:

```text
agent identity
inbox/outbox
threads
search
file reservations
audit trail
```

using MCP + SQLite + Git. ([GitHub][12])

Agents explicitly reserve files before editing them, preventing parallel workers from silently stomping on one another. ([GitHub][13])

For Hermes:

```text
Task lease
+
Agent Mail file lease
```

is a pretty clean combination.

There is now also a Rust version:

[https://github.com/Dicklesworthstone/mcp_agent_mail_rust](https://github.com/Dicklesworthstone/mcp_agent_mail_rust)

with a Git archive + SQLite indexing + robot CLI/TUI. ([GitHub][14])

---

# 13. `beads_viewer`

[https://github.com/Dicklesworthstone/beads_viewer](https://github.com/Dicklesworthstone/beads_viewer)

You have encountered this conceptually before, but I now think you should treat it as infrastructure research, not merely task UI.

It computes deterministic graph analytics such as:

* PageRank
* critical paths
* cycles
* parallel work tracks

and exposes machine-friendly JSON/robot commands specifically so agents don't have to hallucinate graph calculations themselves. ([GitHub][15])

That's a deep principle:

> **Agents should consume computed structure, not recompute deterministic facts in language.**

Same as Pāṭala:

```text
agent shouldn't guess:
"which claim is central?"

graph engine computes centrality
agent interprets it
```

---

# 14. `cass_memory_system`

[https://github.com/Dicklesworthstone/cass_memory_system](https://github.com/Dicklesworthstone/cass_memory_system)

This is more sophisticated than ordinary coding-agent memory.

It distinguishes:

```text
EPISODIC
raw previous sessions

WORKING
structured summaries

PROCEDURAL
distilled reusable rules
```

and tracks success/failure outcomes so procedural memory can evolve rather than remaining a pile of unverified summaries. ([GitHub][16])

That maps beautifully to the distinction we've been discovering:

```text
Pāṭala knowledge ≠ agent memory

but execution history
can produce procedural skills
```

Absolutely worth studying.

---

# 15. `eidetic_engine_cli`

[https://github.com/Dicklesworthstone/eidetic_engine_cli](https://github.com/Dicklesworthstone/eidetic_engine_cli)

This is possibly even more Pāṭala-ish.

It's a Rust memory substrate for coding agents storing:

```text
facts
decisions
procedural rules
anti-patterns
evidence
outcomes
```

with lexical/semantic search, graph relationships and compact provenance-bearing context packs. ([GitHub][17])

Notice the convergence:

```text
ee pack "prepare release"
    ↓
bounded context
+ evidence
+ scores
```

is basically your proposed:

```text
patala_context(
   task,
   token_budget=4000
)
```

Very worth a clone.

---

# 16. `agenttrace` — agent telemetry as build telemetry

[https://github.com/luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace)

One local Rust binary reads histories from many different coding agents and normalizes:

```text
cost
tokens
duration
tool latency
stalls
retries
failures
context pressure
```

into common reports. ([GitHub][18])

This is important because our `Run` model should eventually capture these properties **regardless of harness**.

You could adopt/imitate its importers rather than invent trace parsing for every tool.

```text
Claude trace ─┐
Codex trace   ├→ normalized RunEvents
Hermes trace  │
OpenCode trace┘
```

Very useful.

---

# 17. `A-MEM`, `remem`, etc. are good — but `harness-mem` is especially relevant to you

[https://github.com/Chachamaru127/harness-mem](https://github.com/Chachamaru127/harness-mem)

This is a project-local memory runtime specifically connecting Claude Code, Codex, Cursor **and Hermes** into one SQLite memory lane through MCP/provider adapters. ([GitHub][19])

It's another reason not to invent general agent memory prematurely.

Test this and MemOS first.

---

# 18. `Grok Build Desktop` — excellent trust-boundary architecture

[https://github.com/gallifre/grok-build-desktop](https://github.com/gallifre/grok-build-desktop)

Forget the branding.

The architecture is unusually thoughtful:

```text
UNTRUSTED WEBVIEW
      ↓ typed IPC
TRUSTED RUST HOST
      ├── permission engine
      ├── agent runtime
      ├── project service
      ├── PTY broker
      └── worktree manager
```

Model output and tool arguments are explicitly treated as untrusted, writes happen inside managed worktrees, terminal access uses leases/approval and stale state is checked before accepting changes. ([GitHub][20])

This is exactly how an agent desktop should be designed.

If you ever make the Pāṭala/Hermes control panel desktop-native, mine this heavily.

---

# 19. `mikayla-maki/loom` — capability manifests are a brilliant primitive

[https://github.com/mikayla-maki/loom](https://github.com/mikayla-maki/loom)

Another unrelated Loom.

But this one's central idea is beautiful:

```toml
agent.toml
```

describes the agent's complete capability tree.

Before execution:

```text
loom audit agent.toml
```

resolves and displays every provider, tool and permission **without invoking an LLM**. ([GitHub][21])

That suggests:

```text
Pāṭala Agent Manifest
─────────────────────
models
tools
skills
read scopes
write scopes
review authority
network access
canonical mutation rights
```

Deterministically auditable.

This is exactly what we need for role capabilities.

---

# 20. `BerriAI/self-improving-agent` — self-modification as PR rather than mutation

[https://github.com/BerriAI/self-improving-agent](https://github.com/BerriAI/self-improving-agent)

Extremely simple but the contract is right:

```text
agent detects improvement
        ↓
proposes diff
        ↓
human approves
        ↓
draft PR
```

instead of silently editing its own configuration. ([GitHub][22])

This is the production-friendly analogue of DGM.

The whole thing is basically:

> self-improvement should use your existing software-governance system.

For Pāṭala:

```text
CandidateSkill
→ patch
→ benchmark
→ review
→ accepted version
```

Exactly.

---

# 21. SICA — tiny research repo implementing actual recursive improvement

[https://github.com/MaximeRobeyns/self_improving_coding_agent](https://github.com/MaximeRobeyns/self_improving_coding_agent)

This is much closer to the scientific version.

Loop:

```text
evaluate agent
     ↓
archive results
     ↓
agent edits own code
     ↓
reevaluate
     ↓
keep/reject
```

and all execution is sandboxed. ([GitHub][23])

Before playing with DGM-scale sophistication, this is probably the simplest codebase to understand the mechanics.

---

# 22. `lemoz/darwin-godel-machine`

[https://github.com/lemoz/darwin-godel-machine](https://github.com/lemoz/darwin-godel-machine)

This is an independent implementation of the DGM idea with multi-model mutation search, sandboxed execution, population-style evolution and held-out benchmarking. ([GitHub][24])

I actually like having an independent implementation around because it's easier to distinguish:

```text
paper-essential idea
```

from:

```text
Sakana-specific engineering
```

Pattern mine both.

---

# 23. `madebywild/agent-harness` — canonical agent configuration compiler

[https://github.com/madebywild/agent-harness](https://github.com/madebywild/agent-harness)

This solves a boring problem in an elegant way.

Define once:

```text
.harness/src/
  skills/
  prompts/
  mcp/
  subagents/
  hooks/
```

then **compile** it into native configurations for Codex, Claude, Cursor, Copilot etc. ([GitHub][25])

Notice how often the compiler pattern keeps winning.

```text
canonical config
    ↓
projection compiler
    ↓
Claude config
Codex config
Cursor config
Hermes config
```

You absolutely should not maintain these manually in five formats.

---

# 24. `valkor-ai/loom` — verification harness rather than coding agent

[https://github.com/valkor-ai/loom](https://github.com/valkor-ai/loom)

Yet another Loom, but this one explicitly treats the existing coding agent as replaceable and adds:

```text
plan
→ build
→ test
→ fix
→ preview
→ handoff
```

around it, with resumable `.loom/` state and separate review/repair stages. ([GitHub][26])

This is closer to **Hermes wrapper infrastructure** than an agent.

Worth comparing with Hermes worker lanes.

---

# 25. General engineering work I think fits your taste

A slightly different category: projects where someone looked at an accepted, ugly piece of infrastructure and simply asked **“why is this so complicated?”**

### `uv`

[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

Astral collapsed a huge portion of Python environment/package/tool management into one fast Rust tool with a global cache, universal lockfile, Python management, scripts and workspaces. ([GitHub][27])

The lesson for you isn't “use uv”—you should, where appropriate.

It's:

> **replace a stack of historical abstractions with one coherent model.**

That's exactly your Pāṭala instinct.

---

### `mise`

[https://github.com/jdx/mise](https://github.com/jdx/mise)

One CLI handles:

```text
tool versions
environment variables
tasks
project bootstrap
```

from a project-local declaration. Its 2026 releases now include worktree-aware trust, sandbox defaults, task source tracking and monorepo features. ([GitHub][28])

Excellent agent infrastructure primitive because an agent can enter a repo and deterministically reproduce its tool environment.

---

### `nushell`

[https://github.com/nushell/nushell](https://github.com/nushell/nushell)

[https://github.com/nushell/nushell](https://github.com/nushell/nushell)

The genius idea is simple:

> shell pipelines should carry structured values rather than flattening everything into strings.

([GitHub][29])

This is philosophically relevant to agents.

Traditional agent tooling does:

```text
structured state
→ stringify
→ model
→ stringify
→ parser
→ structured state
```

Nushell asks why we keep throwing structure away.

Pāṭala should resist that same mistake everywhere.

---

# The pattern I'm seeing among the people/projects I think you'll like

They're usually **anti-framework**, but not anti-architecture.

They repeatedly do five things:

### 1. Make state explicit

```text
event log
artifact
manifest
task
graph
```

not hidden in process memory.

### 2. Turn implicit conventions into deterministic primitives

```text
file leases
capability manifests
worktrees
verdicts
task DAGs
context packs
```

### 3. Keep the LLM out of deterministic work

```text
PageRank → code
permission check → code
state transition → reducer
graph query → code
```

LLM does judgment.

### 4. Build small interoperable binaries

Not:

```text
AgentEnterprisePlatform
```

but:

```text
mail
memory
search
guard
task
runtime
```

### 5. Treat history as an asset

```text
sessions
runs
failures
reviews
skills
decisions
```

don't disappear.

That is exactly the architectural personality I think Pāṭala should have.

---

# My **“Tom will probably love these”** ranking from this pass

If I were dropping repos into a folder for you to open one after another:

```text
01 https://github.com/ReinaMacCredy/maestro
02 https://github.com/XiaoConstantine/herdr-workflow
03 https://github.com/broomva/arcan
04 https://github.com/z3z1ma/agent-loom

05 https://github.com/Dicklesworthstone
06 https://github.com/Dicklesworthstone/mcp_agent_mail_rust
07 https://github.com/Dicklesworthstone/beads_viewer
08 https://github.com/Dicklesworthstone/cass_memory_system
09 https://github.com/Dicklesworthstone/eidetic_engine_cli

10 https://github.com/SoloJiang/weft
11 https://github.com/vinhnx/VTCode
12 https://github.com/c4pt0r/pie

13 https://github.com/mikayla-maki/loom
14 https://github.com/madebywild/agent-harness
15 https://github.com/valkor-ai/loom

16 https://github.com/openinterpreter/openinterpreter
17 https://github.com/wulawulu/learn-claude-code-rs
18 https://github.com/ghuntley/how-to-build-a-coding-agent

19 https://github.com/BerriAI/self-improving-agent
20 https://github.com/MaximeRobeyns/self_improving_coding_agent
21 https://github.com/lemoz/darwin-godel-machine
```

Then for **general engineering taste**:

```text
https://github.com/astral-sh/uv
https://github.com/jdx/mise
https://github.com/nushell/nushell
```

The two discoveries I would put a red circle around are **Herdr** and the **Dicklesworthstone flywheel**. Herdr may give you the cleanest formulation yet of *agents proposing immutable evidence while deterministic reducers own lifecycle*. The Dicklesworthstone ecosystem shows the opposite end: what happens when you stop trying to invent an Agent OS and instead create a set of tiny, brutally useful tools that agents compose.

Those two ideas together may actually be a better foundation than Loom itself for the optimized generalized Pāṭala build.

[1]: https://github.com/ReinaMacCredy/maestro?utm_source=chatgpt.com "GitHub - ReinaMacCredy/maestro: Agent harness for codebases. Gives Claude Code, Codex, and CI a shared task system, verdict ledger, and state store so agent work is traceable and auditable. · GitHub"
[2]: https://github.com/broomva/arcan?utm_source=chatgpt.com "GitHub - broomva/arcan: Core agent runtime — event loop, LLM providers (Anthropic, OpenAI), capability system, TUI. Part of the Life Agent OS. · GitHub"
[3]: https://github.com/XiaoConstantine/herdr-workflow?utm_source=chatgpt.com "GitHub - XiaoConstantine/herdr-workflow: Composable, event-sourced multi-agent workflow framework for adversarially reviewed software delivery · GitHub"
[4]: https://github.com/z3z1ma/agent-loom?utm_source=chatgpt.com "GitHub - z3z1ma/agent-loom: Agent Loom is a repo-local truth system for coding agents · GitHub"
[5]: https://github.com/SoloJiang/weft?utm_source=chatgpt.com "GitHub - SoloJiang/weft: Local-first project management & orchestration hub for coding agents — drop in a task; Weft drives your own Claude Code, Codex & OpenCode across many repos toward merged, shipped code. · GitHub"
[6]: https://github.com/vinhnx/vtcode?utm_source=chatgpt.com "GitHub - vinhnx/VTCode: VT Code is a Rust coding agent with LLM-native code understanding, OS-native sandboxing, and multi-provider support. · GitHub"
[7]: https://github.com/c4pt0r/pie?utm_source=chatgpt.com "GitHub - c4pt0r/pie: Rust port of the pi agent harness — coding agent + LLM runtime stack · GitHub"
[8]: https://github.com/openinterpreter/openinterpreter?utm_source=chatgpt.com "GitHub - openinterpreter/openinterpreter: A coding agent for open models like Kimi K3 · GitHub"
[9]: https://github.com/wulawulu/learn-claude-code-rs?utm_source=chatgpt.com "GitHub - wulawulu/learn-claude-code-rs: Build an AI agent harness in Rust, from a minimal loop to tools, subagents, memory, teams, worktrees, MCP, and typed tool routing. · GitHub"
[10]: https://github.com/ghuntley/how-to-build-a-coding-agent?utm_source=chatgpt.com "GitHub - ghuntley/how-to-build-a-coding-agent: A workshop that teaches you how to build your own coding agent. Similar to Roo code, Cline, Amp, Cursor, Windsurf or OpenCode. · GitHub"
[11]: https://github.com/Dicklesworthstone/Dicklesworthstone?utm_source=chatgpt.com "GitHub - Dicklesworthstone/Dicklesworthstone: GitHub profile README · GitHub"
[12]: https://github.com/Dicklesworthstone/mcp_agent_mail?utm_source=chatgpt.com "GitHub - Dicklesworthstone/mcp_agent_mail: Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite · GitHub"
[13]: https://github.com/Dicklesworthstone/beads_viewer/blob/main/AGENTS.md?utm_source=chatgpt.com "beads_viewer/AGENTS.md at main · Dicklesworthstone/beads_viewer · GitHub"
[14]: https://github.com/Dicklesworthstone/mcp_agent_mail_rust?utm_source=chatgpt.com "GitHub - Dicklesworthstone/mcp_agent_mail_rust: Rust MCP server for multi-agent coordination: 34 tools, Git-backed archive, SQLite indexing, advisory file locks, and an interactive TUI console · GitHub"
[15]: https://github.com/dicklesworthstone/mcp_agent_mail?utm_source=chatgpt.com "GitHub - Dicklesworthstone/mcp_agent_mail: Asynchronous coordination layer for AI coding agents: identities, inboxes, searchable threads, and advisory file leases over FastMCP + Git + SQLite · GitHub"
[16]: https://github.com/Dicklesworthstone/cass_memory_system?utm_source=chatgpt.com "GitHub - Dicklesworthstone/cass_memory_system: Procedural memory for AI coding agents: transforms scattered session history into persistent, cross-agent memory so every agent learns from every other · GitHub"
[17]: https://github.com/Dicklesworthstone/eidetic_engine_cli?utm_source=chatgpt.com "GitHub - Dicklesworthstone/eidetic_engine_cli: Durable, local-first, explainable memory for coding agents. A Rust CLI memory substrate built on the franken-stack (Asupersync, FrankenSQLite, Frankensearch, FrankenNetworkX). · GitHub"
[18]: https://github.com/luoyuctl/agenttrace?utm_source=chatgpt.com "GitHub - luoyuctl/agenttrace: Local-first Rust TUI/CLI for auditing AI coding-agent sessions: cost, tokens, latency, failures, and health｜本地优先 Rust TUI/CLI，审计 AI 编程 Agent 会话的成本、Token、延迟、失败与健康度 · GitHub"
[19]: https://github.com/Chachamaru127/harness-mem?utm_source=chatgpt.com "GitHub - Chachamaru127/harness-mem · GitHub"
[20]: https://github.com/gallifre/grok-build-desktop?utm_source=chatgpt.com "GitHub - gallifre/grok-build-desktop: Grok Build Desktop — a local-first AI coding agent for Ollama, built with Tauri, React, Rust, and TypeScript. · GitHub"
[21]: https://github.com/mikayla-maki/loom?utm_source=chatgpt.com "GitHub - mikayla-maki/loom: A secure agent harness runtime and framework · GitHub"
[22]: https://github.com/BerriAI/self-improving-agent?utm_source=chatgpt.com "GitHub - BerriAI/self-improving-agent: Drop-in self-improvement loop for AI agents — two tools + a skill. Agent proposes a diff, human approves, draft PR opens. · GitHub"
[23]: https://github.com/MaximeRobeyns/self_improving_coding_agent?utm_source=chatgpt.com "GitHub - MaximeRobeyns/self_improving_coding_agent: A coding agent framework, that works on its own codebase. · GitHub"
[24]: https://github.com/lemoz/darwin-godel-machine?utm_source=chatgpt.com "GitHub - lemoz/darwin-godel-machine: Self-improving AI agents implementing the Darwin Gödel Machine research paper. Features multi-LLM support, sandboxed execution, population-based evolution, and comprehensive benchmarking. · GitHub"
[25]: https://github.com/madebywild/agent-harness?utm_source=chatgpt.com "GitHub - madebywild/agent-harness: Unified AI agent harness framework for Codex, Claude, Cursor and Copilot by wild · GitHub"
[26]: https://github.com/valkor-ai/loom?utm_source=chatgpt.com "GitHub - valkor-ai/loom: Loop engineering for agentic software delivery. · GitHub"
[27]: https://github.com/astral-sh/uv?utm_source=chatgpt.com "GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub"
[28]: https://github.com/jdx/mise?utm_source=chatgpt.com "GitHub - jdx/mise: dev tools, env vars, task runner · GitHub"
[29]: https://github.com/nushell/nushell?utm_source=chatgpt.com "GitHub - nushell/nushell: A new type of shell · GitHub"

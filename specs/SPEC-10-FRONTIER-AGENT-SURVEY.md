# SPEC-10 — FRONTIER AGENT SURVEY (people/labs to track + the convergence)

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/frontieragent`
**Scope:** the high-signal cluster of agent researchers/labs to watch (Sakana, Prime Intellect, Jiayi
Pan, Graham Neubig, Shunyu Yao, Charles Packer, Muhan Zhang, Omar Khattab, METR, ...) + the **convergence
thesis**: agents move from "LLM+prompt+vectordb+tools" toward a **foundation model + learned computation
policy + graph memory + deterministic environment + verifier + experience archive → self-improvement**.
The strategic implication for us: **persistent verified state (truth/evidence/execution-history/skills/
review) becomes the durable intelligence — models are disposable compute.** We are building that substrate.

---

Yes — **Sakana AI** is the name you were reaching for. And I think your instinct is right: the highest-signal feed for what you're building is not “agent framework Twitter.” It is a relatively small cluster of researchers working on **open-endedness, automated AI R&D, learned orchestration, agent RL, memory, coding-agent environments, and verifiable self-improvement**.

I’d build a watchlist roughly like this.

## 1. Sakana AI / Jeff Clune orbit — highest priority

**Lab:** [https://sakana.ai/](https://sakana.ai/)
**arXiv search:** [https://arxiv.org/search/?query=Sakana+AI&searchtype=all](https://arxiv.org/search/?query=Sakana+AI&searchtype=all)

Sakana is currently unusually aligned with your direction. Fugu treats **orchestration itself as a learned model**: the orchestrator dynamically constructs agentic scaffolds and calls heterogeneous frontier models rather than relying on a fixed hand-coded multi-agent graph. ([arXiv][1])

Read first:

**Sakana Fugu**
[https://arxiv.org/abs/2606.21228](https://arxiv.org/abs/2606.21228)

**Darwin Gödel Machine**
[https://arxiv.org/abs/2505.22954](https://arxiv.org/abs/2505.22954)

**Hyperagents**
[https://arxiv.org/abs/2603.19461](https://arxiv.org/abs/2603.19461)

The progression is striking:

```text
fixed agent
   ↓
agent edits itself
   ↓
archive of competing improved agents
   ↓
meta-agent modifies improvement process
   ↓
learned orchestration between agents/models
```

DGM autonomously modified its own coding-agent implementation and empirically retained useful variants; Hyperagents extends that toward modifying the **meta-process that generates improvements**. ([arXiv][2])

### People to track

**Jeff Clune** — probably #1 for your particular interests. Open-ended evolution, quality-diversity, AI-generating algorithms, DGM, Hyperagents.

Google Scholar/arXiv search:
[https://arxiv.org/search/?query=Jeff+Clune&searchtype=author](https://arxiv.org/search/?query=Jeff+Clune&searchtype=author)

**Jenny Zhang** — DGM + Hyperagents. She is worth following independently rather than treating DGM as merely a Sakana paper.

[https://arxiv.org/search/?query=Jenny+Zhang&searchtype=author](https://arxiv.org/search/?query=Jenny+Zhang&searchtype=author)

**Robert Lange** — evolutionary/meta-learning/open-ended systems; DGM coauthor.

[https://arxiv.org/search/?query=Robert+Lange&searchtype=author](https://arxiv.org/search/?query=Robert+Lange&searchtype=author)

**Cong Lu** — DGM/open-ended self-improvement.

[https://arxiv.org/search/?query=Cong+Lu&searchtype=author](https://arxiv.org/search/?query=Cong+Lu&searchtype=author)

**David Ha** — Sakana cofounder; long-running work on evolutionary computation, world models and unusual architectures.

[https://arxiv.org/search/?query=David+Ha&searchtype=author](https://arxiv.org/search/?query=David+Ha&searchtype=author)

This whole cluster matters because they're asking:

> How can the *system that builds agents* itself become adaptive?

rather than only:

> How can we improve the prompt?

That distinction is central to the endgame Pāṭala architecture.

---

# 2. Prime Intellect — probably the most useful open agent-RL lab for you

**Lab:** [https://www.primeintellect.ai/](https://www.primeintellect.ai/)
**GitHub:** [https://github.com/PrimeIntellect-ai](https://github.com/PrimeIntellect-ai)
**arXiv:** [https://arxiv.org/search/?query=Prime+Intellect&searchtype=all](https://arxiv.org/search/?query=Prime+Intellect&searchtype=all)

Read:

**INTELLECT-3**
[https://arxiv.org/abs/2512.16144](https://arxiv.org/abs/2512.16144)

**INTELLECT-2**
[https://arxiv.org/abs/2505.07291](https://arxiv.org/abs/2505.07291)

This is much more relevant than “they train open models.”

INTELLECT-3 exposes the **actual agentic RL stack**, including asynchronous RL, multi-turn environments and tool use; they open-sourced the training framework and environment infrastructure. ([arXiv][3])

Their conceptual stack is:

```text
Agent Environment
       ↓
trajectory
       ↓
verifier/reward
       ↓
RL
       ↓
better agent
```

That connects directly with your Pāṭala work:

```text
Pāṭala task
   ↓
Hermes run
   ↓
tool/evidence trajectory
   ↓
verification gates
   ↓
accepted/rejected outcome
   ↓
TRAINING DATA
```

This is the part I would start designing for **now**, even if you don't train anything yet.

Every clean Task→Run→Tool→Artifact→Review trace can eventually become an RL trajectory.

### People worth watching

Prime publishes quite collaboratively, but I'd particularly keep tabs on:

* **Sami Jaghouar**
* **Mika Senghaas**
* **Justus Mattern**
* **Jack Min Ong**
* **Fares Obeid**
* **Johannes Hagemann**

Their importance to you is less “celebrity researcher” and more that they are building **open infrastructure for agentic RL**, which is scarce.

---

# 3. Jiayi Pan — extremely high signal

ArXiv:

[https://arxiv.org/search/?query=Jiayi+Pan&searchtype=author](https://arxiv.org/search/?query=Jiayi+Pan&searchtype=author)

Read:

**Learning Adaptive Parallel Reasoning**
[https://arxiv.org/abs/2504.15466](https://arxiv.org/abs/2504.15466)

**SWE-Gym**
[https://arxiv.org/abs/2412.21139](https://arxiv.org/abs/2412.21139)

APR lets models learn when to `spawn()` parallel reasoning branches and when to `join()` them, instead of humans hard-coding a multi-agent topology. ([arXiv][4])

This is conceptually huge.

Current systems:

```text
researcher
 ├─ subagent A
 ├─ subagent B
 └─ subagent C
```

Human designed that.

APR asks the model to learn:

```text
should I think serially?
should I fork?
how many branches?
when should they join?
```

That links directly to Sakana Fugu.

I think the frontier eventually becomes:

[
\pi_\theta(\text{task,state})
\rightarrow
\text{computation graph}
]

rather than:

```python
spawn_agents(5)
```

SWE-Gym is equally relevant because it turns real repositories, tests and executable feedback into a training environment for coding agents and verifiers. ([arXiv][5])

---

# 4. Graham Neubig / OpenHands — study this as agent OS engineering

**Graham Neubig:**
[https://arxiv.org/search/?query=Graham+Neubig&searchtype=author](https://arxiv.org/search/?query=Graham+Neubig&searchtype=author)

**OpenHands:**
[https://github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)

Read:

[https://arxiv.org/abs/2407.16741](https://arxiv.org/abs/2407.16741)

and especially:

[https://arxiv.org/abs/2511.03690](https://arxiv.org/abs/2511.03690)

The newer OpenHands Agent SDK is more relevant than the original giant application. It explicitly addresses:

* sandboxed execution
* lifecycle control
* local↔remote execution
* multi-model routing
* tools
* memory
* APIs/UI
* security analysis

as separable primitives. ([arXiv][6])

People:

**Xingyao Wang**
[https://arxiv.org/search/?query=Xingyao+Wang&searchtype=author](https://arxiv.org/search/?query=Xingyao+Wang&searchtype=author)

**Graham Neubig**
[https://arxiv.org/search/?query=Graham+Neubig&searchtype=author](https://arxiv.org/search/?query=Graham+Neubig&searchtype=author)

For you, Xingyao Wang may actually be the more targeted person to track because he's deeply embedded in software-agent architecture and training.

---

# 5. Shunyu Yao — one of the conceptual fathers of modern agents

[https://arxiv.org/search/?query=Shunyu+Yao&searchtype=author](https://arxiv.org/search/?query=Shunyu+Yao&searchtype=author)

His earlier ReAct work is foundational, but I'd particularly keep the **τ-bench philosophy** in mind:

[https://arxiv.org/abs/2406.12045](https://arxiv.org/abs/2406.12045)

τ-bench evaluates agents against the **actual final state of an environment**, not just whether an LLM judge liked the answer. It also tests repeatability across multiple attempts. ([arXiv][7])

This aligns extremely strongly with Pāṭala:

```text
BAD EVAL

"Does this translation seem good?"
      ↓
LLM judge
```

versus:

```text
PĀṬALA EVAL

expected invariants
provenance retained?
negation retained?
evidence valid?
tests pass?
state transition legal?
      ↓
deterministic verdict
```

People around that lineage:

**Karthik Narasimhan**
[https://arxiv.org/search/?query=Karthik+Narasimhan&searchtype=author](https://arxiv.org/search/?query=Karthik+Narasimhan&searchtype=author)

**Noah Shinn**
[https://arxiv.org/search/?query=Noah+Shinn&searchtype=author](https://arxiv.org/search/?query=Noah+Shinn&searchtype=author)

---

# 6. Charles Packer / Letta — treat memory as OS research

**Charles Packer:**
[https://arxiv.org/search/?query=Charles+Packer&searchtype=author](https://arxiv.org/search/?query=Charles+Packer&searchtype=author)

**Letta:**
[https://github.com/letta-ai/letta](https://github.com/letta-ai/letta)

**MemGPT:**
[https://arxiv.org/abs/2310.08560](https://arxiv.org/abs/2310.08560)

The MemGPT idea remains one of the cleanest abstractions in agent research: model context is analogous to limited fast memory, with explicit movement between tiers and agent-controlled memory operations. ([arXiv][8])

For Pāṭala I wouldn't adopt “chat-agent memory.”

But the abstraction matters:

```text
ACTIVE CONTEXT
small / expensive

WORKING MEMORY
task/run

EPISODIC MEMORY
previous attempts

SEMANTIC MEMORY
claims/knowledge

ARCHIVAL MEMORY
sources/artifacts
```

This is much better than stuffing everything into a vector store.

---

# 7. Muhan Zhang + graph-foundation-memory cluster

One 2026 paper I would put very high on your list:

**SAGE: Self-Evolving Agentic Graph-Memory Engine**

[https://arxiv.org/abs/2605.12061](https://arxiv.org/abs/2605.12061)

People:

[https://arxiv.org/search/?query=Muhan+Zhang&searchtype=author](https://arxiv.org/search/?query=Muhan+Zhang&searchtype=author)

SAGE combines:

```text
memory writer
       ↓
evolving graph
       ↓
graph foundation model reader
       ↓
retrieval feedback
       └─────────→ writer improves memory
```

It explicitly moves beyond a static GraphRAG index toward a **reader/writer feedback loop that improves the memory structure itself**. ([arXiv][9])

That's almost directly applicable:

```text
Pāṭala compiler
     ↓
knowledge graph
     ↓
retrieval failures
     ↓
missing connection / bad projection detected
     ↓
compiler repairs projection
```

This may eventually be more important than hand-designed graph indexing.

---

# 8. SelfMem cluster — memory strategy itself becomes learned

**Paper:**
[https://arxiv.org/abs/2607.03726](https://arxiv.org/abs/2607.03726)

**Shu Yang:**
[https://arxiv.org/search/?query=Shu+Yang&searchtype=author](https://arxiv.org/search/?query=Shu+Yang&searchtype=author)

SelfMem does something conceptually similar to DGM, but specifically for memory: rather than freezing the memory representation/retrieval policy, the agent gets memory operations plus feedback and **learns/refines its memory strategy**. ([arXiv][10])

Again the direction is:

```text
2024
human designs memory

2025
agent writes memory

2026
agent optimizes how it writes/retrieves memory
```

You should architect Pāṭala so that:

```text
canonical epistemic representation
```

remains rigid/auditable,

while:

```text
retrieval strategy
context compilation strategy
memory projection strategy
```

can evolve.

---

# 9. Berkeley systems orbit — Shishir Patil / Ion Stoica / Joey Gonzalez

These people are worth following because they sit exactly where **LLMs meet real computer systems**.

**Shishir Patil:**
[https://arxiv.org/search/?query=Shishir+G.+Patil&searchtype=author](https://arxiv.org/search/?query=Shishir+G.+Patil&searchtype=author)

**Ion Stoica:**
[https://arxiv.org/search/?query=Ion+Stoica&searchtype=author](https://arxiv.org/search/?query=Ion+Stoica&searchtype=author)

**Joseph Gonzalez:**
[https://arxiv.org/search/?query=Joseph+E.+Gonzalez&searchtype=author](https://arxiv.org/search/?query=Joseph+E.+Gonzalez&searchtype=author)

This lineage includes Gorilla/tool-use work and MemGPT.

A recent example of the kind of infra/security thinking I mean is MiniScope:

[https://arxiv.org/abs/2512.11147](https://arxiv.org/abs/2512.11147)

It derives least-privilege constraints for tool-using agents rather than simply trusting the LLM with every available credential/tool. ([arXiv][11])

That's highly relevant once Pāṭala agents can actually mutate state.

Eventually:

```text
ResearchAgent:
    READ sources
    READ graph
    WRITE proposals

ReviewerAgent:
    READ proposals
    WRITE reviews

Publisher:
    ACCEPT reviewed proposal
    MUTATE canonical state
```

No generic super-agent needs every permission.

---

# 10. METR — perhaps the most important evaluation lab to watch

Site:

[https://metr.org/](https://metr.org/)

Research:

[https://metr.org/research/](https://metr.org/research/)

They aren't primarily inventing agent architectures. That's exactly why they're useful.

Their time-horizon evaluations ask roughly:

> how long a real human software task can an AI agent complete reliably?

and their task standard is now being used by outside work to create reproducible autonomous-agent evaluations. ([arXiv][12])

For your purposes:

**METR teaches you how not to fool yourself.**

If you build a scholar agent, eventually measure things like:

```text
10 min research task        95%
1 hour task                 82%
4 hour task                 47%
1 day task                  12%
```

rather than:

> “the demo looked sick.”

That's much more meaningful.

---

# 11. Geoffrey Huntley — not arXiv, but definitely keep him

[https://ghuntley.com/](https://ghuntley.com/)

Agent material:

[https://ghuntley.com/agent/](https://ghuntley.com/agent/)

GitHub:

[https://github.com/ghuntley](https://github.com/ghuntley)

He is different from Clune et al.

His value is stripping away abstraction bullshit.

His coding-agent workshop emphasizes that the basic harness is just a comparatively small loop around a powerful model, and that understanding context/tool allocation matters more than endlessly comparing branded wrappers. ([Geoffrey Huntley][13])

For your architecture, I'd use:

```text
CLUNE
"What could agents eventually become?"

PRIME
"How do we train them?"

NEUBIG
"How do we engineer robust execution?"

METR
"Can they actually do the work?"

GHUNTLEY
"Which parts are actually just 300 lines of code?"
```

That is a very useful intellectual mix.

---

# 12. Sebastian Raschka — yes, but in a different role

[https://sebastianraschka.com/](https://sebastianraschka.com/)

[https://github.com/rasbt](https://github.com/rasbt)

His 2026 material is now directly covering coding-agent harnesses, reasoning models, inference-time scaling and open-weight coding models. ([Sebastian Raschka, PhD][14])

I wouldn't put Raschka in the same category as Jeff Clune.

He's extraordinarily valuable as your **technical interpreter / reality filter**.

When a frontier lab publishes:

```text
new attention architecture
new RL technique
reasoning model
agent scaffold
```

Raschka often answers:

> What does this actually consist of?

and then implements/explains it from first principles.

That's immensely useful for someone building.

---

# 13. Omar Khattab / DSPy — optimization of programs rather than prompts

Keep:

**Omar Khattab:**
[https://arxiv.org/search/?query=Omar+Khattab&searchtype=author](https://arxiv.org/search/?query=Omar+Khattab&searchtype=author)

**DSPy:**
[https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

This research line matters conceptually because the system is treated as a **program with optimizable components**, not a handcrafted prompt pile.

For Pāṭala, eventually:

```text
extract_claim
     ↓
resolve_entity
     ↓
find_evidence
     ↓
construct_argument
     ↓
verify
```

should perhaps be optimized from evaluation traces rather than manually prompt-tuned forever.

DSPy is one of the cleanest intellectual precursors to this.

---

# 14. AI Scientist / automated science cluster

Sakana's AI Scientist is obviously relevant, but study the criticism too.

Independent evaluation found serious weaknesses in novelty judgments, experiment execution and substantiation in the earlier system. ([arXiv][15])

That failure is useful for Pāṭala because your architecture directly attacks those weaknesses:

```text
AI Scientist weakness       Pāṭala primitive

novelty errors        →     literature graph
poor citations        →     evidence contracts
bad experiment        →     verifier
hallucinated result   →     provenance
weak peer review      →     review gate
```

Automated science without epistemic infrastructure is exactly the problem you may be able to improve upon.

---

# 15. A very new thing: science memory as a durable asset

Read this August 2026 paper:

[https://arxiv.org/abs/2608.11224](https://arxiv.org/abs/2608.11224)

It treats agent memory in scientific research not simply as conversational history but as **portable scientific experience**:

* validated scripts
* protocols
* failure conditions
* executable skills
* observations

that survive model replacement. It reports fewer repeated failures and fewer tool calls as the accumulated memory improves. ([arXiv][16])

This is extremely aligned with your philosophy:

> the valuable thing shouldn't be the current agent.

It should be the accumulated:

```text
knowledge
reviews
skills
failures
benchmarks
trajectories
```

because those survive GPT-7 replacing GPT-6.

---

# 16. Self-evolving coding agents is now its own field

Very recent survey:

[https://arxiv.org/abs/2608.03392](https://arxiv.org/abs/2608.03392)

Collection:

[https://github.com/zhouhao1024/Awesome-Self-Evolving-Coding-Agents](https://github.com/zhouhao1024/Awesome-Self-Evolving-Coding-Agents)

It organizes systems according to **what evolves**:

```text
memory
skills
tools
framework
model
collaboration structure
```

and when/how that evolution happens. ([arXiv][17])

Clone that collection.

It will probably surface dozens of the personal projects you're asking me to find faster than generic GitHub search.

---

# 17. One particularly Pāṭala-ish paper: audited skill graphs

Read:

[https://arxiv.org/abs/2512.23760](https://arxiv.org/abs/2512.23760)

The proposal is:

```text
successful trajectory
      ↓
candidate reusable skill
      ↓
normalize into explicit interface
      ↓
replay
      ↓
verifier checks
      ↓
promote to skill graph
```

with audit logs rather than silently modifying the agent. ([arXiv][18])

This is **almost exactly the correct self-improvement model for you**.

Not:

```text
Agent learned something somehow.
```

But:

```text
CandidateSkill
   ↓
evidence
   ↓
benchmark
   ↓
review
   ↓
accepted Skill v7
```

Same epistemic gate as knowledge.

---

# My personal “brains to follow” ranking for this project

Not a ranking of intelligence—just **expected information value for what you're building**:

| Watch                 | Why                                         |
| --------------------- | ------------------------------------------- |
| **Jeff Clune**        | open-ended/self-improving systems           |
| **Jenny Zhang**       | DGM → Hyperagents                           |
| **Jiayi Pan**         | learned parallelism + coding-agent training |
| **Shunyu Yao**        | agent reasoning + real-world evaluation     |
| **Xingyao Wang**      | software-agent architectures/environments   |
| **Graham Neubig**     | open production-grade agents                |
| **Charles Packer**    | agent memory as systems architecture        |
| **Muhan Zhang**       | graph learning/GFM → agent memory           |
| **Shishir Patil**     | tools + systems + agent security            |
| **Omar Khattab**      | optimizable LM programs                     |
| **Sebastian Raschka** | first-principles implementation/explanation |
| **Geoffrey Huntley**  | practical harness/context engineering       |
| **Robert Lange**      | evolution/meta-learning/open-endedness      |
| **David Ha**          | unconventional/evolutionary architectures   |

And **labs/teams**:

```text
1. Sakana AI
2. Prime Intellect
3. OpenHands / Neubig group
4. Berkeley systems / Sky / Gorilla lineage
5. Princeton agent research / Shunyu Yao lineage
6. METR
7. Letta
8. Stanford NLP / DSPy
9. graph-foundation-model groups
10. Nous Research
```

I'd particularly monitor **Sakana + Prime Intellect together** because they attack complementary halves:

```text
SAKANA
How does the agent architecture itself evolve?

PRIME INTELLECT
How do we RL-train agents inside real environments?
```

---

# The convergence I think matters

All these researchers are slowly moving away from the 2024 architecture:

```text
LLM
 + prompt
 + vector database
 + tools
 = agent
```

toward:

```text
                 FOUNDATION MODEL
                        │
              learned computation policy
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   spawn agents       tools          graph memory
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                    trajectory
                        │
                 deterministic
                  environment
                        │
                        ▼
                     verifier
                        │
                  ┌─────┴─────┐
                  ▼           ▼
               success      failure
                  │           │
                  └─────┬─────┘
                        ▼
               experience archive
                        │
          ┌─────────────┼──────────────┐
          ▼             ▼              ▼
       skills         memory       architecture
          │             │              │
          └─────────────┼──────────────┘
                        ▼
                  SELF-IMPROVEMENT
```

And **this is exactly why your Pāṭala work can become much more than a knowledge graph**.

You are independently building the substrate these future systems desperately need:

```text
persistent truth
persistent evidence
persistent execution history
persistent evaluations
persistent skills
persistent failures
persistent review
```

Models become disposable compute.

The accumulated **verified state** becomes the durable intelligence.

If I were allocating research attention right now, I'd spend ~40% on the **Clune/Sakana/open-endedness lineage**, ~25% on **Prime/agent RL and environments**, ~20% on **graph-memory/retrieval**, and ~15% on practical people like **Huntley/Raschka/OpenHands** who expose what actually survives contact with implementation.

[1]: https://arxiv.org/abs/2606.21228?utm_source=chatgpt.com "Sakana Fugu Technical Report"
[2]: https://arxiv.org/abs/2505.22954?utm_source=chatgpt.com "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
[3]: https://arxiv.org/abs/2512.16144?utm_source=chatgpt.com "INTELLECT-3: Technical Report"
[4]: https://arxiv.org/abs/2504.15466?utm_source=chatgpt.com "Learning Adaptive Parallel Reasoning with Language Models"
[5]: https://arxiv.org/abs/2412.21139?utm_source=chatgpt.com "Training Software Engineering Agents and Verifiers with SWE-Gym"
[6]: https://arxiv.org/abs/2511.03690?utm_source=chatgpt.com "The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents"
[7]: https://arxiv.org/abs/2406.12045?utm_source=chatgpt.com "$τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
[8]: https://arxiv.org/abs/2310.08560?utm_source=chatgpt.com "MemGPT: Towards LLMs as Operating Systems"
[9]: https://arxiv.org/abs/2605.12061?utm_source=chatgpt.com "SAGE: A Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory"
[10]: https://arxiv.org/abs/2607.03726?utm_source=chatgpt.com "SelfMem: Self-Optimizing Memory for AI Agents"
[11]: https://arxiv.org/abs/2512.11147?utm_source=chatgpt.com "MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents"
[12]: https://arxiv.org/abs/2607.13411?utm_source=chatgpt.com "Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors"
[13]: https://ghuntley.com/agent/?utm_source=chatgpt.com "how to build a coding agent: free workshop"
[14]: https://sebastianraschka.com/blog/?utm_source=chatgpt.com "Blog and Notes | Sebastian Raschka, PhD"
[15]: https://arxiv.org/abs/2502.14297?utm_source=chatgpt.com "Evaluating Sakana's AI Scientist for Autonomous Research: Wishful Thinking or an Emerging Reality Towards 'Artificial Research Intelligence' (ARI)?"
[16]: https://arxiv.org/abs/2608.11224?utm_source=chatgpt.com "Harnessing agent memory to build lifelong AI partners for materials scientists"
[17]: https://arxiv.org/abs/2608.03392?utm_source=chatgpt.com "Self-Evolving Coding Agents"
[18]: https://arxiv.org/abs/2512.23760?utm_source=chatgpt.com "Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory"

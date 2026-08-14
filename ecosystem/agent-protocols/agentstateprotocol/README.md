# AgentStateProtocol — Git for AI Thoughts

**An open-source checkpointing and recovery protocol for AI agents**

> Save, branch, rollback, and recover an agent's state at each reasoning step. If a tool call fails or a workflow times out, restore a known-good state and keep going.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Package](https://img.shields.io/badge/PyPI-agentstateprotocol-blue.svg)](https://pypi.org/project/agentstateprotocol/)

---

## The Problem

Agents fail in the middle of multi-step chains all the time: flaky APIs, rate limits, partial state, bad tool outputs.

Without state checkpoints, one failure can force a full restart. That wastes latency, tokens, and operational time.

## The Approach

AgentStateProtocol gives your agent a versioned reasoning timeline:

| Git Concept | Agent Equivalent | Why It Helps |
|---|---|---|
| `git commit` | `agent.checkpoint()` | Save state at important points |
| `git reset` | `agent.rollback()` | Recover from bad or failed steps |
| `git branch` | `agent.branch()` | Explore alternative strategies safely |
| `git merge` | `agent.merge()` | Bring winning branch outcomes back |
| `git log` | `agent.history()` | Inspect decision history |
| `git diff` | `agent.diff()` | Compare state transitions |

---

## Quick Start

```bash
pip install agentstateprotocol
```

```python
from agentstateprotocol import AgentStateProtocol

agent = AgentStateProtocol("research-agent")

agent.checkpoint(
    state={"task": "Find best coffee shops in NYC", "stage": "parse"},
    metadata={"confidence": 0.92},
    description="Parsed request",
    logic_step="parse_input",
)

agent.checkpoint(
    state={"task": "Find best coffee shops in NYC", "stage": "search", "results": ["Devocion", "La Cabra"]},
    metadata={"confidence": 0.87},
    description="Collected candidates",
    logic_step="search",
)

# Recover if next step fails
agent.rollback()

# Try a different path
agent.branch("reviews-first")
agent.checkpoint(
    state={"task": "Find best coffee shops in NYC", "stage": "reviews"},
    logic_step="review_aggregation",
)
```

---

## Core Features

### 1. Checkpointing

```python
cp = agent.checkpoint(
    state={"reasoning": "User likely prefers quiet places with Wi-Fi"},
    metadata={"confidence": 0.88, "tokens_used": 132},
    description="Preference inference",
    logic_step="infer_preferences",
)

print(cp.id, cp.hash)
```

### 2. Rollback

```python
agent.rollback()                    # One step back
agent.rollback(steps=3)             # N steps back
agent.rollback(to_checkpoint_id="abc123")
```

### 3. Branching

```python
agent.checkpoint(state={"strategy": "stepwise"})
agent.branch("creative")
agent.checkpoint(state={"strategy": "lateral"})
agent.switch_branch("main")
```

### 4. Safe Execution with Recovery

```python
def risky_api_call(state):
    return call_external_api(state["query"])

result, cp = agent.safe_execute(
    func=risky_api_call,
    state={"query": "latest market headlines"},
    description="fetch_headlines",
    max_retries=3,
    fallback=use_cached_data,
)
```

### 5. Logic Tree Visualization

```python
print(agent.visualize_tree())
```

Example:

```
+-- ? Task accepted [de3eec5f]
    +-- ? Plan generated [3a7996fa]
        +-- ? API failed [372aabc7]
        +-- ? Cache fallback [a4d4e95e]
        +-- ? Retry succeeded [330a3284]
            +-- ? Summary complete [67f8369a]
```

### 6. Decorator Integration

```python
from agentstateprotocol.decorators import agentstateprotocol_step

@agentstateprotocol_step("analyze_data")
def analyze(state):
    return {"analysis": process(state["data"])}

result = analyze({"data": raw_data})
```

---

## Recovery Strategies

| Strategy | Best For | Behavior |
|---|---|---|
| `RetryWithBackoff` | Timeouts / transient errors | Exponential retry delays |
| `AlternativePathStrategy` | Logical dead-ends | Shift to alternate path |
| `DegradeGracefully` | Resource pressure | Return reduced-complexity output |
| `CompositeStrategy` | Complex failure modes | Chain multiple strategies |

```python
from agentstateprotocol import AgentStateProtocol
from agentstateprotocol.strategies import RetryWithBackoff, DegradeGracefully, CompositeStrategy

agent = AgentStateProtocol(
    "resilient-agent",
    recovery_strategies=[
        CompositeStrategy([
            RetryWithBackoff(base_delay=1.0, max_delay=30.0),
            DegradeGracefully(),
        ])
    ],
)
```

---

## Storage Backends

```python
from agentstateprotocol.storage import FileSystemStorage, SQLiteStorage

# File-based storage (easy to inspect)
agent = AgentStateProtocol("my-agent", storage_backend=FileSystemStorage(".agentstateprotocol"))

# SQLite storage (good for production querying)
agent = AgentStateProtocol("my-agent", storage_backend=SQLiteStorage("agent.db"))
```

---

## CLI

```bash
agentstateprotocol demo
agentstateprotocol log
agentstateprotocol tree
agentstateprotocol branches
agentstateprotocol diff abc123 def456
agentstateprotocol metrics
```

---

## Framework Integration

### LangChain-style Wrapping

```python
from agentstateprotocol.decorators import AgentStateProtocolMiddleware

middleware = AgentStateProtocolMiddleware("langchain-agent")
wrapped_chain = middleware.wrap(my_chain.invoke, "process_query")
result = wrapped_chain({"input": "Hello"})
```

### Generic Context Manager

```python
from agentstateprotocol.decorators import checkpoint_context

with checkpoint_context(description="Data processing") as ctx:
    result = process_data(data)
    ctx.state = {"result": result}
```

---

## Architecture

```
+-------------------------------------------------------------+
¦                        Your AI Agent                       ¦
+-------------------------------------------------------------¦
¦  Decorators & Middleware (agentstateprotocol.decorators)   ¦
+-------------------------------------------------------------¦
¦     Core Engine (agentstateprotocol.engine)                ¦
¦   Checkpoint | Branch | Rollback | Logic Tree              ¦
+-------------------------------------------------------------¦
¦  Recovery Strategies (agentstateprotocol.strategies)       ¦
+-------------------------------------------------------------¦
¦  Serializers (agentstateprotocol.serializers)              ¦
+-------------------------------------------------------------¦
¦  Storage: FileSystem | SQLite | Memory                     ¦
+-------------------------------------------------------------+
```

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE).

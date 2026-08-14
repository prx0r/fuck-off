"""lib/agent_delivery.py — the clean agent-delivery layer (loom + maestro + arcan + herdr).

Incorporates the best agent-cleanliness + safety mechanisms from the cloned harnesses:
  loom      — stateful delivery loop (resumable), context routing (read task contracts, not whole repo)
  maestro   — card.yaml task contract (identity, state, governance) + verdict ledger
  arcan     — BudgetState (token/tool-call budgets, the safety governor)
  herdr     — human publication gate (agents propose, humans authorize)

The result: an agent works from a STRUCTURED task contract, spends a BUDGETED run, produces an
inspectable state, and its output only reaches canonical truth through a human gate. Clean, safe,
resumable agent delivery.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


# ---- task contract (loom request manifest / maestro card.yaml) ----
@dataclass
class TaskContract:
    task_id: str
    scope: str                    # what the agent must deliver
    acceptance: list = field(default_factory=list)   # verifiable acceptance criteria
    type: str = "task"
    state: str = "OPEN"           # OPEN | IN_PROGRESS | VERIFIED | CLOSED
    parent: Optional[str] = None  # feature-card parent (maestro)

    def contract_file(self):
        return f".agent-cards/{self.task_id}.card.yaml"


# ---- run budget (arcan BudgetState) ----
@dataclass
class RunBudget:
    tokens_used: int = 0
    max_tokens: int = 100000
    tool_calls: int = 0
    max_tool_calls: int = 50

    def within_budget(self) -> bool:
        return (self.tokens_used <= self.max_tokens
                and self.tool_calls <= self.max_tool_calls)

    def spend_tokens(self, n: int): self.tokens_used += n
    def spend_tool(self): self.tool_calls += 1


# ---- context routing (loom: read field groups / task contracts, not whole repo) ----
@dataclass
class ContextRoute:
    """A compact context bundle the agent reads instead of reloading the whole repo."""
    task_id: str
    fields: dict = field(default_factory=dict)   # e.g. {requirements, progress, repair_notes}
    def describe(self):
        return f"[context:{self.task_id}] {sorted(self.fields.keys())}"


# ---- the delivery loop (loom stateful protocol) ----
class DeliveryLoop:
    def __init__(self, contract: TaskContract, budget: Optional[RunBudget] = None):
        self.contract = contract
        self.budget = budget or RunBudget()
        self.state_store = {}       # .loom-style durable state
        self.review_records = []    # inspection trail
        self.verdict = None

    def route_context(self, *fields) -> ContextRoute:
        """Loom context routing: give the agent only the requested field groups."""
        return ContextRoute(self.contract.task_id, {f: self.state_store.get(f, "") for f in fields})

    def run(self, agent_action, field_groups=("requirements",)):
        """A budgeted, resumable agent run within a context route."""
        ctx = self.route_context(*field_groups)
        if not self.budget.within_budget():
            return {"status": "BUDGET_EXCEEDED", "context": ctx.describe()}
        self.contract.state = "IN_PROGRESS"
        self.state_store["requirements"] = self.contract.scope   # persist (resumable)
        out = agent_action(ctx)
        self.budget.spend_tool()
        self.state_store["result"] = out
        self.review_records.append({"step": "run", "state": self.contract.state})
        return {"status": "RUN_COMPLETE", "budget_left": self.budget.within_budget(),
                "context": ctx.describe()}

    def propose_for_publication(self) -> dict:
        """Herdr human gate: the agent PROPOSES; only a human authorizes publication."""
        self.contract.state = "PENDING_PUBLICATION"
        self.verdict = {"gate": "BLOCKED", "reason": "awaiting_human_authorization",
                        "contract": self.contract.task_id}
        self.review_records.append({"step": "publication_gate", "verdict": self.verdict})
        return self.verdict

    def human_authorize(self) -> dict:
        """The ONLY way to reach canonical truth (herdr human gate)."""
        self.contract.state = "VERIFIED"
        self.verdict = {"gate": "OPEN", "authorized_by": "human",
                        "contract": self.contract.task_id}
        self.review_records.append({"step": "authorized", "verdict": self.verdict})
        return self.verdict

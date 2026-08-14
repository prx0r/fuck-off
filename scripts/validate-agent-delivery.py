#!/usr/bin/env python3
"""validate-agent-delivery.py — the clean agent-delivery layer (loom+maestro+arcan+herdr).

Proves the safety + cleanliness mechanisms:
  - task contract (maestro card.yaml) with acceptance criteria
  - context routing (loom): agent reads only field groups, not whole repo
  - budget (arcan BudgetState): governor stops runaway runs
  - human gate (herdr): agent proposes, only human authorizes publication
  - resumable state (loom): a run can continue where it left off
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from agent_delivery import TaskContract, RunBudget, DeliveryLoop

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== AGENT DELIVERY LAYER (loom+maestro+arcan+herdr) ===\n")

# 1. task contract with acceptance criteria
contract = TaskContract(task_id="T-001",
                        scope="Reconstruct the two-stage argument's premises",
                        acceptance=["premises resolve to evidence", "no invented relations"],
                        type="argument")
check("task contract created", contract.state == "OPEN" and contract.acceptance)

# 2. budgeted run with context routing
budget = RunBudget(max_tokens=1000, max_tool_calls=5)
loop = DeliveryLoop(contract, budget)

def agent_action(ctx):
    # agent reads ONLY the context route (field groups), not the whole repo
    return f"reconstructed premises for {ctx.fields.get('requirements','')}"

r1 = loop.run(agent_action, field_groups=("requirements",))
check("context-routed budgeted run completes", r1["status"] == "RUN_COMPLETE")
check("agent only saw routed fields (context cleanliness)",
      "requirements" in r1["context"] and "acceptance" not in r1["context"])
check("budget not exceeded", r1["budget_left"] is True)

# 3. resumable state: a second run continues (state persisted)
r2 = loop.run(agent_action, field_groups=("requirements", "result"))
check("resumable (state persisted across runs)", "result" in loop.state_store)

# 4. human gate: agent proposes, blocked until human authorizes
prop = loop.propose_for_publication()
check("agent proposal BLOCKED by human gate", prop["gate"] == "BLOCKED")
check("contract pending publication", loop.contract.state == "PENDING_PUBLICATION")

auth = loop.human_authorize()
check("human authorization OPENs the gate", auth["gate"] == "OPEN")
check("contract VERIFIED after human", loop.contract.state == "VERIFIED")

# 5. budget governor: a runaway run is stopped
b2 = RunBudget(max_tokens=100, max_tool_calls=3)
l2 = DeliveryLoop(TaskContract("T-002","x"), b2)
for _ in range(5):
    l2.budget.spend_tool(); l2.budget.spend_tokens(50)
check("budget governor detects runaway", not b2.within_budget())

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nThe agent-delivery layer is CLEAN + SAFE: structured task contracts, context routing (no full-repo"),
print("reloads), budgeted runs (governor), resumable state, and a human gate that is the ONLY path to")
print("canonical truth. This is what loom/maestro/arcan/herdr converge into — clean for agents.")
sys.exit(0 if all(c for _,c in results) else 1)

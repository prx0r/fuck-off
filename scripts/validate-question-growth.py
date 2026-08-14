#!/usr/bin/env python3
"""validate-question-growth.py — the Question-Growth Engine kernel (DEV_PLAN §1.2).

Verifies: the growth tree builds edges from next_pressure; independent questions converging on the same
primitive are measured as ROBUST (not popularity); the growth loop emits learnable examples; next-pressures
resolve correctly.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from question_growth import Question, QuestionGrowthTree

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== QUESTION-GROWTH ENGINE (lib/question_growth.py) ===\n")

# ---- a real question-growth tree (from the Tantrāloka Q1 chain + pushing) ----
t = QuestionGrowthTree()
t.add(Question("Q0", "What is the fundamental nature of reality?", "ROOT",
               theorem="reality is consciousness (prakāśa)", boundary="is it a subject?",
               next_pressure="Q1: is consciousness a subject?", passages=["V2L"], primitive="prakāśa"))
t.add(Question("Q1", "Is consciousness a subject?", "CRUX",
               theorem="consciousness is self-reflexive (vimarśa)", boundary="what does it reflect?",
               next_pressure="Q2: what is the relation of reflection?", passages=["V2O", "V2P"], primitive="vimarśa"))
t.add(Question("Q2", "What is the relation of reflection?", "MECHANISM_GAP",
               theorem="reflection is not separate from the reflected", boundary="not identity",
               next_pressure="Q3: why does manifestation require reflection?", passages=["V2S"], primitive="vimarśa"))
t.add(Question("Q3", "Why does manifestation require reflection?", "SUBVERSION",
               theorem="manifestation presupposes self-awareness", boundary="is this circular?",
               next_pressure="Q4: does the argument assume the subject it proves?",
               passages=["IPK 1.5.11"], primitive="prakāśa"))
t.add(Question("Q4", "Does the argument assume the subject it proves?", "CRUX",
               theorem="the subject is not assumed but revealed", boundary="needs commentarial corpus",
               next_pressure="Q5: does this hold across traditions?", passages=["IPK 1.5.11", "V3H"], primitive="recognition"))
t.add(Question("Q5", "Does this hold across traditions?", "CRUX",
               theorem="a shared structural claim appears in many traditions", boundary="analogy != identity",
               next_pressure="", passages=["TĀ", "Spanda"], primitive="recognition"))

# ---- 1. the growth tree builds edges from next_pressure ----
t._resolve_edges()
n_edges = sum(len(c) for c in t.children.values())
check("the growth tree builds question-growth edges from next_pressure",
      n_edges >= 5, f"({n_edges} edges)")

# ---- 2. independent rediscovery = robustness (the key property) ----
# vimarśa is reached from Q1 and Q2 (2 independent); prakāśa from Q0 and Q3 (2); recognition from Q4,Q5 (2)
robust = t.robust_primitives(min_independent=2)
check("vimarśa is independently rediscovered (2 routes) -> ROBUST",
      robust.get("vimarśa", {}).get("independent_questions") == 2,
      f"({robust.get('vimarśa',{}).get('independent_questions')})")
check("a primitive reached from many directions is measured ROBUST, not just counted once",
      len(robust) == 3 and all(v["robust"] for v in robust.values()), f"({sorted(robust)})")

# ---- 3. robustness is by INDEPENDENT question, not by repetition count ----
# a primitive reached once is NOT robust
single = QuestionGrowthTree()
single.add(Question("A", "one path only", "ROOT", primitive="solitary"))
check("a primitive reached from ONE question is NOT robust",
      not single.robust_primitives(2), f"({single.robust_primitives(2)})")

# ---- 4. the growth loop emits learnable examples ----
ex = t.growth_examples()
check("each (question -> next_pressure) is a learnable growth example",
      len(ex) == 6 and all("target" in e and "input" in e for e in ex), f"({len(ex)} examples)")

# ---- 5. next_pressures resolve ----
nxt = t.next_pressures("Q0")
check("next_pressures(Q0) returns the question it forces",
      len(nxt) == 1 and nxt[0].id == "Q1", f"(-> {nxt[0].id if nxt else None})")

s = t.summary()
check("summary reports the growth tree honestly",
      s["questions"] == 6 and s["robust_primitives"] == 3, f"({s})")

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nQUESTION-GROWTH ENGINE: question-growth tree + independent-rediscovery robustness.")
print("This is the convergence-graph (SPEC-36) + the organism's question-growth loop (DEV_PLAN §1.2).")
sys.exit(0 if all(c for _,c in results) else 1)

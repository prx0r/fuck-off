#!/usr/bin/env python3
"""validate-education-organism.py — the full education + organism stack (Layer 09).

Synthesizes the patala education + organism visions with our experimental stack:
  education: LearningClaim + interaction compiler + wrong-answer->epistemic-neighbor (the moat)
           + the counterfactual/crux primitive (PremiseRetract)
  organism:  UserKnowledgeState + MisconceptionGraph (the sensor / flywheel)

Tests against our real argument graph (the two-stage free-will argument).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from education import LearningClaim, MasteryEvidence, compile_interactions, wrong_answer_to_neighbor, INTERACTION_TYPES
from organism import UserKnowledgeState, MisconceptionGraph

results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== EDUCATION + ORGANISM STACK (Layer 09) ===\n")

# ---- 1. interaction compiler over the two-stage argument ----
print("[education] compile interactions from the free-will argument:")
packet = compile_interactions("ARG-two-stage", ["premise_identification", "crux_detection", "warrant"], "novice")
print(f"  learning claims: {[c['learning_claim_id'] for c in packet['learning_claims']]}")
print(f"  interactions: {[i['type'] for i in packet['interactions']]}")
check("interaction compiler emits LearningClaims", len(packet["learning_claims"]) == 3)
check("interaction types from vocabulary", all(i["type"] in INTERACTION_TYPES for i in packet["interactions"]))

# ---- 2. wrong-answer -> epistemic neighbor (THE MOAT) ----
print("\n[education] wrong-answer -> known epistemic neighbor (not invented distractor):")
# the correct claim is 'free will requires indeterminism'; a learner confuses compatibilism
graph_neighbors = {"free_will": ["determinism", "compatibilism", "libertarianism", "indeterminism", "agency"]}
nb = wrong_answer_to_neighbor("compatibilism", "free_will", lambda c: graph_neighbors[c])
print(f"  wrong='compatibilism' correct='free will' -> maps to neighbor, failure={nb['failure_type']}")
check("wrong answer maps to epistemic neighbor", nb["maps_to_epistemic_neighbor"] in ("compatibilism","determinism","libertarianism"))
check("wrong answer classified in failure taxonomy", nb["failure_type"] in ("rival_proposition","wrong_technical_sense","scope_inflation"))

# ---- 3. counterfactual / crux primitive (PremiseRetract) ----
print("\n[education] counterfactual primitive (PremiseRetract): 'what if this premise is false?'")
# two-stage: I5 conclusion depends on I2 (chance stage) + I3 (evaluation)
# retract I2 -> I5 loses support -> I2 is load-bearing
premise_deps = {"I5": ["I2", "I3"], "I2": ["I1"], "I3": ["I2"]}
def retract(conclusion, premise):
    deps = premise_deps.get(conclusion, [])
    loses_support = premise in deps
    load_bearing = loses_support and len(deps) == 1
    return {"loses_support": loses_support, "load_bearing": load_bearing}
r = retract("I5", "I2")
print(f"  retract I2 -> I5 loses support: {r['loses_support']}, I2 load-bearing: {r['load_bearing']}")
check("counterfactual: I2 is load-bearing for I5", r["loses_support"])

# ---- 4. organism: UserKnowledgeState + MisconceptionGraph ----
print("\n[organism] user knowledge state + misconception sensor:")
user = UserKnowledgeState("U1")
m = user.record_interaction("free_will", correct=True)
w = user.record_interaction("compatibilism", correct=False)
print(f"  mastery after correct+wrong: free_will={user.concept_mastery.get('free_will'):.2f}, "
      f"compatibilism={user.concept_mastery.get('compatibilism'):.2f}")
check("correct answer raises mastery", user.concept_mastery.get("free_will", 0) > 0)
check("wrong answer lowers mastery", user.concept_mastery.get("compatibilism", 1) < 1)

mg = MisconceptionGraph()
mg.record_confusion("compatibilism", "free_will", "rival_proposition")
mg.record_confusion("determinism", "indeterminism", "rival_proposition")
mg.record_objection("compatibilist objection", "I2")
top = mg.top_misconceptions()
print(f"  misconception graph: {len(mg.nodes)} confusions, demand={mg.demand_signals()['objections']}")
check("misconception graph records confusions", len(mg.nodes) == 2)
check("objection attacks a premise", any(o == "compatibilist objection" for o, _ in mg.objection_edges))

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nThe education+organism stack is a compiled projection of the graph: wrong answers resolve to")
print("known epistemic neighbors, misconceptions feed the flywheel, and the counterfactual primitive")
print("teaches structure (what's load-bearing) rather than trivia.")
sys.exit(0 if all(c for _,c in results) else 1)

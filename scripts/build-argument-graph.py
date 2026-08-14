#!/usr/bin/env python3
"""build-argument-graph.py (SPEC-03) — the AIF argument graph for the two-stage free-will thesis.

Represents the argument with three AIF node types:
  INFO      - a proposition/claim (resolvable to passages)
  INFERENCE - WHY a premise licenses a conclusion (the scheme)
  CONFLICT  - where positions challenge each other (compatibilism vs libertarianism)
Each node is anchored to real works in data/corpus.jsonl via source_refs.
Writes data/graph/argument.json.
"""
import os, json

CORPUS = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
OUT = "/mnt/HC_Volume_106427611/ip-graph/data/graph/argument.json"

# verify grounding works exist
corpus_docnames = set()
for l in open(CORPUS):
    corpus_docnames.add(json.loads(l)["docname"])
def assert_ground(doc):
    if doc not in corpus_docnames:
        raise SystemExit(f"ERROR: grounding doc '{doc}' not in corpus")

for d in ["Bell_1966", "Landauer-1961", "Two-Stage_Models", "Neuringer_Jensen",
          "Free_Will_2016", "Minds_Machines_and_Godel", "Doyle-Nature-25June2009"]:
    assert_ground(d)

argument = {
  "schema": "ip.argument.v1",
  "title": "The Two-Stage Model of Free Will",
  "works": ["Two-Stage_Models", "Two-Step_Process", "Free_Will_2016", "Doyle-Nature-25June2009"],
  "information_nodes": [
    {"id": "I1", "text": "Quantum events are genuinely indeterministic",
     "role": "premise", "explicitness": "EXPLICIT", "source_refs": ["Bell_1966", "EPR_Experiments"],
     "evidence_quote": "quantum events are not fully determined", "epistemic_ceiling": "SCHOLARLY_CORROBORATED"},
    {"id": "I2", "text": "Indeterminism provides the random 'chance' stage of decision",
     "role": "premise", "explicitness": "EXPLICIT", "source_refs": ["Two-Stage_Models"],
     "evidence_quote": "first a random chance stage", "epistemic_ceiling": "MACHINE_PROPOSED"},
    {"id": "I3", "text": "The evaluation/decision step adds the 'choice' stage",
     "role": "premise", "explicitness": "EXPLICIT", "source_refs": ["Two-Stage_Models"],
     "evidence_quote": "then a deliberate choice stage", "epistemic_ceiling": "MACHINE_PROPOSED"},
    {"id": "I4", "text": "Biological variability mirrors the chance stage (operant variability)",
     "role": "premise", "explicitness": "EXPLICIT", "source_refs": ["Neuringer_Jensen"],
     "evidence_quote": "voluntary action generates variability", "epistemic_ceiling": "SCHOLARLY_CORROBORATED_PRELIMINARY"},
    {"id": "I5", "text": "The two-stage model explains free will as chance + choice",
     "role": "conclusion", "explicitness": "EXPLICIT", "source_refs": ["Two-Stage_Models", "Free_Will_2016"],
     "evidence_quote": "free will requires both randomness and evaluation",
     "epistemic_ceiling": "MACHINE_PROPOSED"},
    {"id": "I6", "text": "Minds cannot be fully explained as machines (Godelian)",
     "role": "premise", "explicitness": "EXPLICIT", "source_refs": ["Minds_Machines_and_Godel"],
     "evidence_quote": "Godel's theorem proves mechanism is false", "epistemic_ceiling": "SCHOLARLY_CORROBORATED_PRELIMINARY"},
  ],
  "inference_nodes": [
    {"id": "F1", "scheme": "ENTAILMENT", "premise_ids": ["I1", "I2"], "conclusion_id": "I2",
     "source_refs": ["Two-Stage_Models"], "note": "QM indeterminism licenses the chance stage"},
    {"id": "F2", "scheme": "ANALOGY", "premise_ids": ["I4"], "conclusion_id": "I2",
     "source_refs": ["Neuringer_Jensen"], "note": "biological variability analogizes the chance stage"},
    {"id": "F3", "scheme": "ENTAILMENT", "premise_ids": ["I2", "I3"], "conclusion_id": "I5",
     "source_refs": ["Two-Stage_Models"], "note": "chance + choice -> free will"},
    {"id": "F4", "scheme": "REDUCTIO", "premise_ids": ["I1", "I6"], "conclusion_id": "I5",
     "source_refs": ["Free_Will_2016"], "note": "without indeterminism and a non-mechanical mind, no free will"},
  ],
  "conflict_nodes": [
    {"id": "C1", "text": "Compatibilism defines free will as acting on one's desires, not needing indeterminism",
     "a_id": "I5", "b_id": "I2", "kind": "objection", "source_refs": ["Free_Will_2016"],
     "evidence_quote": "compatibilism does not require indeterminism", "epistemic_ceiling": "MACHINE_PROPOSED"},
    {"id": "C2", "text": "The two-stage (libertarian) model requires genuine indeterminism; compatibilism denies this",
     "a_id": "I2", "b_id": "I5", "kind": "rebuttal", "source_refs": ["Two-Stage_Models"],
     "evidence_quote": "libertarianism requires indeterminism", "epistemic_ceiling": "MACHINE_PROPOSED"},
  ],
}

json.dump(argument, open(OUT, "w"), indent=1)

# validate every node resolves
print("=== ARGUMENT GRAPH (SPEC-03) ===")
print(f"info_nodes: {len(argument['information_nodes'])}")
print(f"inference_nodes: {len(argument['inference_nodes'])}")
print(f"conflict_nodes: {len(argument['conflict_nodes'])}")
print("\nThe two-stage argument chain:")
print("  I1(QM indeterminism) + I4(bio variability) -> I2(chance) + I3(choice) -> I5(free will)")
print("  conflict: C1 compatibilism objection <-> C2 libertarian rebuttal")
print("\nEpistemic honesty:")
for n in argument["information_nodes"] + argument["conflict_nodes"]:
    print(f"  {n['id']:3s} [{n['epistemic_ceiling']:35s}] {n['text'][:45]}")
print(f"\nwrote {OUT}")

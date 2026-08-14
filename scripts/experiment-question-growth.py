#!/usr/bin/env python3
"""experiment-question-growth.py — the Question-Growth Engine (from the Pushing method).

Prima materia from research-library/pushing: the Logicvid method is a GRAPH-GROWTH machine —
decomposition loop (text → claims → definitions → dependencies → proof/boundary) + question-growth
loop (graph tension → paradox → hidden premises → branches → new graph).

The key insight (logicvid3): "the same primitive should be rediscovered independently from many
directions" — every root question starts a TREE. If we record how questions grow, we can learn the
growth. This is the What-If Machine + Co-Evolving Organism made concrete.

PushingRecord: QUESTION → DISTINCTIONS → THEOREM → BOUNDARY → NEXT_PRESSURE → PASSAGES.
"""
import json, hashlib

def PushingRecord(qid, question, shape, theorem, boundary, next_pressure, passages):
    return {"id": qid, "question": question, "question_shape": shape, "theorem": theorem,
            "boundary": boundary, "next_pressure": next_pressure, "passages": passages,
            "hash": hashlib.sha256(question.encode()).hexdigest()[:10]}

print("=== QUESTION-GROWTH ENGINE (from the Pushing method) ===\n")

# ---- a real question-growth tree (inspired by logicvid3 + the Tantraloka Q1 chain) ----
# each record: a question, its theorem, its honest boundary, and the NEXT question it forces
records = {
    "Q0": PushingRecord("Q0", "What is the fundamental nature of reality?",
        "ROOT", "reality is consciousness (prakāśa)", "not yet: is it a subject?",
        "Q1: is consciousness a subject?", ["V2L"]),
    "Q1": PushingRecord("Q1", "Is consciousness a subject?",
        "CRUX", "consciousness is self-reflexive (vimarśa)", "not yet: what does it reflect?",
        "Q2: what is the relation of reflection?", ["V2O", "V2P"]),
    "Q2": PushingRecord("Q2", "What is the relation of reflection?",
        "MECHANISM_GAP", "reflection is not separate from the reflected", "boundary: not identity",
        "Q3: why does manifestation require reflection?", ["V2S"]),
    "Q3": PushingRecord("Q3", "Why does manifestation require reflection?",
        "SUBVERSION", "manifestation presupposes self-awareness", "boundary: is this circular?",
        "Q4: does the argument assume the subject it proves?", ["IPK 1.5.11"]),
    "Q4": PushingRecord("Q4", "Does the argument assume the subject it proves?",
        "CRUX", "the subject is not assumed but revealed", "boundary: needs commentarial corpus",
        "Q5: does this hold across traditions?", ["IPK 1.5.11", "V3H"]),
}

# ---- build the growth graph: edges = question → next_pressure ----
print("[records] the pushing chain (question → theorem → boundary → next):")
for qid, r in records.items():
    print(f"  {qid:4s} [{r['question_shape']:15s}] {r['question'][:40]}")
    print(f"         → theorem: {r['theorem'][:45]}")
    print(f"         → boundary: {r['boundary'][:40]}")
    print(f"         → next: {r['next_pressure'][:45]}")

# ---- the growth graph (nodes = questions, edges = question-growth) ----
print("\n[growth graph] the question tree:")
edges = []
for qid, r in records.items():
    # next_pressure string maps to a question id (find it)
    nxt = r["next_pressure"].split(":")[0].strip()
    for k, rr in records.items():
        if rr["question"] == nxt or nxt.startswith(k):
            edges.append((qid, k))
# display the tree
from collections import defaultdict
children = defaultdict(list)
for a, b in edges: children[a].append(b)
def show(node, depth=0):
    print("  " * depth + f"├─ {node}: {records[node]['question'][:45]}")
    for c in children[node]: show(c, depth+1)
show("Q0")

# ---- the KEY property: rediscover the same primitive from multiple directions ----
print("\n[the key insight] 'the same primitive rediscovered from many directions'")
# Q1 (self-reflexivity) and Q3 (manifestation-presupposes-awareness) both reach vimarśa
vimarśa_routes = [qid for qid, r in records.items() if "reflex" in r["theorem"] or "self-aware" in r["theorem"]]
print(f"  vimarśa (self-reflexivity) reached from {len(vimarśa_routes)} independent questions:")
for q in vimarśa_routes: print(f"    {q}: {records[q]['question'][:40]}")
print(f"  → multiple convergence = robust primitive (not one fragile chain)")

# ---- the growth loop: 'if we record how questions grow, we can learn the growth' ----
print("\n[growth signal] each record is a supervised example: question + passages → theorem")
print("  → a model could predict next_pressure from (question + passages) — learnable growth")
print(f"  records: {len(records)}  question-shapes used: {sorted(set(r['question_shape'] for r in records.values()))}")

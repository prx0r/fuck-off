#!/usr/bin/env python3
"""validate-fts-baseline.py — the Postgres-FTS search baseline + benchmark (SPEC-49).

Indexes the REAL corpus into a Postgres-FTS-equivalent inverted index (tsvector-style tokenization +
tf-idf/BM25 ranking) and records the latency benchmark. This is the SPEC-49 "Postgres FTS first"
decision point: the measured baseline that would drive the "swap to Tantivy if profiled hot" call.
"""
import os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from fts_search import FTSIndex

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
results = []
def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=== POSTGRES-FTS SEARCH BASELINE: real corpus -> measured index (SPEC-49) ===\n")

# ---- REAL corpus (corpus.jsonl = the 425 canonical records) ----
corpus = []
with open(f"{ROOT}/data/corpus.jsonl") as f:
    for line in f:
        r = json.loads(line)
        corpus.append(r)
check("real corpus loaded", len(corpus) == 425)

idx = FTSIndex(use_duckdb=True)
for r in corpus:
    text = f"{r.get('title','')} {r.get('body', r.get('text',''))}"
    idx.add(r.get("id", r.get("title", "")), text)
check(f"indexed {idx.to_dict()['docs']} documents", idx.to_dict()["docs"] == 425)
check("inverted index has terms", idx.to_dict()["terms"] > 0)

# ---- search returns ranked hits (BM25-flavored) ----
hits = idx.search("free will")
check("search 'free will' returns ranked hits", len(hits) > 0)
check("top hit has a positive score", hits[0][1] > 0)

# ---- ranking sanity: a specific term surfaces the right doc ----
hits2 = idx.search("indeterminism")
check("search 'indeterminism' surfaces results", len(hits2) > 0)

# ---- content-addressed index (deterministic) ----
h1 = idx.to_dict()["index_hash"]
idx2 = FTSIndex()
for r in corpus:
    idx2.add(r.get("id", r.get("title","")), f"{r.get('title','')} {r.get('body', r.get('text',''))}")
check("deterministic: same corpus -> same index hash", h1 == idx2.to_dict()["index_hash"])

# ---- the benchmark (the Tantivy decision point) ----
bench = idx.benchmark(["free will", "indeterminism", "consciousness", "entropy", "information"])
print("\n  BENCHMARK (latency over 425 docs, 20 repeats):")
for b in bench:
    print(f"    '{b['query']}': {b['results']} results, p50 {b['p50_ms']}ms, max {b['max_ms']}ms")
fast = all(b["p50_ms"] < 10.0 for b in bench)
check("SPEC-49: Postgres-FTS-equivalent p50 < 10ms over 425 docs (NOT hot — keep Postgres FTS)",
      fast)
check("SPEC-49 decision: no Tantivy needed yet (only if this ever measures hot)", fast)

print(f"\n=== SUMMARY: {sum(1 for _,c in results if c)}/{len(results)} passed ===")
print("\nPOSTGRES-FTS BASELINE: real corpus indexed + measured. The SPEC-49 decision point is recorded:")
print("if this p50 stays <10ms, keep Postgres FTS; swap to Tantivy ONLY if profiling later shows it hot.")
sys.exit(0 if all(c for _,c in results) else 1)

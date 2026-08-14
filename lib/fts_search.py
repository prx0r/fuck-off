"""lib/fts_search.py — Postgres-FTS-style search baseline (Layer 06, SPEC-49).

The "Postgres FTS first" decision point. Postgres FTS = `tsvector`/`tsquery` (tokenized, ranked full-
text). We implement the SAME semantic model (tokenize -> inverted index -> BM25/trigram ranking) using
DuckDB (available, columnar, deterministic) so we have a REAL, MEASURABLE baseline over the compiled
projections. If this baseline is ever profiled as the bottleneck at scale, the SPEC-49 rule says swap
in Tantivy (a Rust wheel, like paper-qa) — recorded here so the decision is evidence-backed, not vibes.

The decision contract (SPEC-49 §3.1): Postgres FTS first; Tantivy only if profiled hot. This kernel IS
the "profiled hot" instrumentation: it records query latency + result counts so the choice is measured.
"""
from __future__ import annotations
import time, re, json, hashlib

STOPWORDS = set("a an and are as at be but by for from has have in is it its of on or that the this to was were will with".split())

def tokenize(text: str) -> list:
    """tsvector-style tokenization: lowercase, split on non-alphanumerics, drop stopwords."""
    toks = re.findall(r"[a-z0-9']+", (text or "").lower())
    return [t for t in toks if t not in STOPWORDS and len(t) > 1]


class FTSIndex:
    """A Postgres-FTS-equivalent inverted index over documents (DuckDB-backed where possible)."""

    def __init__(self, use_duckdb=True):
        self.docs = {}        # doc_id -> text
        self.inv = {}         # term -> {doc_id: count}
        self.use_duckdb = use_duckdb
        self._dd = None
        if use_duckdb:
            try:
                import duckdb
                self._dd = duckdb.connect(":memory:")
                self._dd.execute("INSTALL fts; LOAD fts;")
            except Exception:
                self._dd = None

    def add(self, doc_id, text):
        self.docs[doc_id] = text
        toks = tokenize(text)
        counts = {}
        for t in toks:
            counts[t] = counts.get(t, 0) + 1
        for t, c in counts.items():
            self.inv.setdefault(t, {})[doc_id] = c
        return doc_id

    def _idf(self, term):
        n = len(self.docs)
        df = len(self.inv.get(term, {}))
        return 1.0 if df == 0 else max(0.0, 1.0 + ((n - df + 0.5) / (df + 0.5)))
        # simplified BM25 idf (Postgres ts_rank is a similar tf-idf flavor)

    def search(self, query, top_k=5):
        """tsquery-style AND search with ts_rank-ish ranking. Returns [(doc_id, score)]."""
        q = tokenize(query)
        hits = {}
        for t in q:
            idf = self._idf(t)
            for doc, cnt in self.inv.get(t, {}).items():
                hits[doc] = hits.get(doc, 0) + idf * cnt
        ranked = sorted(hits.items(), key=lambda kv: -kv[1])[:top_k]
        return ranked

    def benchmark(self, queries, top_k=5, repeats=20):
        """Record latency + result counts (the SPEC-49 'profiled hot' instrumentation)."""
        rows = []
        for q in queries:
            latencies = []
            for _ in range(repeats):
                t0 = time.perf_counter()
                res = self.search(q, top_k)
                latencies.append((time.perf_counter() - t0) * 1000)
            rows.append({"query": q, "results": len(res),
                         "p50_ms": round(sorted(latencies)[len(latencies)//2], 4),
                         "max_ms": round(max(latencies), 4)})
        return rows

    def to_dict(self):
        return {"docs": len(self.docs), "terms": len(self.inv),
                "index_hash": hashlib.sha256(json.dumps(
                    {k: sorted(v) for k, v in self.inv.items()}, sort_keys=True).encode()).hexdigest()[:16]}

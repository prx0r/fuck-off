# SPEC-00 — CANONICAL INFRASTRUCTURE BUILD (the master build spec)

**Status:** CANONICAL · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/performancedoyle`
**Scope:** the end-to-end read architecture — the repo becomes a **compiler/factory producing immutable,
addressable read artifacts** served by Astro + Workers/MCP + Cloudflare edge, not a request-time
knowledge reconstructor. This is the **single governing build spec**; the numbered SPEC-01…-06 detail
individual pieces.

---

Yes. After reading the repo, I would **not rewrite this into Rust or turn it into a conventional database-backed web app**. The architecture you started is pointed in the right direction, but the implementation needs one major shift:

> **The repository should become a compiler/factory that produces immutable, independently addressable read artifacts. The website/API/MCP should mostly serve those artifacts, not reconstruct knowledge at request time.**

That gets you much closer to the actual performance frontier.

Your current repo is only 425 clean documents / 490 nodes / 6,484 edges, but it already contains a 37.8 MB monolithic `corpus.jsonl`, a 1.24 MB graph JSON and a 9.86 MB GEXF.  The corpus is small enough that almost anything works today; the decisions below are about making the architecture still work at **10k, 100k, or millions of works**.

# 1. The architecture I would actually build

```text
                           WRITE PLANE
                              │
      ┌───────────────────────┴────────────────────────┐
      │                                                │
 ingestion                                         enrichment
 Python workers                                    LLM / rules
 OCR / parsing                                     entities
 normalization                                     relations
 provenance                                        embeddings
      │                                                │
      └──────────────────┬─────────────────────────────┘
                         ▼
                  CANONICAL STORE
              PostgreSQL + object store
                         │
                         ▼
                PROJECTION COMPILER
        Python / DuckDB / Rust hot kernels
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
      HTML             JSON            Parquet
    pages/bundles    API objects       bulk data
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                         R2
                  immutable objects
                         │
                         ▼
              CLOUDFLARE EDGE CACHE
                         │
         ┌───────────────┼────────────────┐
         ▼               ▼                ▼
       HUMAN           REST/API           MCP
       Astro           Worker        Streamable HTTP
```

The important distinction is:

```text
WRITE SIDE = expensive, rich, flexible
READ SIDE  = stupid, immutable, cached
```

Your `docs/05-performance.md` already says essentially this: compute on write, immutable versioned URLs, one-request agent bundles and CDN-first reads.

I would make that principle **structural**, rather than merely documentation.

---

# 2. Biggest thing I would change: kill the monolithic canonical JSONL

Right now:

```text
data/corpus.jsonl       37.8 MB
data/graph/graph.json    1.2 MB
data/graph/doc_graph.gexf 9.8 MB
```

`corpus.jsonl` is useful as an export.

It should **not** be your fundamental unit of storage.

Instead:

```text
data/
  source/
    sha256/
      ab/
        abcdef....pdf

  canonical/
    works.parquet
    passages.parquet
    entities.parquet
    edges.parquet

  artifacts/
    works/
      ip-work-123/
        v1/
          metadata.json
          text.md
          compact.json
          evidence.json
    concepts/
      free-will/
        v7/
          index.json
          context.json
    graphs/
      v12/
        nodes.parquet
        edges.parquet
        adjacency/
          free-will.json
```

And maintain a tiny manifest:

```json
{
  "dataset": "ip-graph",
  "version": 12,
  "works": 425,
  "graph_version": 12,
  "root_hash": "...",
  "generated_at": "..."
}
```

Then:

```text
/data/corpus.jsonl
```

becomes a **generated export**.

Likewise:

```text
/data/corpus.parquet
/data/corpus.ndjson.zst
```

can be generated for researchers.

The canonical conceptual unit should be:

```text
work
passage
entity
assertion
relation
evidence
```

not "one huge JSON line dump".

---

# 3. Your current graph builder will become the first scaling failure

This is a much bigger issue than Python.

Your `build-graph.py` currently creates document similarity by comparing every document against every later document. Inside that nested loop it can additionally search through the document array to recover its concept sets.

At 425 docs: irrelevant.

At 100,000 docs:

[
\binom{100000}{2}
\approx 5,000,000,000
]

candidate document pairs.

Don't optimize that loop.

**Delete the algorithm.**

Build an inverted index:

```text
free_will      -> [doc1, doc7, doc81, ...]
determinism    -> [doc3, doc7, doc14, ...]
entropy        -> [doc9, doc82, ...]
```

Then pairs are generated only within postings for concepts actually shared.

Even better:

```text
doc_concept
-----------
doc_id
concept_id
frequency
confidence
```

with indexes:

```sql
CREATE INDEX ON doc_concept(concept_id, doc_id);
CREATE INDEX ON doc_concept(doc_id, concept_id);
```

Document similarity then becomes something like:

```sql
SELECT
    a.doc_id,
    b.doc_id,
    COUNT(*) AS shared
FROM doc_concept a
JOIN doc_concept b
  ON a.concept_id = b.concept_id
 AND a.doc_id < b.doc_id
GROUP BY a.doc_id, b.doc_id;
```

But I would still calculate this **offline**, then write the result once.

---

# 4. Make the build incremental

Your navigation currently describes a basically linear rebuild:

```text
inventory
→ clean
→ extract
→ markdown
→ classify
→ purge
→ build graph
```

That is fine for 425 docs.

Not for 100k.

Every stage needs content hashes.

For every source:

```text
source_hash
extractor_version
extraction_hash
normalizer_version
normalized_hash
ontology_version
relation_model_version
projection_version
```

Then:

```text
source unchanged?
       │
       ├─ yes → skip extraction
       │
       ▼
extraction unchanged?
       │
       ├─ yes → skip segmentation
       │
       ▼
semantic result unchanged?
       │
       └─ yes → don't invalidate read projections
```

You should eventually be able to add one PDF and see something like:

```text
1 source changed
1 extraction rebuilt
143 passages rebuilt
18 concept memberships changed
7 graph nodes invalidated
32 adjacency bundles rebuilt
21 HTML pages rebuilt
0 unrelated artifacts touched
```

That is how you scale the *factory*.

---

# 5. Content-address everything

You already intend to use SHA-256 addressing.

Make it pervasive.

Instead of:

```text
/pdf/einstein.pdf
```

internally:

```text
/blob/sha256/4f8a0...
```

Then maintain friendly aliases:

```text
/works/einstein-1905
        ↓
sha256:4f8a0...
```

This gives you:

* automatic deduplication
* immutable caching
* perfect ETags
* easy provenance
* cheap invalidation
* reproducibility
* CDN cacheability
* signed manifests later

And version URLs become:

```text
/work/einstein-1905/v4
/concept/free-will/v17
/bundle/free-will/v17
```

Those can literally be cached for a year.

---

# 6. Separate the canonical graph from graph projections

Right now `graph.json` is simultaneously conceptually close to your graph and an export format.

Don't let it become canonical.

Have:

```text
entities
relations
relation_evidence
entity_aliases
work_entities
passages
works
```

Canonical relational representation.

Then compile:

```text
graph.json
graph.gexf
graph.graphml
nodes.parquet
edges.parquet
cytoscape.json
agent adjacency bundles
visualization tiles
```

from it.

GEXF should especially remain an **export**, not runtime data. Your current GEXF is already ~9.8 MB for only 425 works.

---

# 7. There is also an ontology/schema bug I would fix immediately

Your ontology edge example has:

```json
{
  "source": "ip:concept:determinism",
  ...
  "source": {
    "work": "...",
    "author": "..."
  }
}
```

The second `source` overwrites the first in JSON.

Make the vocabulary unambiguous:

```json
{
  "id": "edge_...",
  "subject": "ip:concept:determinism",
  "predicate": "negates",
  "object": "ip:concept:free_will",

  "provenance": {
    "work_id": "...",
    "passage_id": "...",
    "agent": "...",
    "method": "..."
  },

  "evidence": [{
    "passage_id": "...",
    "quote": "...",
    "start": 1034,
    "end": 1098
  }],

  "confidence": 0.94
}
```

That is considerably more durable.

And I'd deliberately use:

```text
subject
predicate
object
```

because it maps naturally to RDF/nanopubs later without forcing your internal representation to become RDF.

---

# 8. More importantly: fix the semantics of `authored_by`

Your current builder does roughly:

```python
find_authors(text)
...
doc → authored_by → every author whose name appears
```

That isn't `authored_by`.

That's:

```text
mentions_person
```

This matters enormously once agents trust the graph.

Separate:

```text
authored_by
mentions
quotes
cites
discusses_position_of
criticizes
responds_to
```

The retrieval layer being 10 ms is worthless if the graph returns a semantic falsehood in 10 ms.

---

# 9. Frontend: Astro is actually correct here

For **this specific project**, Astro is close to ideal.

The site is fundamentally:

* works
* people
* concepts
* claims
* arguments
* evidence
* timelines
* graph views

Most of that should simply be HTML.

Astro defaults to producing HTML and only sends browser JavaScript for components explicitly hydrated as islands. ([Docs][1])

So:

```text
/work/einstein-1905     0 JS
/person/einstein        0 JS
/concept/free-will      0 JS
/relation/foo           0 JS
/passage/x              0 JS
```

Interactive islands:

```text
<Search />
<GraphExplorer />
<Compare />
<Timeline />
<ArgumentMap />
```

I would probably use:

```text
Astro
+ vanilla web components / Preact
```

rather than React everywhere.

Astro can prerender the overwhelming majority of the site at build time. ([Docs][2])

---

# 10. Deploy Astro and the API as one Cloudflare unit

Cloudflare's current Workers Static Assets architecture is particularly appropriate now: static files and Worker code can deploy together, with static assets automatically globally cached. ([Cloudflare Docs][3])

Configure roughly:

```text
/*               static asset first
/api/*           Worker
/mcp             Worker
/search          Worker
```

Do **not** run Worker middleware over every HTML request.

Cloudflare explicitly supports assets-first routing; when a matching static asset exists it can be served without invoking your Worker. ([Cloudflare Docs][4])

So your ideal hot path becomes:

```text
GET /concept/free-will
       │
       ▼
Cloudflare edge
       │
       ▼
cached HTML
       │
       ▼
user
```

Not:

```text
Cloudflare
→ Worker
→ Hyperdrive
→ Postgres
→ reconstruct concept
→ JSON
→ frontend
→ render
```

The first design wins by an absurd margin.

---

# 11. Hyperdrive: yes, but much less than your existing doc implies

Your current doctrine says:

```text
Workers + Hyperdrive + PostgreSQL
```

I agree with the components, but **Hyperdrive should only be in the dynamic fallback path**.

Hyperdrive is useful because it maintains database connection pools close to Workers and avoids repeated database handshake/authentication round trips. ([Cloudflare Docs][5]) It can also cache eligible read queries. ([Cloudflare Docs][6])

So use it for:

```text
/search?q=
/api/query
/admin/*
/review/*
/user/*
rare uncached graph query
```

Not:

```text
/work/123
/concept/free-will
/person/einstein
```

Those should already exist as bytes.

Cloudflare also recommends prepared statements in supported PostgreSQL drivers and notes that disabling type fetching can eliminate an unnecessary round trip in applicable schemas. ([Cloudflare Docs][7])

Those optimizations matter **after** cache misses reach the DB.

---

# 12. Smart Placement only for DB-heavy dynamic routes

Cloudflare Workers ordinarily execute near the visitor. Smart Placement can instead move execution closer to upstream infrastructure such as your database. ([Cloudflare Docs][8])

That's useful for:

```text
browser Phnom Penh
     ↓
CF network
     ↓
Worker near Neon DB
     ↓
Hyperdrive
     ↓
Postgres
```

for DB-heavy API calls.

But don't put the static site behind that.

Cloudflare warns that Worker-first asset handling combined with Smart Placement can move asset serving away from the user; assets-first preserves local static delivery. ([Cloudflare Docs][9])

So split it:

```text
STATIC EDGE
nearest user

DYNAMIC COMPUTE
nearest DB where appropriate
```

---

# 13. R2 should become your enormous read-oriented data lake

This is where I would put:

```text
original PDFs
images
OCR outputs
canonical source snapshots

immutable projections
agent bundles
bulk exports
Parquet
NDJSON.zst
graph snapshots
search snapshots
```

And you can put frequently accessed R2-backed responses into Cloudflare's cache. ([Cloudflare Docs][10])

Your public API can therefore frequently be:

```text
Worker:
    resolve logical ID
    fetch immutable R2 object
    return

eventually:

Cloudflare CDN:
    return cached object without Worker
```

---

# 14. Use different data formats for different jobs

This is important.

There isn't one "fastest format."

### Browser/human

```text
HTML
```

Nothing beats already-rendered semantic HTML for a content site.

### General API / LLM agents

```text
compact JSON
```

Example:

```json
{
  "id":"ip:concept:free_will",
  "label":"Free Will",
  "definition":"...",
  "relations":[...]
}
```

LLMs don't benefit from you handing them Protobuf bytes.

### Streaming corpus

```text
NDJSON
```

Excellent for incremental processing.

### Huge analytics/research downloads

```text
Parquet + Zstd
```

This should probably replace JSONL as your serious bulk analytics format.

Then:

```sql
SELECT *
FROM read_parquet('works.parquet')
WHERE theme='free_will';
```

using DuckDB without importing a database.

### Internal high-QPS service-to-service

```text
Protobuf
```

But only if you genuinely reach a bottleneck.

---

# 15. Add "compiled agent views"

This is probably the highest-value architectural thing for Pāṭala-like systems.

Don't make an agent do:

```text
get_concept
get_edges
get_sources
get_passages
get_authors
get_definitions
get_disagreements
get_citations
```

seven times.

Compile:

```text
/bundle/concept/free-will?v=17
```

returning:

```json
{
  "entity": {...},
  "definition": {...},
  "positions": [...],
  "relations": [...],
  "primary_evidence": [...],
  "important_works": [...],
  "disagreements": [...],
  "neighbors": [...],
  "provenance": {...}
}
```

Your own performance doctrine already proposes this exact principle: **one agent question ≈ one request** with bounded context bundles.

I would go much further with it.

Offer:

```text
GET /api/v1/concepts/free-will
GET /api/v1/concepts/free-will?view=compact
GET /api/v1/concepts/free-will?view=evidence
GET /api/v1/concepts/free-will?view=context&budget=8000
GET /api/v1/concepts/free-will?view=graph&depth=1
```

`budget=` is especially interesting.

The compiler can build bundles to approximate:

```text
budget=2000 tokens
budget=8000 tokens
budget=32000 tokens
```

Then agent retrieval becomes extremely efficient.

---

# 16. MCP should be a thin adapter over that API

Do not build a separate MCP knowledge system.

Make:

```text
canonical model
       │
       ├── HTML projection
       ├── REST projection
       └── MCP adapter
```

Current MCP uses JSON-RPC and Streamable HTTP as its remote transport. ([Model Context Protocol][11]) The July 2026 protocol work also moves toward stateless routing and explicit state handles, which is extremely compatible with Cloudflare-style horizontally distributed servers. ([Model Context Protocol Blog][12])

So your MCP can be essentially:

```text
POST /mcp
```

with tools such as:

```text
resolve
search
get
context
trace
compare
neighbors
evidence
```

Not 70 micro-tools.

For example:

```text
context(
  id="ip:concept:free_will",
  depth=1,
  include=["positions","evidence","relations"],
  token_budget=8000
)
```

One tool call.

That is agent performance.

---

# 17. SEO and agent retrieval should use the same canonical identifiers

Every entity gets one canonical public URL:

```text
https://example.org/concept/free-will
https://example.org/person/albert-einstein
https://example.org/work/bell-1964
```

Then corresponding representations:

```text
/concept/free-will
/concept/free-will.json
/concept/free-will.md
/api/v1/concepts/free-will
```

All share:

```text
ip:concept:free_will
```

And HTML contains structured metadata:

```html
<link rel="canonical" ...>
<script type="application/ld+json">...</script>
```

You effectively get:

```text
human graph
search-engine graph
agent graph
API graph
```

from one underlying entity model.

---

# 18. Keep Python for your factory

I strongly disagree with prematurely rewriting this pipeline in Rust.

Your Python is currently doing:

```text
filesystem work
pdftotext
JSON
regex
LLM orchestration eventually
data transformations
```

Rust will not meaningfully improve the whole-system performance of those workloads.

Use:

```text
Python      orchestration / ingestion / ML
DuckDB      analytical transformations
Polars      columnar transforms
SQL         relational transformations
```

Then profile.

Use Rust only when something becomes objectively hot:

```text
Tantivy search indexing
special parsers
massive serialization
tokenization
high-volume graph kernels
```

This agrees with the performance doctrine you already wrote.

---

# 19. The repo itself should become a monorepo with clear layers

I would restructure it toward this:

```text
fuck-off/
│
├── apps/
│   ├── web/                    # Astro
│   ├── api/                    # Cloudflare Worker
│   └── mcp/                    # MCP adapter
│
├── packages/
│   ├── schema/                 # canonical schemas
│   ├── ids/                    # ID resolver
│   ├── contracts/              # API schemas
│   └── projections/            # projection definitions
│
├── pipeline/
│   ├── ingest/
│   ├── extract/
│   ├── normalize/
│   ├── segment/
│   ├── entities/
│   ├── relations/
│   ├── graph/
│   ├── search/
│   └── publish/
│
├── ontology/
│   ├── entities.yaml
│   ├── relations.yaml
│   ├── themes.yaml
│   └── ontology.schema.json
│
├── migrations/
│
├── data/
│   ├── manifests/
│   └── fixtures/
│
├── exports/                    # generated, gitignored
│
├── benchmarks/
│   ├── api/
│   ├── build/
│   ├── search/
│   └── web/
│
├── docs/
│
└── tests/
    ├── contracts/
    ├── provenance/
    ├── graph/
    └── performance/
```

Do **not** keep 38 MB corpus dumps in Git long-term.

Store manifests in Git.

Store bulk immutable bytes in R2.

---

# 20. Canonical database schema I'd use

Something roughly like:

```text
works
-----
id
canonical_slug
title
date
author_id
source_hash
version

passages
--------
id
work_id
ordinal
text_hash
text
start_offset
end_offset

entities
--------
id
kind
canonical_label
version

entity_aliases
--------------
entity_id
alias
language

mentions
--------
passage_id
entity_id
start
end
confidence

relations
---------
id
subject_id
predicate
object_id
version
status

relation_evidence
-----------------
relation_id
passage_id
quote_start
quote_end
confidence

artifacts
---------
logical_id
version
content_hash
media_type
r2_key
byte_size
token_count

aliases
-------
logical_id
latest_version
```

That last `artifacts` table becomes extremely useful.

It lets your entire system resolve:

```text
ip:concept:free_will
       ↓
version 17
       ↓
sha256:...
       ↓
R2 object
```

---

# 21. Search architecture

Don't jump to Elasticsearch.

For your current size:

```text
Postgres FTS
+ pg_trgm
```

is more than enough.

For the static human site, you could even build the search index offline.

Eventually, if measured search latency becomes material:

```text
Tantivy
```

is where Rust starts becoming interesting.

For semantic search:

```text
embedding index
```

should be a **secondary retrieval index**, not your knowledge graph.

Keep:

```text
graph truth ≠ vector similarity
```

Very important.

---

# 22. I'd add a projection DAG

This may be the single biggest engineering improvement.

Instead of procedural scripts:

```text
run build-graph.py
```

describe artifact dependencies:

```text
source
 └─ extraction
     └─ passages
         ├─ entities
         │   └─ graph
         │       ├─ adjacency
         │       ├─ concept pages
         │       └─ agent bundles
         │
         ├─ search-index
         │
         └─ embeddings
```

Every node identified by:

```text
input hashes
code version
config version
```

Then rebuilding becomes incremental automatically.

You don't necessarily need Dagster/Airflow.

A small deterministic build engine could do this.

---

# 23. Performance budgets

I would actually put these into CI.

### Website

```text
static reading route JS       < 10 KB
ordinary content JS           ideally 0 KB
compressed HTML               < 100 KB typical
LCP                             < 1 s good-network target
CLS                             ~0
```

### Cached API

```text
Worker compute                 < 3 ms
P50 edge response             network dominated
P99                            tracked independently
```

### Agent

```text
ordinary lookup                1 HTTP request
context bundle                 1 HTTP request
MCP retrieval                  1 tool call
default response               < 4k tokens
depth                          max 2 by default
```

### Build

```text
new document should NOT
rebuild entire corpus
```

That one should be a hard requirement.

---

# 24. So the end-state stack I'd choose

## Humans

```text
Astro
Preact islands only where needed
semantic HTML
JSON-LD
Cloudflare Workers Static Assets
Cloudflare CDN
```

Astro's islands architecture specifically exists to avoid shipping unnecessary client JavaScript. ([Docs][1])

## Public machine reads

```text
precompiled compact JSON
R2
Cloudflare CDN
ETags
immutable URLs
```

## Dynamic API

```text
Cloudflare Workers / TypeScript
Zod/TypeBox generated schemas
Hyperdrive
PostgreSQL
```

Hyperdrive provides connection pooling and query caching, but it should sit behind cache misses rather than being your default retrieval layer. ([Cloudflare Docs][5])

## MCP

```text
same Worker platform
Streamable HTTP
stateless tools
API/projection functions reused internally
```

Current MCP is explicitly moving toward stateless, routable HTTP operation, which fits this architecture extremely well. ([Model Context Protocol Blog][12])

## Factory

```text
Python
DuckDB
Polars
LLM workers
Queues
```

## Search

```text
Postgres first
Tantivy when measured
```

## Storage

```text
Postgres     structured canonical state
R2           blobs + immutable projections
Parquet      bulk analytical publication
Git          schemas/code/manifests, NOT corpus
```

## Rust

```text
only measured hot kernels
```

---

# 25. Priority order for *this exact repo*

I would **not** start by building Astro.

I would do this order:

1. **Fix the canonical schemas** — especially `subject/predicate/object`, provenance, passages, evidence IDs and the current `authored_by` semantic problem. The ontology's duplicate `source` field should be fixed now.
2. **Introduce stable IDs + SHA-256 identities** for works, passages, entities, relations and artifacts.
3. **Replace full rebuild semantics with incremental hashes.**
4. **Replace the O(n²)/worse document graph build with inverted indexes.**
5. **Make JSONL an export, not the canonical database.**
6. Add `works/passages/entities/relations/evidence` relational tables.
7. Build the **projection compiler**.
8. Generate per-entity static JSON/Markdown/HTML/bundles.
9. Push immutable projections to R2.
10. Build Astro over those projections.
11. Put Workers only on `/api`, `/search`, `/mcp`, auth/review routes.
12. Add Hyperdrive only where requests genuinely need PostgreSQL.
13. Add compact agent bundles and MCP.
14. Add Parquet bulk exports.
15. Benchmark.
16. **Only then** decide whether any Python kernel deserves Rust.

The key insight is that your existing performance doctrine is **already mostly correct**.  The implementation currently behaves like a small research prototype: one corpus file, one graph file, full rebuilds, regex ontology extraction, pairwise graph construction. The next evolution is not "pick a faster framework." It is turning this into a **knowledge compiler whose output is a globally cached immutable data structure**.

That architecture should transfer almost directly into Pāṭala as well: the Information Philosopher corpus becomes a small proving ground for the same read architecture you eventually want for texts, translations, passages, arguments, evidence, scholars, timelines and educational projections.

[1]: https://v4.docs.astro.build/en/concepts/islands/?utm_source=chatgpt.com "Astro Islands | Docs"
[2]: https://v4.docs.astro.build/en/basics/rendering-modes/?utm_source=chatgpt.com "Rendering Modes | Docs"
[3]: https://developers.cloudflare.com/workers/static-assets/?utm_source=chatgpt.com "Static Assets · Cloudflare Workers docs"
[4]: https://developers.cloudflare.com/workers/static-assets/routing/worker-script/?utm_source=chatgpt.com "Worker script · Cloudflare Workers docs"
[5]: https://developers.cloudflare.com/hyperdrive/concepts/connection-pooling/?utm_source=chatgpt.com "Connection pooling · Cloudflare Hyperdrive docs"
[6]: https://developers.cloudflare.com/hyperdrive/concepts/query-caching/?utm_source=chatgpt.com "Query caching · Cloudflare Hyperdrive docs"
[7]: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/?utm_source=chatgpt.com "Connect to PostgreSQL · Cloudflare Hyperdrive docs"
[8]: https://developers.cloudflare.com/workers/configuration/placement/?utm_source=chatgpt.com "Placement · Cloudflare Workers docs"
[9]: https://developers.cloudflare.com/workers/static-assets/binding/?utm_source=chatgpt.com "Configuration and Bindings · Cloudflare Workers docs"
[10]: https://developers.cloudflare.com/r2/examples/cache-api/?utm_source=chatgpt.com "Use the Cache API · Cloudflare R2 docs"
[11]: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports?utm_source=chatgpt.com "Transports - Model Context Protocol"
[12]: https://blog.modelcontextprotocol.io/posts/2026-07-28/?utm_source=chatgpt.com "The 2026-07-28 Specification | Model Context Protocol Blog"

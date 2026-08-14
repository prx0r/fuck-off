# SPEC-07 — ECOSYSTEM SURVEY (third-party repos, datasets, benchmarks)

**Status:** CANONICAL REFERENCE · **Owner:** ip-graph · **Imported from:** R2 `sanskritree/gitclone`
**Scope:** what to steal / ingest / benchmark from the open knowledge-graph ecosystem. Split into
tiers (Tier 0 clone-first, Tier 1 datasets, Tier 2 architecture, weird personal gold). The highest-value
finding: **build 5 adapters** (`import_openalex` `import_s2orc` `import_scifact` `import_xaif`
`import_eleutheria`) into ONE common target (`ExternalRecord → CanonicalCandidate → Validation →
Proposal → AcceptedObject`) so the 425-doc Doyle corpus + EleutherIA + SciFact + xAIF all enter the same
engine.

---

Yes. There is enough existing work here that you should **not** build the Western/scientific epistemic graph from scratch.

After going past the obvious GraphRAG repos, I’d split what I found into three categories:

* **steal architecture/code**
* **ingest structured datasets**
* **use as interoperability targets / benchmarks**

The genuinely interesting repos are often small personal projects rather than the famous GraphRAG stacks.

## Tier 0 — clone these first

### 1. RKA — closest thing I found to your research-state architecture

[https://github.com/infinitywings/rka](https://github.com/infinitywings/rka)

This is extremely relevant. RKA models a research workflow as:

```text
literature
→ decisions
→ missions
→ journal entries
→ claims
→ evidence clusters
→ research questions
```

It has claims typed as `hypothesis | evidence | method | result | observation | assumption`, explicit contradiction handling, provenance traversal, a review queue, decision supersession with staleness propagation, hierarchical research topics, FTS5 + vector retrieval, context bundles, MCP, REST, and a research-map UI. Its SQLite schema already includes `claims`, `claim_edges`, `evidence_clusters`, `topics`, `review_queue`, `entity_links`, artifacts, decisions, literature, missions and events. ([GitHub][1])

**What I would steal:**

```text
claims
claim_edges
evidence_clusters
review_queue
supersession propagation
research_map
pending_maintenance
provenance()
context()
multi_hop()
```

Especially study its idea of:

```text
claim changed
    ↓
derived knowledge becomes stale
    ↓
review queue
```

That belongs in your general Pāṭala kernel.

**Action: CLONE + CODE-READ DEEPLY.**

---

### 2. Kappa Graph — shockingly close to the epistemic weighting idea

[https://github.com/aaronsb/knowledge-graph-system](https://github.com/aaronsb/knowledge-graph-system)

Small/personal and unusually interesting.

It explicitly distinguishes retrieval from **epistemic strength**. Concepts accumulate supporting and contradicting evidence; disagreement is retained rather than collapsed, provenance is maintained, and the system computes grounding strength and semantic diversity. It exposes CLI, MCP and even a FUSE filesystem over the graph. ([GitHub][2])

Its conceptual model is basically:

```text
concept
 ├── supporting evidence
 ├── contradicting evidence
 ├── provenance
 ├── grounding score
 └── diversity score
```

That maps frighteningly well onto what you've been independently developing.

I **wouldn't copy its confidence formula blindly**. But I'd absolutely read how evidence accumulation and contradiction preservation are implemented.

Potential Pāṭala equivalent:

[
G(c)=f(S_c,C_c,D_c,Q_c)
]

where:

* (S) supporting evidence
* (C) contradicting evidence
* (D) source diversity
* (Q) evidence quality

You could then distinguish:

```text
asserted confidence
model confidence
evidential support
scholarly consensus
```

rather than one mushy score.

**Action: CLONE. Mine epistemic schema + scoring.**

---

### 3. Vouch — don't rebuild the write/review gate

[https://github.com/vouchdev/vouch](https://github.com/vouchdev/vouch)

This remains one of the strongest finds.

Vouch is a git-native knowledge base where agents **propose** writes, another actor approves them, every claim requires a cited source, sources are content-hashed, and accepted changes enter an append-only audit history. It exposes the workflow through MCP and CLI. ([GitHub][3])

That's almost exactly:

```text
proposal
→ validation
→ review
→ accept/reject
→ immutable history
```

For Pāṭala/general epistemic infrastructure:

```text
AgentAssertion
    ↓
Proposal
    ↓
ValidationResult
    ↓
ReviewerDecision
    ↓
AcceptedArtifact
    ↓
Supersession chain
```

Don't clone its whole worldview.

**Do clone its gate implementation and protocol contract** and determine whether your Piece 5 can wrap/adapt it rather than recreating it.

**Action: CLONE + inspect SPEC.md and audit log code.**

---

### 4. DocGraph — underrated governance layer

[https://github.com/Detective-XH/DocGraph](https://github.com/Detective-XH/DocGraph)

This is another small repo that is much closer to your problem than generic GraphRAG.

It indexes Markdown, DOCX, HTML and PDF into SQLite, then performs explicit **drift audits**. Its research-provenance pack tracks claim IDs, source types, confidence, verification status, assessment dates, evidence links, validity periods, contradictions and supersession. It surfaces problems such as `research.unverified_evidence`, `research.competing_interpretations`, and `research.superseded_claim`. ([GitHub][4])

That's gold.

Pāṭala should eventually be capable of:

```text
patala audit

E0031 evidence missing
E0182 upstream claim superseded
E0291 translation changed after argument extraction
E0412 competing interpretation unresolved
E0781 scholarly review expired
```

Rather than merely having tests.

**Action: CLONE. Steal the drift-audit pattern.**

---

### 5. Eigenius — typed scientific knowledge with derivations

[https://github.com/eigenius/eigenius](https://github.com/eigenius/eigenius)

This is one of the most conceptually ambitious scientific ones I found.

It distinguishes knowledge into progressively stronger classes:

```text
Declared
Observed
Derived
Verified
```

and uses a typed, versioned graph with provenance and replayable derivations; its strongest verification level can incorporate formal proof systems such as Lean. ([GitHub][5])

This is **very useful conceptually** for Pāṭala.

Your corresponding hierarchy might eventually be:

```text
ASSERTED
EXTRACTED
RECONSTRUCTED
EVIDENCE_GROUNDED
HUMAN_REVIEWED
ADJUDICATED
FORMALLY_CHECKED
```

Crucially these are not simply "confidence."

They describe **how something came to be known**.

**Action: CLONE, especially schemas/types/derivation model.**

---

### 6. graphify — tiny personal project with the correct compiler mentality

[https://github.com/rhanka/graphify](https://github.com/rhanka/graphify)

This is very aligned with the architecture we were just discussing. It takes arbitrary corpora, extracts ontology-typed entities/relations, reconciles aliases across documents and treats the graph as a compiled representation of the corpus. Its flagship corpus has canonicalized entities extracted from multiple source works with provenance references and community clustering. ([GitHub][6])

Important piece:

```text
source documents
       ↓
extract
       ↓
canonicalize
       ↓
reconcile
       ↓
typed graph
```

rather than:

```text
LLM reads chunks at query time forever
```

Steal its reconciliation tests and ontology-validation concepts.

**Action: CLONE. Compare entity reconciliation directly with your pipeline.**

---

### 7. sage-wiki — graph-as-compile-output

[https://github.com/xoai/sage-wiki](https://github.com/xoai/sage-wiki)

This contains one architectural idea I strongly agree with:

> the graph is a **compile output**, not a second database that must independently remain synchronized with the documents.

It supports graph extraction/resolution over document collections and can scale from file-backed personal knowledge toward PostgreSQL. ([GitHub][7])

That maps directly onto the optimized architecture:

```text
canonical epistemic objects
         ↓
       compiler
         ↓
 ┌───────┼────────┐
 HTML   graph    API/MCP
```

instead of maintaining three competing truths.

**Action: CLONE, architecture-pattern only.**

---

### 8. Obra's knowledge-graph — excellent agent interface design

[https://github.com/obra/knowledge-graph](https://github.com/obra/knowledge-graph)

Very small, very useful.

It parses Markdown into a graph, exposes fuzzy search, semantic search, path finding, communities, bridges and centrality, and provides an MCP surface with around ten graph operations. More importantly, it has a `prove-claim` agent skill that explicitly tells the agent to decompose claims, locate relevant entities, traverse relationships, inspect evidence and report citations. ([GitHub][8])

That's approximately how your agent should use the graph:

```text
resolve
search
paths
neighbors
evidence
prove_claim
```

instead of 70 microscopically granular MCP tools.

**Action: CLONE. Steal MCP/tool granularity + prove-claim workflow.**

---

# Tier 1 — actual structured data you can ingest

This is where it gets particularly valuable.

## 9. ARG Tech AIF argument datasets

[https://github.com/arg-tech/aif-arg-datasets](https://github.com/arg-tech/aif-arg-datasets)

This is arguably the **single most important existing argument dataset source** for your Western-philosophy / argument engine.

ARG Tech maintains large public argument/debate datasets encoded using AIF/xAIF. Their representation distinguishes:

```text
L-node  locution
I-node  proposition

RA      inference/support
CA      conflict/attack
MA      rephrase

TA      transition
YA      illocutionary anchoring
```

and includes speaker/locution structure alongside proposition graphs. Their collection includes datasets such as QT30 with nearly 20k utterances and various argument-mining/shared-task corpora. ([GitHub][9])

You should build an adapter:

```text
xAIF
 ↓
Pāṭala

I-node → Proposition
RA     → Support/Inference
CA     → Attack/Defeater
MA     → Paraphrase/Equivalence
L      → SourceUtterance
```

Do **not** reshape your canonical schema around xAIF.

Make an importer/exporter.

Then immediately you have real argument graphs to test your engine against.

**Action: INGEST. High priority.**

---

## 10. SciFact — scientific Claim ↔ Evidence gold

[https://github.com/allenai/scifact](https://github.com/allenai/scifact)

This one is almost custom-made for training/testing a scientific Pāṭala.

SciFact gives:

```text
claim
evidence document
evidence sentences
SUPPORT / CONTRADICT
citation relationships
```

Its claim schema explicitly records claim text, documents containing evidence, sentence-level rationales and support/contradiction labels. ([GitHub][10])

Example mapping:

```text
SciFact claim
      ↓
Assertion

evidence[doc][sentences]
      ↓
EvidenceUse → Passage

SUPPORT
      ↓
supports

CONTRADICT
      ↓
defeats / contradicts
```

Even better, its claim/evidence annotations are CC BY 4.0 while corpus abstracts inherit the underlying S2ORC licensing. ([GitHub][11])

**Action: DOWNLOAD + INGEST IMMEDIATELY.**

This should become one of your core regression benchmarks.

---

## 11. FactKG — 108k claims with reasoning structures

[https://github.com/jiho283/FactKG](https://github.com/jiho283/FactKG)

FactKG contains roughly **108,000 natural-language claims** classified across reasoning patterns such as:

```text
one-hop
conjunction
existence
multi-hop
negation
```

with corresponding knowledge-graph evidence structures. ([GitHub][12])

You don't particularly care about its underlying DBpedia facts.

You care that it gives you a huge benchmark for:

> can `patala_context()` retrieve the graph necessary to determine this claim?

Use it to test:

```text
depth budgets
negation
multi-hop
conjunction
context bundling
```

**Action: INGEST benchmark subset, not necessarily entire KG.**

---

## 12. ExplaGraphs — argument → explanation graph

[https://github.com/swarnaHub/ExplaGraphs](https://github.com/swarnaHub/ExplaGraphs)

Each item contains:

```text
belief
argument
stance
explanation graph
```

where the explanation is itself a graph of `(concept, relation, concept)` edges. ([GitHub][13])

This is useful for something slightly different:

**testing whether an argument can be decomposed into an explicit explanatory path.**

Very relevant for education later.

```text
answer
 ↓
required conceptual chain
 ↓
student proves understanding
```

**Action: INGEST as evaluation data.**

---

## 13. SuggestBot argument/evidence data

[https://github.com/kixlab/suggestbot_dataset](https://github.com/kixlab/suggestbot_dataset)

This underrated dataset contains argument posts with annotated **verifiable sentences** and factual information that supports/refutes them. It separates posts, extracted arguments and source documents. ([GitHub][14])

Very useful mapping:

```text
argument
→ information need
→ supporting/refuting source
```

That is almost the exact process an autonomous Pāṭala scholar-agent needs to learn.

**Action: INGEST for evidence-retrieval evaluation.**

---

## 14. MSVEC — multi-domain scientific claims

[https://github.com/lamps-lab/msvec](https://github.com/lamps-lab/msvec)

Small but useful because it intentionally crosses scientific domains. It contains scientific claims paired with supporting/refuting research-paper evidence across medicine, space, geology, biology and other areas. ([GitHub][15])

Its real value isn't volume.

It's testing whether your evidence machinery generalizes outside a single domain.

**Action: INGEST regression suite.**

---

## 15. BioKGBench — agents checking claims against a KG

[https://github.com/westlake-autolab/BioKGBench](https://github.com/westlake-autolab/BioKGBench)

Excellent agent benchmark.

Tasks include:

```text
KGCheck:
claim + knowledge graph → determine support

KGQA:
question + graph → answer

SCV:
claim + scientific paper → determine support
```

with a supplied biomedical KG/corpus. ([GitHub][16])

This gives you a ready-made way to compare:

```text
vector RAG
vs
graph retrieval
vs
Pāṭala evidence bundles
```

**Action: CLONE + benchmark your MCP against it.**

---

## 16. FACTors — 118k real fact-check claims

[https://github.com/altuncu/FACTors](https://github.com/altuncu/FACTors)

This dataset aggregates **118k+ fact-checking claims** from dozens of organizations and identifies overlapping claims checked by multiple organizations. ([GitHub][17])

The overlapping-claim subset is particularly interesting.

You can model:

```text
same proposition
├─ evaluator A → judgment
├─ evaluator B → judgment
└─ evaluator C → judgment
```

which resembles scholarly adjudication.

Potential test bed for:

```text
claim identity
near-duplicate resolution
review disagreement
consensus
```

**Action: INGEST overlaps first.**

---

# Tier 1.5 — scientific corpus infrastructure: don't build this yourself

## 17. S2ORC

[https://github.com/allenai/s2orc](https://github.com/allenai/s2orc)

This is your route into actual scientific text.

S2ORC provides machine-readable scientific paper content integrated with Semantic Scholar's paper/citation graph, and current releases are distributed through Semantic Scholar's dataset APIs. ([GitHub][18])

Don't ingest all of it initially.

Use your question-first expansion strategy:

```text
consciousness
free will
causation
information
entropy
quantum foundations
```

and pull relevant papers + citations.

**Action: USE AS SCIENTIFIC RAW MATERIAL.**

---

## 18. s2orc-doc2json

[https://github.com/allenai/s2orc-doc2json](https://github.com/allenai/s2orc-doc2json)

Do **not** write your own scientific PDF parser before testing this.

It has parsers for:

```text
PDF → Grobid → structured JSON
LaTeX → JSON
JATS XML → JSON
```

and preserves scientific-document structure under the S2ORC representation. ([GitHub][19])

For your generalized ingestion layer:

```text
PDF
 ↓
GROBID/S2ORC
 ↓
sections
paragraphs
bibliography
citation spans
 ↓
Pāṭala passages
```

**Action: CLONE AND ADAPT.**

---

## 19. OpenAlex

[https://github.com/ourresearch/OpenAlex](https://github.com/ourresearch/OpenAlex)

OpenAlex is your bibliographic skeleton rather than something you should recreate. It connects works, authors, institutions, topics, venues, publishers, funders and citations across hundreds of millions of scholarly entities. ([GitHub][20])

Use:

```text
OpenAlex ID
DOI
Semantic Scholar ID
ORCID
```

as external identifiers attached to canonical Pāṭala objects.

Don't attempt to own:

```text
authors
institutions
citation metadata
venue graph
```

unless you're enriching them.

**Action: EXTERNAL BACKBONE / ID CROSSWALK.**

---

## 20. peS2o

[https://github.com/allenai/peS2o](https://github.com/allenai/peS2o)

This is a cleaned/filtered derivative of S2ORC built specifically for efficient machine processing. The current published format has simple fields such as Semantic Scholar IDs, date information, source and normalized text, with tens of millions of scientific documents available in released versions. ([GitHub][21])

Potentially easier than raw PDF ingestion for building a **large-scale semantic science prototype**.

**Action: SAMPLE, don't mirror all 40M documents.**

---

# Tier 2 — architectural things to pinch selectively

## 21. Google Knowledge Catalog / Open Knowledge Format

[https://github.com/GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog)

Very recent and unusually relevant to your agent-readable artifact idea.

Its Open Knowledge Format uses Markdown + structured frontmatter, stable source IDs, explicit generated/verified metadata, freshness state, progressive-disclosure indexes and graph-shaped links. ([GitHub][22])

Look particularly at:

```text
sources
generated
verified
status
stale_after
index.md
```

I wouldn't adopt the entire format.

But your compiled agent projections could support an OKF exporter.

**Action: ADAPTER TARGET.**

---

## 22. OBO Graphs

[https://github.com/geneontology/obographs](https://github.com/geneontology/obographs)

Very useful lesson from a mature scientific ecosystem.

OBO Graphs uses a deliberately developer-friendly core:

```json
{
  "subj": "...",
  "pred": "...",
  "obj": "..."
}
```

with optional layers of richer ontology semantics. ([GitHub][23])

This reinforces the direction I gave you earlier:

```text
canonical edge:
subject
predicate
object
```

Then attach provenance/evidence separately.

**Action: COPY DESIGN PRINCIPLE + possible exporter.**

---

## 23. TrustGraph

[https://github.com/trustgraph-ai/trustgraph](https://github.com/trustgraph-ai/trustgraph)

[https://github.com/trustgraph-ai](https://github.com/trustgraph-ai)

This is much larger than a personal project, but useful for retrieval architecture.

It emphasizes explicit graph paths, fact-level provenance and explainable context selection rather than treating arbitrary vector chunks as truth. ([GitHub][24])

Don't adopt the platform.

Inspect:

```text
context graph representation
provenance propagation
retrieval trace
```

**Action: PATTERN MINE.**

---

## 24. SubgraphRAG

[https://github.com/Graph-COM/SubgraphRAG](https://github.com/Graph-COM/SubgraphRAG)

ICLR 2025 system for retrieving small relevant subgraphs before reasoning. ([GitHub][25])

This is directly relevant to:

```text
?depth=
?budget=
context bundle
```

Your goal is not:

```text
send graph
```

but:

[
G_q = \operatorname{retrieve}(G,q,B)
]

where (B) constrains nodes/edges/tokens.

**Action: PORT retrieval evaluation ideas.**

---

## 25. GraphRAG Benchmark

[https://github.com/GraphRAG-Bench/GraphRAG-Benchmark](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)

Don't invent your own evaluation suite for whether graphs help retrieval.

This benchmark explicitly studies where graph-based RAG wins or loses versus conventional retrieval and now includes multiple GraphRAG variants. ([GitHub][26])

**Action: USE EVALUATION CASES.**

---

# Weird personal-project gold

These aren't foundational, but I would still clone several.

### 26. Personal AI Infrastructure

[https://github.com/mnott/PAI](https://github.com/mnott/PAI)

It stores temporal subject-predicate-object triples with `valid_from` / `valid_to`, content-addressed entity identities and graph-completion retrieval seeded by vector search. ([GitHub][27])

Useful pieces:

```text
temporal validity
content-addressed entity identity
vector seed → graph completion
```

**Clone.**

---

### 27. SwarmVault

[https://github.com/swarmclawai/swarmvault](https://github.com/swarmclawai/swarmvault)

[https://github.com/swarmclawai](https://github.com/swarmclawai)

Personal/local knowledge system with contradictions, open questions, research maps, source sessions and hybrid retrieval. ([GitHub][28])

Interesting for human-facing knowledge maintenance.

**Mine UX + linting.**

---

### 28. MegaMem

[https://github.com/C-Bjorn/MegaMem](https://github.com/C-Bjorn/MegaMem)

Knowledge graph + MCP built around gradual formalization rather than requiring everything to become structured immediately. ([GitHub][29])

This is a useful principle for ingestion:

```text
raw source
→ extracted candidate
→ structured candidate
→ accepted canonical object
```

not every LLM output immediately entering the graph.

---

### 29. graphGita

[https://github.com/bhaskatripathi/graphGita](https://github.com/bhaskatripathi/graphGita)

Much smaller and less rigorous than Pāṭala, but directly relevant because it attempts philosophical-text retrieval with knowledge graphs and multiple commentarial interpretations. ([GitHub][30])

I wouldn't borrow the architecture.

I'd look for mistakes you don't want to repeat:

```text
concept conflation
commentary conflation
insufficient provenance
graph == interpretation
```

**Mine as a comparison project.**

---

### 30. EleutherIA

[https://github.com/romain-girardi-eng/EleutherIA](https://github.com/romain-girardi-eng/EleutherIA)

This one deserves a serious clone because it is almost exactly your proposed **Western philosophy vertical**.

It covers ancient free-will/fate/moral-responsibility debates, combines a textual corpus, a FAIR-oriented KG, hybrid search and agentic GraphRAG, and includes ancient philosophical works plus modern reception. ([GitHub][31])

This answers your previous question decisively:

**do not start Western philosophy by re-ingesting all ancient free-will material yourself.**

First crosswalk EleutherIA.

Potential:

```text
EleutherIA entity
      ↓
external_id mapping
      ↓
Pāṭala entity

EleutherIA work
      ↓
Work

EleutherIA passage
      ↓
Passage

EleutherIA relation
      ↓
RelationCandidate
```

Then add the layer they don't give you:

```text
formal arguments
evidence use
objections
cruxes
review history
adjudication
education
```

**Action: CLONE + inspect actual data/schema before doing Western free will.**

---

# One repo that is conceptually adjacent but I'd avoid adopting wholesale

### OriginTrail DKG

[https://github.com/OriginTrail/dkg](https://github.com/OriginTrail/dkg)

It has interesting ideas around verifiable knowledge assets, cryptographic provenance and multi-agent publishing. ([GitHub][32])

But you do **not** need blockchain/decentralization to get:

```text
immutable content
hashing
signed manifests
provenance
review history
```

You can get 95% of what matters with:

```text
SHA-256
append-only events
Sigstore
signed releases
R2
Postgres
Git
```

Study the **Knowledge Asset** abstraction.

Don't import the infrastructure.

---

# Another one worth knowing: Substrate

[https://github.com/danielmiessler/Substrate](https://github.com/danielmiessler/Substrate)

Its ontology connects:

```text
problems
solutions
claims
arguments
evidence/data
people
organizations
projects
plans
values
ideas
```

([GitHub][33])

Conceptually useful because it treats knowledge as an actionable interconnected substrate rather than documents.

Again: ontology inspiration, not engine adoption.

---

# What I would actually clone tonight

I would make a research directory like:

```text
third-party/
├── epistemic/
│   ├── rka/
│   ├── kappa-graph/
│   ├── vouch/
│   ├── docgraph/
│   └── eigenius/
│
├── compilers/
│   ├── graphify/
│   ├── sage-wiki/
│   └── obra-knowledge-graph/
│
├── argumentation/
│   ├── aif-arg-datasets/
│   ├── explagraphs/
│   └── suggestbot/
│
├── science/
│   ├── scifact/
│   ├── factkg/
│   ├── biokgbench/
│   ├── msvec/
│   └── s2orc-doc2json/
│
├── philosophy/
│   ├── eleutheria/
│   └── graphgita/
│
└── retrieval/
    ├── subgraphrag/
    └── graphrag-benchmark/
```

I **would not clone Microsoft GraphRAG first**. It is useful reference infrastructure, but the niche repos above contain more of the pieces you're actually missing. Microsoft GraphRAG is fundamentally a text→entities/relations→community summaries→retrieval pipeline, and its own documentation warns that indexing can be expensive. ([GitHub][34])

---

# The integration picture is becoming surprisingly clean

What I'm seeing across these projects is this:

```text
              EXISTING WORLD
                    │
 ┌──────────────────┼─────────────────────┐
 │                  │                     │
 ▼                  ▼                     ▼
OpenAlex/S2ORC     xAIF              SciFact/FactKG
papers/citations  arguments          claim/evidence
 │                  │                     │
 └──────────────┬───┴─────────────────────┘
                ▼
        PĀṬALA IMPORT LAYER
                │
                ▼
     canonical Work / Passage
                │
                ▼
 Entity ─ Claim ─ Argument ─ Evidence
                │
        ┌───────┴─────────┐
        ▼                 ▼
     Vouch-like        RKA-like
       gate          research state
        │                 │
        └────────┬────────┘
                 ▼
          REVIEW / AUDIT
      DocGraph-like drift
                 │
                 ▼
         epistemic weights
          Kappa-like layer
                 │
                 ▼
         PROJECTION COMPILER
                 │
       ┌─────────┼──────────┐
       ▼         ▼          ▼
      Astro     API        MCP
               │
       SubgraphRAG-style
       bounded retrieval
```

This is substantially better than creating an isolated Western-philosophy graph.

## The biggest immediate opportunity

I would build **five adapters before building more ontology**:

```text
import_openalex()
import_s2orc()
import_scifact()
import_xaif()
import_eleutheria()
```

And one common target:

```text
ExternalRecord
      ↓
CanonicalCandidate
      ↓
Validation
      ↓
Proposal
      ↓
AcceptedObject
```

Then your current 425-document Information Philosopher corpus, ancient philosophy from EleutherIA, ARG Tech argument graphs and SciFact scientific evidence all enter **the same engine**.

At that point you can find out whether the Pāṭala abstractions are genuinely universal.

I suspect **that test will teach you more about the architecture than another month of designing schemas in isolation.**

[1]: https://github.com/infinitywings/rka?utm_source=chatgpt.com "GitHub - infinitywings/rka: Research Knowledge Agent — MCP server + REST API + React dashboard for AI-assisted research orchestration · GitHub"
[2]: https://github.com/aaronsb/knowledge-graph-system?utm_source=chatgpt.com "GitHub - aaronsb/knowledge-graph-system: Kappa Graph — κ(G). A semantic knowledge graph where knowledge has weight. Extracts concepts, measures grounding strength, preserves disagreement, traces everything to source. · GitHub"
[3]: https://github.com/vouchdev/vouch?utm_source=chatgpt.com "GitHub - vouchdev/vouch: A git-native, review-gated knowledge base for AI agents: they propose writes, you approve them. Every claim cites a source, every change is a diff in your repo. MCP + CLI. · GitHub"
[4]: https://github.com/Detective-XH/DocGraph?utm_source=chatgpt.com "GitHub - Detective-XH/DocGraph: Govern your documents like code. MCP server that indexes .md/.docx/.html/.pdf into a SQLite knowledge graph and runs drift audits — stale policies, conflicting research claims, superseded docs, undocumented code exports. 12 MCP tools incl. cross-reference graph, governance + provenance metadata, topic similarity. Single binary, zero runtime deps. · GitHub"
[5]: https://github.com/eigenius/eigenius?utm_source=chatgpt.com "GitHub - eigenius/eigenius: the platform monorepo (kernel, orchestration, CLI, deployment) · GitHub"
[6]: https://github.com/rhanka/graphify?utm_source=chatgpt.com "GitHub - rhanka/graphify: AI coding assistant skill (Claude Code, Codex, OpenCode, OpenClaw, Factory Droid, Trae). Turn any folder of code, docs, papers, or images into a queryable knowledge graph · GitHub"
[7]: https://github.com/xoai/sage-wiki?utm_source=chatgpt.com "GitHub - xoai/sage-wiki: sage-wiki is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph. One Go binary scales it from a personal vault to a team hub to a company knowledge graph. · GitHub"
[8]: https://github.com/obra/knowledge-graph?utm_source=chatgpt.com "GitHub - obra/knowledge-graph: Query and traverse an Obsidian vault as a knowledge graph. Semantic search, path finding, community detection — all local. Claude Code plugin included. · GitHub"
[9]: https://github.com/arg-tech/aif-arg-datasets?utm_source=chatgpt.com "GitHub - arg-tech/aif-arg-datasets: The repository containing links, descriptions and references for the datasets from ARG Tech group. · GitHub"
[10]: https://github.com/allenai/scifact/blob/master/doc/data.md?utm_source=chatgpt.com "scifact/doc/data.md at master · allenai/scifact · GitHub"
[11]: https://github.com/allenai/scifact/blob/master/LICENSE.md?utm_source=chatgpt.com "scifact/LICENSE.md at master · allenai/scifact · GitHub"
[12]: https://github.com/jiho283/FactKG?utm_source=chatgpt.com "GitHub - jiho283/FactKG: Official repository of FactKG · GitHub"
[13]: https://github.com/swarnaHub/ExplaGraphs?utm_source=chatgpt.com "GitHub - swarnaHub/ExplaGraphs: [EMNLP 2021] Dataset and PyTorch Code for ExplaGraphs: An Explanation Graph Generation Task for Structured Commonsense Reasoning · GitHub"
[14]: https://github.com/kixlab/suggestbot_dataset?utm_source=chatgpt.com "GitHub - kixlab/suggestbot_dataset: From Internet Argument Corpus (IAC) 2.0 dataset, this dataset covers 10,000 posts containing claims that can be verified with facts. The dataset contains annotations on verifiable sentences for each post and factual information that supports or refutes each annotation. · GitHub"
[15]: https://github.com/lamps-lab/msvec?utm_source=chatgpt.com "GitHub - lamps-lab/msvec: A new testing dataset, MSVEC, namely Multi-Domain Scientific Claim Verification Evaluation Corpus (MSVEC), covering true and false evidenced scientific claims in multiple domains, designed to evaluate the robustness of Scientific Claim Verification models. · GitHub"
[16]: https://github.com/westlake-autolab/BioKGBench?utm_source=chatgpt.com "GitHub - westlake-autolab/BioKGBench: BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science · GitHub"
[17]: https://github.com/altuncu/FACTors?utm_source=chatgpt.com "GitHub - altuncu/FACTors: The dataset and source codes presented in the paper titled \"FACTors: A New Dataset for Studying Fact-checking Ecosystem\" accepted for the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2025) as a Resource & Reproducibility paper. · GitHub"
[18]: https://github.com/allenai/s2orc?utm_source=chatgpt.com "GitHub - allenai/s2orc: S2ORC: The Semantic Scholar Open Research Corpus: https://www.aclweb.org/anthology/2020.acl-main.447/ · GitHub"
[19]: https://github.com/allenai/s2orc-doc2json?utm_source=chatgpt.com "GitHub - allenai/s2orc-doc2json: Parsers for scientific papers (PDF2JSON, TEX2JSON, JATS2JSON) · GitHub"
[20]: https://github.com/ourresearch/OpenAlex?utm_source=chatgpt.com "GitHub - ourresearch/OpenAlex: Index of open source code for OpenAlex---an open, comprehensive catalog of scholarship, connecting papers, authors, institutions, and journals. · GitHub"
[21]: https://github.com/allenai/pes2o?utm_source=chatgpt.com "GitHub - allenai/peS2o: Pretraining Efficiently on S2ORC! · GitHub"
[22]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"
[23]: https://github.com/geneontology/obographs?utm_source=chatgpt.com "GitHub - geneontology/obographs: Basic and Advanced OBO Graphs: specification and reference implementation · GitHub"
[24]: https://github.com/trustgraph-ai/trustgraph?utm_source=chatgpt.com "GitHub - trustgraph-ai/trustgraph: The deterministic context engineering platform for open source AI. Connect open models and ontologies with context graph harnesses to build explainable, reliable agents. · GitHub"
[25]: https://github.com/Graph-COM/SubgraphRAG?utm_source=chatgpt.com "GitHub - Graph-COM/SubgraphRAG: [ICLR 2025] Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation · GitHub"
[26]: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark?utm_source=chatgpt.com "GitHub - GraphRAG-Bench/GraphRAG-Benchmark: The official repo of GraphRAG-Bench for evaluating GraphRAG models. \"When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation\". (ICLR'26) · GitHub"
[27]: https://github.com/mnott/PAI?utm_source=chatgpt.com "GitHub - mnott/PAI: Personal AI Infrastructure · GitHub"
[28]: https://github.com/swarmclawai/swarmvault?utm_source=chatgpt.com "GitHub - swarmclawai/swarmvault: The local-first LLM Wiki: open-source knowledge graph builder, RAG knowledge base, and agent memory store. Built on Andrej Karpathy's pattern. An Obsidian alternative for personal knowledge management, AI second brain, and durable Claude Code / Codex / OpenClaw memory. · GitHub"
[29]: https://github.com/C-Bjorn/MegaMem?utm_source=chatgpt.com "GitHub - C-Bjorn/MegaMem: Transform your Obsidian vault into a powerful knowledge graph with MCP support · GitHub"
[30]: https://github.com/bhaskatripathi/graphGita?utm_source=chatgpt.com "GitHub - bhaskatripathi/graphGita: First scientific re-interpretation of Bhagwad Gita with Knowledge Graphs improved with Monte Carlo Tree Search · GitHub"
[31]: https://github.com/romain-girardi-eng/EleutherIA/wiki/Historical-Periods?utm_source=chatgpt.com "GitHub - romain-girardi-eng/EleutherIA: AI-powered scholarly research platform for ancient philosophical debates on free will, fate & moral responsibility (6th c. BCE – 6th c. CE). Agentic GraphRAG · 17k+ KG nodes · 189 ancient works · multi-LLM · hybrid search. · GitHub"
[32]: https://github.com/OriginTrail/dkg?utm_source=chatgpt.com "GitHub - OriginTrail/dkg: OriginTrail Decentralized Knowledge Graph (DKG) is a decentralized knowledge infrastructure for multi-agent AI memory — enabling agents to publish, verify, and query shared knowledge as cryptographically verifiable graph assets across a peer-to-peer network. · GitHub"
[33]: https://github.com/danielmiessler/substrate?utm_source=chatgpt.com "GitHub - danielmiessler/Substrate: An Open-source Framework for Human Understanding, Meaning, and Progress. · GitHub"
[34]: https://github.com/microsoft/graphrag?utm_source=chatgpt.com "GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub"

# AGENTS.md — read this FIRST. The governing file for every agent in ip-graph.

*Auto-loaded when an agent works in this project. Read this, then `NAVIGATION.md`, then `TODO.md` and
`BUILDNOTES.md` before building anything. This project turns the scraped informationphilosopher.com
corpus into a queryable knowledge graph, following the conventions of its sibling project Pāṭala
(`/root/projects/patala`).*

---

## 0. THE ONE RULE

> **Nothing is "real" because a file exists. It is real when it has a reproducible pipeline, a clean
> input, and verifiable output.**

A scraped file is not content. An extracted `.txt` is not verified text. A graph edge is not a claim.
"425 docs extracted" is not "the corpus is clean." Always state what you actually verified, with counts
that match ground truth.

---

## 1. WHAT THIS PROJECT IS

- **Input:** the informationphilosopher.com scrape (only full copy, backed up to R2:
  `r2:atlas-sources/informationphilosopher`).
- **Problem:** ~97% of the scraped HTML is broken (Apache "Bad Request" error pages). The real value
  is in the **PDFs** (primary scientific/philosophical papers) + a handful of real HTML pages.
- **Goal:** a knowledge graph of the information-philosophy network (free will, determinism, quantum,
  information, entropy, mind, chance).

**Corpus reality (verified ground truth, 2026-08-14):**
- Clean usable corpus: **425 documents** (6 html + 419 pdf)
- Quarantined error pages: 24 in `data/extracted_md/_errors/`, 788 in `data/raw/errors/`
- Graph: **490 nodes, 6484 edges**

---

## 2. THE LAYOUT (agent-usable names, patala-style)

```
/mnt/HC_Volume_106427611/ip-graph/
  data/              all CONTENT (separated from code/docs, like patala)
    raw/               cleaned source (html_articles/ · pdfs/ · images/ · errors/ + MANIFEST.json)
    extracted/         plain text per doc (html/ · pdf/ · _ocr/)
    extracted_md/      markdown per doc (_errors/ = quarantined)
    graph/             graph outputs (graph.json · doc_graph.gexf · concepts.jsonl · works.jsonl)
    corpus.jsonl       ONE machine-readable corpus (425 versioned records)
  scripts/           the PIPELINE, dash-case action-verb names (patala-style)
  docs/              numbered concern docs (01-corpus … 05-performance)
  mcp/               future agent-tool layer (empty; reserved for agent MCP)
  AGENTS.md          the GOVERNING rules (read first)
  BUILDNOTES.md      the build HISTORY
  NAVIGATION.md      this master index
  TODO.md            the live TASK TRACKER
```

---

## 3. THE OPERATING AXIOMS (non-negotiable)

1. **Never `sleep` to wait.** Do other work while long tasks run in background (`nohup … &`).
2. **Background with `nohup`/`setsid`, log to a file.** Never block the shell on a long job.
3. **Kill by specific PID, never `pkill`.** Find PID with `ps -eo pid,cmd | grep <name>`.
4. **The corpus is backed up to R2** (`r2:atlas-sources/informationphilosopher`). Keep it that way —
   verify with `rclone check` before deleting any local source.
5. **Reuse, don't rebuild.** Check `scripts/` + `docs/` + the cloned KG tools
   (`/mnt/HC_Volume_106427611/kg-tools/`) before writing new machinery.
6. **Closed vocabulary only.** The graph ontology (`docs/04-ontology.md`) is the contract. No invented
   relations/concepts. Every concept/edge needs an `evidence_quote`.
7. **Never delete, quarantine.** When removing junk, move it to an `_errors/` / `errors/` dir, don't
   `rm` it, until a reviewer confirms it's safe to permanently delete.
8. **Keep numbers reconciled.** Every doc must match ground truth. If you change the corpus or graph,
   update the counts in `docs/01-corpus.md`, `02-extraction.md`, `03-graph.md`, `BUILDNOTES.md`.

---

## 4. THE NAVIGATION (read in order)

0. **`AGENTS.md`** — this file.
0b. **`NAVIGATION.md`** — the master index (resolve anything → location/script/how-to-run).
0c. **`TODO.md`** — the live task tracker.
0d. **`BUILDNOTES.md`** — the build history + decisions.
1. **`docs/01-corpus.md`** — the source data.
2. **`docs/02-extraction.md`** — the text pipeline.
3. **`docs/03-graph.md`** — the graph output.
4. **`docs/04-ontology.md`** — the concept + relation vocabulary (the graph contract).
5. **`docs/05-performance.md`** — the performance doctrine.

---

## 5. VERIFY BEFORE CLAIMING DONE

```bash
cd /mnt/HC_Volume_106427611/ip-graph
# corpus integrity (must be 425, all records valid)
python3 -c "import json; n=[json.loads(l) for l in open('data/corpus.jsonl')]; print(len(n),'records OK')"
# graph integrity
python3 -c "import json; g=json.load(open('data/graph/graph.json')); print(len(g['nodes']),'nodes',len(g['edges']),'edges')"
# R2 backup intact
rclone check /mnt/HC_Volume_106427611/CX-Train/informationphilosopher r2:atlas-sources/informationphilosopher
```

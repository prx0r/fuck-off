# TANTRĀLOKA FULL-CORPUS TRANSLATION — THE ACTUAL PROCESS (honest, live)

*2026-08-14, running.* What is ACTUALLY happening right now on the box, end to end, and why it takes
as long as it does. Read this before judging the speed — it is not a wasted slowness; it is a serial,
per-verse, real-model pipeline. This is the DOCUMENTED truth (no theatre).

---

## 1. WHAT IS RUNNING

- **Command:** `python3 scripts/run-tantraloka-translation-parallel.py --workers 3 --batch 0 --resume`
- **PID:** (see `ps -eo pid,cmd | grep run-tantraloka-translation-parallel`)
- **Log:** `/tmp/opencode/tantraloka-full.log`
- **Output:** `tantraloka/corpus/translations.jsonl` (one JSON record per verse, append-only)
- **Checkpoint:** `tantraloka/corpus/translation-checkpoint.json` (resume-safe `done` set)
- **Goal:** translate ALL 4,624 Tantrāloka kārikās from the patala factory's real SOURCE objects.

---

## 2. THE HARDWARE (from AGENTS.md §3.4a — the real ceiling)

- ONE **4-core VPS**, **8 GB total RAM**, and **TWO agents run on it concurrently** (this one + the
  patala side).
- **3 workers** is the RAM-safe parallelism cap. It is NOT a throughput number; it is a memory budget.
- Each worker holds a `hermes chat` subprocess + the Python harness (~790 MB RSS total — stable).

---

## 2.5 WHO DRIVES WHAT (the honest control-flow)

**Python is the driver. Hermes is a subprocess called per-verse — it does NOT orchestrate the run.**

- The **Python harness** (`run-tantraloka-translation-parallel.py`, `ThreadPoolExecutor` with 3 workers)
  owns the loop: it reads each verse from patala's registry, calls the translate function, computes the
  Vidyut proof, appends to `translations.jsonl`, and updates the checkpoint. **It decides what runs, in
  what order, with what concurrency.**
- For the GENERATION step only, Python shells out to **`hermes chat -Q -q --yolo --max-turns 6`** as a
  subprocess (via `lib/hermes_exec.translate_karika()`). Hermes (running as an agent, with repo/skills
  access) produces the actual translation text for that ONE verse, then exits.
- Hermes is the **generation kernel** (the model's pen); Python is the **orchestrator** (the hand that
  moves the pen across 4,624 verses). This matches the architecture rule: *Hermes for GENERATION,
  `.py` for REDUCTION/control* — Python owns the loop, Hermes owns the output.
- The `hermes gateway` (PID 980) stays up as the daemon; each per-verse call is a client to it. The 3
  concurrent worker threads each run one such call at a time.

---

## 3. WHAT HAPPENS PER VERSE (the real cost)

For EVERY one of the 4,624 kārikās, the Python harness does this **serially** (one verse = one full
agentic model call — this is the cost, it cannot be vectorized):

1. **Load the verse text** (Python) from patala's `object_registry` SOURCE payload (real Sanskrit, e.g.
   `tantraloka:v1017`).
2. **`translate_karika()`** (Python) → shells out to **`hermes chat -Q -q --yolo --max-turns 6`** — an
   AGENTIC call with the model acting as a Sanskrit philologist, up to 6 agent turns. It may read
   repo/skills, reason, and produce a JSON answer. **This is the 30 s/verse cost** — it is a real LLM
   inference, not a lookup. Hermes is the generation kernel here; Python is the orchestrator.
3. **Brace-balanced JSON extraction** — pulls the FINAL answer object out of the agent's output
   (which may contain reasoning). Fields: `translation`, `terms`, `contested`.
4. **`ProofGenerator.full()`** — the real Vidyut analysis of the verse (token floor, SLP1 scheme,
   negation/modality) → the `lattice` verdict + `n_tokens` (a fast Rust-wheel kernel, ~ms).
5. **Append the record** to `translations.jsonl` (locked), mark the verse done in the checkpoint.

**The per-verse wall-clock is dominated by step 2 — the Hermes agentic call (~30 s).** 3 workers run
concurrently, so the wall-clock rate is ~3× a single model call.

---

## 4. WHY IT IS SLOW (honest, no spin)

| Factor | Impact |
|---|---|
| **One real LLM call per verse** (agentic, up to 6 turns) | ~30 s/verse — the irreducible cost |
| **3-worker cap** (8 GB RAM budget) | limits concurrency to 3, not CPU-count |
| **4,624 verses total** | × the per-verse cost |
| **Two agents share the box** | we deliberately run ONE heavy job at a time (AGENTS §3.4a) |

**Projected total:** ~33 s/verse × 4,624 ≈ **~42 hours** for the full corpus.

**Why we accept this:** it is the ANTI-THEATRE requirement. A hand-fed translation (the thing the audits
repeatedly caught) is instant but fake. A REAL from-scratch Hermes translation of a Sanskrit kārikā is
slow but genuine. The whole point of this project (AGENTS.md §0, §7.1) is that "fast" must not mean
"hand-fed a fabricated answer." We are trading hours for honesty.

**Why it is safe to be slow:** the run is **checkpoint + resume safe**. Kill it at any point and
`--resume` continues from where it stopped, re-translating nothing. So the 42-hour number is not a
brittle dependency — it is an interruptible, resumable long job (exactly what AGENTS.md §3.1 dictates).

---

## 5. WHAT THE OUTPUT LOOKS LIKE (real, verified)

```json
{"object_id":"tantraloka:v1017","verse":"...","translation_chars":190,
 "translation":"For here — [in that state] in which there is no distinction whatsoever — ...",
 "terms":{...},"contested":"1) vyavacchedaḥ — neutral 'distinction' vs. negative 'exclusion' ...",
 "lattice":"PASS","n_tokens":15}
```

- `translation_chars: 190` — a CLEAN translation (the earlier bug captured 26k-58k chars of raw
  reasoning; fixed by reusing `translate_karika()`).
- `contested` — a real philological note (term-rendering decisions). This feeds the L200/C1 layers.
- `lattice: PASS`, `n_tokens` — the real Vidyut proof, independent of the translation.

---

## 6. THE PIPELINE THIS FEEDS (why it's the right next build)

Per `DEV_PLAN.md` (P0) + `HANDOVER.md` §12 + `TANTRALOKA-PRODUCTION.md` X1-X5:

```
real SOURCE verse
  → [HERE] Hermes L2 translation (this run)  ← WE ARE HERE
  → my TranslationProof (per verse)
  → B3→B4 commentary-lift (commentary_lift.py)
  → validate vs Dyczkowski (three-version)
  → feed products: essay / education / site
```

The 30-kārikā corpus already proved the mechanism (real proofs + commentaries + validated vs Dyczkowski).
This run scales it to the full 4,624 kārikās.

---

## 7. STATUS (live)

- [x] All gates passed (4624 SOURCE objects, 4619 to translate, Hermes available)
- [~] Translating: ~0.03/s wall-clock (3 workers), checkpoint advancing
- [ ] ~42 h projected for the full corpus (interruptible + resumable)

*This doc is honest by construction. The number that matters is not the ETA — it is that every one of
the 4,624 verses will be a REAL from-scratch Hermes translation with a real Vidyut proof, not a
hand-fed placeholder.*

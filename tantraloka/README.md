# TANTRĀLOKA — the Mona Lisa: a live autonomous full-stack organism

*2026-08-14 · status: READY-TO-GO PLAN. Tantrāloka (Abhinavagupta) is the canonical test of the whole
Verified Epistemic Organism. We translate it FROM SCRATCH from the Sanskrit root (not reading Dyczkowski),
run it through every layer, and then validate against Dyczkowski. This folder is the operational plan:
hypotheses per layer, what we expect to see and why, the test for each, and the correct order — imagined
as a LIVE AUTONOMOUS SYSTEM, from bibliography ingestion through the full chain.*

---

## THE VISION (why Tantrāloka is the Mona Lisa)

Tantrāloka is the intellectual apex of the Pratyabhijñā/Śaiva tradition — Abhinavagupta's magnum opus.
It:
- connects DIRECTLY to the IPVV (our existing proof) + the recognition thesis (our gold),
- has the richest existing pushing material (35 LOGICVID sessions on `pushing-tantraloka/`),
- has BOTH the Sanskrit root (what we translate) AND Dyczkowski's full translation (the gold for validation),
- is philosophically load-bearing (reflexivity, upāyas, recognition — the exact cruxes our organism exists for).

**The test:** run the ENTIRE organism on one real text, from raw Sanskrit bibliography ingestion to
translation/argument/education products, autonomously, then validate the output against Dyczkowski.

---

## THE SOURCES (on disk, verified)

| Source | Path | Role |
|---|---|---|
| **Sanskrit root** (the input) | `gretil_tantraloka.txt` (17,684 lines, Kashmir Series 1918-38 via GRETIL/Takashima) | the kārikās we translate FROM |
| **Ingested root** | `data/tantraloka/root-verses.json` (5,860 kārikās, `AbhT_x.y` refs) | machine-ready |
| **Āhnika 1** (flagship) | `data/tantraloka/ahnika-1.json` (333 verses, upāyas) | the from-scratch translation unit |
| **Dyczkowski vols 1-11** (the gold) | `texts-original/tantraloka-vol{1..11}-dyczkowski.txt` | the VALIDATION reference |
| **Pushing material** (the compass) | `research-library/recognition/pushing-tantraloka/` (35 sessions) | what the text's cruxes are |
| **Jayaratha's Viveka** | in the GRETIL root | the commentary |

---

## THE LIVE AUTONOMOUS SYSTEM (the full chain, in order)

```
BIBLIOGRAPHY → TAGGING → CONDITION → TIME-PERIOD → TIMELINE → INGEST
   → SOURCE → L0 token floor → TranslationProof → Commentary → Argument
   → Crux → Synthesis → Essay → Education → PRODUCTS (bundles/Astro/MCP)
        ↕ (staleness + feedback re-prioritize)
```

Each step below is a LAYER with: the HYPOTHESIS, the EXPECTED RESULT + WHY, the TEST, and the ORDER.

---

## PHASE A — THE SCHOLARLY PRE-INGESTION (the atlas layer)

### A1 — Bibliography registration
- **Hypothesis:** Tantrāloka registers as a canonical WORK with correct external IDs (GRETIL, Kashmir
  Series, Dyczkowski) and the transmission graph (WORK → EDITION → ETEXT → the Sanskrit root + Dyczkowski).
- **Expected:** 1 work, 1 edition (KST 1918-38), 2 etexts (GRETIL root + Dyczkowski vols). The organism can
  resolve "Tantrāloka" to its source registry entries with rights (both CC-BY-NC-SA / non-commercial).
- **Why:** the atlas rule — Postgres is entity truth, R2 is bytes, the event log is history. We must know
  WHAT the object is before we translate it.
- **Test:** `source_registry.py` — every source_ref (GRETIL, Dyczkowski, Jayaratha) resolves to a registered
  source with rights + health. 0 dangling.
- **Kernels:** `source_registry.py`, `epistemic.py`.

### A2 — Tagging (tradition / school / genre)
- **Hypothesis:** Tantrāloka tags as: tradition=Trika/Śaiva, school=Pratyabhijñā (with Siddhānta/mantra
  dialogue), genre=philosophical treatise, author=Abhinavagupta (c. 975-1025), language=Sanskrit, dialect
  = the Saiddhāntika-technical register the sivaqueue semantic-shift atlas knows.
- **Expected:** the correct term-senses per school (e.g. `śakti`, `prakāśa`, `vimarśa`, `upāya`, `mala`)
  resolve to their Trika senses, NOT flat dictionary readings.
- **Why:** GEM/term-context — a translator must pick the CORRECT sense per period/tradition. The semantic-
  shift atlas (sivaqueue) is the reference.
- **Test:** tag the 333 Āhnika-1 verses; verify the key terms resolve to Trika senses; verify `kula`,
  `upāya`, `cakra` map correctly.
- **Kernels:** `vidyut_l0` (SLP1), the sivaqueue semantic-shift atlas.

### A3 — Condition / textual state
- **Hypothesis:** the GRETIL root is a clean electronic transcription of the Kashmir Series edition with
  Jayaratha's Viveka interleaved. We can separate kārikās (root) from commentary (Viveka) by the `AbhT_x.y`
  refs + prose-vs-verse structure.
- **Expected:** clean verse extraction (verified: 5,860 kārikās) with the commentary flagged separately.
  No verse text leaks into commentary and vice versa.
- **Why:** the KORAL two-graph rule — the reality graph (root kārikās) must never be corrupted by the
  interpretation graph (Jayaratha's commentary).
- **Test:** `integrity_gate.py` — root kārikās = PRIMARY + CLEAN; Jayaratha = SECONDARY. A synthesis citing
  only Jayaratha (no root kārikā) FAILS the primary-source gate.
- **Kernels:** `ingest-tantraloka-root.py` (done), `integrity_gate.py`.

### A4 — Time-period / timeline placement
- **Hypothesis:** Tantrāloka places in the timeline at c. 975-1025 (Abhinavagupta), between the early
  Siddhānta (sivaqueue targets 1-50) and the later Krama works, as a PRATYABHIJÑĀ apex. Its conceptual
  lineage: Nārāyaṇakaṇṭha → Utpaladeva → Abhinavagupta (IPVV) → Jayaratha (Viveka).
- **Expected:** the timeline shows Tantrāloka as a node with temporal edges (BEFORE Jayaratha, AFTER
  Utpaladeva, CONCURRENT with the IPVV). This is "temporal scholarship" (VISION E).
- **Why:** VISION E — the graph as a time-series, not a snapshot. Where the doctrine sits in history
  matters for which term-senses were live.
- **Test:** `graphiti-temporal` valid_at/invalid_at on the Tantrāloka node + its lineage edges.
- **Kernels:** `graphiti`-temporal pattern, the historyTimeline data.

---

## PHASE B — THE REFINERY (the translation spine)

### B1 — INGEST (raw → SOURCE)
- **Hypothesis:** the Sanskrit root enters as SOURCE objects, content-addressed (sha256 per kārikā), with
  the verse text as the primary-source reality graph.
- **Expected:** 5,860 SOURCE objects, each a kārikā with a stable `AbhT_x.y` id + content hash.
- **Why:** content-addressing = immutable versioned identity (the atlas rule).
- **Test:** `source_registry` — every kārikā resolves, hashes stable, dedupe exact.
- **Kernels:** `ingestion_organism.py` (the refinery), `source_registry.py`.

### B2 — L0 token floor (vidyut)
- **Hypothesis:** `vidyut_l0` normalizes the Sanskrit to SLP1 and produces position-anchored word tokens
  (the Text-Fabric slot model). The HONEST finding: vidyut.cheda is statistical, so the deterministic SLP1
  splitter is the floor.
- **Expected:** each kārikā → SLP1 → word tokens with lemma/morphology where available. Sandhi-split where
  unambiguous (e.g. `tadubhaya` → `tad ubhaya`).
- **Why:** the L0 token floor is the stable position primitive every later layer anchors to (GEM 5.3).
- **Test:** `vidyut_l0.py` on Āhnika-1 verses — position-anchored, monotonic, deterministic.
- **Kernels:** `vidyut_l0.py`.

### B3 — TranslationProof (the moat)
- **Hypothesis:** our from-scratch translation of each kārikā produces a **non-aggregate 11-dim proof vector**
  (SOURCE_COVERAGE … HUMAN_REVIEW), gate BLOCKED on any failing hard dimension. We translate from the
  Sanskrit root, NOT reading Dyczkowski.
- **Expected:** kārikās pass coverage/morphology/negation/modality; term-consistency holds across Āhnika 1;
  PARALLEL_WITNESS shows agreement with (independently) the established readings. **The gate stays BLOCKED
  until a human adjudicates** (the honest ceiling).
- **Why:** the moat — proof-carrying, never a scalar, never auto-promoted.
- **Test:** `translation.py` + `translation_variant.py` (three-version against the other available
  renderings as the interpretation check).
- **Kernels:** `translation.py`, `translation_variant.py`.

### B4 — Commentary (passage-local)
- **Hypothesis:** the Jayaratha Viveka + our own passage-local commentary attach per-kārikā as the
  interpretation-space, KORAL-separated from the root.
- **Expected:** each kārikā has a compact commentary that (a) cites the root, (b) notes where our
  reading differs from the established (this is where the Dyczkowski comparison will surface).
- **Why:** the three-version doctrine — divergence = the interpretation-space the commentary adjudicates.
- **Test:** `essay_ingest` / commentary stage on Āhnika-1 verses.
- **Kernels:** `essay_ingest.py`, `scholar_review.py`.

---

## PHASE C — THE REASONING ENGINE

### C1 — Argument + Crux
- **Hypothesis:** the Tantrāloka's claims become AIF arguments (info/inference/conflict) and the pushing
  sessions' cruxes surface as real crux nodes (reflexivity, upāyas, recognition, theodicy).
- **Expected:** the 35 pushing sessions map onto cruxes over the actual kārikās (e.g. `AbhT_1.52` → the
  reflexivity crux). The argument graph links kārikā → proposition → crux.
- **Why:** the organism's reasoning engine — crux = "what would change our mind" (GEM 6.3).
- **Test:** `crux-compiler` + `review.py` on the Āhnika-1 arguments.
- **Kernels:** `review.py`, `essay_ingest.py`, crux-compiler.

### C2 — Synthesis
- **Hypothesis:** the converged reading of Āhnika 1 (the upāyas + reflexivity + recognition) synthesizes
  into a coherent position, derivation-complete, adjudicated inputs only.
- **Expected:** a synthesis object that cites every load-bearing kārikā + the adjudicated crux resolutions.
- **Why:** synthesis = converged scholarship, gated by the immune system.
- **Test:** `evolve.py` / synthesis over the Āhnika-1 argument graph.
- **Kernels:** `evolve.py`, `review.py`.

---

## PHASE D — THE REPRODUCTIVE + SENSORY SYSTEM (products + growth)

### D1 — Essay (sentence-sourced)
- **Hypothesis:** a reactive essay on Āhnika 1, every sentence dependency-linked to its kārikā(s) — so a
  source retraction recompiles the essay.
- **Expected:** a scholarly essay where each claim resolves to an `AbhT_x.y` (reactive, not dead prose).
- **Why:** reactive documents (Law 7) — prose never silently contains a refuted claim.
- **Test:** `essay_ingest` reactive stage; mutate a kārikā → the essay section goes stale.
- **Kernels:** `essay_ingest.py`, `staleness.py`.

### D2 — Education
- **Hypothesis:** a learner reconstructs the Tantrāloka's argument — wrong answers resolve to known
  epistemic neighbors (the moat), pedagogy targets the weakest skill.
- **Expected:** a gold interaction set over Āhnika-1 (the reflexivity crux as a test: "why must prakāśa
  be accompanied by vimarśa?").
- **Why:** education is a projection of the graph (the moat).
- **Test:** `education.py` / `pedagogy.py` on the Āhnika-1 argument.
- **Kernels:** `education.py`, `pedagogy.py`, `organism.py`.

### D3 — Products (bundles → Astro → MCP)
- **Hypothesis:** the compiled Tantrāloka is served as static bundles + Astro pages + MCP tools (0-JS,
  JSON-LD, canonical).
- **Expected:** a `/tantraloka/` site section with the root, translation, proof, commentary, argument,
  essay, education — all served from the compiled projections.
- **Why:** the read plane — compute on write, read from CDN.
- **Test:** `build-static-site.py` + the Astro build + `edge/server.py`.
- **Kernels:** `context_compiler.py`, `seo.py`, `bundle_router.py`.

---

## PHASE E — VALIDATION vs DYCZKOWSKI (the payoff)

### E1 — The three-version comparison
- **Hypothesis:** where our from-scratch translation AGREES with Dyczkowski = the HARD CORE (both
  independently reached it); where we DIFFER = the interpretation-space the commentary must adjudicate.
- **Expected:** a per-kārikā agreement score; high agreement on the load-bearing technical terms (prakāśa,
  vimarśa, upāya), divergence on contested readings (which the pushing sessions already flagged).
- **Why:** GEM 5.1 — the three-version method IS the scholarship.
- **Test:** `translation_variant.py` on Āhnika-1 vs Dyczkowski.
- **Kernels:** `translation_variant.py`.

### E2 — The comparison becomes scholarship
- **Hypothesis:** the divergences feed back as cruxes → the organism re-prioritizes (learner demand on the
  contested passages). This is the flywheel.
- **Expected:** the organism flags the contested kārikās for re-review, raising their Q (question demand)
  and R (review deficit) in `next_action`.
- **Why:** the co-evolving organism — scholarship → learning → misconceptions → source-repair.
- **Test:** `ingestion_organism.learner_probe` + `next_action` re-prioritization on the contested verses.
- **Kernels:** `ingestion_organism.py`, `next_action.py`.

---

## THE CORRECT ORDER (the autonomous live-system sequence)

```
STEP 1  A1 Bibliography → A2 Tagging → A3 Condition → A4 Timeline   (the atlas: WHAT it is)
STEP 2  B1 INGEST → B2 L0 → B3 TranslationProof → B4 Commentary     (the refinery: the spine)
STEP 3  C1 Argument/Crux → C2 Synthesis                             (the reasoning engine)
STEP 4  D1 Essay → D2 Education → D3 Products                        (the reproductive/sensory)
STEP 5  E1 Validate vs Dyczkowski → E2 feed divergences back         (the payoff + the flywheel)
```

**The rule:** each step's output is the input to the next. Nothing proceeds until the previous layer's
gate passes (0 invariant violations, primary-source gate, honest ceilings). Staleness propagates any change
downstream; the queue re-prioritizes on learner demand + review deficit.

---

## WHAT WE EXPECT TO SEE AND WHY (the honest headline hypotheses)

| Layer | Expect to see | Why |
|---|---|---|
| Bibliography | 1 work → 2 etexts resolve, rights ok | the atlas entity graph |
| Tagging | Trika/Pratyabhijñā terms, correct senses | the semantic-shift term-context |
| Timeline | Tantrāloka at c.975-1025, after Utpaladeva | temporal scholarship (VISION E) |
| L0 | 5,860 position-anchored SLP1 tokenizations | the stable slot model |
| TranslationProof | 11-dim vector, gate BLOCKED until human | the moat, never auto-promoted |
| Argument/Crux | reflexivity crux on AbhT_1.52 | the pushing sessions become crux nodes |
| Essay | reactive, every sentence cites a kārikā | reactive documents (Law 7) |
| Education | learner reconstructs upāyas, reflexivity | education as graph projection |
| **Validation** | **high agreement with Dyczkowski on load-bearing terms; divergence on the flagged cruxes** | **three-version = the scholarship** |

---

## THE READY-TO-GO CHECKLIST

- [x] Sanskrit root ingested (5,860 kārikās, 333 in Āhnika 1)
- [x] Dyczkowski vols 1-11 on disk (the gold)
- [x] Pushing material (35 sessions) available (the crux compass)
- [x] All kernels built + 76/76 tests (the machinery)
- [x] The read plane (Astro + bundles + MCP) works
- [ ] **STEP 1**: bibliography + tagging + timeline (A1-A4)
- [ ] **STEP 2**: L0 + TranslationProof on Āhnika 1 (B1-B3)
- [ ] **STEP 3**: Argument/Crux on Āhnika 1 (C)
- [ ] **STEP 4**: Essay + Education + Products (D)
- [ ] **STEP 5**: Validate vs Dyczkowski + feed back (E)

---

## Proofs / resolution
- Sources: `data/tantraloka/root-verses.json`, `ahnika-1.json`, Dyczkowski vols, pushing-tantraloka/
- Kernels: `BUILT-BY-LAYER.md` (the 38 kernels), `KERNELS-INDEX.md`
- The organism: `ingestion_organism.py`, `next_action.py`, `translation.py`, `integrity_gate.py`
- The read plane: `scripts/build-static-site.py`, `web/`, `edge/`

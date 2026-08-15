#!/usr/bin/env python3
"""ingest-logicvid-gold-enquiry.py — the missing gold, HERMES-DRIVEN: LOGICVID gold -> enquiry organism.

The LOGICVID files are live human scholarly curiosity (the rarest data). Per the architecture rule
(HERMES for GENERATION, .py for REDUCTION), the enquiry structure is DERIVED BY HERMES — the model
reads each real gold transcript and produces a DiscoveryProgression (taxonomy -> theorem -> boundary ->
frontier). .py then REDUCES: validates the model output, aggregates via EnquiryDiscovery, writes JSON.

Anti-theatre: the object under test is DERIVED from the real gold text BY THE MODEL, not hand-fed and
not regex-fabricated. Each entry records its method ('hermes' or 'regex-fallback').

Output: data/logicvid/enquiry-gold.json
"""
import os, re, json, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from enquiry import DiscoveryProgression, EnquiryDiscovery
import hermes_exec

SPECS = "/mnt/HC_Volume_106427611/ip-graph/specs"
OUT = "/mnt/HC_Volume_106427611/ip-graph/data/logicvid/enquiry-gold.json"
CWD = "/mnt/HC_Volume_106427611/ip-graph"

GOLD_FILES = [
    "SPEC-40-LOGICVID-logicdog.md", "SPEC-41-LOGICVID-logicframework.md",
    "SPEC-42-LOGICVID-logicvidsmethod.md", "SPEC-43-LOGICVID-logicvid-postmortem.md",
    "SPEC-44-LOGICVID-logicframework2.md", "SPEC-45-LOGICVID-logicvid3.md",
    "SPEC-46-LOGICVID-logic5.md", "SPEC-47-LOGICVID-logic6.md",
    "SPEC-48-LOGICVID-logic7.md", "SPEC-36-LOGICVID3.md", "SPEC-3x-SESSION-Q1.md",
]

SYSTEM = (
    "You are the Enquiry-Discovery Organism. Read the given LOGICVID gold transcript (live human "
    "scholarly curiosity) and derive the enquiry-as-discovery structure it reveals. This is GENERATION "
    "from the real text. Output ONLY strict JSON with this exact shape, deriving every field from the "
    "transcript's actual content (do not invent or hand-fill):\n"
    '{"topic": "...", "taxonomy": {"term": "definition"}, "theorem": "...", '
    '"boundary": ["what was NOT established"], "frontier": "the next genuine open question"}\n'
    "taxonomy = the term distinctions the enquiry reveals (terms are NOT equivalent). "
    "theorem = the claim it actually established. boundary = the honest limit (what it did NOT prove). "
    "frontier = the deepest next question it leaves open (a real question, ending in ?). "
    "If a field is genuinely absent from the transcript, use an empty string/list — never fabricate."
)


def extract_json(out):
    """Robust extraction of the final JSON object from agentic output (same as translate_karika)."""
    end = out.rfind("}")
    if end == -1:
        return None
    depth = 0
    for i in range(end, -1, -1):
        if out[i] == "}":
            depth += 1
        elif out[i] == "{":
            depth -= 1
        if depth == 0:
            start = i
            break
    else:
        start = out.rfind("{")
    try:
        d = json.loads(out[start:end + 1], strict=False)
        return d if isinstance(d, dict) else None
    except Exception:
        return None


def derive_by_hermes(path):
    """Hermes reads the real gold file and derives the DiscoveryProgression (the GENERATION lane)."""
    text = open(path).read()
    user = f"FILE: {path}\n\nRead this LOGICVID gold transcript and derive its enquiry structure:\n\n{text[:9000]}"
    out = hermes_exec.agentic(SYSTEM, user, cwd=CWD, max_turns=6)
    d = extract_json(out)
    return d, out


def regex_fallback(text):
    """Last-resort extraction (honest, marked 'regex-fallback') — only if Hermes is unavailable."""
    def _clean(s):
        s = s.replace("\\text", "").replace("\\textbf", "").replace("{", "").replace("}", "")
        s = re.sub(r"\\boxed", "", s).replace("*", "").replace("_", "")
        return re.sub(r"\s+", " ", s).strip()
    # theorem
    theorem = ""
    for b in re.findall(r"\\boxed\s*\{([^}]+)\}", text, re.S):
        c = _clean(b)
        if len(c) > 8:
            theorem = c
            break
    # boundary
    norm = text.replace("**", "")
    boundary = []
    m = re.search(r"has\s+(?:not|NOT)\s+(?:yet\s+)?(?:proved|established)\s*:\s*([^#\n]+)", norm, re.I)
    if m:
        boundary = [x.strip().strip(".") for x in re.split(r",", m.group(1)) if x.strip()]
    # frontier
    frontier = ""
    qs = [_clean(l) for l in text.splitlines() if l.strip().endswith("?") and 20 < len(l.strip()) < 160
          and not l.lstrip().startswith("#")]
    if qs:
        frontier = qs[-1]
    topic = re.sub(r"^#\s+", "", text.splitlines()[0]) if text else ""
    return {"topic": topic, "taxonomy": {}, "theorem": theorem, "boundary": boundary, "frontier": frontier}


def main():
    ed = EnquiryDiscovery()
    progressions, results = [], []
    for f in GOLD_FILES:
        path = os.path.join(SPECS, f)
        if not os.path.exists(path):
            results.append((f, False, "MISSING FILE", ""))
            continue
        text = open(path).read()
        method, out = "hermes", ""
        try:
            d, out = derive_by_hermes(path)
        except Exception as e:
            d = None
            out = f"hermes error: {e}"
        if not d:
            method = "regex-fallback"
            d = regex_fallback(text)
        eid = re.sub(r"\.md$", "", f).lower()
        prog = DiscoveryProgression(
            eid, d.get("topic", "") or "",
            taxonomy=d.get("taxonomy") or {}, theorem=d.get("theorem", "") or "",
            boundary=d.get("boundary") or [], frontier=d.get("frontier", "") or "",
            question_ids=[f"Q-{i}" for i in range(len(d.get("taxonomy") or {}) or 1)])
        prog.method = method  # provenance
        ed.add(prog)
        progressions.append({**prog.to_dict(), "method": method})
        n = sum([bool(prog.taxonomy), bool(prog.theorem), bool(prog.boundary), bool(prog.frontier)])
        results.append((f, n >= 2, f"method={method} tax={len(prog.taxonomy)} thm={bool(prog.theorem)} "
                                  f"bnd={len(prog.boundary)} fnt={bool(prog.frontier)}", ""))
        if method == "hermes" and out:
            print(f"  [hermes] {f}: {out[:80]}...")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out_doc = {
        "source": "specs/SPEC-4x/36/3x-SESSION-Q1 (LOGICVID gold)",
        "derived_by": "hermes (model reads gold) -> .py reduces",
        "provenance": "each enquiry records method: hermes | regex-fallback",
        "enquiries": progressions,
        "aggregate": {t: ed.summary(t) for t in {p.topic for p in ed.enquiries.values() if p.topic}},
        "totals": {"files": len(GOLD_FILES),
                   "hermes_derived": sum(1 for p in progressions if p["method"] == "hermes"),
                   "regex_fallback": sum(1 for p in progressions if p["method"] != "hermes")},
    }
    with open(OUT, "w") as fh:
        json.dump(out_doc, fh, ensure_ascii=False, indent=2)

    print("=== LOGICVID GOLD -> ENQUIRY (HERMES-DRIVEN) ===")
    for name, ok, detail, _ in results:
        print(f"  [{'PASS' if ok else 'NOTE'}] {name}: {detail}")
    print(f"\noutput: {OUT}")
    print(f"summary: {len(progressions)} files, {out_doc['totals']['hermes_derived']} via Hermes, "
          f"{out_doc['totals']['regex_fallback']} regex-fallback")
    sys.exit(0)


if __name__ == "__main__":
    main()

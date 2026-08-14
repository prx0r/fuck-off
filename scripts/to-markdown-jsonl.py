#!/usr/bin/env python3
"""Convert extracted txt -> Markdown (per doc) + corpus.jsonl (one record per doc).

Fast: reads existing .txt, adds a YAML-ish header + structure, writes .md + one jsonl.
"""
import os, re, glob, json
from datetime import date

TXT_ROOT = "/mnt/HC_Volume_106427611/ip-graph/data/extracted"
MD_ROOT = "/mnt/HC_Volume_106427611/ip-graph/data/extracted_md"
JSONL_PATH = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"
os.makedirs(MD_ROOT, exist_ok=True)

def clean_lines(text):
    lines = [ln.rstrip() for ln in text.split("\n")]
    # collapse 3+ blank lines to 1
    out = []
    blanks = 0
    for ln in lines:
        if not ln.strip():
            blanks += 1
            if blanks > 1:
                continue
        else:
            blanks = 0
        out.append(ln)
    return out

def detect_title(first_lines):
    """Heuristic: first non-empty line often the title."""
    for ln in first_lines:
        s = ln.strip()
        if s and len(s) < 120 and not re.search(r"\b(page|http|citation|doi|©|copyright)\b", s, re.I):
            return s
    return ""

records = []
txts = sorted(glob.glob(os.path.join(TXT_ROOT, "**", "*.txt"), recursive=True))
for f in txts:
    rel = os.path.relpath(f, TXT_ROOT)
    parts = rel.split(os.sep)
    kind = parts[0]          # html | pdf
    section = parts[1] if len(parts) > 2 else "root"
    docname = os.path.splitext(os.path.basename(f))[0]

    text = open(f, encoding="utf-8", errors="ignore").read()
    lines = clean_lines(text)
    title = detect_title(lines[:8]) or docname.replace("_", " ").replace("-", " ").title()

    # Build markdown
    md = [f"# {title}", "", f"**source:** {kind} · **section:** {section}", f"**file:** {docname}", "---", ""]
    # Skip title line if repeated
    body = lines
    if body and body[0].strip() == title.strip():
        body = body[1:]
    md.extend(body)
    md_text = "\n".join(md) + "\n"

    md_dir = os.path.join(MD_ROOT, kind, section)
    os.makedirs(md_dir, exist_ok=True)
    with open(os.path.join(md_dir, docname + ".md"), "w", encoding="utf-8") as w:
        w.write(md_text)

    records.append({
        "id": f"ip:{kind}:{section}:{docname}",
        "title": title,
        "kind": kind,
        "section": section,
        "docname": docname,
        "source_path": rel,
        "char_count": len(text),
        "text": text,
    })

with open(JSONL_PATH, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")

print(f"=== CONVERTED {len(records)} docs ===")
md_count = len(glob.glob(os.path.join(MD_ROOT, "**", "*.md"), recursive=True))
print(f"markdown files: {md_count}")
print(f"corpus.jsonl: {os.path.getsize(JSONL_PATH)/1048576:.1f}MB, {len(records)} records")
# sanity
print("\nsample record keys:", list(records[0].keys()))

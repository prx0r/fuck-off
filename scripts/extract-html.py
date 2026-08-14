#!/usr/bin/env python3
"""Stage A1: extract clean plain-text from real HTML articles into 02_extracted/html/."""
import os, re, glob, html as htmllib, json

SRC = "/mnt/HC_Volume_106427611/ip-graph/data/raw/html_articles"
DST = "/mnt/HC_Volume_106427611/ip-graph/data/extracted/html"

def clean_body(text):
    # isolate bodycontent if present
    m = re.search(r'<div class="bodycontent"[^>]*>(.*?)</div>', text, re.S)
    b = m.group(1) if m else text
    b = re.sub(r"<script.*?</script>", "", b, flags=re.S)
    b = re.sub(r"<style.*?</style>", "", b, flags=re.S)
    # convert block tags to newlines for readability
    b = re.sub(r"</(p|div|h1|h2|h3|h4|li|br|tr|blockquote|td)>", "\n", b, flags=re.I)
    b = re.sub(r"<[^>]+>", "", b)
    b = htmllib.unescape(b)
    lines = [ln.strip() for ln in b.split("\n")]
    lines = [ln for ln in lines if ln]
    return "\n".join(lines)

report = []
for f in sorted(glob.glob(os.path.join(SRC, "**/*.html"), recursive=True)):
    rel = os.path.relpath(f, SRC)
    try:
        text = open(f, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        report.append({"path": rel, "error": str(e)}); continue
    body = clean_body(text)
    if len(body) < 100:
        report.append({"path": rel, "skipped": "too short", "len": len(body)}); continue
    outdir = os.path.join(DST, os.path.dirname(rel))
    os.makedirs(outdir, exist_ok=True)
    outname = os.path.splitext(os.path.basename(f))[0] + ".txt"
    with open(os.path.join(outdir, outname), "w", encoding="utf-8") as w:
        w.write(body)
    report.append({"path": rel, "len": len(body), "ok": True})

print("=== HTML EXTRACTION ===")
ok = [r for r in report if r.get("ok")]
skip = [r for r in report if not r.get("ok")]
print(f"extracted: {len(ok)}, skipped/short: {len(skip)}")
for r in sorted(skip, key=lambda x: -x.get("len", 0))[:15]:
    print(f"  [short] {r['len']:6d} {r['path']}")
with open("/mnt/HC_Volume_106427611/ip-graph/docs/html_extract_report.json", "w") as f:
    json.dump(report, f, indent=1)

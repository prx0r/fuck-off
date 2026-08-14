#!/usr/bin/env python3
"""Stage A2: extract text from PDFs into 02_extracted/pdf/ using pdftotext.

Skips scanned/image PDFs that produce no text (they'd need OCR via GROBID/Tesseract later).
"""
import os, glob, subprocess, json, sys

SRC = "/mnt/HC_Volume_106427611/ip-graph/data/raw/pdfs"
DST = "/mnt/HC_Volume_106427611/ip-graph/data/extracted/pdf"
report_path = "/mnt/HC_Volume_106427611/ip-graph/docs/pdf_extract_report.json"

def extract(f, outdir):
    os.makedirs(outdir, exist_ok=True)
    base = os.path.splitext(os.path.basename(f))[0]
    out = os.path.join(outdir, base + ".txt")
    # -layout keeps column layout reasonable; limit to text layer (no OCR)
    r = subprocess.run(["pdftotext", "-layout", f, out], capture_output=True, text=True)
    if r.returncode != 0:
        return {"ok": False, "error": r.stderr.strip()[:200]}
    size = os.path.getsize(out)
    return {"ok": size > 100, "size": size}

pdfs = sorted(glob.glob(os.path.join(SRC, "**/*.pdf"), recursive=True))
report = []
for i, f in enumerate(pdfs, 1):
    rel = os.path.relpath(f, SRC)
    outdir = os.path.join(DST, os.path.dirname(rel))
    res = extract(f, outdir)
    res["path"] = rel
    report.append(res)
    if i % 50 == 0:
        print(f"  {i}/{len(pdfs)}", flush=True)

ok = [r for r in report if r.get("ok")]
no_text = [r for r in report if not r.get("ok")]
print(f"\n=== PDF EXTRACTION DONE: {len(ok)} ok, {len(no_text)} no-text/scanned ===")
with open(report_path, "w") as f:
    json.dump(report, f, indent=1)
print("saved", report_path)

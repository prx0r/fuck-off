#!/usr/bin/env python3
"""OCR the 8 scanned PDFs (image-only, no text layer) using ocrmypdf + tesseract.
Then re-extract text to 02_extracted/pdf/<section>/ and update corpus.jsonl.
"""
import os, subprocess, json

RAW = "/mnt/HC_Volume_106427611/ip-graph/data/raw/pdfs"
OCR_DIR = "/mnt/HC_Volume_106427611/ip-graph/data/extracted/pdf/_ocr"
EXTRACT_DIR = "/mnt/HC_Volume_106427611/ip-graph/data/extracted/pdf"
JSONL = "/mnt/HC_Volume_106427611/ip-graph/data/corpus.jsonl"

PDFS = [
    "introduction/Stapp_Copenhagen_Interpretation.pdf",
    "solutions/Culverwell1890.pdf",
    "solutions/Culverwell1894.pdf",
    "solutions/Quantum_Mechanics_Thermodynamics_Strong_Cosmological_Principle.pdf",
    "solutions/Sperry1966Chicago.pdf",
    "solutions/Watson_Behaviorism.pdf",
    "solutions/Wheeler.pdf",
    "solutions/gabor1946.pdf",
]
os.makedirs(OCR_DIR, exist_ok=True)

for rel in PDFS:
    src = os.path.join(RAW, rel)
    base = os.path.splitext(os.path.basename(rel))[0]
    section = os.path.dirname(rel)
    ocr_pdf = os.path.join(OCR_DIR, base + ".ocr.pdf")
    txt_out = os.path.join(EXTRACT_DIR, section, base + ".txt")
    print(f"OCR: {rel}", flush=True)
    r = subprocess.run(["ocrmypdf", "--force-ocr", "--optimize", "1",
                        src, ocr_pdf], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"   ocrmypdf error: {r.stderr.strip()[:300]}", flush=True)
        continue
    os.makedirs(os.path.dirname(txt_out), exist_ok=True)
    subprocess.run(["pdftotext", "-layout", ocr_pdf, txt_out], capture_output=True)
    sz = os.path.getsize(txt_out) if os.path.exists(txt_out) else 0
    print(f"   -> {txt_out} ({sz} bytes)", flush=True)

print("OCR pass done.")

"""lib/hermes_exec.py — the REAL execution path: wire the organism to Hermes (AGENTIC).

The honest gap: my agent_delivery.run() took a python callable — a pure abstraction with NO real
execution. This kernel makes it real: it shells to Hermes so the organism can actually GENERATE
translations, commentary, cruxes, essays — from the model — instead of hand-feeding them.

CORRECT INVOCATION (per patala docs/global/HERMES-CALLING.md + agentpatala's model.py chat_agentic):
  `hermes -z "<prompt>"` is BLIND — one-shot text completion, no file access, no tools/skills
  (~3.8% yield on translation). The CORRECT path is AGENTIC `hermes chat`:
      hermes chat -Q -q "<system>\n<user>" --yolo --max-turns 8 -m <model> --provider <provider>
  Hermes as an AGENT can read the repo, skills, and reference maps itself.

ARCHITECTURE RULE (from the shared BUILD-WIRE-HERMES-GENERATION audit):
  Hermes for GENERATION. .py for REDUCTION.
  - GENERATION (translation, commentary, essays, new pushing) -> hermes chat (agentic)
  - REDUCTION (review, staleness, evidence, gates, epistemic) -> deterministic .py
"""
from __future__ import annotations
import os, subprocess, time

HERMES_BIN = os.environ.get("HERMES_BIN", "hermes")
DEFAULT_MODEL = os.environ.get("PATALA_MODEL", "deepseek-v4-flash")
DEFAULT_PROVIDER = os.environ.get("PATALA_PROVIDER", "opencode-go")
WORKDIR = os.environ.get("PATALA_WORKDIR", "/root/projects/patala")
# the patala Hermes profile is the active, skills-loaded profile (hermes -p patala)
PROFILE = os.environ.get("HERMES_PROFILE", "patala")


class HermesError(Exception):
    pass


def _killpg(proc):
    try:
        os.killpg(os.getpgid(proc.pid), 15)  # SIGTERM the whole group
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def agentic(system, user, skills="", max_turns=8, timeout=240, session=None, model=DEFAULT_MODEL,
            provider=DEFAULT_PROVIDER, cwd=None, max_retries=2, profile=PROFILE):
    """The CORRECT agentic call: `hermes chat -Q -q` with file access + skills (not blind -z).

    Mirrors agentpatala's pipeline/model.py chat_agentic(). Hermes as an agent can read the repo +
    skills + reference maps. Returns the model output text.
    """
    cmd = [HERMES_BIN, "chat", "-Q", "-q", f"{system}\n\n{user}", "--yolo",
           "--max-turns", str(max_turns), "-m", model, "--provider", provider]
    if profile:
        cmd += ["-p", profile]
    if skills:
        cmd += ["--skills", skills]
    if session:
        cmd += ["--resume", session]
    last_err = None
    for attempt in range(max_retries):
        try:
            proc = subprocess.Popen(cmd, cwd=cwd or WORKDIR, start_new_session=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            try:
                out, _ = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                _killpg(proc)
                raise HermesError(f"hermes chat timed out after {timeout}s")
            if proc.returncode != 0:
                last_err = out.strip()[-300:] or f"exit {proc.returncode}"
                continue
            return out.strip()
        except FileNotFoundError:
            raise HermesError(f"hermes binary not found ({HERMES_BIN}); set HERMES_BIN")
        except HermesError as e:
            last_err = str(e)
            time.sleep(1 * (attempt + 1))
    raise HermesError(f"hermes chat failed after {max_retries} retries: {last_err}")


def quick(prompt_text, model=DEFAULT_MODEL, provider=DEFAULT_PROVIDER, timeout=120):
    """A quick `hermes -z` one-shot for trivial checks (NOT for translation generation)."""
    cmd = [HERMES_BIN, "-z", prompt_text, "-m", model, "--provider", provider]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, _ = proc.communicate(timeout=timeout)
        return out.strip()
    except subprocess.TimeoutExpired:
        _killpg(proc)
        return ""
    except Exception:
        return ""


def translate_karika(sanskrit, work_id="tantraloka", model=DEFAULT_MODEL):
    """Generate a real from-scratch translation of a Sanskrit kārikā via AGENTIC Hermes.

    This is the anti-theatre replacement for hand-feeding TranslationProof fields: the model actually
    translates the verse (as an agent, reading the repo/skills), and the proof is computed on real output.
    """
    system = (
        "You are a Sanskrit philologist translating the Tantrāloka from scratch. Do NOT reproduce any "
        "existing English translation. Translate literally + faithfully, then note contested terms.")
    user = (
        f"Translate this kārikā:\n\nKĀRIKĀ: {sanskrit}\n\n"
        'Output JSON: {"translation": "...", "terms": {"term": "sense"}, "contested": "..."}')
    out = agentic(system, user, model=model)
    try:
        import json
        # the agentic output has reasoning (which may contain {..} itself) + the FINAL JSON answer.
        # The reliable extraction: the LAST brace-balanced JSON object in the string (the answer).
        # Walk backward from the last '}' to the matching '{'.
        end = out.rfind("}")
        if end == -1:
            return {"translation": out, "terms": {}, "contested": "", "_raw": out}
        depth = 0
        for i in range(end, -1, -1):
            ch = out[i]
            if ch == "}": depth += 1
            elif ch == "{": depth -= 1
            if depth == 0:
                start = i
                break
        else:
            start = out.rfind("{")
        candidate = out[start:end+1]
        parsed = json.loads(candidate, strict=False)
        if isinstance(parsed, dict):
            return parsed
        return {"translation": out, "terms": {}, "contested": "", "_raw": out}
    except Exception:
        return {"translation": out, "terms": {}, "contested": "", "_raw": out}


def available():
    """Check Hermes is usable (agentic) — returns True/False, doesn't raise."""
    try:
        r = agentic("Reply with exactly: HERMES_OK", "Confirm you are the agent.", max_turns=2, timeout=60)
        return "HERMES_OK" in r or "HERMES" in r
    except Exception:
        return False


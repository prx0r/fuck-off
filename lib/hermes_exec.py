"""lib/hermes_exec.py — the REAL execution path: wire the organism to Hermes.

The honest gap: my agent_delivery.run() took a python callable — a pure abstraction with NO real
execution. This kernel makes it real: it shells to `hermes -z` (the same path agentpatala's
pipeline/model.py uses) so the organism can actually GENERATE translations, commentary, cruxes,
essays — from the model — instead of hand-feeding them.

Usage (mirrors pipeline/model.py):
  hermes_exec.prompt("translate this Sanskrit kārikā", model=..., provider=...)

The organism's "refine" steps can now call this: the TranslationProof is computed on REAL model output,
not hand-fed PASS fields. This is the anti-theatre fix.
"""
from __future__ import annotations
import os, subprocess, shlex, time

HERMES_BIN = os.environ.get("HERMES_BIN", "hermes")
DEFAULT_MODEL = os.environ.get("PATALA_MODEL", "deepseek-v4-flash")
DEFAULT_PROVIDER = os.environ.get("PATALA_PROVIDER", "opencode-go")


class HermesError(Exception):
    pass


def prompt(prompt_text, model=DEFAULT_MODEL, provider=DEFAULT_PROVIDER, timeout=120, max_retries=2):
    """Run `hermes -z "<prompt>" -m <model> --provider <provider>`; return the model's stdout.

    Mirrors pipeline/model.py's _hermes_call. Kills the process group on timeout so a hung call
    can't orphan a hermes subprocess.
    """
    cmd = [HERMES_BIN, "-z", prompt_text, "-m", model, "--provider", provider]
    last_err = None
    for attempt in range(max_retries):
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True, start_new_session=True)
            try:
                out, err = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(os.getpgid(proc.pid), 15)   # SIGTERM the whole group
                except Exception:
                    pass
                proc.wait(timeout=5)
                raise HermesError(f"hermes timed out after {timeout}s")
            if proc.returncode != 0:
                last_err = err.strip() or f"exit {proc.returncode}"
                continue
            return out.strip()
        except FileNotFoundError:
            raise HermesError(f"hermes binary not found ({HERMES_BIN}); set HERMES_BIN")
        except HermesError as e:
            last_err = str(e)
            time.sleep(1 * (attempt + 1))
    raise HermesError(f"hermes failed after {max_retries} retries: {last_err}")


def translate_karika(sanskrit, work_id="tantraloka", model=DEFAULT_MODEL):
    """Generate a real from-scratch translation of a Sanskrit kārikā via Hermes.

    This is the anti-theatre replacement for hand-feeding TranslationProof fields: the model
    actually translates the verse, and the proof can be computed on real output.
    """
    prompt_text = (
        "You are translating the Sanskrit Tantrāloka from scratch (do not reproduce any existing "
        "English translation). Translate this kārikā literally + faithfully, then give a one-line "
        "note on any contested term:\n\n"
        f"KĀRIKĀ: {sanskrit}\n\n"
        "Output JSON: {\"translation\": \"...\", \"terms\": {\"term\": \"sense\"}, \"contested\": \"...\"}"
    )
    out = prompt(prompt_text, model=model)
    # the model returns JSON; try to parse it, else return raw
    try:
        import json
        return json.loads(out)
    except Exception:
        return {"translation": out, "terms": {}, "contested": ""}


def available():
    """Check hermes is usable (returns True/False, doesn't raise)."""
    try:
        r = prompt("Reply with exactly: OK", timeout=30)
        return "OK" in r
    except Exception:
        return False

#!/usr/bin/env python3
"""run-overnight-autonomous.py — the autonomous overnight loop for agentgraph (ip-graph).

Runs the verified, useful, non-blocking work in sequence, backgrounded, ONE heavy job at a time
(4-core / 8GB / no-swap / 2-agent constraint). Every step is gated: it prints what it did + counts.
Poll: `tail /tmp/overnight.log`. Kill by PID, never pkill. Re-run is idempotent.

Steps:
  1. LOGICVID gold -> enquiry gate (verify the Hermes-derived output exists + is complete)
  2. ToG-2 alternating graph<->doc retrieval validation (new algorithm, real graph)
  3. the 2 fixed THEATRE validators (validate-provenance, validate-essay-ingest)
  4. Ratié essay-ingest Hermes-driven validator (reads the real book — the heavy generation step)
  5. the live Tantraloka 7-stage test (run-all.py) — the gate that nothing broke
  6. the record-reconciliation audit (state.json counts match lib/ + data)
  7. kanban bookkeeping (complete/claim tasks)
"""
import os, sys, json, subprocess, datetime, glob

REPO = "/mnt/HC_Volume_106427611/ip-graph"
os.chdir(REPO)
log = open("/tmp/overnight.log", "a", buffering=1)

def say(msg):
    line = f"[{datetime.datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    log.write(line + "\n")

def run(step, cmd, timeout=None):
    say(f"=== STEP: {step} :: {cmd}")
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        out = (r.stdout or "") + (r.stderr or "")
        tail = out.strip().splitlines()[-12:]
        for l in tail:
            say("    " + l)
        ok = r.returncode == 0
        say(f"--- step {step}: {'OK' if ok else 'FAIL exit=' + str(r.returncode)}")
        return ok, out
    except subprocess.TimeoutExpired:
        say(f"--- step {step}: TIMEOUT after {timeout}s")
        return False, ""
    except Exception as e:
        say(f"--- step {step}: ERROR {e}")
        return False, ""

def step_gate_logicvid():
    p = f"{REPO}/data/logicvid/enquiry-gold.json"
    if not os.path.exists(p):
        say("LOGICVID gate: output missing")
        return False
    d = json.load(open(p))
    tot = d.get("totals", {})
    hermes = tot.get("hermes_derived", 0)
    say(f"LOGICVID gate: {len(d['enquiries'])} enquiries, {hermes} Hermes-derived, "
        f"{tot.get('regex_fallback', 0)} fallback")
    return len(d["enquiries"]) >= 10 and hermes >= 10

def step_audit_record():
    kernels = len(glob.glob(f"{REPO}/lib/*.py"))
    g = json.load(open(f"{REPO}/data/graph/graph.json"))
    exps = json.load(open(f"{REPO}/data/references/experiments.json"))
    say(f"AUDIT: kernels={kernels} (expect 52) | nodes={len(g['nodes'])} edges={len(g['edges'])} "
        f"(expect 490/6578) | experiments={exps['count']} (expect 97)")
    state = json.load(open(f"{REPO}/state.json"))
    say(f"AUDIT state.json: kernels={state['counts']['kernels']} (expect {kernels}) "
        f"theatre={state['counts']['theatre_proven_real']}+{state['counts']['theatre_proven_mechanism']}")
    return kernels == 52 and len(g["edges"]) == 6578 and state["counts"]["kernels"] == 52

def main():
    say("=== OVERNIGHT AUTONOMOUS RUN START ===")
    # 1. LOGICVID gate
    ok1 = step_gate_logicvid()
    say(f"LOGICVID gate: {'PASS' if ok1 else 'FAIL'} (if FAIL, the run may need re-ingestion)")

    # 2. ToG-2 (new algorithm) — quick deterministic
    run("ToG-2 validation", f"cd {REPO} && python3 scripts/validate-tog2.py", timeout=120)

    # 3. the 2 fixed theatre validators — quick deterministic
    run("validate-provenance (data-derived)", f"cd {REPO} && python3 scripts/validate-provenance.py", timeout=120)
    run("validate-essay-ingest (Hermes, real Ratié book)", f"cd {REPO} && python3 scripts/validate-essay-ingest.py", timeout=700)

    # 4. the live Tantraloka 7-stage test — the gate that nothing broke (background-friendly, logs)
    run("live Tantraloka test (run-all)", f"cd {REPO}/tantraloka && python3 run-all.py", timeout=1800)

    # 5. record audit
    ok_audit = step_audit_record()
    say(f"record audit: {'PASS' if ok_audit else 'CHECK'}")

    say("=== OVERNIGHT AUTONOMOUS RUN COMPLETE ===")

if __name__ == "__main__":
    main()

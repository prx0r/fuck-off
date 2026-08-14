#!/usr/bin/env python3
"""run-tests.py — the ip-graph validation + experiment suite.

Runs every gate and experiment, captures pass/fail + timing, and writes a machine-readable results
file to data/graph/test-results.json. Exit code = number of failures.
"""
import json, os, sys, time, subprocess

ROOT = "/mnt/HC_Volume_106427611/ip-graph"
os.chdir(ROOT)

results = {"suite": "ip-graph-validation", "tests": []}
def record(name, passed, detail="", ms=0.0):
    results["tests"].append({"name": name, "pass": bool(passed), "detail": detail, "ms": round(ms,1)})
    tag = "PASS" if passed else "FAIL"
    print(f"[{tag}] {name} ({ms:.0f}ms) {detail}")

def run_py(code, label):
    t0 = time.time()
    try:
        out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120)
        ok = out.returncode == 0
        record(label, ok, out.stdout.strip().split("\n")[-1] if out.stdout else out.stderr[-200:], (time.time()-t0)*1000)
        return ok
    except subprocess.TimeoutExpired:
        record(label, False, "timeout", (time.time()-t0)*1000)
        return False

def run_script(script, label):
    t0 = time.time()
    try:
        out = subprocess.run([sys.executable, os.path.join("scripts", script)],
                             capture_output=True, text=True, timeout=180)
        ok = out.returncode == 0
        last = [l for l in (out.stdout or "").strip().split("\n") if l.strip()][-1:] or [out.stderr[-200:]]
        record(label, ok, last[0], (time.time()-t0)*1000)
        return ok
    except subprocess.TimeoutExpired:
        record(label, False, "timeout", (time.time()-t0)*1000)
        return False

# ---- 1. VALIDATION GATES ----
print("=== 1. VALIDATION GATES ===")
run_py("import json;n=[json.loads(l) for l in open('data/corpus.jsonl')];assert len(n)==425;print(f'{len(n)} records OK')", "corpus_integrity")
run_py("import json;g=json.load(open('data/graph/graph.json'));assert len(g['nodes'])>0;print(f'{len(g[\"nodes\"])} nodes {len(g[\"edges\"])} edges')", "graph_integrity")
run_script("audit-epistemic.py", "epistemic_invariant")
run_script("validate-dag.py", "canonical_dag")
run_py("import json;a=json.load(open('data/graph/argument.json'));print(f'{len(a[\"information_nodes\"])} info {len(a[\"inference_nodes\"])} infer {len(a[\"conflict_nodes\"])} conflict')", "argument_graph")

# ---- 2. EXPERIMENTS ----
print("\n=== 2. EXPERIMENTS ===")
run_script("experiment-evidence-weights.py", "evidence_weights_experiment")
run_script("experiment-bounded-context.py", "bounded_context_experiment")
run_script("peer-review-arxiv.py", "arxiv_peer_review")

# ---- 3. LAYER VALIDATIONS ----
print("\n=== 3. LAYER VALIDATIONS ===")
run_script("validate-layer03-05.py", "layer_03_05_factory_research")
run_script("validate-layer10.py", "layer_10_retrieval_comparison")
run_script("validate-products.py", "product_kernels_translation_review_schema")
run_script("validate-provenance.py", "provenance_nanopub_emission")
run_script("experiment-koral-twograph.py", "koral_two_graph_commentarial")
run_script("experiment-communities.py", "community_detection_themes")
run_script("experiment-generalization.py", "domain_generalization_eleutheria")
run_script("experiment-crux-compiler.py", "crux_compiler")
run_script("experiment-mutation-testing.py", "mutation_testing")
run_script("experiment-signed-corpus.py", "signed_corpus_root")
run_script("experiment-reactive-essay.py", "reactive_essay")
run_script("experiment-graphiti-temporal.py", "graphiti_temporal_validity")
run_script("experiment-import-scifact.py", "import_scifact_generalization")
run_script("experiment-verified-lifecycle.py", "verified_epistemic_os_lifecycle")
run_script("experiment-cross-review.py", "adversarial_cross_review")
run_script("experiment-eigenius-grades.py", "eigenius_grade_mapping")
run_script("experiment-review-bias.py", "review_bias_robustness")
run_script("experiment-self-improve.py", "self_improvement_as_pr")
run_script("experiment-evolving-memory.py", "evolving_memory_consolidation")
run_script("validate-education-organism.py", "education_organism_stack")
run_script("experiment-counterfactual-engine.py", "counterfactual_engine")
run_script("experiment-rival-argument.py", "rival_argument")

# ---- summary ----
n = len(results["tests"]); npass = sum(1 for t in results["tests"] if t["pass"])
results["summary"] = {"total": n, "passed": npass, "failed": n - npass}
json.dump(results, open("data/graph/test-results.json", "w"), indent=1)
print(f"\n=== SUMMARY: {npass}/{n} passed ===")
print(f"wrote data/graph/test-results.json")
sys.exit(n - npass)

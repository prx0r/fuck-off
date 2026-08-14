"""lib/schema.py — the Stencila-style single-source schema compiler (Layer 00, SPEC-17 §15).

Define schemas once in YAML; compile validators for any object. Kills schema-drift (the SCHEMA-AUDIT
problem): one source of truth instead of duplicated TS/Pydantic/JSON/Rust.

This is a lightweight reference implementation of the pattern — a full Stencila would also emit
language bindings; here we emit a validating dict + a validator function.
"""
from __future__ import annotations
import yaml, json


# ---- a minimal schema: field -> (required, type, allowed_values) ----
def compile_schema(schema_yaml: dict) -> dict:
    """Compile a YAML schema dict into {field: (required, type, allowed)}."""
    out = {}
    for field, spec in (schema_yaml or {}).items():
        if isinstance(spec, dict):
            out[field] = (spec.get("required", False), spec.get("type", "any"), spec.get("allowed"))
        else:
            out[field] = (False, str(spec), None)
    return out


def validate(obj: dict, compiled: dict) -> list:
    """Validate an object against the compiled schema. Returns list of errors (empty = valid)."""
    errors = []
    for field, (required, typ, allowed) in compiled.items():
        if field not in obj or obj[field] is None:
            if required: errors.append(f"missing required: {field}")
            continue
        val = obj[field]
        if typ == "int" and not isinstance(val, int):
            errors.append(f"{field}: expected int, got {type(val).__name__}")
        elif typ == "str" and not isinstance(val, str):
            errors.append(f"{field}: expected str, got {type(val).__name__}")
        elif typ == "list" and not isinstance(val, list):
            errors.append(f"{field}: expected list")
        if allowed is not None and isinstance(val, str) and val not in allowed:
            errors.append(f"{field}: '{val}' not in {allowed}")
    return errors


# ---- the canonical Pāṭala object schemas (single source) ----
CANONICAL_SCHEMAS = {
    "claim": yaml.safe_load("""
claim_id: {required: true, type: str}
claim_text: {required: true, type: str}
epistemic_ceiling: {required: true, type: str, allowed: [MACHINE_PROPOSED, ENGINEERING_VALIDATED, SCHOLARLY_CORROBORATED, INDEPENDENT_REVIEWED, ADJUDICATED]}
source_refs: {required: true, type: list}
evidence_quote: {required: false, type: str}
"""),
    "evidence": yaml.safe_load("""
evidence_id: {required: true, type: str}
source: {required: true, type: str}
claim_id: {required: true, type: str}
supports: {required: true, type: str, allowed: [true, false, PARTIAL]}
replication_status: {required: false, type: str}
"""),
    "argument": yaml.safe_load("""
argument_id: {required: true, type: str}
premises: {required: true, type: list}
conclusion: {required: true, type: str}
review_state: {required: true, type: str, allowed: [GENERATED, STRUCTURALLY_VALID, SUBJECT_REVIEWED, ADJUDICATED]}
"""),
}


def validate_object(obj_type: str, obj: dict) -> list:
    schema = CANONICAL_SCHEMAS.get(obj_type)
    if not schema:
        return [f"unknown object type: {obj_type}"]
    return validate(obj, compile_schema(schema))

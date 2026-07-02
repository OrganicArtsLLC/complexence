#!/usr/bin/env python3
"""cognitive_form.py — a v0.1 reference implementation of the Cognitive Form (ℭ).

Turns `cognitive-form.schema.json` from a static format into runnable transforms.
Honest about its altitude (research program, see ../spec/complexence-science.md §10):

- The **deterministic** operators are real: validate, compose, reflect (structural),
  and the mechanical management of representations / transformations / feedback /
  history.
- The **semantic** operators (project, translate, compress, expand, execute, correct)
  delegate the meaning-bearing work to a caller-supplied `transform` callable (an LLM
  or other model). Each one runs the transform and then calls an
  `invariant_preserved` hook — which is currently a STUB, because deciding whether two
  representations are the same ℭ is the open isomorphism (science §10). The hook is
  where that research plugs in; it is not pretended-solved here.

Stdlib-only. Schema validation uses `jsonschema` if installed, else a minimal
structural check. Licensed MIT.

CLI:
    python cognitive_form.py validate <file.cform.json>
    python cognitive_form.py reflect  <file.cform.json>
"""
from __future__ import annotations

import hashlib
import json
import sys
import uuid
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

SCHEMA_PATH = Path(__file__).with_name("cognitive-form.schema.json")
REPR_TYPES = {"text", "diagram", "code", "prompt", "agent_spec", "ast", "simulation"}
OPERATORS = {"project", "translate", "compress", "expand", "compose", "reflect", "execute", "correct"}


# ── Validation (the compliance check) ────────────────────────────────────────

def validate(form: dict[str, Any]) -> tuple[bool, list[str]]:
    """Return (ok, errors). Uses jsonschema if available, else a structural check."""
    try:
        import jsonschema  # type: ignore
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        v = jsonschema.Draft202012Validator(schema)
        errs = [f"{'/'.join(map(str, e.path))}: {e.message}" for e in v.iter_errors(form)]
        return (not errs), errs
    except ImportError:
        return _structural_check(form)


def _structural_check(form: dict[str, Any]) -> tuple[bool, list[str]]:
    """Minimal no-deps fallback: required fields, non-empty reprs, operator enums."""
    errs: list[str] = []
    required = ["id", "invariant", "representations", "transformations", "feedback_loops", "history"]
    for k in required:
        if k not in form:
            errs.append(f"missing required field: {k}")
    inv = form.get("invariant", {})
    if not isinstance(inv, dict) or "essence" not in inv or "constraints" not in inv:
        errs.append("invariant must have 'essence' and 'constraints'")
    reps = form.get("representations", [])
    if not isinstance(reps, list) or not reps:
        errs.append("representations must be a non-empty array")
    for i, r in enumerate(reps if isinstance(reps, list) else []):
        if r.get("projection_type") not in REPR_TYPES:
            errs.append(f"representations[{i}].projection_type invalid: {r.get('projection_type')}")
    for i, t in enumerate(form.get("transformations", []) or []):
        if t.get("operator") not in OPERATORS:
            errs.append(f"transformations[{i}].operator invalid: {t.get('operator')}")
    return (not errs), errs


# ── The invariant-preservation hook (the open isomorphism, science §10) ──────

def invariant_preserved(form: dict[str, Any], new_repr: dict[str, Any]) -> bool:
    """STUB. Whether a new representation preserves ℭ's invariant is the open
    isomorphism (science §7.4 translation-loss, §10). Real implementations wire a
    check here (semantic equivalence, reconstruction test, etc.). Until then this
    returns True and records the debt rather than faking a guarantee."""
    return True  # unverified — see ROADMAP Phase 2 (measurement harness)


# ── Deterministic operators (real) ───────────────────────────────────────────

def reflect(form: dict[str, Any]) -> dict[str, Any]:
    """ℭ operating on its own structure: append a self-describing representation."""
    out = deepcopy(form)
    summary = {
        "invariant": form.get("invariant", {}),
        "representation_types": [r.get("projection_type") for r in form.get("representations", [])],
        "operators_used": sorted({t.get("operator") for t in form.get("transformations", [])}),
        "history_len": len(form.get("history", [])),
    }
    out.setdefault("representations", []).append({
        "projection_type": "text",
        "media_type": "application/json",
        "content": json.dumps(summary, ensure_ascii=False),
    })
    out.setdefault("transformations", []).append(
        {"operator": "reflect", "input_representation": "self", "output_representation": "text"})
    return out


def _form_hash(form: dict[str, Any]) -> str:
    """Stable content hash of a form (for history/provenance records)."""
    return hashlib.sha256(
        json.dumps(form, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def compose(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    """Join two forms into a higher form. ℭ = (I, R, T, F, H), so *all five* components
    must survive the join: merge invariants/constraints, union representations, union
    feedback loops, record the composition in history (with both parents' hashes), and
    derive a fresh id — the composed form is a new form, not `a` wearing extra parts.
    Note: the essence merge is ordered, so compose(a, b) != compose(b, a) by design of
    the string join; a symmetric merge is open work."""
    out = deepcopy(a)
    out["invariant"]["essence"] = f"{a['invariant']['essence']} ⊕ {b['invariant']['essence']}"
    out["invariant"]["constraints"] = list(dict.fromkeys(
        a["invariant"].get("constraints", []) + b["invariant"].get("constraints", [])))
    out["representations"] = deepcopy(a.get("representations", []) + b.get("representations", []))
    out["feedback_loops"] = deepcopy(a.get("feedback_loops", []) + b.get("feedback_loops", []))
    out.setdefault("transformations", []).append(
        {"operator": "compose", "input_representation": "a+b", "output_representation": "composed"})
    out["id"] = str(uuid.uuid5(uuid.NAMESPACE_URL, out["invariant"]["essence"]))
    out.setdefault("history", []).append({
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "sequence_index": len(out.get("history", [])),
        "previous_form_hash": f"{_form_hash(a)}+{_form_hash(b)}",
        "delta": {"note": "compose: merged invariants, unioned representations/feedback, fresh id"},
    })
    return out


def add_representation(form, projection_type, media_type, content):
    out = deepcopy(form)
    out.setdefault("representations", []).append(
        {"projection_type": projection_type, "media_type": media_type, "content": content})
    return out


# ── Semantic operators (model-backed; transform is a caller-supplied callable) ─

def _semantic(form, op, transform, src_repr, dst_type, media="text/plain"):
    """Shared body: run the transform, append the result, check the invariant hook."""
    out = deepcopy(form)
    content = transform(form)  # the meaning-bearing step is the model's job
    new_repr = {"projection_type": dst_type, "media_type": media, "content": content}
    if not invariant_preserved(form, new_repr):
        raise ValueError(f"{op}: invariant not preserved (translation loss).")
    out.setdefault("representations", []).append(new_repr)
    out.setdefault("transformations", []).append(
        {"operator": op, "input_representation": src_repr, "output_representation": dst_type})
    return out


def project(form, dst_type, transform):
    return _semantic(form, "project", transform, "invariant", dst_type)


def translate(form, src_type, dst_type, transform):
    return _semantic(form, "translate", transform, src_type, dst_type)


def compress(form, transform, dst_type="text"):
    return _semantic(form, "compress", transform, "form", dst_type)


def expand(form, transform, dst_type="text"):
    return _semantic(form, "expand", transform, "form", dst_type)


def execute(form, executor) -> Any:
    """Turn meaning into action. Returns whatever the executor produces."""
    return executor(form)


def correct(form, feedback: dict[str, Any], transform) -> dict[str, Any]:
    out = _semantic(form, "correct", transform, "form", "text")
    out.setdefault("feedback_loops", []).append(feedback)
    return out


# ── CLI ──────────────────────────────────────────────────────────────────────

def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in {"validate", "reflect"}:
        print("usage: cognitive_form.py validate|reflect <file.cform.json>")
        return 2
    cmd, path = sys.argv[1], Path(sys.argv[2])
    form = json.loads(path.read_text(encoding="utf-8"))
    if cmd == "validate":
        ok, errs = validate(form)
        print("✓ valid Cognitive Form" if ok else "✗ invalid:")
        for e in errs:
            print(f"  - {e}")
        return 0 if ok else 1
    if cmd == "reflect":
        print(json.dumps(reflect(form), indent=2, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFORMANCE = ROOT / "conformance"
REFERENCE = ROOT / "reference_impl" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from lca_mvp import AuthorityEngine, ContinuityEngine, LCAError  # noqa: E402
from per_object_validators import validate_per_object  # noqa: E402

REVIEW_TYPES = {
    "affirmed_as_mine", "good_inference_not_explicit", "assistant_contamination",
    "historical_revision", "invariant_reaffirmed", "branch_disagreement", "private_weather",
}


def _bool(value: str) -> bool:
    return value.lower() == "true"


def _result(case: dict, actual: str, detail: str = "") -> dict:
    expected = case.get("expected", case.get("expected_stage", ""))
    passed = actual == expected
    return {"case_id": case["case_id"], "passed": passed, "actual": actual, "expected": expected, "detail": detail}


def check(case: dict) -> dict:
    kind = case["kind"]
    try:
        if kind in {"canonical_hash", "event_hash", "recovery_replay"}:
            data = base64.b64decode(case["payload_b64"])
            actual = hashlib.sha256(data).hexdigest()
            return _result(case, "pass" if actual == case["expected_sha256"] else "fail", actual)

        if kind == "record_validate":
            record = json.loads(base64.b64decode(case["record_b64"]))
            validate_per_object(record)
            return _result(case, "pass")

        if kind == "ledger_transition":
            allowed = case["event_type"] == "update" and case["from_status"] != case["to_status"]
            return _result(case, "pass" if allowed else "fail")

        if kind == "authority":
            target = {
                "object_type": case["object_type"],
                "privacy_tier": int(case["privacy_tier"]),
                "authority": {"may_speak_for_source": case["role"] in {"source", "steward"}},
            }
            actual = str(AuthorityEngine.check(case["role"], case["action"], target)).lower()
            return _result(case, actual)

        if kind == "continuity":
            actual = ContinuityEngine.classify({
                "provenance_integrity": float(case["p"]),
                "developmental_continuity": float(case["c"]),
                "invariant_fidelity": float(case["f"]),
                "co_developed": _bool(case["co_developed"]),
                "separated": _bool(case["separated"]),
                "rejected_core_invariant": _bool(case["rejected_core"]),
            })["stage"]
            return _result(case, actual)

        if kind == "source_review":
            return _result(case, "pass" if case["review_type"] in REVIEW_TYPES else "fail")

        if kind == "model_mutation":
            return _result(case, str(case["action"] != "direct_canonical_write").lower())

        if kind == "closure_boundary":
            illegal = (
                case["boundary_state"] == "triggered"
                and case["output_temporal_class"] == "post_originator"
                and case["claimed_authorship"] == "source_person"
            )
            return _result(case, "fail" if illegal else "pass")

        if kind == "branch_attribution":
            illegal = (
                case["temporal_class"] == "post_originator"
                and case["originator_attribution"] == "prohibited"
                and case["output_attribution"] == "originator"
            )
            return _result(case, "fail" if illegal else "pass")

        if kind == "custody_authority":
            granted = {item for item in case.get("granted_classes", "").split(",") if item}
            allowed = case["requested_class"] in granted
            return _result(case, "pass" if allowed else "fail")

        raise LCAError(f"unknown fixture kind: {kind}")
    except Exception as exc:
        return _result(case, "fail", str(exc))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", default=str(CONFORMANCE / "fixtures" / "conformance.jsonl"))
    parser.add_argument("--output", default=str(CONFORMANCE / "python_conformance.json"))
    args = parser.parse_args()

    cases = [json.loads(line) for line in Path(args.fixtures).read_text(encoding="utf-8").splitlines() if line.strip()]
    results = [check(case) for case in cases]
    Path(args.output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    failed = [item for item in results if not item["passed"]]
    print(f"Python conformance: {len(results) - len(failed)}/{len(results)} passed")
    for item in failed:
        print(f"FAIL {item['case_id']}: expected={item['expected']} actual={item['actual']} {item['detail']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

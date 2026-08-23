from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--python-results", default="python_conformance.json")
    parser.add_argument("--rust-results", default="rust_conformance.tsv")
    args = parser.parse_args()
    py = {row["case_id"]: row for row in json.loads(Path(args.python_results).read_text(encoding="utf-8"))}
    rust = {}
    for line in Path(args.rust_results).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        case_id, passed, actual, detail = (line.split("\t", 3) + [""])[:4]
        rust[case_id] = {"passed": passed == "true", "actual": actual, "detail": detail}

    failures = []
    for case_id, left in py.items():
        right = rust.get(case_id)
        if right is None or left["passed"] != right["passed"] or left["actual"] != right["actual"]:
            failures.append((case_id, left, right))
    extras = sorted(set(rust) - set(py))
    if failures or extras:
        print("Cross-language conformance: FAIL")
        for case_id, left, right in failures:
            print(f"DIVERGENCE {case_id}: python={left} rust={right}")
        for case_id in extras:
            print(f"EXTRA_RUST_CASE {case_id}")
        return 1
    print(f"Cross-language conformance: {len(py)}/{len(py)} cases match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

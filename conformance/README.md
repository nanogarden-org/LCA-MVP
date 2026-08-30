# LCA conformance package

This directory contains the shared, language-neutral conformance suite for the LCA MVP. It checks the stable semantic boundary across the Python reference runner and an independent dependency-free Rust runner.

## Contents

- `fixtures/conformance.jsonl` — shared language-neutral fixtures.
- `python/per_object_validators.py` — per-object validator rules layered over the common schema envelope.
- `python/run_conformance.py` — Python conformance runner.
- `python/compare_results.py` — cross-language result comparator.
- `rust/src/main.rs` — dependency-free Rust conformance runner with deterministic SHA-256 and the same decision rules.

The Python runner uses the existing reference `canonical_json` and `sha256` functions. The Rust runner independently verifies the canonical fixture bytes and reproduces the same hashes and decisions without importing the Python implementation.

## Current verification

At the current `0.1.0-alpha / MVP 001a` checkpoint:

- Python: **18/18 fixtures pass**;
- Rust: **18/18 fixtures pass**; and
- cross-language comparison: **18/18 cases match**.

The comparison fails if either implementation disagrees on a case's pass/fail result or actual decision value.

## Run the Python reference

From this directory:

```text
python python/run_conformance.py --output python_conformance.json
```

## Run the Rust runner

From this directory:

```text
rustc rust/src/main.rs -O -o rust_runner.exe
rust_runner.exe fixtures/conformance.jsonl rust_conformance.tsv
```

The generated result files and executable are local verification artifacts; they are not required source files.

## Compare both implementations

```text
python python/compare_results.py --python-results python_conformance.json --rust-results rust_conformance.tsv
```

## Conformance scope

The fixtures cover:

1. per-object record validation;
2. canonical payload hashing;
3. ledger transition rules;
4. authority and private-weather decisions;
5. P/C/F/A continuity classification;
6. SourceReview acceptance/rejection;
7. recovery payload hashing;
8. event hashing;
9. direct ML mutation denial; and
10. proposal-only ML permission.

The Rust runner intentionally does not implement the entire LCA platform. It implements the narrow hardening boundary: parse enough of the shared fixture, verify deterministic hashes, evaluate high-consequence decisions, and reject direct canonical mutation.

## Signature boundary

This runnable slice verifies deterministic hashes, not public-key signatures. That is an intentional dependency boundary: the conformance semantics are stable, while the signed-event profile still needs a pinned Ed25519 implementation and signed fixtures. A future Rust hardening step should add that verified crypto dependency before accepting externally signed events. A hash match must never be interpreted as proof of signer identity.

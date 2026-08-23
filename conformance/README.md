# LCA conformance package

This package is the next implementation milestone for LCA. It tests the stable semantic interfaces before moving the ledger and authority boundary into Rust.

## Contents

- `fixtures/conformance.jsonl`: shared language-neutral fixtures.
- `python/per_object_validators.py`: per-object validator rules layered over the common schema envelope.
- `python/run_conformance.py`: Python reference runner.
- `python/compare_results.py`: cross-language result comparator.
- `rust/src/main.rs`: dependency-free Rust conformance runner with deterministic SHA-256 and the same decision rules.

The Python runner uses the existing reference `canonical_json` and `sha256` functions. The Rust runner independently verifies the canonical fixture bytes and reproduces the same hashes and decisions without importing the Python implementation.

## Run the Python reference

From `conformance`:

```text
python python/run_conformance.py --output python_conformance.json
```

## Run the Rust runner

From `conformance`:

```text
rustc rust/src/main.rs -O -o rust_runner.exe
rust_runner.exe fixtures/conformance.jsonl rust_conformance.tsv
```

## Compare both implementations

```text
python python/compare_results.py --python-results python_conformance.json --rust-results rust_conformance.tsv
```

The comparison fails if either implementation disagrees on a case’s pass/fail result or actual decision value.

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
9. direct ML mutation denial;
10. proposal-only ML permission.

The Rust runner intentionally does not implement the entire LCA platform. It implements the narrow hardening boundary: parse enough of the shared fixture, verify deterministic hashes, evaluate high-consequence decisions, and reject direct canonical mutation.

## Signature boundary

This first runnable slice verifies deterministic hashes, not public-key signatures. That is an intentional dependency boundary: the conformance semantics are now stable, while the signed-event profile still needs a pinned Ed25519 implementation and signed fixtures. The Rust hardening step should add that verified crypto dependency before accepting externally signed events. A hash match must never be interpreted as proof of signer identity.

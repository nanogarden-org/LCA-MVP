# LCA Conformance and Hardening Package

## Purpose

This package turns the stable part of LCA's architecture into executable conformance semantics. It is deliberately narrower than a complete platform: the Python implementation is the reference for the current semantic contract, while Rust independently checks the high-consequence boundary that ML and interface components must not bypass.

The package is the gate between the conceptual MVP and a hardened service:

```text
shared fixtures
    -> Python reference decisions
    -> Rust independent decisions
    -> cross-language comparison
    -> only then expand the Rust boundary
```

## Package contents

- `conformance/fixtures/conformance.jsonl` — language-neutral cases for records, hashes, ledger transitions, authority, continuity, review, recovery, and ML mutation permissions.
- `conformance/python/per_object_validators.py` — per-object content requirements layered over the common `lca-schema-0.1` envelope.
- `conformance/python/run_conformance.py` — Python reference runner.
- `conformance/python/compare_results.py` — comparison of Python and Rust actual decisions.
- `conformance/rust/src/main.rs` — dependency-free Rust runner for parsing fixture records, deterministic SHA-256, authority, continuity, review, ledger, recovery, and ML-boundary checks.

## Current gate

The current package passes 18/18 fixtures in Python, 18/18 in Rust, and 18/18 cross-language comparison. The shared hash fixtures use canonical JSON bytes and verify that both implementations calculate the same SHA-256 results for records, events, and replay payloads.

The intended Rust sequence is now explicit:

```text
parse record
 -> verify schema envelope
 -> verify canonical hash
 -> evaluate authority/privacy
 -> accept or reject transition
 -> append event
 -> replay deterministically
```

The current runner covers the first semantic slice. The next Rust hardening increment should add a real signed-event fixture after the cryptographic profile is pinned. Ed25519 verification must use a reviewed, version-pinned cryptographic crate or platform provider; a hash is not treated as a signature, and this package does not pretend otherwise.

## Exit criteria before broadening Rust

1. Every object type has at least one valid and one invalid fixture.
2. Canonical serialization is specified in one profile and tested against independent implementations.
3. Signed event envelopes have valid, invalid, wrong-key, and altered-payload fixtures.
4. Replay detects missing, reordered, duplicated, or tampered events.
5. Authority fixtures cover role, purpose, privacy tier, domain, and explicit grant conditions.
6. ML proposals can be accepted only through the same review and ledger boundary as human or steward changes.

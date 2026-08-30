# LCA Python reference implementation

This directory contains the Python-first executable slice of LCA. It is intentionally dependency-light so the semantic contract can be tested before choosing a production database, vector service, or model provider.

## Current status

At the current `0.1.0-alpha / MVP 001a` checkpoint, the reference implementation's **11/11 behavior tests pass**, and the demo completes with an intact ledger and no integrity failures.

## Run

From this directory:

```text
python -m unittest discover -s tests -v
python run_demo.py
```

The test suite can also be run with pytest:

```text
python -m pytest -q tests
```

The implementation demonstrates:

- canonical record envelopes;
- immutable versions;
- append-only event history;
- hash-chain integrity checking;
- typed relations;
- basic retrieval;
- source review records;
- continuity classification;
- authority checks; and
- recovery-oriented snapshots.

ML adapters should be added around this core as proposal-only services. They must not directly mutate the store.

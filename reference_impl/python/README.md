# LCA Python reference implementation

This is the Python-first executable slice of LCA. It is intentionally dependency-light so that the semantic contract can be tested before choosing a production database, vector service, or model provider.

## Run

```text
python -m unittest discover -s tests -v
python run_demo.py
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
- authority checks;
- and recovery-oriented snapshots.

ML adapters should be added around this core as proposal-only services. They must not directly mutate the store.


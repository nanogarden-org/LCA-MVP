# Rust core path

The MVP should remain Python-first while the object model and evaluation suite are still changing. A later Rust core should implement the stable, high-consequence boundary:

- canonical record parsing;
- deterministic serialization;
- append-only ledger writes;
- hash/signature verification;
- lifecycle transitions;
- authority and privacy decisions;
- snapshot/replay/recovery;
- and a typed API that ML workers cannot bypass.

The Rust implementation should be tested against the Python reference using the same canonical JSONL fixtures. It should not introduce a second meaning for Archive, Portrait, Bud, Branch, provenance, or authority.

Suggested future crate layout:

```text
lca-core/
  src/
    record.rs
    provenance.rs
    ledger.rs
    policy.rs
    recovery.rs
    conformance.rs
```

The first Rust milestone is not a high-performance graph database. It is a small, deterministic policy/ledger core that can reject an unauthorized write and reproduce the same event-chain result as the Python reference.


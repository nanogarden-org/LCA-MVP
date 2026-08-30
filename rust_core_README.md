# Rust core path

The LCA MVP remains Python-first while the object model and evaluation suite evolve. The repository currently includes an independent, dependency-free Rust conformance runner at [conformance/rust/src/main.rs](./conformance/rust/src/main.rs). That runner validates the narrow hardening boundary against the shared fixtures; it is not yet a complete Rust core crate.

At the current checkpoint, the Rust runner passes **18/18 conformance fixtures** and matches the Python decisions and deterministic hashes in **18/18 comparisons**. See the [conformance package README](./conformance/README.md) for the exact commands.

## Planned Rust boundary

A future Rust core should implement the stable, high-consequence boundary:

- canonical record parsing;
- deterministic serialization;
- append-only ledger writes;
- hash/signature verification;
- lifecycle transitions;
- authority and privacy decisions;
- snapshot/replay/recovery; and
- a typed API that ML workers cannot bypass.

The Rust implementation should continue to be tested against the Python reference using the same canonical JSONL fixtures. It should not introduce a second meaning for Archive, Portrait, Bud, Branch, provenance, or authority.

## Suggested future crate layout

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

The first full Rust-core milestone is not a high-performance graph database. It is a small, deterministic policy and ledger core that can reject an unauthorized write and reproduce the same event-chain result as the Python reference.

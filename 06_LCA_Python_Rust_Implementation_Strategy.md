# LCA Python/Rust implementation strategy

## Recommendation

Use a **Python-first reference implementation with a Rust hardening path**.

Python is the right first language for LCA because the initial uncertainty is semantic and experimental: schema iteration, document ingestion, retrieval experiments, evaluation harnesses, model adapters, and source-review workflows will change quickly. Python also has the broadest current ecosystem for NLP, data validation, evaluation, and ML orchestration.

Rust should be introduced where correctness, isolation, tamper resistance, concurrency, and deployment footprint matter more than experimentation speed. The Rust layer should not define LCA semantics independently. It should implement a conformance-tested subset of the already-defined record, ledger, policy, and recovery contracts.

## Proposed split

```text
Python
├── ingestion and document adapters
├── YAML/Markdown/JSON bindings
├── schema validation and migrations
├── ML extraction, retrieval, reranking, and response adapters
├── evaluation harness and fixture generation
├── review workflow and research notebook layer
└── reference API / CLI

Rust
├── canonical record parser and canonicalizer
├── append-only ledger writer
├── hash/signature verification
├── authority and privacy policy evaluator
├── snapshot/replay/recovery primitives
├── bounded concurrent service boundary
└── optional WASM or static deployment target
```

## Why not Rust-only first?

Rust-only would improve early runtime guarantees but slow the part of the project where the ontology, object types, review labels, and evaluation criteria are still being discovered. LCA’s main early risk is not raw throughput; it is semantic drift and false authority. The first implementation should therefore optimize for inspectability and iteration.

## Why Rust later?

The ledger and policy boundary eventually become high-consequence infrastructure. Rust is a good candidate for:

- preventing accidental mutation through stronger type and ownership constraints;
- stable cross-platform binaries;
- isolated policy evaluation;
- concurrent event ingestion;
- deterministic replay;
- lower-memory deployment;
- a small local service that can run without a Python/ML runtime;
- and an auditable core that ML components cannot silently bypass.

## Contract boundary

Both implementations should conform to the same artifacts:

1. `lca-schema-0.1` record schemas;
2. canonical JSON serialization rules;
3. event types and required ledger fields;
4. relationship vocabulary;
5. lifecycle and validation state transitions;
6. authority decision semantics;
7. snapshot and recovery format;
8. conformance fixtures and expected decisions.

The Python implementation is the reference behavior while the Rust implementation is being brought into conformance. A Rust rewrite must not silently change what Portrait, Bud, or Branch means.

## Suggested repository layout

```text
LCA-MVP 001a/
├── 00_LCA-MVP-001a_Index.md
├── 01_LCA_Combined_Mindmap.md
├── 02_LCA_Origins_vs_Revised_Comparison.md
├── 03_LCA_Current_Technology_MVP_Build_Plan.md
├── 04_LCA_MVP_Backlog_and_Traceability.md
├── 05_LCA_Source_Manifest.md
├── 06_LCA_Python_Rust_Implementation_Strategy.md
├── 07_LCA_ML_Learning_and_Constraints.md
├── 08_LCA_Standards_Profile.md
├── 09_LCA_Missing_Pieces_and_Research_Gaps.md
├── reference_impl/
│   └── python/
│       ├── lca_mvp.py
│       ├── lca_schema_0_1.json
│       ├── run_demo.py
│       ├── README.md
│       └── tests/
└── rust_core/
    ├── Cargo.toml
    ├── src/lib.rs
    └── README.md
```

## Python reference package phases

### P0 — single-process reference

- standard-library SQLite store;
- JSON Schema envelope;
- append-only versions/events;
- lexical and typed-relation retrieval;
- authority checks;
- continuity transition tests;
- unit and integration fixtures.

### P1 — research service

- separate `lca_core`, `lca_io`, `lca_retrieval`, `lca_ml`, and `lca_eval` modules;
- PostgreSQL option;
- FTS and temporal queries;
- model adapters;
- source-review UI;
- recovery-package CLI;
- OpenTelemetry instrumentation.

### P2 — hardened service boundary

- Rust ledger/policy service;
- Python ML worker communicates through a typed API;
- ML worker can propose transformations but cannot directly mutate canonical state;
- policy service authorizes every write and sensitive read;
- conformance tests run against both implementations.

## Python/Rust interoperability test

The same fixture should be:

1. created by Python;
2. exported as canonical JSONL;
3. imported and verified by Rust;
4. replayed into a fresh store;
5. queried through both implementations;
6. compared for record hashes, event hashes, relations, lifecycle state, authority outcomes, and recovery output.

The implementations may differ internally. They may not differ in authoritative meaning.


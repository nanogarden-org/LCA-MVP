# LCA missing pieces and research gaps

## Status categories

- **MVP missing:** blocks a credible first controlled run.
- **Pilot hardening:** not required for a local demo, but required for real personal or institutional data.
- **Research gap:** cannot be closed by ordinary engineering alone.
- **Governance gap:** requires an explicit human/legal decision.

## 1. Canonical schema gaps

### MVP missing

- per-object validation beyond the common envelope;
- relationship vocabulary and cardinality rules;
- explicit temporal model for observed, recorded, valid-from, and superseded times;
- controlled vocabularies for source class, response class, weather source, privacy tier, and authority action;
- machine-readable migration maps;
- canonical serialization and hash rules.

### Pilot hardening

- JSON-LD/PROV/ODRL bindings;
- semantic versioning policy;
- schema registry and compatibility tests;
- signed schema releases;
- localization and accessibility metadata.

## 2. Ledger and integrity gaps

### MVP missing

- deterministic event IDs and canonical JSON hashing;
- explicit transaction/concurrency semantics;
- snapshot and replay commands;
- tamper and corruption tests;
- append-only policy enforced at the API boundary rather than only by convention.

### Pilot hardening

- signed events and recovery manifests;
- external timestamping or notarization if the use case requires it;
- redaction/tombstone semantics that preserve permitted metadata without exposing content;
- multi-writer conflict resolution;
- cross-device synchronization.

## 3. Retrieval and memory-engine gaps

### MVP missing

- temporal/as-of query support;
- graph traversal and typed edge queries;
- contradiction and supersession views;
- retrieval traces explaining ranking;
- index deletion/rebuild verification;
- privacy-preserving index boundaries.

### Pilot hardening

- vector retrieval with explicit embedding-space identity;
- hybrid ranking evaluation;
- semantic query language;
- graph projection rebuilds;
- cross-scope access controls;
- cache leakage tests.

## 4. ML and learning gaps

### MVP missing

- model-run registry;
- dataset snapshot registry;
- proposal versus promotion lifecycle;
- time-based train/evaluation splits;
- false-memory and contamination fixtures;
- model-swap drift report;
- abstention and uncertainty contract.

### Pilot hardening

- active-learning queue from SourceReviews;
- unlearning/exclusion workflows;
- data poisoning detection;
- fairness and accessibility evaluation where relevant;
- privacy-preserving training or local inference for sensitive domains;
- reproducible environment and dependency manifests.

## 5. Authority, rights, and privacy gaps

### MVP missing

- explicit AuthorityGrant object;
- purpose, scope, expiry, and revocation;
- decision record for every sensitive read/write;
- private weather exclusion from retrieval, indexes, training, logs, and exports;
- third-party material handling.

### Governance gap

- who is the living-source authenticator;
- who can act as steward;
- who may review or override a dispute;
- what happens when trustees disagree;
- how source consent is withdrawn;
- which jurisdiction governs succession, licensing, deletion, and branch rights;
- whether a branch can refuse continuation.

## 6. Living Source ↔ Bud coupling gaps

### MVP missing

- authenticated SourceReview workflow;
- correction and endorsement UI;
- invariant reaffirmation/revision history;
- divergence-repair queue;
- review cadence and longitudinal dataset.

### Research gap

- what counts as meaningful co-development;
- how to distinguish adaptation from contamination;
- whether behavioral continuity can be measured without implying subjective continuity;
- how to evaluate negotiated values across years;
- how to compare independent Bud candidates without forcing them into a single identity claim.

## 7. Orientation layer gaps

### MVP missing

- explicit P/C/F/A fields;
- transition rules and reasons;
- invariant evidence and revision history;
- branch classification when fidelity falls while provenance remains high.

### Research gap

- calibration of P/C/F/A thresholds;
- whether continuity is scalar, vector-valued, or multidimensional;
- how to represent domain-specific fidelity;
- whether authority can be negotiated independently of similarity;
- how to avoid converting a governance heuristic into an identity score.

## 8. Product and interface gaps

### MVP missing

- source onboarding;
- review queue;
- evidence-path view;
- contradiction view;
- privacy and authority visualization;
- recovery/export button;
- clear labels for source, interpretation, and generated continuation.

### Pilot hardening

- accessibility;
- multilingual content;
- low-bandwidth/export-first workflow;
- trustee and legal review dashboard;
- user-controlled retention and deletion;
- human-readable audit reports.

## 9. Security and operations gaps

### MVP missing

- authentication boundary;
- secrets handling;
- structured audit logs;
- dependency and model inventory;
- backup and restore drill;
- prompt-injection and memory-poisoning tests.

### Pilot hardening

- threat model;
- key rotation;
- key escrow or threshold governance if needed;
- secure enclave or isolated policy service for high-consequence deployments;
- incident response;
- disaster recovery objectives;
- supply-chain verification.

## 10. Scientific and philosophical gaps

These are intentionally not disguised as engineering tickets:

- Is a Bud a useful governance category without being a claim of consciousness?
- Can a system preserve development without collapsing into a personality summary?
- Can “invariant” be defined in a way that respects revision and context?
- What is the difference between a branch’s legitimate autonomy and a model’s ungrounded continuation?
- Can a future neural observation improve provenance without being mistaken for autobiographical access?
- What evidence would count against the LCA identity model?
- How should LCA handle an explicit source statement that rejects future continuation?

## 11. Missing deliverables before institutional pilot

1. LCA-Core-0.1 conformance specification.
2. Per-type JSON Schemas.
3. Python reference package with CLI and recovery export.
4. Rust ledger/policy conformance crate or service.
5. Synthetic adversarial fixture corpus.
6. Source-review interface.
7. AuthorityGrant and privacy policy evaluator.
8. Model/dataset registry.
9. Evaluation report template.
10. Threat model and incident response plan.
11. Consent and third-party rights protocol.
12. Pilot steward charter.


# Contributing to LCA

LCA is research software with an explicit governance boundary. Contributions should make the system more inspectable, reversible, testable, and honest about what it does not prove.

## Before opening a change

- Read the [MVP index](./00_LCA-MVP-001a_Index.md), [ML constraints](./07_LCA_ML_Learning_and_Constraints.md), and [conformance package](./conformance/README.md).
- Do not add personal or private source material to fixtures without an explicit release decision.
- Keep canonical records and derived indexes separate.
- Preserve authorship and provenance; do not rewrite source text into assistant-authored text.
- Add or update a shared fixture for every semantic change.

## Change expectations

### Schema and record changes

Update the schema, Python validator, shared JSONL fixtures, and Rust conformance behavior together. A schema change without a fixture is incomplete.

### Ledger changes

Every canonical mutation must produce an event. Include actor, reason, evidence, source and target versions, transformation identity, previous event hash, and recovery behavior.

### ML changes

ML components may propose transformations, retrieve evidence, rank candidates, or request review. They may not directly mutate canonical state. Any proposed promotion must pass the same authority, privacy, review, and ledger boundary as a human-originated change.

### Rust changes

Rust should harden confirmed interfaces. Keep the first Rust responsibility narrow and high-consequence: parse, verify, decide, accept/reject, append, replay. Do not move unstable product behavior into Rust merely because it is faster or more durable.

## Pull request checklist

- [ ] The change has a clear source or architectural rationale.
- [ ] Existing provenance and authorship fields remain intact.
- [ ] A positive and negative fixture cover the changed rule.
- [ ] Python tests pass.
- [ ] Rust conformance passes when the shared contract is affected.
- [ ] Cross-language results match.
- [ ] No private source material, credentials, or generated local state was added.
- [ ] Documentation states what the change does not prove.

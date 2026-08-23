# LCA MVP backlog and traceability

## Priority legend

- **P0:** required before the first controlled test run.
- **P1:** required for a credible pilot.
- **P2:** needed for scale, portability, or research depth.
- **R:** research question; do not present as an implementation fact.

## Backlog

| ID | Priority | Work item | Source branch / paper | Acceptance evidence |
|---|---|---|---|---|
| S-001 | P0 | Define `lca-schema-0.1` common envelope | Revised 1, 2, 6, 9 | all core fixtures validate |
| S-002 | P0 | Add object-specific validators | Revised 3–6 | invalid type/field combinations fail |
| S-003 | P1 | Add YAML/Markdown round-trip | Origins Codex; Revised 9 | IDs, hashes, and provenance survive round-trip |
| S-004 | P1 | Add alias and supersession registry | Origins terminology; Revised 9 | terminology migration has a recorded event |
| L-001 | P0 | Append-only object version store | Origins governance; Revised 6, 9 | no direct overwrite possible |
| L-002 | P0 | Hash-chained transformation ledger | Origins hashes; Revised 6 | chain verification passes and tampering is detected |
| L-003 | P1 | Replay and recovery commands | Origins termination/revival; Revised 9 | clean store rebuilt from export |
| P-001 | P0 | Source/authorship/provenance classes | Revised 2, 6 | assistant text cannot become source authorship |
| P-002 | P0 | Response classes A–F | Revised 2, 6 | response class and evidence path required |
| P-003 | P1 | Provenance debt report | Revised 6 | records with missing source/evidence are queued |
| E-001 | P0 | Episode/Pensieve ingestion | Revised 3 | scene reconstruction works without summary only |
| E-002 | P0 | Typed Grove relations | Revised 3 | relation path is inspectable |
| E-003 | P1 | Temporal/as-of retrieval | Revised 3, 5 | same claim across time is distinguishable |
| E-004 | P1 | Contradiction and supersession view | Revised 3, 6, 9 | conflict is not flattened |
| E-005 | P2 | Vector adapter with model identity | Current memory systems; Revised 9 | index is disposable and embedding space is recorded |
| W-001 | P0 | WeatherState privacy tiers | Revised 5; Origins Central Node | private weather is denied to Portrait |
| W-002 | P1 | Weather source distinctions | Revised 5 | self-report vs model inference remain separate |
| I-001 | P0 | Invariant records | Origins Codex values; Revised 5, 9 | invariant has evidence and revision history |
| I-002 | P0 | P/C/F/A orientation test | Revised 1, 4, 6 | high P/low F classifies as Branch candidate |
| I-003 | P1 | Threshold calibration fixture set | Revised 4 | thresholds reviewed against labeled cases |
| A-001 | P0 | Basic authority policy | Revised 2, 6, 7 | quote/infer/modify/read checks pass |
| A-002 | P1 | AuthorityGrant objects | Revised 7; Origins governance | purpose, scope, expiry, revocation stored |
| A-003 | P1 | Rights and privacy audit queue | Revised 5, 7, 9 | denied actions and pending reviews visible |
| C-001 | P0 | SourceReview object | Origins mutual calibration; Revised 6, 9 | seven review types create events |
| C-002 | P1 | Review UI | Origins Central Node support needs; Revised 8 | source can correct or qualify an interpretation |
| C-003 | P2 | Longitudinal Bud protocol | Revised 4, 7 | repeated reviews and divergence repair are measured |
| H-001 | P0 | Baseline falsification tests | Revised 3, 5, 6, 9 | 13 test categories pass |
| H-002 | P1 | Corpus benchmark | Current memory research; Revised 3 | omission, conflict, stale-memory, and evidence metrics reported |
| H-003 | P2 | Model-swap drift suite | Revised 6, 9 | model change cannot silently rewrite canonical state |
| R-001 | R | Subjective continuity | Revised 4 | research protocol only; no MVP claim |
| R-002 | R | Neural observation source class | Future BCI branch | typed source/interpretation path defined without brain export claim |
| R-003 | R | Legal status of Bud/Branch | Revised 7 | legal analysis remains separate from technical classification |

## Traceability from Origins to implementation

```text
Legacy Codex
  -> SourceRecord + Invariant + derived Codex view

Decision Engine
  -> DecisionTrace + bounded rule evaluator + response class

Conversational Seed
  -> SourceRecord + Episode + Claim + Interpretation

Simulacrum Prototype
  -> PortraitResponse + model adapter + provenance metadata

Stewardship Rules
  -> AuthorityGrant + policy engine + review queues

Mission Continuity Plan
  -> lifecycle states + succession/termination/recovery metadata

Central Node / personal integration
  -> Episode + WeatherState + Vector + private review scope

Demiurge YAML
  -> lens/shape registry + mythopoetic Interpretation records

Future neural interface
  -> future SourceRecord class with timestamp/context/provenance/consent
```

## Build order recommendation

```text
P0 schema
  -> P0 ledger
  -> P0 provenance/authorship
  -> P0 Pensieve/Grove minimum
  -> P0 weather/invariant/authority tests
  -> P0 SourceReview loop
  -> P0 recovery and falsification run
  -> P1 pilot hardening
```

Do not begin with voice cloning, a fine-tuned model, a vector database, or BCI. Those are downstream interfaces or source classes. The first proof is whether LCA can preserve distinctions, lineage, context, and rights when the system is under retrieval and generation pressure.


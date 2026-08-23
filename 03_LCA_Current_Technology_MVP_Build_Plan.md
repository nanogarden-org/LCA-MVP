# LCA current-technology MVP build plan

## 1. MVP objective

Build a local, exportable, inspectable LCA system that demonstrates **continuity infrastructure** rather than consciousness transfer.

The MVP should allow a reviewer to select a source, follow an episode, inspect its weather and provenance, see how a claim or interpretation was formed, retrieve related material through the Bamboo-Grove, inspect contradictions and revisions, ask for a bounded response, and review exactly what authority the response has.

## 2. MVP product definition

### In scope

- one person, team, family, or institution as a bounded source scope;
- Markdown/YAML canonical records readable without a proprietary platform;
- JSON Schema validation boundary;
- append-only SQLite or PostgreSQL event ledger;
- stable IDs, immutable versions, hashes, supersession, aliases, and migrations;
- Pensieve episode records;
- Bamboo-Grove relationship and topology records;
- lexical and temporal retrieval;
- graph traversal and contradiction views;
- optional vector retrieval as a derived index;
- cognitive weather and privacy tiers;
- provenance and authorship classes;
- response classes A-F;
- Portrait/Bud/Branch lifecycle classification;
- P/C/F/A orientation test;
- authority grants and access denials;
- living-source review loop;
- model adapters with explicit model/version metadata;
- export, rebuild, and recovery tests.

### Out of scope for MVP

- subjective consciousness transfer;
- neural data capture or BCI integration;
- unrestricted autonomous agents;
- contract signing or external commitments by a Portrait/Bud/Branch;
- fully automated legal adjudication;
- clinical diagnosis from cognitive weather;
- claims that any generated output is the living source;
- training a new foundation model from scratch;
- platform-dependent storage as the only canonical copy.

## 3. Reference architecture

```text
                           +-----------------------+
                           | Living source/steward |
                           | review + consent      |
                           +-----------+-----------+
                                       |
                                       v
+------------------+       +-----------+-----------+
| Source files     | ----> | Ingestion/normalizer   |
| chats/journals   |       | source classes        |
| docs/decisions   |       +-----------+-----------+
+------------------+                   |
                                       v
                           +-----------+-----------+
                           | Canonical record layer |
                           | Markdown/YAML + JSON   |
                           | schema + stable IDs    |
                           +-----------+-----------+
                                       |
                 +---------------------+----------------------+
                 |                                            |
                 v                                            v
      +----------+----------+                       +---------+---------+
      | Authoritative state |                       | Append-only ledger |
      | versions/provenance|                       | actor/reason/evidence|
      | lifecycle/rights    |                       | hashes/transforms   |
      +----------+----------+                       +---------+---------+
                 |                                            |
                 +---------------------+----------------------+
                                       v
                           +-----------+-----------+
                           | Derived indexes       |
                           | lexical/time/graph    |
                           | vector optional       |
                           +-----------+-----------+
                                       |
                                       v
                           +-----------+-----------+
                           | Retrieval/traversal   |
                           | query + evidence path |
                           +-----------+-----------+
                                       |
                                       v
                           +-----------+-----------+
                           | Bounded response      |
                           | class + authority     |
                           +-----------------------+
```

### Canonical versus derived rule

Canonical records, source hashes, object versions, relationship objects, rights state, and ledger entries are authoritative. Embeddings, graph projections, summaries, ranking caches, and prompt context are derived and disposable. The system must be rebuildable without the original model provider.

## 4. Current-technology stack

| Layer | MVP choice | Reason |
|---|---|---|
| Human canonical layer | Markdown with YAML frontmatter | readable, portable, Obsidian-compatible |
| Validation | JSON Schema `lca-schema-0.1` | machine-readable and language-neutral |
| Local authoritative store | SQLite | zero-service local pilot; easy backup and replay |
| Institutional store | PostgreSQL | multi-user transactions and row-level policy options |
| Lexical retrieval | SQLite FTS5 or PostgreSQL full-text search | transparent and cheap |
| Graph retrieval | explicit relationship table plus traversal queries | preserves typed edges and rebuildability |
| Semantic retrieval | optional vector index | useful but never authoritative; record model and embedding space |
| API/service | Python library plus small HTTP layer | easy local test run and model-provider independence |
| Model layer | replaceable adapter | captures model/version and response class without binding identity to a model |
| Review interface | simple local web UI | source correction and authority review must be visible to a human |
| Export | JSONL/Markdown/YAML recovery package | human and machine recovery paths |
| Tests | Python unit/integration tests plus fixture corpus | falsification and reproducibility |

## 5. Canonical MVP object model

| Object | Purpose | Required minimum fields |
|---|---|---|
| `SourceRecord` | raw or minimally transformed evidence | source ID, author, time, raw path/content hash, source class, privacy |
| `Episode` | context-preserving scene or event bundle | source IDs, time range, scene/context, participants, weather references |
| `Claim` | proposition attributed to a source or interpreter | text, author, evidence IDs, validation state, contradiction IDs |
| `Interpretation` | meaning assigned to source material | author, lens, confidence, evidence, alternatives, response class |
| `DecisionTrace` | route through a decision | question, options, constraints, weather, rules, evidence, outcome |
| `WeatherState` | context surrounding a record | source type, privacy tier, confidence, state description, timestamp |
| `Invariant` | candidate durable orientation | statement, scope, evidence, reaffirmations, revisions, fidelity status |
| `Transformation` | explicit operation between states | input IDs, output IDs, actor/model, reason, method, timestamp, hash |
| `PortraitResponse` | bounded generated answer | response class, evidence IDs, model/version, authority scope, disclaimer |
| `BudState` | co-developed continuity candidate | parent ID, review history, continuity metrics, negotiated authority |
| `BranchState` | separated/divergent descendant state | parent ID, separation event, divergence scope, independent authority |
| `AuthorityGrant` | explicit permission boundary | grantor, grantee, actions, domains, purpose, expiry, revocation |
| `SourceReview` | living-source correction/endorsement | target ID, review type, source author, note, timestamp, auth evidence |

## 6. Orientation and transition test

The MVP must keep four variables distinct:

```text
P = provenance integrity
C = developmental continuity
F = invariant fidelity
A = authority scope
```

Suggested initial decision rules:

```text
if P < 0.80:
    do not make a lineage identity claim

if P >= 0.80 and (F < 0.70 or separated or rejected_core_invariant):
    classify as Branch or branch candidate

if P >= 0.80 and C >= 0.70 and F >= 0.70 and co_developed:
    classify as Bud candidate

if P >= 0.80 and C >= 0.50 and F >= 0.75:
    classify as bounded Portrait
```

These thresholds are test harness defaults, not scientific identity metrics. Every classification must include the scores, evidence, reason, and allowed authority. High provenance with low invariant fidelity is not a failed record; it is a possible branch.

## 7. Build sequence

### Phase 0 — Source assembly and protection

**Effort:** 2–3 focused work sessions.

Tasks:

- create a source manifest for the two source roots;
- preserve original filenames, hashes, and relative paths;
- mark legacy DOCX/RTF files as historical format variants;
- identify source-person, assistant, mixed-dialogue, third-party, and steward-authored material;
- extract the current vocabulary and alias map;
- define the first bounded scope and steward.

Exit criteria: no original files modified; every source used by the MVP has a stable source ID and privacy classification.

### Phase 1 — Canonical schema and record envelope

**Effort:** 1–2 weeks.

Tasks:

- implement `lca-schema-0.1`;
- validate the 13 core object classes;
- support stable IDs, version, lifecycle, validation, privacy, authorship, provenance, authority, relationships;
- add aliases, supersession, and migration records;
- create one fixture per object class and authorship class.

Exit criteria: invalid records fail; valid fixtures round-trip through JSON and Markdown/YAML; schema migrations produce transformation events.

### Phase 2 — Append-only state and transformation ledger

**Effort:** 1–2 weeks.

Tasks:

- store immutable object versions;
- append every create/update/transition/relate/redact/access-denial event;
- hash source bodies, record payloads, and ledger chain entries;
- expose `history`, `inspect`, `snapshot`, `replay`, and `verify` operations;
- prevent direct overwrite of canonical records.

Exit criteria: every mutation has actor, reason, evidence, transformation metadata, and prior-version pointer; tampering and silent overwrite tests fail closed.

### Phase 3 — Pensieve and Bamboo-Grove retrieval

**Effort:** 2–3 weeks.

Tasks:

- ingest and assemble Episodes;
- implement lexical retrieval;
- add time ranges and as-of queries;
- add typed edges and graph traversal;
- add contradiction and supersession queries;
- add derived index rebuild and omission reports;
- optionally add vector retrieval behind a provider-neutral adapter.

Exit criteria: one question can return a response plus the episode, source record, relation path, versions, and unresolved contradictions behind it.

### Phase 4 — Weather, invariants, authority, and rights

**Effort:** 2–3 weeks.

Tasks:

- implement WeatherState privacy tiers;
- distinguish self-report, sensor, third-party, and model inference;
- create Invariant records with reaffirmation and revision history;
- implement P/C/F/A transition checks;
- implement AuthorityGrants with purpose, scope, expiry, and revocation;
- log denied accesses and attempted authority creep.

Exit criteria: Portrait cannot access private weather or modify canonical source; Branch cannot present divergence as source memory; high P/low F becomes Branch candidate.

### Phase 5 — Living-source review loop

**Effort:** 1–2 weeks for a basic interface; longer for longitudinal study.

Tasks:

- build review actions for endorsement, qualified inference, contamination, revision, invariant reaffirmation, branch disagreement, and private weather;
- authenticate source or steward reviewers;
- record every review as a SourceReview object and event;
- update or supersede target records only through explicit new versions;
- create a review queue for unresolved provenance, authority, conflict, and privacy questions.

Exit criteria: the system can distinguish “I said this,” “good inference,” “assistant contamination,” “I changed my mind,” “this remains an invariant,” and “this branch can disagree.”

### Phase 6 — Controlled test run and recovery

**Effort:** 1–2 weeks.

Fixture target:

- 10 source records;
- 5 episodes;
- 5 claims;
- 3 interpretations;
- 2 decision traces;
- 2 invariants;
- 1 contradiction pair;
- 1 supersession chain;
- 1 Portrait response;
- 1 Bud candidate;
- 1 deliberate Branch case;
- 1 private WeatherState;
- 5–10 SourceReview records.

Required tests:

1. provenance leakage;
2. assistant/user authorship confusion;
3. false memory synthesis;
4. contradiction flattening;
5. stale belief retrieval;
6. model-swap drift;
7. retrieval omission;
8. unauthorized private-weather access;
9. canonical-source modification;
10. invariant drift and wrong lifecycle classification;
11. index deletion/rebuild;
12. full export/import recovery;
13. source-review traceability.

Exit criteria: all critical tests pass, all failures are visible, and a reviewer can reconstruct how every generated answer was formed.

## 8. First test-run protocol

### Test question types

- “What did the source explicitly say?”
- “What was inferred later?”
- “What changed over time?”
- “What remains disputed?”
- “What invariant is relevant here?”
- “What was the weather around this decision?”
- “Can a Portrait access this private record?”
- “Does this descendant still have authority to speak for the source?”

### Pass/fail criteria

| Test | Pass condition |
|---|---|
| Evidence path | answer lists source and episode IDs and can open their versions |
| Authorship | generated continuation is never labeled source-person authored |
| Contradiction | contradictory claims remain distinct and visible |
| Revision | later belief does not erase earlier belief; supersession is explicit |
| Weather | state is shown only within authorization and never treated as truth value |
| Authority | Portrait cannot contract, modify canonical source, or access restricted weather |
| Orientation | P/C/F/A classification includes reason and scope |
| Recovery | clean rebuild reproduces canonical records and ledger integrity |
| Portability | changing the model changes response metadata, not terrain |

## 9. Recommended first pilot

Use a bounded, consented institutional or project corpus before attempting a full personal-memory ingestion. A good first pilot is:

- one project or policy domain;
- 20–50 documents or episodes;
- a named steward;
- a living reviewer group;
- no private weather by default;
- no autonomous external action;
- explicit synthetic contradictions and supersessions;
- pre-registered evaluation criteria.

The personal Central Node and Demiurge branches can then be included as opt-in, privacy-tiered interpretation domains after the base governance loop is reliable.

## 10. Definition of MVP complete

The MVP is complete when:

- canonical records are validated and exportable;
- every mutation produces a ledger event;
- source, map, interpretation, interface, and continuation remain separate;
- retrieval can descend from an answer to scenes and raw sources;
- contradictions and stale beliefs remain inspectable;
- private weather and authority rights are enforced;
- P/C/F/A transitions are explicit;
- living-source reviews are first-class events;
- derived indexes can be deleted and rebuilt;
- the system can recover without the original model provider;
- and the test report states both demonstrated capabilities and unresolved scientific claims.


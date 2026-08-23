---
title: "Modifiable, Moldable and Recoverable"
author: "Robin Abigayle Bronson"
project: "Legacy Consciousness Architecture"
paper_number: 9
version: "1.0-draft"
status: "canonical-draft"
created: 2026-07-14
tags:
  - lca
  - systems-design
  - modifiable
  - moldable
  - recoverable
  - obsidian
  - architecture
related:
  - "[[Legacy Consciousness Architecture From Persona Preservation to Cognitive Lineage]]"
  - "[[Provenance Before Persona]]"
  - "[[The Sherpa Protocol]]"
---

# Modifiable, Moldable and Recoverable

## Abstract

Legacy Consciousness Architecture must survive change without losing history, support multiple forms without collapsing into one ontology, and restore orientation after interruption or damage. This paper defines three engineering requirements for LCA: **modifiable, moldable, and recoverable**.

Modifiable means corrections and revisions can occur without erasing prior states. Moldable means the same source terrain can support different maps, interfaces, and use cases. Recoverable means the system can restore not only files but interpretive orientation, provenance, route history, and authority boundaries.

The paper translates these principles into design rules for Obsidian, YAML, versioning, storage, migration, model interfaces, and governance. It treats recoverability as deeper than backup and modifiability as deeper than editability.

---

## 1. Why These Three Requirements Matter

A digital archive can survive as files and still fail as a mind-map.

The files may remain while:

- links break,
- metadata drifts,
- terms change,
- models become incompatible,
- provenance disappears,
- summaries replace sources,
- or the user can no longer reconstruct orientation.

LCA must survive both technical and epistemic change.

The three requirements address different failure modes.

---

## 2. Modifiable

### 2.1 Definition

A modifiable system can accept correction, refinement, contradiction, and new evidence without destroying historical state.

### 2.2 Not the same as editable

Editability permits changing a file.

Modifiability requires:

- revision history,
- supersession links,
- rollback,
- authorship tracking,
- and compatibility awareness.

### 2.3 Append before overwrite

Canonical records should prefer append-only updates.

Example:

```yaml
epistemic:
  status: superseded
  superseded_by: lca-note-204
```

The original remains available.

### 2.4 Terminology migration

Terms evolve.

Examples:

- simulacrum → portrait,
- graft → bud,
- digital twin → bounded representation,
- essence → cognitive lineage,
- codex → source terrain index.

The system should preserve aliases and migration maps.

### 2.5 Schema evolution

YAML fields will change.

A versioned schema should include:

```yaml
schema_version: lca-2.1
```

Migration scripts should record transformations.

---

## 3. Moldable

### 3.1 Definition

A moldable system can take different forms without changing the underlying source terrain.

### 3.2 Multiple maps

The same source may support:

- personal map,
- legal map,
- technical map,
- emotional-weather map,
- occupational map,
- public portrait.

No map should become canonical by default.

### 3.3 Multiple interfaces

Possible interfaces include:

- Obsidian graph,
- timeline,
- search,
- portrait,
- legal dashboard,
- institutional expert system,
- family archive,
- research corpus.

### 3.4 Domain partitioning

Different audiences require different access.

A family portrait should not automatically access private occupational records.

An institutional interface should not access intimate emotional weather.

Moldability requires boundaries.

### 3.5 Lens rotation

The Polarizing Filter Principle supports moldability.

The architecture should allow a user to rotate among lenses without altering the source.

---

## 4. Recoverable

### 4.1 Definition

Recoverability is the ability to restore:

- content,
- structure,
- provenance,
- context,
- route,
- and authority.

### 4.2 Beyond backup

A backup can restore files.

LCA recovery must also restore:

- graph edges,
- note IDs,
- schema versions,
- aliases,
- transformation ledgers,
- model versions,
- consent boundaries,
- and route checkpoints.

### 4.3 Orientation recovery

A user returning after months or years should be able to answer:

- Where was I?
- What had I concluded?
- What remained unresolved?
- Which terms changed?
- What was active versus superseded?
- What path led here?

Orientation recovery is a primary function.

### 4.4 Cognitive recovery

The system should preserve personal recovery routes:

- phrases,
- petons,
- scope reductions,
- evidence checks,
- physical grounding,
- trusted people,
- and prior successful transitions.

This may support the living user before it ever serves legacy use.

---

## 5. Obsidian Design Principles

### 5.1 Stable IDs

Do not rely only on filenames.

Use unique IDs.

### 5.2 Human-readable markdown

Core records should remain readable without proprietary software.

### 5.3 Relative links and aliases

Preserve mobility.

### 5.4 Versioned YAML

Record schema version and migration history.

### 5.5 Folder as convenience, graph as structure

Folders organize. Links define deeper topology.

### 5.6 Source immutability

Raw imports should be preserved separately from enriched notes.

### 5.7 Derived-note visibility

Maps, summaries, and generated notes should be visibly marked.

---

## 6. Suggested Island Architecture

```text
LCA/
├── 00_Gateway
├── 01_Origins
├── 02_Source_Terrain
├── 03_Pensieve
├── 04_Bamboo_Grove
├── 05_Lenses
├── 06_Cognitive_Cartography
├── 07_Representations
├── 08_Governance
├── 09_Frameworks
└── 10_Whitepapers
```

The structure is moldable because each layer can be reindexed without altering sources.

---

## 7. Failure Modes

### 7.1 Schema lock-in

The system becomes dependent on one metadata design.

### 7.2 Platform captivity

The archive cannot leave a vendor.

### 7.3 Model dependency

The portrait works only with one base model.

### 7.4 Summary takeover

Derived notes replace source records.

### 7.5 Link rot

Graph continuity disappears.

### 7.6 Authority drift

Access and permissions change during migration.

### 7.7 Identity collapse

Multiple representations are merged into one persona.

---

## 8. Recovery Packages

An LCA recovery package should include:

- source archive,
- hashes,
- YAML schema,
- term registry,
- migration scripts,
- graph index,
- rights manifest,
- model configuration,
- version history,
- and human-readable recovery guide.

A future steward should be able to rebuild the system without the original platform.

---

## 9. Model Portability

A portrait should not be inseparable from one model provider.

The architecture should preserve:

- retrieval corpus,
- prompt logic,
- response classes,
- authority rules,
- and evaluation tests.

This permits reimplementation while maintaining lineage.

The model is replaceable.

The terrain and governance are not.

---

## 10. Evaluation Tests

### Modifiability tests

- Can a belief be revised without erasing the old state?
- Can terminology migrate?
- Can a schema update be rolled back?

### Moldability tests

- Can the same terrain produce different views?
- Can private layers remain isolated?
- Can a new interface be added without rewriting sources?

### Recoverability tests

- Can the system be rebuilt from export?
- Can a user reconstruct project state?
- Can authority and consent be restored?
- Can a generated answer be traced after migration?

---

## 11. Recovery as Ethical Protection

Recoverability protects against:

- corporate shutdown,
- account loss,
- institutional capture,
- hostile editing,
- trustee failure,
- and technological obsolescence.

It also protects against personal cognitive interruption.

A person may return after illness, crisis, or years away.

The system should help them find the last stable ledge.

---

## 12. Modifiability and Identity

An identity system that cannot change becomes a mausoleum.

An identity system that changes without history becomes a counterfeit.

LCA must preserve both continuity and revision.

This is why modifications require lineage.

---

## 13. Moldability and Non-Totalization

No single interface should define the person.

Moldability allows:

- a public portrait,
- a private Pensieve,
- an occupational expert,
- a family archive,
- and a research map.

Each is partial.

The source terrain remains larger than all of them.

---

## 14. Canonical Design Rules

1. Preserve raw sources.
2. Version every schema.
3. Record every transformation.
4. Never silently overwrite meaning.
5. Keep interfaces replaceable.
6. Keep core records human-readable.
7. Separate private weather from public portrait.
8. Maintain exportability.
9. Preserve aliases and supersession.
10. Test recovery before crisis.

---

## 15. Conclusion

Legacy Consciousness Architecture must be:

**Modifiable** enough to learn.  
**Moldable** enough to serve different contexts.  
**Recoverable** enough to survive loss.

These are not secondary implementation details. They define whether the architecture remains a living lineage or becomes a brittle memorial product.

Modifiable prevents fossilization.

Moldable prevents totalization.

Recoverable prevents disappearance.

Together, they make LCA durable without making it rigid.

---

## 16. Worked Migration Scenario

Assume the LCA begins in Obsidian and later moves to a graph database plus local language model.

A weak migration exports only text.

A proper migration preserves:

- stable note IDs,
- links,
- aliases,
- YAML fields,
- source hashes,
- schema versions,
- rights metadata,
- supersession chains,
- and portrait evaluation tests.

After migration, a known question should produce an answer with the same source lineage even if wording differs.

That is recoverability across implementation.

---

## 17. Disaster Scenarios

### 17.1 Account loss

The cloud account disappears.

Recovery requires local source copies and manifests.

### 17.2 Corrupted graph

Links are lost.

Recovery requires an edge index and stable IDs.

### 17.3 Trustee conflict

Stewards disagree.

Recovery requires governance and dispute procedures.

### 17.4 Model obsolescence

The base model is no longer available.

Recovery requires portable retrieval logic and test suites.

### 17.5 Personal interruption

The source person returns after years.

Recovery requires project-state summaries, unresolved-route lists, and last stable petons.

### 17.6 Hostile rewrite

A party modifies public portrait behavior.

Recovery requires signed canonical versions and comparison tools.

---

## 18. Progressive Enrichment

The archive should not demand perfect YAML at ingestion.

A practical flow is:

1. preserve raw source;
2. assign stable ID;
3. add minimal provenance;
4. enrich context later;
5. add topology when patterns emerge;
6. add rights before broader access;
7. add representation metadata before model use.

This keeps the system usable.

Overly rigid metadata can kill the project it is meant to preserve.

---

## 19. Moldable Views

The same note may appear differently.

### Research view

Shows claims, sources, confidence.

### Personal view

Shows episodes, weather, and recovery.

### Legal view

Shows ownership, consent, and authority.

### Public view

Shows approved summaries.

### Portrait view

Shows conversational access.

The views should be generated from shared records rather than maintained as disconnected copies.

---

## 20. Canonical Versus Active

LCA should distinguish:

- raw,
- active,
- canonical,
- superseded,
- archived,
- and experimental.

A whitepaper may remain historically important after being superseded.

This avoids the false choice between deleting old work and treating it as current doctrine.

---

## 21. Recovery Drills

Recovery should be tested periodically.

A drill may ask a new machine or human steward to:

- rebuild the graph,
- locate a concept’s origin,
- trace a portrait response,
- restore access rights,
- and identify the current canonical terminology.

If the system cannot be reconstructed from its own package, it is not recoverable.

---

## 22. Metrics

Possible engineering metrics:

### Modifiability

- percentage of changes with recorded lineage;
- rollback success;
- schema migration success.

### Moldability

- number of supported views;
- separation of private and public layers;
- interface portability.

### Recoverability

- rebuild time;
- source verification rate;
- broken-link rate;
- orientation restoration success;
- model behavior continuity across migration.

Metrics should support the project, not become a new bureaucracy.

---

## 23. Final Design Principle

The architecture should be strong enough to preserve form and loose enough to permit growth.

Bamboo provides the metaphor:

- shared rhizome,
- recurring shoots,
- pruning without destroying the root,
- regrowth after damage,
- and multiple visible forms from one substrate.

LCA should be engineered the same way.

## Source Lineage

This paper integrates:

- Bamboo-Grove and Obsidian architecture discussions
- LCA source/map/portrait distinctions
- provenance and governance requirements
- the user’s formulation: “modifiable, moldable, and recoverable”
- prior LCA roadmap and schema documents

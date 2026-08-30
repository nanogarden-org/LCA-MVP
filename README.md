# Legacy Consciousness Architecture (LCA)

**LCA** is an inspectable continuity architecture for preserving source material, decisions, values, context, contradictions, corrections, and authority boundaries across time.

> Preserve the terrain. Expose the provenance. Bound the authority. Leave identity claims open.

[Open the HTML orientation page](./index.html) · [Read the MVP index](./00_LCA-MVP-001a_Index.md) · [Run the conformance package](./conformance/README.md)

The [public stake and timeline](./LCA_PUBLIC_STAKE_AND_TIMELINE.md) records what this alpha package places on the public record at the current checkpoint and what remains unresolved.

## What LCA is

LCA is a reference architecture for a governed memory and continuity system. It combines:

- an Archive for source records;
- a Pensieve for episodes, claims, interpretations, and decision traces;
- a Bamboo-Grove for temporal and relational topology;
- a provenance and transformation ledger;
- an invariant/orientation layer;
- authority, privacy, and rights enforcement;
- a living-source review loop; and
- Portrait, Bud, and Branch response boundaries.

The model may retrieve, compare, summarize, classify, or propose. The model may not silently become the canonical source, erase contradiction, promote an unverified memory, or grant itself authority.

## Why it exists

Long-lived AI memory can preserve errors as easily as it preserves insight. It can also confuse assistant language with source language, flatten historical changes, expose private context, and make a fluent answer sound more authoritative than its evidence.

LCA makes those failure modes visible and testable through stable IDs, typed records, authorship classes, provenance, append-only events, deterministic hashes, review records, and authority decisions.

## Where to start

1. Read the [combined mindmap](./01_LCA_Combined_Mindmap.md) for the architecture.
2. Read the [current-technology MVP plan](./03_LCA_Current_Technology_MVP_Build_Plan.md) for scope and build stages.
3. Run the [Python reference implementation](./reference_impl/python/README.md).
4. Run the [shared Python/Rust conformance package](./conformance/README.md).
5. Read the [ML learning and constraints](./07_LCA_ML_Learning_and_Constraints.md) before adding model training or automated promotion.
6. Read the [public-release checklist](./PUBLIC_RELEASE_CHECKLIST.md) before publishing source material.

The public research layer is the [revised whitepaper set](./research/LCA_Revised_Whitepapers_Obsidian/). The earlier `LCA Origins` archive remains outside this package so its personal, private, and third-party material can be reviewed separately.

## How the MVP works

```text
source
  -> typed record
  -> authorship / provenance / privacy review
  -> model or human transformation proposal
  -> authority decision
  -> append-only event
  -> deterministic replay and recovery
  -> bounded response with evidence path
```

The current implementation is intentionally Python-first. Rust is the hardening boundary for confirmed semantics: parsing, schema checks, deterministic hashes, authority evaluation, event acceptance/rejection, append behavior, and replay. It is not intended to become the entire LCA platform.

## Current status

`0.1.0-alpha / MVP 001a` — runnable reference package on the public `main` branch.

Validation at the current checkpoint:

- 11/11 Python MVP behavior tests pass;
- 18/18 Python conformance fixtures pass;
- 18/18 Rust conformance fixtures pass; and
- 18/18 cross-language decision and hash comparisons match.

The reference demo also completes with an intact ledger and no integrity failures. See the nested READMEs for the exact commands and the boundaries each test suite covers.

This package does not demonstrate consciousness transfer, subjective identity continuation, or full autobiographical brain-state export. It demonstrates an inspectable continuity protocol that can be built with current technology.

## Public release boundaries

The revised whitepaper set is included as the intended public research layer. Publication and future additions still require human review for private weather, personal data, third-party copyrighted material, unpublished correspondence, secrets, credentials, and any source record that was not intended for public release.

The original LCA research folders remain provenance sources outside this MVP package. Their inclusion in a public repository should be an explicit release decision, not an automatic copy operation.

## Relationship to TurtleML

LCA and [TurtleML](https://github.com/nanogarden-org/TurtleML) share a contract-first direction:

- Python proves semantics first;
- authority is separate from knowledge;
- provenance is explicit;
- internals may evolve while seams remain stable; and
- Rust enters as a durable policy and boundary layer after the semantic tests stabilize.

LCA applies that posture to continuity, memory, source review, and lineage rather than recursive edge nodes and actuator authority.

## License

LCA is released under the [MIT License](./LICENSE), matching TurtleML. Copyright (c) 2026 nanogarden-org.

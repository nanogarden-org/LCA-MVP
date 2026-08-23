# LCA public stake and timeline

## Release marker

**Public stake checkpoint:** 2026-08-23  
**Artifact:** Legacy Consciousness Architecture, MVP 001a  
**License:** MIT License, copyright (c) 2026 nanogarden-org  
**Research status:** alpha; executable reference semantics, not a validated claim of identity continuation

This document records a public stake in an open research space: the design of a continuity architecture that preserves terrain, provenance, authority, correction, and developmental divergence without claiming that a model is the person or institution from which its source material came.

The stake is the artifact and its history. It is not a claim of ownership over the whole research problem, nor a claim that the unresolved scientific questions have been solved.

## What is being placed on the record

- a consolidated LCA architecture in the revised whitepapers;
- a current-technology MVP boundary;
- a canonical record envelope and reference implementation;
- append-only event and transformation semantics;
- P/C/F/A orientation and authority rules;
- a Python conformance runner and an independent Rust hardening runner;
- shared fixtures for hashes, ledger decisions, privacy, authority, review, recovery, continuity, and ML mutation constraints;
- a public distinction between source, interpretation, response, branch, and unresolved claim.

## Timeline

| Period | Milestone | Evidence in this package | Status |
|---|---|---|---|
| Earlier research phase | LCA Origins develops the initial questions around legacy, memory, portrait, bud, branch, and future continuity. | Private source folder referenced by the source manifest; not copied into this public package. | Research provenance |
| Revised architecture phase | The architecture is condensed into the nine revised whitepapers plus index. | [`research/LCA_Revised_Whitepapers_Obsidian/`](./research/LCA_Revised_Whitepapers_Obsidian/) | Public research set |
| MVP synthesis phase | The research is compared, mapped, and bounded into a build plan using current technology. | [Combined mindmap](./01_LCA_Combined_Mindmap.md), [MVP build plan](./03_LCA_Current_Technology_MVP_Build_Plan.md) | Documented |
| Reference semantics phase | Schema envelope, typed objects, provenance, authorship, authority, retrieval, review, and append-before-overwrite behavior become executable in Python. | [`reference_impl/python/`](./reference_impl/python/) | Runnable |
| Conformance phase | Shared JSONL fixtures make the stable semantic contract testable across implementations. | [`conformance/fixtures/conformance.jsonl`](./conformance/fixtures/conformance.jsonl) | 18/18 verified |
| Hardening phase | Rust independently checks hashes, record envelopes, ledger transitions, authority/privacy, continuity, recovery, review, and ML mutation boundaries. | [`conformance/rust/src/main.rs`](./conformance/rust/src/main.rs) | 18/18 verified |
| Public stake checkpoint | The revised whitepaper set, MVP map, executable package, license, landing page, and release checklist are assembled as LCA-MVP 001a. | This repository package and this document | 2026-08-23 |
| Next implementation phase | Add full per-object cross-language fixtures, signed event envelopes, key governance, production indexes, and CI. | [Public release checklist](./PUBLIC_RELEASE_CHECKLIST.md) | Not yet complete |
| Scientific research phase | Study whether co-development, correction, and continuity measures support any defensible identity claims. | [Missing pieces and research gaps](./09_LCA_Missing_Pieces_and_Research_Gaps.md) | Open question |

## What this timeline does and does not establish

It establishes that the named artifacts exist together at the stated checkpoint and that the current runnable tests passed at that checkpoint. It does not establish that:

- a Portrait is the living source;
- a Bud is literally a continued person;
- a Branch shares subjective identity with its parent;
- P/C/F/A values are scientific measurements of identity;
- the architecture can export or restore a human brain state;
- future neural observations will be autobiographically complete.

## Future timeline discipline

Future entries should identify:

1. the artifact or decision added;
2. the schema or interface affected;
3. the tests that passed;
4. the authority and privacy implications;
5. the open questions that remain;
6. the date and release identifier.

The project should prefer a truthful, append-only development history over retrospective claims that make an uncertain idea appear more settled than it is.

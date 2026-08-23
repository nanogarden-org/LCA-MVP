# Public release checklist

This checklist is the gate from a private working package to a public GitHub repository.

## Repository hygiene

- [ ] Create a fresh public-repository working copy rather than publishing the entire private Atlas tree.
- [ ] Include `README.md`, `index.html`, `LICENSE`, `CONTRIBUTING.md`, and `SECURITY.md`.
- [ ] Remove databases, caches, virtual environments, compiled binaries, notebooks with outputs, and local path manifests that reveal private structure.
- [ ] Add a repository-specific `.gitignore`.
- [ ] Add CI for Python tests, conformance, and Rust compilation after the Rust build profile is finalized.

## Source review

- [x] Include `research/LCA_Revised_Whitepapers_Obsidian/` as the intended public condensed research set.
- [ ] Review every revised whitepaper for personal, private, or third-party material before pushing publicly.
- [ ] Review every file under `LCA Origins` for personal, private, or third-party material.
- [ ] Review every file under `LCA_Revised_Whitepapers_Obsidian` for the same.
- [ ] Keep `LCA Origins` outside the public package unless separately approved; copy only approved material.
- [ ] Replace private local filesystem paths in public documentation with repository-relative paths.
- [ ] Mark quotations, external sources, and reused diagrams with their rights and attribution.

## LCA integrity

- [ ] Preserve the distinction between source record, claim, interpretation, and response.
- [ ] Preserve the distinction between lineage and identity.
- [ ] Keep private weather separate from public identity claims.
- [ ] Keep model proposals outside canonical state until review.
- [ ] Do not describe the MVP as consciousness transfer or subjective identity continuation.
- [ ] Label P/C/F/A as governance and orientation heuristics, not measurements of a person.

## Technical gate

- [ ] Python MVP tests pass.
- [ ] Shared Python conformance passes.
- [ ] Rust conformance passes.
- [ ] Cross-language results match.
- [ ] Signed-event verification is implemented before accepting externally signed events.
- [ ] Recovery/replay is tested against missing, reordered, duplicated, and tampered events.
- [ ] At least one valid and one invalid fixture exists for every schema object type.

## Publication decision

- [ ] The copyright holder and license are confirmed.
- [ ] Maintainer and contact information are present.
- [ ] The initial release tag and alpha status are chosen.
- [ ] Open research questions are listed separately from implemented guarantees.
- [ ] A human has approved the exact files to publish.

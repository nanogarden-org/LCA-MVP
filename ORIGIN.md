# LCA — Origin, Chronology, and Challenge Notes

## Problem observed

Long-lived AI and knowledge systems can blur distinctions that become critical over time: source versus interpretation, custody versus ownership, fluent continuation versus identity, inherited context versus inherited authority, and preservation versus succession.

LCA was developed to keep those seams explicit and auditable rather than allowing a convincing model output to collapse them.

## Specific architectural treatment

The current public architecture emphasizes:

- canonical source records and append-only provenance;
- explicit separation of ownership, custody, interpretation, attribution, authority, and identity;
- Portrait/Bud/Branch lifecycle distinctions;
- bounded authority and external legal/governance anchors;
- an originator-closure boundary for post-originator material;
- cross-language conformance rather than implementation-specific semantics.

The project does not claim ownership of archival science, digital estates, trusts, identity theory, provenance, memory systems, succession law, or AI alignment as broad fields.

## Public chronology

Git history records when specific LCA formulations, code, fixtures, and documents became public in this repository.

That supports chronology for these artifacts. It does not establish that no earlier related work exists, create legal ownership over abstract ideas, or prove that later similar work was derived from LCA.

## Why runnable toy models and conformance fixtures matter

The architecture is intentionally accompanied by small executable pieces because continuity claims are easy to make rhetorically and difficult to verify.

A reference implementation and shared fixtures turn questions such as “does authority propagate?” or “did two languages make the same bounded decision?” into inspectable behavior.

## Break it

High-value counterexamples include:

1. generated material promoted to originator evidence without explicit review;
2. custody becoming de facto identity or authority;
3. a branch receiving powers through context inheritance alone;
4. two conforming implementations producing different decisions or hashes;
5. a legal/governance mapping being represented as if the software itself created authority;
6. an untracked transformation changing the continuity record;
7. a failure mode where preservation succeeds technically but attribution becomes false.

Open an issue with a minimal case, conflicting related work, or an argument that one of the boundaries is unnecessary or incorrectly drawn. The architecture should improve when challenged.

# Legacy Consciousness Architecture (LCA)

**LCA** is an inspectable continuity and succession architecture for preserving source material, decisions, values, context, contradictions, corrections, rights, assets, and authority boundaries across time.

> Preserve the terrain. Expose the provenance. Bound the authority. Fund the continuity. Separate succession from identity.

[Read the MVP index](./00_LCA-MVP-001a_Index.md) · [Read the MVP 002 architecture](./11_LCA_Continuity_Succession_Legal_Business_Architecture.md) · [Read the MVP 002 build plan](./12_LCA_MVP_002_Build_Plan.md) · [Run the conformance package](./conformance/README.md)

## Current status

`0.2.0-alpha / MVP 002` — continuity succession architecture layered onto the runnable 001a reference package.

MVP 001a established a local, inspectable continuity kernel with canonical records, append-only provenance, bounded responses, source review, authority grants, and Portrait/Bud/Branch lifecycle distinctions.

MVP 002 extends that system into **continuity succession infrastructure**:

```text
person / originator
  -> corpus + assets + rights + instructions
  -> Continuity Estate
  -> legal shell + fiduciary roles
  -> LCA continuity kernel
  -> ABCI identity/authority boundary
  -> TurtleML active runtime
  -> authorized future branches
```

The project still does **not** claim consciousness transfer, legal personhood transfer, or that a generated continuation is literally the originator.

## What changed in MVP 002

The continuity problem now includes what happens when the originator can no longer serve as the active biological/legal source of authority.

New first-class architecture includes:

- `ContinuityEstate` — corpus, material/digital/intellectual assets, continuity objects, rights, and sustaining resources;
- `OriginatorClosureBoundary` — prevents post-originator generated material from silently becoming primary originator evidence;
- succession roles — executor, custodian, steward, trustee, operator, branch steward, and release authority;
- A0-A9 machine-readable authority classes;
- `BranchRegistryEntry` — explicit descendant identity, temporal class, lineage, provenance, and attribution constraints;
- `LegalInstrumentBinding` — maps LCA policy to external wills, trusts, contracts, assignments, licenses, or other authoritative instruments without pretending to replace them;
- `SealPolicy` and `TerminationCondition` — silence, release, training, destruction, and integrity-stop rules;
- `ContinuityTreasury` — models royalties, licensing, reserves, preservation costs, compute, storage, legal/admin costs, and shutdown thresholds;
- TurtleML active-runtime integration;
- ABCI identity/capability/provenance/authority boundary integration;
- a legal/business review packet for human counsel and fiduciaries.

The core distinction is:

```text
ownership != custody != interpretation != attribution != authority != identity
```

## What LCA is

LCA is a reference architecture for governed memory, continuity, and succession. It combines:

- an Archive for source records;
- a Pensieve for episodes, claims, interpretations, and decision traces;
- a Bamboo-Grove for temporal and relational topology;
- a provenance and transformation ledger;
- an invariant/orientation layer;
- authority, privacy, and rights enforcement;
- a living-source review loop;
- Portrait, Bud, and Branch response boundaries;
- a Continuity Estate and succession layer;
- legal-instrument mappings;
- business-sustainability and treasury policy;
- TurtleML runtime participation; and
- ABCI boundary exchange semantics.

The model may retrieve, compare, summarize, classify, propose, or continue an explicitly registered branch. It may not silently become the canonical source, erase contradiction, promote an unverified memory, inherit identity by fluency, or grant itself authority.

## Relationship to TurtleML

[TurtleML](https://github.com/nanogarden-org/TurtleML) is now an **active runtime substrate** for LCA rather than only a related project.

TurtleML's core invariant:

```text
signal != feature != inference != claim != authorized action
```

maps directly into LCA continuity:

```text
evidence
  != interpretation
  != inference
  != continuity claim
  != originator attribution
  != authorized external action
```

A participating TurtleML node can carry estate ID, branch ID, temporal class, provenance root, capabilities, and scoped LCA authority while remaining heterogeneous and local-first.

Knowledge may propagate between nodes without propagating permission or originator attribution.

## Relationship to ABCI

[ABCI](https://github.com/nanogarden-org/ABCI) is the planned **identity, capability, provenance, and authority seam** between LCA/TurtleML regions and external systems.

ABCI is currently an architectural placeholder rather than a production-ready package. LCA MVP 002 therefore defines an initial exchange surface that ABCI can later formalize:

- actor/node identity;
- estate and branch identity;
- capability declaration;
- provenance root;
- requested action;
- authority evidence;
- policy decision;
- denial reason;
- transformation/transaction reference.

An ABCI message carrying an authority field does not create legal authority. It transports machine policy derived from valid grants and external human/legal/governance decisions.

## Legal focus

LCA does not ask present-day law to recognize a model as the person who created the corpus.

Instead, the architecture maps continuity policy onto conventional legal surfaces where applicable, including:

- wills and trusts;
- fiduciary access to digital assets;
- business entities;
- copyright/IP assignments;
- licenses;
- contracts;
- beneficiary or succession instructions;
- custody and archival agreements.

For a Connecticut-oriented pilot, useful design anchors include the Connecticut Revised Uniform Fiduciary Access to Digital Assets Act, the Connecticut Uniform Trust Code, and U.S. copyright law. See the MVP 002 architecture document for references and boundaries.

**This repository is a research/reference architecture, not legal, tax, fiduciary, or investment advice.** Machine-readable mappings do not replace properly executed legal instruments or professional review.

## Business focus

The project now treats continuity as an operational and economic problem as well as an archival one.

Potential product surfaces include:

- Continuity Estate Builder;
- local-first Continuity Vault;
- Trajectory Registry for unfinished work and research;
- bounded Branch Runtime;
- Steward Console;
- institutional/founder succession package;
- conformance and verification tooling;
- legal/business review exports.

Potential revenue surfaces include setup/mapping engagements, archival preparation, institutional licenses, support, conformance tooling, qualified-partner custody/hosting, and policy-governed licensing of estate-owned IP.

Canonical export and local recovery remain architectural requirements. A subscription or hosting provider must never become the only path to the continuity estate.

## Existing runnable foundation

The 001a implementation remains the current executable foundation while 002 is implemented.

At the previous checkpoint:

- 11/11 Python MVP behavior tests passed;
- 18/18 Python conformance fixtures passed;
- 18/18 Rust conformance fixtures passed; and
- 18/18 cross-language decision and hash comparisons matched.

MVP 002 must preserve backward compatibility with those semantics while adding succession, legal/business mapping, TurtleML metadata, and ABCI boundary tests.

## MVP 002 first demonstrator

The planned demonstrator is a local **Continuity Estate Sandbox** with:

- estate overview;
- asset/IP registry;
- succession map;
- A0-A9 authority matrix;
- trajectory registry;
- seal/release policies;
- continuity treasury simulation;
- branch console;
- TurtleML node participation;
- ABCI-style boundary log; and
- portable legal/business review export.

The demonstrator may simulate budgets, succession triggers, licensing policy, and external requests. It may not declare death/incapacity, sign contracts, move money, transfer property, bypass provider authentication, or act as a trustee/executor/fiduciary.

## Where to start

1. Read the [MVP index](./00_LCA-MVP-001a_Index.md).
2. Read the [Continuity Succession, Legal, and Business Architecture](./11_LCA_Continuity_Succession_Legal_Business_Architecture.md).
3. Read the [MVP 002 build plan](./12_LCA_MVP_002_Build_Plan.md).
4. Read the [001a current-technology build plan](./03_LCA_Current_Technology_MVP_Build_Plan.md) for the runnable foundation.
5. Run the [Python reference implementation](./reference_impl/python/README.md).
6. Run the [shared Python/Rust conformance package](./conformance/README.md).
7. Read the [ML learning and constraints](./07_LCA_ML_Learning_and_Constraints.md) before adding model training or automated promotion.
8. Read the [public-release checklist](./PUBLIC_RELEASE_CHECKLIST.md) before publishing source material.

## Architecture invariant introduced by MVP 002

> **The substrate is replaceable. The continuity contract is not silently replaceable.**

Hardware, models, custodians, operators, trustees, and storage media may change. LCA remains conformant only while identity, provenance, temporal position, authority, rights, assets, trajectory, invariants, branches, and their external legal sources remain explicit and auditable.

## License

LCA is released under the [MIT License](./LICENSE), matching TurtleML. Copyright (c) 2026 nanogarden-org.

# LCA MVP 002 Build Plan

**Working title:** Continuity Succession MVP  
**Architecture basis:** `11_LCA_Continuity_Succession_Legal_Business_Architecture.md`

## 1. Product objective

Build a local-first, inspectable prototype that proves LCA can carry a human or institutional corpus across a simulated succession boundary while preserving provenance, authority, attribution, rights, business assets, and branch identity.

The MVP does **not** prove consciousness transfer and does **not** autonomously execute legal or fiduciary acts.

It proves a narrower and commercially useful capability:

> A continuity estate can remain intelligible, governable, portable, and economically maintainable after the originating source stops being the active authority.

## 2. MVP 002 architecture

```text
Originator / Living Source
          |
          v
+---------------------------+
| Continuity Estate Builder |
| corpus + assets + rights  |
+-------------+-------------+
              |
              v
+-------------+-------------+
| LCA Continuity Kernel     |
| provenance / trajectory   |
| roles / branches / seals  |
| treasury / legal mappings |
+-------------+-------------+
              |
       +------+------+
       |             |
       v             v
+------+-----+ +-----+------+
| ABCI seam  | | TurtleML   |
| identity   | | active     |
| capability | | runtime    |
| authority  | | nodes      |
+------+-----+ +-----+------+
       |             |
       +------+------+
              |
              v
       External systems
       / archive / UI
```

## 3. New modules

### `estate`

Responsibilities:

- create `ContinuityEstate` records;
- inventory `AssetRecord` objects;
- attach rights and ownership metadata;
- record account references without storing plaintext credentials;
- group assets by physical, digital, intellectual, and continuity domains.

### `succession`

Responsibilities:

- define `SuccessionTrigger` records;
- simulate verified trigger activation;
- create `OriginatorClosureBoundary`;
- activate role transitions;
- freeze primary-originator authorship after closure;
- preserve archival mode even when interactive mode is terminated.

### `governance`

Responsibilities:

- manage `ContinuityRole` and `AuthorityProfile` objects;
- enforce A0-A9 authority classes;
- distinguish custody from interpretation, publication, licensing, and governance powers;
- record human/fiduciary approvals as `FiduciaryDecisionRecord` objects.

### `branches`

Responsibilities:

- register post-originator branches;
- require parent lineage and provenance root;
- enforce temporal class;
- prohibit silent originator attribution;
- preserve divergence and branch-specific authority.

### `rights`

Responsibilities:

- represent `LegalInstrumentBinding` objects;
- track verification state;
- represent `SealPolicy`, `LicensePolicy`, and `RevenueRight` objects;
- export review packets for counsel/fiduciaries;
- never claim the machine-readable mapping is itself the legal instrument.

### `treasury`

Responsibilities:

- model preservation and operating budgets;
- associate revenue rights with assets;
- simulate royalty/licensing inflows;
- model reserves and shutdown thresholds;
- require external approval for any real transaction.

### `turtle_adapter`

Responsibilities:

- expose continuity estate ID;
- expose branch ID and temporal class;
- expose provenance root;
- expose capabilities and authority profile;
- ensure knowledge propagation does not propagate authority;
- support local-first heterogeneous TurtleML nodes.

### `abci_adapter`

Responsibilities:

- form boundary envelopes containing actor, node, estate, branch, provenance, requested action, and authority decision;
- log external action attempts;
- fail closed when authority evidence is missing or stale;
- provide the future contract surface shared with ABCI.

## 4. Canonical schema additions

Add JSON Schema definitions for:

- `ContinuityEstate`
- `AssetRecord`
- `LegalInstrumentBinding`
- `SuccessionTrigger`
- `OriginatorClosureBoundary`
- `ContinuityRole`
- `AuthorityProfile`
- `BranchRegistryEntry`
- `SealPolicy`
- `TerminationCondition`
- `ContinuityTreasury`
- `RevenueRight`
- `LicensePolicy`
- `FiduciaryDecisionRecord`
- `ABCIExchangeRecord`
- `TurtleRuntimeRecord`

Every new object must inherit the existing LCA envelope fields for stable ID, version, authorship, provenance, privacy, lifecycle, relationships, and transformation history.

## 5. Business-facing workflow

```text
1. INVENTORY
   corpus + projects + IP + accounts + assets

2. CLASSIFY
   ownership + privacy + rights + release + continuity value

3. MAP SUCCESSION
   executor + custodian + steward + trustee/operator + branch rules

4. BIND LEGAL SOURCES
   record links to actual wills/trusts/contracts/assignments/instructions

5. DEFINE BUSINESS METABOLISM
   royalties + licensing + reserves + operating costs + termination thresholds

6. TEST CLOSURE
   simulated originator boundary

7. ACTIVATE BRANCH
   derived runtime receives scoped authority

8. VERIFY EDGE ACTION
   TurtleML node requests action through ABCI boundary

9. REVIEW
   human/fiduciary approves, denies, or requires correction

10. EXPORT
    canonical archive + ledger + legal/business review packet
```

## 6. First demonstrator

The first demonstrator should be a **Continuity Estate Sandbox** accessible through a local web UI.

### Screens

1. **Estate Overview**
   - estate identity;
   - living/post-originator state;
   - corpus count;
   - asset count;
   - active roles;
   - treasury simulation status;
   - integrity state.

2. **Asset & IP Registry**
   - works;
   - repositories;
   - domains;
   - business assets;
   - licenses;
   - revenue rights;
   - legal-binding references.

3. **Succession Map**
   - trigger;
   - executor;
   - custodian;
   - steward;
   - trustee/operator;
   - branch inheritance graph.

4. **Authority Matrix**
   - rows: people/agents/nodes;
   - columns: A0-A9;
   - filters: estate domain, branch, expiry, purpose.

5. **Trajectory Registry**
   - unfinished project;
   - evidence;
   - invariants;
   - open questions;
   - continuation permission;
   - branch policy.

6. **Seal & Release Policies**
   - public/private/sealed;
   - release date/condition;
   - training permission;
   - quotation permission;
   - destruction/retirement conditions.

7. **Continuity Treasury**
   - simulated revenue streams;
   - preservation reserve;
   - compute/storage/legal budgets;
   - runway;
   - shutdown threshold.

8. **Branch Console**
   - branch lineage;
   - temporal class;
   - provenance root;
   - permitted attribution;
   - divergence record;
   - active TurtleML nodes.

9. **Boundary Log**
   - ABCI-style requests;
   - requested action;
   - authority evidence;
   - grant/deny result;
   - human/fiduciary decision.

10. **Export / Review Packet**
    - JSONL archive;
    - Markdown/YAML human-readable estate map;
    - hashes;
    - authority matrix;
    - legal-instrument reference list;
    - unresolved questions;
    - warnings that require counsel/fiduciary review.

## 7. Security boundary

The MVP must **not** store account passwords, secret answers, recovery codes, private keys, or bypass credentials in ordinary LCA records.

Account records should contain metadata such as:

```yaml
asset:
  type: digital_account
  provider: example
  account_identifier_ref: vault://account/example
  credential_storage: external_secret_vault
  fiduciary_access_policy_ref: policy://digital-assets/example
```

ABCI/TurtleML adapters should receive scoped capability tokens or mediated access where implemented, never broad reusable credentials merely because the continuity estate owns the account.

## 8. Legal review packet

The MVP should generate a packet designed for a human attorney/fiduciary to review, containing:

- estate inventory;
- IP inventory;
- digital asset/account inventory;
- named roles;
- desired authority scopes;
- desired seal/release rules;
- desired licensing policies;
- continuity treasury purpose and expense classes;
- unresolved jurisdictional questions;
- external legal instruments already in existence;
- mismatches between desired machine policy and verified legal authority.

The packet should use language such as **desired**, **mapped**, **verified**, **unverified**, and **requires professional review**. It should never label an unexecuted LCA policy as legally binding.

## 9. Commercial validation questions

The pilot should test not only technical correctness but whether users can answer:

- What would be lost if the originator disappeared tomorrow?
- Who actually controls each relevant asset?
- Who is allowed to preserve, interpret, publish, license, or extend it?
- Which instructions exist only as intent and which are tied to executed legal instruments?
- Which assets can fund preservation?
- How long can the estate sustain itself under the current budget model?
- Which future branch statements are source-backed versus inferred?
- Can a customer move the full canonical estate to another provider?

If the system cannot answer those questions, it is not yet continuity succession infrastructure.

## 10. MVP 002 phases

### Phase A — schema extension

Implement the new object classes and fixtures. Preserve backward compatibility with 001a fixtures.

**Exit:** all existing 001a tests continue passing; new objects validate and round-trip.

### Phase B — succession engine

Implement simulated triggers, closure boundary, role activation, and branch registration.

**Exit:** generated post-boundary content cannot become originator evidence.

### Phase C — legal/right mapping

Implement legal-instrument bindings, asset registry, seal policies, license policies, and review-state vocabulary.

**Exit:** every asserted authority can identify whether it is merely desired, internally granted, or externally verified.

### Phase D — treasury simulation

Implement revenue rights, budgets, reserves, operating costs, and termination thresholds.

**Exit:** system can project preservation runway without executing financial transactions.

### Phase E — TurtleML integration

Add a pair of local TurtleML nodes representing an archival node and research branch node.

**Exit:** evidence can propagate while action authority remains scoped and non-transitive.

### Phase F — ABCI boundary proof

Implement an LCA/ABCI exchange envelope prototype.

**Exit:** external action requests fail closed without valid identity, provenance, purpose, and authority evidence.

### Phase G — local Continuity Estate Sandbox

Expose the modules in a local web UI.

**Exit:** a reviewer can trace one asset from originator corpus -> legal mapping -> succession role -> branch -> TurtleML runtime -> ABCI action request -> approval/denial -> ledger.

### Phase H — export and independent review

Generate a portable archive and legal/business review packet.

**Exit:** a reviewer can understand the estate without the original model provider or UI.

## 11. MVP 002 completion criteria

MVP 002 is complete when:

- all 001a conformance tests remain green;
- the new succession object classes are schema-valid;
- custody and authority are independently enforceable;
- a simulated closure boundary prevents post-originator false attribution;
- branch lineage is explicit and inspectable;
- legal-instrument mappings state verification status;
- sealed material fails closed;
- treasury behavior is simulated but cannot autonomously transact;
- TurtleML nodes carry continuity/branch/authority metadata;
- ABCI-style external requests are auditable and deny missing authority;
- a complete human-readable and machine-readable continuity-estate export succeeds;
- and the system can be moved away from the current runtime/provider without losing canonical state.

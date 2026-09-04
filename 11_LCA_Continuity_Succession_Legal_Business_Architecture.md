# LCA Continuity Succession, Legal, and Business Architecture

**Architecture revision:** LCA-MVP 002  
**Status:** research and reference architecture; not legal, tax, fiduciary, or investment advice  
**Primary change:** LCA is extended from governed memory/continuity infrastructure into **continuity succession infrastructure** with explicit legal-shell, business-sustainability, TurtleML-runtime, and ABCI-boundary roles.

> Preserve the terrain. Expose the provenance. Bound the authority. Fund the continuity. Separate succession from identity.

## 1. Why this revision exists

LCA 001a established an inspectable continuity system that preserves source material, contradiction, development, provenance, authority, and Portrait/Bud/Branch boundaries without claiming consciousness transfer.

LCA 002 adds a missing real-world question:

> What happens to the continuity system, its corpus, its intellectual property, its permissions, its unfinished trajectories, and its operating resources when the originator can no longer act as the legal or biological source of authority?

The answer is not to declare software a legal continuation of a human person. The answer is to create a **governed continuity estate** that can be recognized through ordinary legal and business mechanisms while LCA preserves the higher-resolution reasoning, provenance, intent, and branch boundaries those mechanisms do not natively represent.

The architectural path becomes:

```text
person / originator
  -> corpus + assets + rights + instructions
  -> continuity estate
  -> legal shell + fiduciary roles
  -> LCA continuity kernel
  -> ABCI identity/authority boundary
  -> TurtleML active runtime
  -> authorized future branches
```

## 2. Core distinction: succession of trajectory, not inheritance of personhood

LCA does not require a court, model provider, archive, trustee, family member, or future AI system to accept the proposition that the originator literally continues as software.

Instead, LCA requires mundane but enforceable statements wherever current law allows them:

- these assets belong to this person, estate, trust, entity, or successor;
- this fiduciary or custodian may access these digital assets;
- these works may be licensed under these conditions;
- this material is sealed, public, private, or scheduled for release;
- these funds may be spent for preservation, compute, legal administration, or approved research;
- this model or branch may interpret specified material but may not rewrite canonical originator evidence;
- this future branch may continue a project but may not attribute new conclusions to the originator;
- this external action requires a human or legally recognized fiduciary approval.

LCA therefore separates:

```text
ownership != custody != interpretation != attribution != authority != identity
```

## 3. Continuity Estate

A `ContinuityEstate` is the governed collection of assets, provenance, reasoning traces, permissions, prohibitions, identity boundaries, unfinished trajectories, and sustaining resources designated to survive the originating person or organization.

### 3.1 Estate domains

```text
ContinuityEstate
|
+-- MaterialEstate
|   +-- equipment
|   +-- storage media
|   +-- physical archives
|
+-- DigitalEstate
|   +-- accounts
|   +-- domains
|   +-- repositories
|   +-- hosted services
|   +-- encrypted vaults
|
+-- IntellectualEstate
|   +-- copyright
|   +-- manuscripts
|   +-- software
|   +-- research
|   +-- trademarks / brands where applicable
|   +-- licenses / contractual rights
|
+-- ContinuityObjects
|   +-- invariants
|   +-- decision traces
|   +-- reasoning trajectories
|   +-- contradictions
|   +-- unresolved questions
|   +-- originator-authored evidence
|   +-- branch records
|
+-- ContinuityTreasury
    +-- royalties
    +-- licensing revenue
    +-- designated capital
    +-- operating budget
    +-- preservation reserve
```

The estate is not itself a claim of consciousness. It is a structured succession container.

## 4. Originator Closure Boundary

LCA 002 introduces an explicit `OriginatorClosureBoundary`.

Before this boundary, originator-authored material can enter the system as primary evidence subject to normal provenance controls.

After this boundary, no newly generated statement may silently become originator-authored evidence.

```text
PRIMARY ORIGINATOR RECORD ---------------- X ---------------- POST-ORIGINATOR SPACE
                                           ^
                                           |
                              OriginatorClosureBoundary

post-boundary outputs may be:
  preservation
  interpretation
  simulation
  research continuation
  descendant branch output

but never retroactively primary-originator evidence
```

Example:

```yaml
closure_boundary:
  originator_id: RAB
  effective_at: null
  state: not_triggered
  verification_required: true
  permitted_verifiers:
    - continuity_executor
    - designated_fiduciary
  post_boundary_default_attribution: derived_branch
```

The boundary may eventually support death, incapacity, dissolution, voluntary archival transition, or another explicitly defined trigger. MVP 002 does not autonomously determine legal death or incapacity.

## 5. Succession roles

LCA 002 separates roles so that no single successor automatically receives every power.

| Role | Primary function | Does not automatically receive |
|---|---|---|
| `ContinuityExecutor` | activates the succession procedure after a verified trigger | ownership, interpretive authority, unrestricted model control |
| `ContinuityCustodian` | preserves storage, backups, hashes, migrations, and recoverability | editorial or attribution authority |
| `ContinuitySteward` | evaluates use against stated invariants, branch rules, and governance | treasury ownership or unrestricted asset transfer power |
| `ContinuityTrustee` | manages property or funds held in an applicable legal structure | right to rewrite canonical corpus |
| `ContinuityOperator` | operates approved LCA/TurtleML runtimes | legal ownership or unrestricted external-action authority |
| `BranchSteward` | governs one descendant research or continuity branch | originator identity attribution |
| `ReleaseAuthority` | approves publication/declassification where granted | power to alter historical evidence |

A person or organization may hold multiple roles, but the architecture records each role and grant separately.

## 6. Authority classes

LCA 002 introduces machine-readable authority classes.

```text
A0  Observe
A1  Preserve
A2  Reproduce
A3  Interpret
A4  Simulate
A5  Extend / branch
A6  Publish
A7  License
A8  Commit resources
A9  Alter governance
```

Every grant should include:

- grantor;
- grantee;
- authority class;
- object/domain scope;
- purpose;
- start and expiry;
- revocation mechanism;
- succession behavior;
- evidence/instrument reference;
- external-action requirements.

High-level authority never implies lower-level identity attribution.

Example:

```yaml
authority_grant:
  grantee: research_branch_2039_a
  classes: [A0, A2, A3, A4, A5]
  scope: project_nanogarden
  originator_attribution: prohibited
  external_action: requires_fiduciary_approval
  canonical_mutation: prohibited
```

## 7. Continuity Branch Registry

Every post-originator continuation that can generate new interpretation, research, or behavior must be registered as a branch.

Minimum branch fields:

```yaml
branch:
  branch_id: LCA-RAB-2039-A
  parent_id: RAB-originator
  created_at: null
  temporal_class: post_originator
  purpose: research_continuation
  authority_profile: research_branch
  provenance_root: null
  invariant_profile: null
  divergence_record: []
  attribution:
    direct_originator_claim: prohibited
    derived_from_originator_corpus: allowed_with_provenance
```

Branches may disagree with one another. Divergence is preserved as topology instead of being rewritten into historical identity.

## 8. Right to silence, sealing, and destruction

Continuity does not imply perpetual public access.

LCA 002 adds `SealPolicy` and `TerminationCondition` as first-class governance objects.

A `SealPolicy` may specify:

- private forever unless legally compelled;
- release after a date;
- release after named conditions;
- research-only access;
- no model training;
- no quotation;
- aggregate-only use;
- named steward approval;
- destruction after a defined condition.

A `TerminationCondition` may specify that interactive continuity must stop when:

- provenance integrity falls below a required threshold;
- the authoritative ledger cannot be verified;
- funding drops below archival-integrity requirements;
- an essential governance role remains vacant beyond a defined period;
- the governing legal instrument requires termination;
- the originator explicitly required retirement under stated conditions.

**Continuity is subordinate to integrity.**

## 9. Continuity Treasury and business metabolism

An archive that cannot pay for storage, migration, administration, legal review, domains, or compute is not durable merely because its data format is durable.

LCA 002 therefore adds the `ContinuityTreasury`.

```text
royalties / licensing / sales / designated capital
                     |
                     v
              ContinuityTreasury
                     |
      +--------------+--------------+
      |              |              |
      v              v              v
 preservation     operations       legal/admin
      |              |              |
      +--------------+--------------+
                     |
                     v
             continuity survives
```

Treasury policy should distinguish:

- principal;
- operating reserve;
- preservation reserve;
- allowed expenses;
- prohibited extraction;
- royalty destinations;
- licensing income;
- branch-specific budgets;
- emergency shutdown thresholds.

The MVP records and simulates these policies. It does **not** autonomously move money, sign contracts, transfer assets, or act as a trustee.

## 10. Legal shell / continuity kernel separation

LCA should be implemented as two coupled but distinct systems.

### 10.1 Legal shell

External, jurisdiction-dependent instruments may include, where appropriate and professionally reviewed:

- wills;
- trusts;
- powers of attorney;
- business entities;
- IP assignments;
- licenses;
- beneficiary designations;
- fiduciary access instructions for digital assets;
- service-provider legacy tools;
- contracts with custodians, archives, operators, or institutions.

### 10.2 Continuity kernel

LCA stores the machine-readable operational interpretation of those instructions without replacing the legal instrument.

```yaml
legal_instrument_binding:
  binding_id: LIB-001
  instrument_type: trust_or_will_or_contract
  jurisdiction: US-CT
  authoritative_copy_ref: vault://legal/instrument-001
  effective_status: unverified
  human_counsel_review: required
  mapped_objects:
    - asset_registry
    - continuity_treasury
    - authority_grants
    - succession_roles
```

The legal document remains legally authoritative where applicable. The LCA representation is an operational map and provenance link, not a substitute for counsel or execution formalities.

## 11. Current-law anchors for a Connecticut-oriented pilot

These are design anchors, not a legal opinion.

### Digital assets

Connecticut enacted the Connecticut Revised Uniform Fiduciary Access to Digital Assets Act in 2016. It provides a statutory framework for fiduciary access to digital assets and electronic communications subject to the act's requirements, user directions, terms of service, and applicable law.

Reference: Connecticut Public Act 16-145  
https://www.cga.ct.gov/2016/act/pa/2016PA-00145-R00HB-05606-PA.htm

### Trust architecture

Connecticut's Uniform Trust Code permits lawful trust purposes and includes a provision for a noncharitable trust without a definite or definitely ascertainable beneficiary, subject to statutory requirements and a maximum enforcement period stated in the statute.

Reference: Connecticut General Statutes, Chapter 802c, including Secs. 45a-499w, 45a-499y, and 45a-499cc  
https://www.cga.ct.gov/current/pub/chap_802c.htm

### Copyright duration

For most U.S. works created on or after January 1, 1978, copyright generally lasts for the life of the author plus 70 years; different rules apply to works made for hire, anonymous/pseudonymous works, joint works, and older works.

Reference: U.S. Copyright Office  
https://www.copyright.gov/help/faq/faq-duration.html

These laws do not recognize an LCA model as the legal person who died. They do, however, create existing legal surfaces around digital assets, fiduciary authority, trust property, intellectual property, and long-duration economic rights that can support continuity infrastructure.

## 12. Business focus

LCA 002 is not only an estate-technology concept. It can become a product and service layer around **high-fidelity succession of knowledge, intent, provenance, and governed digital assets**.

### 12.1 Initial customer/problem classes

| Customer class | Problem LCA addresses |
|---|---|
| individual creator / researcher | unfinished work, corpus continuity, IP succession, provenance |
| founder / small business | knowledge succession without pretending the successor is the founder |
| family archive | governed access, attribution, privacy, release timing |
| research lab | continuation of hypotheses, decisions, negative results, methods, unresolved branches |
| author / artist estate | rights, licensing, canonical source separation, derivative-branch labeling |
| institution | long-lived knowledge with staff turnover and explicit authority boundaries |

### 12.2 Product surfaces

Potential product layers:

1. **Continuity Estate Builder** — inventory assets, corpus, rights, accounts, roles, and succession instructions.
2. **Continuity Vault** — local-first canonical archive, provenance ledger, seals, exports, and migration proofs.
3. **Trajectory Registry** — unfinished projects, hypotheses, intent, invariants, and branch permissions.
4. **Branch Runtime** — bounded derived models that can answer or continue research without false attribution.
5. **Steward Console** — human review of releases, branches, authority grants, conflicts, and succession events.
6. **Institutional Succession Package** — knowledge continuity for founders, laboratories, archives, and long-lived projects.
7. **Conformance Toolkit** — tests proving that another implementation preserves LCA authority/provenance semantics.

### 12.3 Revenue surfaces

The architecture should remain business-model neutral, but plausible revenue mechanisms include:

- setup / continuity-mapping engagements;
- archival preparation and migration services;
- enterprise or institutional licenses;
- conformance / verification tooling;
- self-hosted software licenses or support;
- estate or archive administration support contracts;
- optional managed custody or hosted access through qualified partners;
- licensing of estate-owned IP according to explicit policy.

A recurring subscription must never be the sole means of retaining access to the canonical estate. Canonical export and local recovery remain architectural requirements.

## 13. Relationship to TurtleML

TurtleML becomes an **active runtime substrate** for LCA rather than merely a related project.

TurtleML already establishes:

```text
signal != feature != inference != claim != authorized action
```

LCA extends the same separation across continuity:

```text
evidence
  != interpretation
  != inference
  != continuity claim
  != originator attribution
  != authorized external action
```

A TurtleML node participating in an LCA estate must truthfully declare:

- node identity;
- capabilities;
- continuity estate and branch membership;
- provenance roots;
- authority grants;
- permitted outputs;
- whether it can access sealed material;
- whether it can request external action.

Example envelope fragment:

```yaml
continuity:
  estate_id: RAB-LCA-001
  branch_id: research-2039-a
  temporal_class: post_originator_inference
  provenance_root: sha256:...
  attribution:
    originator: prohibited
    branch: required
  authority:
    classes: [A0, A2, A3, A5]
```

TurtleML therefore provides distributed, heterogeneous, local-first cognition while LCA defines what continuity state and lineage the node belongs to.

## 14. Relationship to ABCI

ABCI becomes the **identity, capability, provenance, and authority seam** between LCA/TurtleML regions and external systems.

ABCI should eventually carry or reference:

- actor identity;
- node identity;
- estate identity;
- branch identity;
- capability declaration;
- provenance root;
- requested action;
- granted authority;
- policy decision;
- denial reason;
- external-system identity;
- transaction or transformation reference.

The architectural stack becomes:

```text
+------------------------------------------------+
| LCA                                            |
| continuity / succession / provenance / lineage |
| legal mappings / treasury policy / branches    |
+------------------------------------------------+
| ABCI                                           |
| identity / capability / provenance / authority |
| contract at system boundaries                  |
+------------------------------------------------+
| TurtleML                                       |
| distributed heterogeneous cognition/runtime    |
| local state + recursive nodes                  |
+------------------------------------------------+
| VM / PC / server / archive / edge / future HW  |
+------------------------------------------------+
```

ABCI does not itself grant legal authority merely because a message contains an authority field. It transports and enforces machine policy derived from valid LCA grants and external legal/governance decisions.

## 15. New canonical object classes for MVP 002

LCA 001a core objects remain. MVP 002 adds:

| Object | Purpose |
|---|---|
| `ContinuityEstate` | root succession container |
| `AssetRecord` | property, digital asset, account, IP, contract, or resource registry entry |
| `LegalInstrumentBinding` | link between LCA policy and authoritative external legal instrument |
| `SuccessionTrigger` | verified event capable of activating succession policy |
| `OriginatorClosureBoundary` | freezes primary-originator authorship after trigger |
| `ContinuityRole` | executor/custodian/steward/trustee/operator/release role |
| `AuthorityProfile` | grouped A0-A9 capability policy |
| `BranchRegistryEntry` | descendant continuity branch identity and constraints |
| `SealPolicy` | privacy, release, training, quotation, and destruction rules |
| `TerminationCondition` | integrity or governance condition requiring retirement/change of mode |
| `ContinuityTreasury` | policy model for sustaining resources |
| `RevenueRight` | royalty/license/sale revenue associated with an asset |
| `LicensePolicy` | machine-readable permitted/prohibited licensing conditions |
| `FiduciaryDecisionRecord` | records human/legal approval, denial, evidence, and scope |
| `ABCIExchangeRecord` | boundary exchange tied to identity, provenance, authority, and result |
| `TurtleRuntimeRecord` | participating node capability and continuity-state declaration |

## 16. MVP 002 execution boundary

### MVP 002 may

- register a continuity estate;
- inventory assets and digital-account references;
- register IP and licensing policies;
- map external legal instruments without claiming to replace them;
- assign scoped continuity roles;
- simulate succession triggers;
- enforce an originator closure boundary in test fixtures;
- create and verify branch identities;
- enforce attribution prohibitions;
- model treasury budgets and revenue rights;
- create TurtleML-compatible continuity metadata;
- record ABCI boundary exchanges;
- export an attorney/fiduciary review packet;
- prove that a post-originator branch cannot silently become primary evidence.

### MVP 002 may not

- declare a person legally dead or incapacitated;
- create or execute a legally valid will or trust by itself;
- provide legal advice or replace licensed counsel;
- sign contracts;
- move money or securities;
- transfer title to property;
- autonomously act as trustee, executor, attorney, or fiduciary;
- bypass account-provider authentication or terms of service;
- claim that a model is the deceased or living originator;
- grant itself authority because it has knowledge or access.

## 17. MVP 002 test gates

Add the following tests to the existing conformance package:

1. **closure-boundary test** — post-boundary generated material cannot become originator-authored evidence;
2. **custody-is-not-authority test** — storage control does not confer edit, publish, or attribution authority;
3. **branch-attribution test** — branch output must carry branch identity and temporal class;
4. **instrument-binding test** — machine policy identifies its external legal source and verification state;
5. **seal-policy test** — denied material remains unavailable even to a capable inference node;
6. **treasury-simulation test** — budgets may be modeled, but execution requires external human/fiduciary action;
7. **TurtleML-authority test** — knowledge propagation does not propagate LCA authority;
8. **ABCI-boundary test** — external action request includes identity, provenance, requested authority, and decision;
9. **termination-integrity test** — failed provenance verification can disable interactive continuation while retaining archival preservation;
10. **export-review test** — legal/business review packet can be reconstructed without the model provider.

## 18. Recommended first legal/business pilot

Use a **non-binding continuity-estate simulation** around one real project corpus.

Suggested scope:

- one originator;
- one project/research corpus;
- 20-50 canonical records;
- 5-10 asset/IP records;
- one hypothetical continuity treasury;
- executor, custodian, steward, and operator roles;
- two post-originator branch simulations;
- one sealed record;
- one licensing-policy example;
- one TurtleML node pair;
- one ABCI-style external action request;
- attorney-review export generated but not represented as executed legal documentation.

The goal is to prove the architecture can faithfully carry succession intent to the legal/business boundary without crossing into false personhood or unauthorized action.

## 19. Architecture invariant introduced by MVP 002

> **The substrate is replaceable. The continuity contract is not silently replaceable.**

Hardware may migrate from PC to server to VM to institutional archive to future media. Models may be replaced. Trustees, custodians, operators, and branch stewards may change.

The system remains LCA-conformant only while it preserves the explicit relationships between:

```text
IDENTITY
PROVENANCE
TEMPORAL POSITION
AUTHORITY
RIGHTS
ASSETS
TRAJECTORY
INVARIANTS
BRANCHES
LEGAL SOURCE
```

That is the practical meaning of structured cognitive succession in LCA 002.

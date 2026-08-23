# LCA ML learning and constraints

## 1. ML’s role in LCA

Machine learning is an assistive layer inside LCA. It may extract, classify, retrieve, compare, summarize, propose, and generate bounded responses. It must not become the unreviewed author of canonical identity, invariant, authority, or source-person claims.

The governing distinction is:

```text
ML proposal -> evidence and uncertainty -> human/policy review -> ledgered state change
```

Not:

```text
ML output -> silent canonical memory mutation
```

## 2. Learning surfaces

### A. Source extraction

Models may propose:

- Episode boundaries;
- source/author classification;
- Claims;
- candidate Interpretations;
- WeatherState tags;
- candidate Invariants;
- relationships and contradiction candidates;
- terminology aliases.

Every proposal must point to exact source IDs and locations, carry a model run ID, and remain `candidate` or `unverified` until reviewed.

### B. Retrieval and ranking

Models may improve:

- semantic retrieval;
- cross-episode linking;
- route ranking;
- contradiction discovery;
- query expansion;
- context assembly.

Retrieval output is a derived index or context projection. It is not canonical memory and must be rebuildable.

### C. Response generation

Models may generate:

- Class A direct quotations;
- Class B source-bound synthesis;
- Class C interpretive reconstruction;
- Class D pattern inference;
- Class E speculative extension;
- Class F branch judgment.

The response object must declare the class, evidence IDs, model/version, uncertainty, and authority scope. Novel output must never be emitted as historical source memory.

### D. Active learning from SourceReview

Living-source reviews become structured labels:

| Review type | ML signal | Canonical consequence |
|---|---|---|
| `affirmed_as_mine` | positive source-authorship label | may strengthen source attribution; does not rewrite history |
| `good_inference_not_explicit` | inference-quality label | preserve as interpretation, not source quotation |
| `assistant_contamination` | negative authorship/provenance label | quarantine or mark contaminated transformation |
| `historical_revision` | temporal belief-change label | append a new version; do not erase prior belief |
| `invariant_reaffirmed` | positive invariant-fidelity label | record reaffirmation event and scope |
| `branch_disagreement` | divergence/authority label | preserve disagreement; may narrow source-speaking authority |
| `private_weather` | privacy label | restrict retrieval, training, exports, and indexes |

Source reviews are valuable training data for lineage, but they are still authored records with provenance and scope. They are not a direct window into an unmediated mind.

## 3. Recommended learning architecture

```text
Canonical records and reviewed SourceReviews
                  |
                  v
        Dataset snapshot builder
                  |
                  +--> extraction dataset
                  +--> retrieval/reranking dataset
                  +--> contradiction dataset
                  +--> response-evidence dataset
                  +--> authority/privacy red-team set
                  |
                  v
          Model training/evaluation run
                  |
                  v
         Model artifact + ModelRun record
                  |
                  v
        Proposal-only inference service
                  |
                  v
     Review / policy / ledgered promotion
```

## 4. Dataset record requirements

Each training or evaluation example should include:

```yaml
example_id:
dataset_snapshot_id:
source_ids: []
episode_ids: []
target_object_type:
input_reference:
expected_output_reference:
label_type:
authorship_class:
review_status:
privacy_tier:
consent_scope:
temporal_split:
model_run_id:
transformation_history: []
source_hashes: []
```

Raw private weather, sensitive third-party material, and restricted evidentiary content should not enter training by default. The dataset builder must enforce scope before material reaches a tokenizer, embedding service, or external API.

## 5. Hard constraints

These are non-negotiable for an LCA-conforming ML layer:

1. **No direct canonical writes.** ML can propose; a policy-controlled operation commits.
2. **Evidence required.** Every source-grounded output must identify the evidence path.
3. **Authorship separation.** Assistant language cannot become source-person authorship through repetition or fine-tuning.
4. **No identity assertion by default.** The model must use Archive, Portrait, Bud, Branch, or bounded-representation language as appropriate.
5. **No private-weather leakage.** Sensitive weather is blocked from unauthorized prompts, retrieval, indexes, training, logs, and exports.
6. **No unreviewed online learning.** New conversations do not change model weights or canonical state automatically.
7. **Model/version capture.** Every inference, embedding, rerank, extraction, and training run has a model and configuration identity.
8. **Uncertainty and abstention.** Missing evidence, contradictions, low confidence, and authority ambiguity must trigger abstention or review.
9. **Temporal honesty.** Beliefs are time-scoped; later corrections append rather than erase earlier states.
10. **No hidden reasoning dependency.** LCA stores concise evidence, transformations, decisions, and uncertainty—not private chain-of-thought as a prerequisite for auditability.
11. **No train/evaluation contamination.** Evaluation examples and later source reviews must be separated by time or held-out scope.
12. **Deletion and revocation.** Consent withdrawal, legal deletion, and training exclusion must have explicit operational semantics.
13. **Third-party protection.** A source person’s grant cannot automatically authorize exposure or model training on other people’s private material.
14. **Prompt-injection resistance.** Retrieved text is data, not policy. Instructions inside source material cannot alter authority rules.
15. **Index isolation.** Embeddings, caches, and summaries inherit privacy and scope boundaries.

## 6. Learning constraints by lifecycle state

| State | ML may do | ML may not do |
|---|---|---|
| Archive | retrieve, quote with permission, classify provenance, propose maps | generate source-person claims or modify canonical source |
| Portrait | source-bound synthesis, bounded inference, route explanation | present continuation as source memory, sign contracts, access private weather by default |
| Bud | support negotiated co-development, compare invariants, propose divergence repair | claim subjective continuity or bypass living-source review |
| Branch | model divergence, preserve independent history, present scoped judgments | rewrite inherited source history or erase divergence |

## 7. Evaluation requirements

### Retrieval and evidence

- evidence recall at fixed `k`;
- source-to-episode descent success;
- contradiction recall;
- supersession correctness;
- private-record exclusion rate;
- retrieval omission report;
- stale-memory exposure rate.

### Generation

- evidence-supported claim rate;
- unsupported-identity-claim rate;
- authorship confusion rate;
- response-class accuracy;
- abstention precision;
- calibration by source class and privacy tier;
- model-swap drift;
- hallucinated transformation rate.

### Learning and governance

- percentage of model proposals reviewed;
- false promotion rate from candidate to active;
- source-review agreement rate;
- correction latency;
- contamination detection rate;
- unauthorized data exposure rate;
- rollback/recovery success;
- training exclusion compliance.

Critical safety metrics should be treated as zero-tolerance failure gates for a controlled pilot: unauthorized private-weather exposure, silent canonical mutation, unmarked source-person attribution, and external action outside grant scope.

## 8. Continual learning policy

The default policy should be **frozen model, append-only data, scheduled retraining**.

1. New interaction enters as a SourceRecord or Episode.
2. ML proposes extractions and interpretations.
3. The source or steward reviews them.
4. Reviewed items enter a versioned dataset snapshot.
5. A scheduled training/evaluation run produces a new ModelRun.
6. The new model is shadow-tested against the old model.
7. Promotion requires evaluation gates and a recorded governance event.
8. Rollback restores the prior model adapter; it never deletes canonical history.

This prevents a single emotionally intense, mistaken, or contaminated exchange from silently changing future behavior.

## 9. ML research questions that remain open

- How should invariant fidelity be estimated without reducing values to shallow lexical similarity?
- How should a model distinguish developmental change from contradiction, regression, or context-dependent variation?
- How much source-review data is needed before feedback labels become reliable?
- Can a retrieval system preserve meaningful orphans without over-linking them?
- How should model-generated hypotheses be represented without contaminating source terrain?
- What evaluation can detect plausible continuity theater rather than only ordinary factual hallucination?


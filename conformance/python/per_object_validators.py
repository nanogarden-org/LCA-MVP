from __future__ import annotations

import re

from lca_mvp import LCAError, validate_record  # noqa: E402

ORIGINAL_TYPES = {
    "SourceRecord", "Episode", "Claim", "Interpretation", "DecisionTrace",
    "WeatherState", "Invariant", "Transformation", "PortraitResponse",
    "BudState", "BranchState", "AuthorityGrant", "SourceReview",
}

REQUIRED_CONTENT = {
    "SourceRecord": ({"text", "title", "uri"}, "at least one source locator/content field is required"),
    "Episode": ({"scene", "title"}, "scene or title is required"),
    "Claim": ({"text"}, "claim text is required"),
    "Interpretation": ({"text", "lens"}, "interpretation text and lens are required"),
    "DecisionTrace": ({"question", "outcome"}, "decision question and outcome are required"),
    "WeatherState": ({"state"}, "weather state is required"),
    "Invariant": ({"statement"}, "invariant statement is required"),
    "Transformation": ({"input_ids", "output_ids", "method"}, "transformation inputs, outputs, and method are required"),
    "PortraitResponse": ({"response_class", "evidence_ids"}, "response class and evidence IDs are required"),
    "BudState": ({"parent_id", "co_developed"}, "Bud parent and co-development status are required"),
    "BranchState": ({"parent_id", "separation_event", "divergence_scope"}, "Branch parent, separation, and divergence are required"),
    "AuthorityGrant": ({"grantor", "grantee", "allowed_actions"}, "grantor, grantee, and actions are required"),
    "SourceReview": ({"target_id", "review_type", "note"}, "review target, type, and note are required"),
    "ContinuityEstate": ({"estate_id", "originator_id", "state", "domains"}, "estate identity, originator, state, and domains are required"),
    "AssetRecord": ({"asset_type", "owner_ref", "continuity_value"}, "asset type, owner reference, and continuity value are required"),
    "LegalInstrumentBinding": ({"instrument_type", "authoritative_copy_ref", "verification_state"}, "legal instrument type, authoritative reference, and verification state are required"),
    "SuccessionTrigger": ({"trigger_type", "verification_required", "state"}, "trigger type, verification requirement, and state are required"),
    "OriginatorClosureBoundary": ({"originator_id", "state", "post_boundary_default_attribution"}, "originator, boundary state, and default attribution are required"),
    "ContinuityRole": ({"role_type", "holder_id", "estate_id"}, "role, holder, and estate are required"),
    "AuthorityProfile": ({"subject_id", "classes", "scope"}, "subject, authority classes, and scope are required"),
    "BranchRegistryEntry": ({"branch_id", "parent_id", "temporal_class", "attribution"}, "branch lineage, temporal class, and attribution policy are required"),
    "SealPolicy": ({"access", "training_permission", "release_policy"}, "access, training, and release policy are required"),
    "TerminationCondition": ({"condition_type", "effect"}, "termination condition and effect are required"),
    "ContinuityTreasury": ({"purpose", "preservation_reserve", "transaction_mode"}, "treasury purpose, reserve, and transaction mode are required"),
    "RevenueRight": ({"asset_id", "revenue_type", "beneficiary_ref"}, "asset, revenue type, and beneficiary are required"),
    "LicensePolicy": ({"asset_id", "permitted_uses", "approval_required"}, "asset, permitted uses, and approval flag are required"),
    "FiduciaryDecisionRecord": ({"decision_maker", "decision", "target_id"}, "decision maker, decision, and target are required"),
    "ABCIExchangeRecord": ({"actor_id", "estate_id", "requested_action", "authority_decision"}, "ABCI actor, estate, action, and authority decision are required"),
    "TurtleRuntimeRecord": ({"node_id", "estate_id", "branch_id", "capabilities"}, "Turtle node, estate, branch, and capabilities are required"),
}


def _validate_mvp002_envelope(record: dict) -> None:
    required = {"schema_version","object_type","id","version","status","validation_state","content","authorship","provenance","authority","privacy_tier","relationships"}
    missing = sorted(required - record.keys())
    if missing:
        raise LCAError(f"record missing required fields: {', '.join(missing)}")
    if record["schema_version"] != "lca-schema-0.1":
        raise LCAError("unsupported schema_version")
    if record["object_type"] not in REQUIRED_CONTENT:
        raise LCAError("unsupported object_type")
    if not re.fullmatch(r"lca-[a-z0-9][a-z0-9-]*", record["id"]):
        raise LCAError("invalid stable id")
    if not isinstance(record["content"], dict):
        raise LCAError("content must be an object")
    if not isinstance(record["relationships"], list):
        raise LCAError("relationships must be a list")


def validate_per_object(record: dict) -> None:
    if record["object_type"] in ORIGINAL_TYPES:
        validate_record(record)
    else:
        _validate_mvp002_envelope(record)
    required, message = REQUIRED_CONTENT[record["object_type"]]
    content_keys = set(record["content"].keys())
    if record["object_type"] == "SourceRecord":
        valid = bool(content_keys & required)
        missing = sorted(required - content_keys)
    else:
        valid = required <= content_keys
        missing = sorted(required - content_keys)
    if not valid:
        raise LCAError(f"{record['object_type']}: {message}; missing {', '.join(missing)}")

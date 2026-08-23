from __future__ import annotations

import sys
from pathlib import Path

REFERENCE = Path(__file__).resolve().parents[2] / "reference_impl" / "python"
if str(REFERENCE) not in sys.path:
    sys.path.insert(0, str(REFERENCE))

from lca_mvp import LCAError, validate_record  # noqa: E402


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
}


def validate_per_object(record: dict) -> None:
    validate_record(record)
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

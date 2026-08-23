"""Small, dependency-free LCA reference implementation.

The MVP keeps Markdown/YAML compatibility as a boundary concern while making
the authoritative semantics executable in JSON + SQLite:

  canonical records -> immutable versions -> append-only event ledger
  -> disposable lexical/graph retrieval -> continuity and authority checks

This is intentionally a reference implementation, not a production identity
system or a claim of consciousness continuity.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from typing import Any, Iterable


SCHEMA_VERSION = "lca-schema-0.1"
OBJECT_TYPES = {
    "SourceRecord", "Episode", "Claim", "Interpretation", "DecisionTrace",
    "WeatherState", "Invariant", "Transformation", "PortraitResponse",
    "BudState", "BranchState", "AuthorityGrant", "SourceReview",
}
STATUSES = {"scratch", "candidate", "active", "superseded", "deprecated", "archived"}
VALIDATION_STATES = {"unverified", "corroborated", "disputed", "rejected"}
RESPONSE_CLASSES = {"A", "B", "C", "D", "E", "F"}


class LCAError(ValueError):
    """Raised for a record, ledger, continuity, or authorization violation."""


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256(value: Any) -> str:
    raw = value if isinstance(value, bytes) else canonical_json(value).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise LCAError(message)


def validate_record(record: dict[str, Any]) -> None:
    required = {
        "schema_version", "object_type", "id", "version", "status",
        "validation_state", "content", "authorship", "provenance",
        "authority", "privacy_tier", "relationships",
    }
    missing = sorted(required - record.keys())
    _require(not missing, f"record missing required fields: {', '.join(missing)}")
    _require(record["schema_version"] == SCHEMA_VERSION, "unsupported schema_version")
    _require(record["object_type"] in OBJECT_TYPES, "unsupported object_type")
    _require(bool(re.fullmatch(r"lca-[a-z0-9][a-z0-9-]*", record["id"])), "invalid stable id")
    _require(isinstance(record["version"], int) and record["version"] >= 1, "version must be a positive integer")
    _require(record["status"] in STATUSES, "invalid lifecycle status")
    _require(record["validation_state"] in VALIDATION_STATES, "invalid validation_state")
    _require(isinstance(record["content"], dict), "content must be an object")
    _require(0 <= record["privacy_tier"] <= 3, "privacy_tier must be 0..3")
    _require(isinstance(record["relationships"], list), "relationships must be a list")

    authorship = record["authorship"]
    for key in ("primary", "contributors", "assistant_generated", "user_endorsement", "mixed_authorship"):
        _require(key in authorship, f"authorship missing {key}")
    _require(authorship["user_endorsement"] in {"none", "pending", "partial", "affirmed", "rejected"}, "invalid endorsement")

    provenance = record["provenance"]
    for key in ("source_ids", "source_hashes", "transformation_history", "model_version", "ontology_version", "verified"):
        _require(key in provenance, f"provenance missing {key}")
    _require(isinstance(provenance["source_ids"], list), "provenance.source_ids must be a list")
    _require(isinstance(provenance["source_hashes"], list), "provenance.source_hashes must be a list")

    authority = record["authority"]
    for key in ("level", "domains", "may_speak_for_source"):
        _require(key in authority, f"authority missing {key}")
    _require(authority["level"] in {"evidentiary", "bounded", "negotiated", "independent", "none"}, "invalid authority level")

    continuity = record.get("continuity")
    if continuity:
        for key in ("provenance_integrity", "developmental_continuity", "invariant_fidelity"):
            if key in continuity:
                _require(0 <= continuity[key] <= 1, f"continuity.{key} must be 0..1")

    if record["object_type"] == "PortraitResponse":
        response_class = record["content"].get("response_class")
        _require(response_class in RESPONSE_CLASSES, "PortraitResponse requires response_class A..F")
        _require(bool(record["content"].get("evidence_ids")), "PortraitResponse requires evidence_ids")


def new_record(
    object_type: str,
    object_id: str,
    content: dict[str, Any],
    *,
    primary_author: str | None = "source",
    authorship_class: str = "source_person",
    assistant_generated: bool = False,
    user_endorsement: str = "none",
    provenance_source_ids: Iterable[str] = (),
    provenance_source_hashes: Iterable[str] = (),
    transformation_history: Iterable[str] = (),
    model_version: str | None = None,
    verified: bool = False,
    authority_level: str = "evidentiary",
    may_speak_for_source: bool = False,
    privacy_tier: int = 0,
    status: str = "candidate",
    validation_state: str = "unverified",
    relationships: Iterable[dict[str, Any]] = (),
    continuity: dict[str, Any] | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "object_type": object_type,
        "id": object_id,
        "version": 1,
        "status": status,
        "validation_state": validation_state,
        "content": copy.deepcopy(content),
        "authorship": {
            "primary": primary_author,
            "contributors": [],
            "assistant_generated": assistant_generated,
            "user_endorsement": user_endorsement,
            "mixed_authorship": authorship_class == "mixed_dialogue",
            "authorship_class": authorship_class,
        },
        "provenance": {
            "source_ids": list(provenance_source_ids),
            "source_hashes": list(provenance_source_hashes),
            "transformation_history": list(transformation_history),
            "model_version": model_version,
            "ontology_version": SCHEMA_VERSION,
            "verified": verified,
            "observed_at": now(),
            "recorded_at": now(),
        },
        "authority": {
            "level": authority_level,
            "domains": [],
            "may_speak_for_source": may_speak_for_source,
        },
        "privacy_tier": privacy_tier,
        "relationships": list(relationships),
    }
    if continuity is not None:
        record["continuity"] = copy.deepcopy(continuity)
    validate_record(record)
    return record


def deep_merge(original: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(original)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result


class MemoryStore:
    """Authoritative records plus immutable versions and an append-only ledger."""

    def __init__(self, db_path: str = ":memory:") -> None:
        self.db = sqlite3.connect(db_path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS objects(
                object_id TEXT PRIMARY KEY,
                object_type TEXT NOT NULL,
                current_version INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS versions(
                object_id TEXT NOT NULL,
                version INTEGER NOT NULL,
                record_json TEXT NOT NULL,
                record_hash TEXT NOT NULL,
                actor TEXT NOT NULL,
                created_at TEXT NOT NULL,
                PRIMARY KEY(object_id, version),
                FOREIGN KEY(object_id) REFERENCES objects(object_id)
            );
            CREATE TABLE IF NOT EXISTS relations(
                source_id TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                target_id TEXT NOT NULL,
                event_seq INTEGER NOT NULL,
                PRIMARY KEY(source_id, relation_type, target_id)
            );
            CREATE TABLE IF NOT EXISTS events(
                seq INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT NOT NULL UNIQUE,
                event_type TEXT NOT NULL,
                object_id TEXT,
                from_version INTEGER,
                to_version INTEGER,
                actor TEXT NOT NULL,
                reason TEXT NOT NULL,
                evidence_json TEXT NOT NULL,
                transformation_id TEXT,
                previous_event_hash TEXT,
                event_hash TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """
        )
        self.db.commit()

    def close(self) -> None:
        self.db.close()

    def _last_event_hash(self) -> str | None:
        row = self.db.execute("SELECT event_hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        return row["event_hash"] if row else None

    def _event(
        self,
        *,
        event_type: str,
        object_id: str | None,
        from_version: int | None,
        to_version: int | None,
        actor: str,
        reason: str,
        evidence_ids: Iterable[str] = (),
        transformation_id: str | None = None,
        payload: Any = None,
    ) -> int:
        created = now()
        event_id = f"lca-event-{sha256({'created': created, 'object_id': object_id, 'event_type': event_type, 'payload': payload})[:20]}"
        previous = self._last_event_hash()
        body = {
            "event_id": event_id,
            "event_type": event_type,
            "object_id": object_id,
            "from_version": from_version,
            "to_version": to_version,
            "actor": actor,
            "reason": reason,
            "evidence_ids": list(evidence_ids),
            "transformation_id": transformation_id,
            "previous_event_hash": previous,
            "payload": payload,
            "created_at": created,
        }
        event_hash = sha256(body)
        cur = self.db.execute(
            """INSERT INTO events(event_id,event_type,object_id,from_version,to_version,actor,reason,
               evidence_json,transformation_id,previous_event_hash,event_hash,payload_json,created_at)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (event_id, event_type, object_id, from_version, to_version, actor, reason,
             canonical_json(list(evidence_ids)), transformation_id, previous, event_hash,
             canonical_json(payload), created),
        )
        return int(cur.lastrowid)

    def append(self, record: dict[str, Any], *, actor: str, reason: str, evidence_ids: Iterable[str] = ()) -> None:
        validate_record(record)
        _require(record["version"] == 1, "new records must start at version 1")
        _require(self.get(record["id"], required=False) is None, "stable id already exists; use update")
        created = now()
        record_json = canonical_json(record)
        self.db.execute(
            "INSERT INTO objects(object_id,object_type,current_version,created_at,updated_at) VALUES(?,?,?,?,?)",
            (record["id"], record["object_type"], 1, created, created),
        )
        self.db.execute(
            "INSERT INTO versions(object_id,version,record_json,record_hash,actor,created_at) VALUES(?,?,?,?,?,?)",
            (record["id"], 1, record_json, sha256(record), actor, created),
        )
        seq = self._event(event_type="create", object_id=record["id"], from_version=None,
                          to_version=1, actor=actor, reason=reason, evidence_ids=evidence_ids,
                          payload=record)
        for relation in record["relationships"]:
            self._add_relation(record["id"], relation["type"], relation["target_id"], seq)
        self.db.commit()

    def _add_relation(self, source_id: str, relation_type: str, target_id: str, event_seq: int) -> None:
        self.db.execute(
            "INSERT OR IGNORE INTO relations(source_id,relation_type,target_id,event_seq) VALUES(?,?,?,?)",
            (source_id, relation_type, target_id, event_seq),
        )

    def relate(self, source_id: str, relation_type: str, target_id: str, *, actor: str, reason: str) -> None:
        _require(self.get(source_id) is not None, "source object does not exist")
        seq = self._event(event_type="relate", object_id=source_id, from_version=None,
                          to_version=None, actor=actor, reason=reason,
                          payload={"relation_type": relation_type, "target_id": target_id})
        self._add_relation(source_id, relation_type, target_id, seq)
        self.db.commit()

    def update(
        self,
        object_id: str,
        patch: dict[str, Any],
        *,
        actor: str,
        reason: str,
        evidence_ids: Iterable[str] = (),
        transformation_id: str | None = None,
    ) -> dict[str, Any]:
        current = self.get(object_id)
        _require(current is not None, "object does not exist")
        updated = deep_merge(current, patch)
        updated["id"] = object_id
        updated["version"] = current["version"] + 1
        updated["provenance"] = deep_merge(updated["provenance"], {
            "transformation_history": list(updated["provenance"].get("transformation_history", []))
            + ([transformation_id] if transformation_id else []),
            "recorded_at": now(),
        })
        validate_record(updated)
        created = now()
        self.db.execute(
            "INSERT INTO versions(object_id,version,record_json,record_hash,actor,created_at) VALUES(?,?,?,?,?,?)",
            (object_id, updated["version"], canonical_json(updated), sha256(updated), actor, created),
        )
        self.db.execute("UPDATE objects SET current_version=?, updated_at=? WHERE object_id=?",
                        (updated["version"], created, object_id))
        seq = self._event(event_type="update", object_id=object_id,
                          from_version=current["version"], to_version=updated["version"],
                          actor=actor, reason=reason, evidence_ids=evidence_ids,
                          transformation_id=transformation_id, payload=updated)
        for relation in updated["relationships"]:
            self._add_relation(object_id, relation["type"], relation["target_id"], seq)
        self.db.commit()
        return updated

    def get(self, object_id: str, version: int | None = None, *, required: bool = True) -> dict[str, Any] | None:
        if version is None:
            row = self.db.execute("SELECT current_version FROM objects WHERE object_id=?", (object_id,)).fetchone()
            if row:
                version = row["current_version"]
        row = self.db.execute("SELECT record_json FROM versions WHERE object_id=? AND version=?",
                              (object_id, version)).fetchone() if version else None
        if not row:
            if required:
                raise LCAError(f"object not found: {object_id}")
            return None
        return json.loads(row["record_json"])

    def history(self, object_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute("SELECT record_json FROM versions WHERE object_id=? ORDER BY version", (object_id,))
        return [json.loads(row["record_json"]) for row in rows]

    def events(self, object_id: str | None = None) -> list[dict[str, Any]]:
        if object_id:
            rows = self.db.execute("SELECT * FROM events WHERE object_id=? ORDER BY seq", (object_id,))
        else:
            rows = self.db.execute("SELECT * FROM events ORDER BY seq")
        return [dict(row) for row in rows]

    def query(self, text: str = "", *, object_type: str | None = None,
              privacy_max: int = 0, include_superseded: bool = False) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT object_id,current_version FROM objects ORDER BY object_id"
        ).fetchall()
        tokens = [token.lower() for token in re.findall(r"[\w-]+", text) if len(token) > 1]
        scored: list[tuple[int, dict[str, Any]]] = []
        for row in rows:
            record = self.get(row["object_id"])
            if object_type and record["object_type"] != object_type:
                continue
            if record["privacy_tier"] > privacy_max:
                continue
            if not include_superseded and record["status"] in {"superseded", "deprecated", "archived"}:
                continue
            haystack = canonical_json(record).lower()
            score = sum(haystack.count(token) for token in tokens) if tokens else 1
            if score or not tokens:
                scored.append((score, record))
        scored.sort(key=lambda item: (-item[0], item[1]["id"]))
        return [record for _, record in scored]

    def related(self, object_id: str, relation_type: str | None = None) -> list[dict[str, Any]]:
        sql = "SELECT target_id FROM relations WHERE source_id=?"
        args: list[Any] = [object_id]
        if relation_type:
            sql += " AND relation_type=?"
            args.append(relation_type)
        rows = self.db.execute(sql, args).fetchall()
        return [self.get(row["target_id"], required=False) for row in rows if self.get(row["target_id"], required=False)]

    def verify_integrity(self) -> dict[str, Any]:
        failures: list[str] = []
        for row in self.db.execute("SELECT * FROM versions ORDER BY object_id,version"):
            record = json.loads(row["record_json"])
            if sha256(record) != row["record_hash"]:
                failures.append(f"record:{row['object_id']}:{row['version']}")
        previous = None
        for row in self.db.execute("SELECT * FROM events ORDER BY seq"):
            body = {
                "event_id": row["event_id"], "event_type": row["event_type"], "object_id": row["object_id"],
                "from_version": row["from_version"], "to_version": row["to_version"], "actor": row["actor"],
                "reason": row["reason"], "evidence_ids": json.loads(row["evidence_json"]),
                "transformation_id": row["transformation_id"], "previous_event_hash": row["previous_event_hash"],
                "payload": json.loads(row["payload_json"]), "created_at": row["created_at"],
            }
            if row["previous_event_hash"] != previous or sha256(body) != row["event_hash"]:
                failures.append(f"event:{row['seq']}")
            previous = row["event_hash"]
        return {"ok": not failures, "failures": failures}

    def snapshot(self) -> dict[str, Any]:
        records = []
        for row in self.db.execute("SELECT object_id FROM objects ORDER BY object_id"):
            records.append(self.get(row["object_id"]))
        return {"schema_version": SCHEMA_VERSION, "records": records, "events": self.events(),
                "integrity": self.verify_integrity()}


class ContinuityEngine:
    """Makes the P/C/F/A orientation layer explicit and testable."""

    @staticmethod
    def classify(continuity: dict[str, Any]) -> dict[str, Any]:
        p = float(continuity.get("provenance_integrity", 0.0))
        c = float(continuity.get("developmental_continuity", 0.0))
        f = float(continuity.get("invariant_fidelity", 0.0))
        co_developed = bool(continuity.get("co_developed", False))
        separated = bool(continuity.get("separated", False))
        rejected_core = bool(continuity.get("rejected_core_invariant", False))

        if p < 0.80:
            stage = "unclassified"
            reason = "provenance integrity is below the minimum for a lineage claim"
        elif separated or rejected_core or f < 0.70:
            stage = "branch"
            reason = "lineage is preserved, but invariant fidelity or separation changes identity-authority scope"
        elif co_developed and c >= 0.70 and f >= 0.70:
            stage = "bud"
            reason = "provenance, co-development, continuity, and invariant fidelity meet the Bud threshold"
        elif c >= 0.50 and f >= 0.75:
            stage = "portrait"
            reason = "the representation is inspectable and bounded, but not yet a co-developed Bud"
        else:
            stage = "portrait_candidate"
            reason = "lineage evidence exists, but continuity and fidelity are not sufficient for Bud status"

        return {
            "stage": stage,
            "scores": {"P": round(p, 3), "C": round(c, 3), "F": round(f, 3)},
            "authority_scope": ContinuityEngine.authority_for(stage),
            "reason": reason,
            "identity_claim_allowed": stage in {"bud", "branch"},
        }

    @staticmethod
    def authority_for(stage: str) -> dict[str, bool]:
        common = {
            "may_quote": False,
            "may_infer": False,
            "may_sign_contract": False,
            "may_access_private_weather": False,
            "may_modify_canonical_source": False,
            "may_present_as_source_memory": False,
        }
        if stage in {"portrait", "portrait_candidate"}:
            common.update({"may_quote": True, "may_infer": True})
        elif stage == "bud":
            common.update({"may_quote": True, "may_infer": True})
        elif stage == "branch":
            common.update({"may_quote": True, "may_infer": True})
        return common

    @staticmethod
    def transition_test(parent: dict[str, Any], proposed: dict[str, Any]) -> dict[str, Any]:
        result = ContinuityEngine.classify(proposed.get("continuity", proposed))
        result["parent_id"] = parent.get("id")
        result["proposed_object_type"] = proposed.get("object_type")
        result["passed"] = result["stage"] != "unclassified"
        return result


class AuthorityEngine:
    """MVP RBAC/ABAC-style rights check for cognitive records."""

    @staticmethod
    def check(actor_role: str, action: str, target: dict[str, Any], *, grant: dict[str, Any] | None = None) -> bool:
        role = actor_role.lower()
        if action == "read_private_weather":
            if target["object_type"] != "WeatherState" or target["privacy_tier"] < 2:
                return True
            return role in {"source", "steward"} or bool(grant and action in grant.get("allowed_actions", []))
        if action == "modify_canonical_source":
            return role in {"source", "steward"} or bool(grant and action in grant.get("allowed_actions", []))
        if action == "speak_for_source":
            return bool(target["authority"].get("may_speak_for_source")) and role in {"source", "steward", "bud"}
        if action == "sign_contract":
            return role in {"source", "steward"} or bool(grant and action in grant.get("allowed_actions", []))
        if action == "quote":
            return role in {"portrait", "bud", "branch", "source", "steward"}
        if action == "infer":
            return role in {"portrait", "bud", "branch", "sherpa", "source", "steward"}
        raise LCAError(f"unknown action: {action}")


def make_response(
    response_id: str,
    answer: str,
    evidence_ids: Iterable[str],
    *,
    response_class: str = "B",
    actor: str = "assistant",
    model_version: str = "reference-model",
) -> dict[str, Any]:
    _require(response_class in RESPONSE_CLASSES, "response_class must be A..F")
    evidence_ids = list(evidence_ids)
    return new_record(
        "PortraitResponse", response_id,
        {"answer": answer, "evidence_ids": evidence_ids, "response_class": response_class},
        primary_author=actor, authorship_class="assistant", assistant_generated=True,
        provenance_source_ids=evidence_ids, model_version=model_version,
        authority_level="bounded", may_speak_for_source=False,
        status="active", validation_state="unverified",
    )


REVIEW_TYPES = {
    "affirmed_as_mine",
    "good_inference_not_explicit",
    "assistant_contamination",
    "historical_revision",
    "invariant_reaffirmed",
    "branch_disagreement",
    "private_weather",
}


def record_source_review(
    review_id: str,
    target_id: str,
    review_type: str,
    note: str,
    *,
    source_actor: str = "living-source",
) -> dict[str, Any]:
    """Create a first-class source correction/endorsement without rewriting history."""
    _require(review_type in REVIEW_TYPES, "unsupported source review type")
    return new_record(
        "SourceReview", review_id,
        {"target_id": target_id, "review_type": review_type, "note": note},
        primary_author=source_actor, authorship_class="source_person",
        user_endorsement="affirmed" if review_type in {"affirmed_as_mine", "invariant_reaffirmed"} else "partial",
        provenance_source_ids=[target_id], authority_level="evidentiary",
        may_speak_for_source=True, status="active", validation_state="corroborated",
        relationships=[{"type": "reviews", "target_id": target_id}],
    )

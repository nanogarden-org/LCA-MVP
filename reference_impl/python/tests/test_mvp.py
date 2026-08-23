import unittest

from lca_mvp import (
    AuthorityEngine,
    ContinuityEngine,
    LCAError,
    MemoryStore,
    make_response,
    new_record,
    record_source_review,
)


class LCAMVPTests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()
        self.source = new_record(
            "SourceRecord", "lca-source-founder-principle",
            {"text": "Preserve raw sources and make every transformation inspectable.", "title": "Founder principle"},
            primary_author="living-source", authorship_class="source_person",
            provenance_source_ids=["lca-source-founder-principle"],
            provenance_source_hashes=["sha256:fixture"], verified=True,
            authority_level="evidentiary", may_speak_for_source=True, status="active",
            validation_state="corroborated",
        )
        self.store.append(self.source, actor="living-source", reason="seed canonical source")

    def tearDown(self):
        self.store.close()

    def test_append_before_overwrite_and_ledger_integrity(self):
        updated = self.store.update(
            self.source["id"],
            {"content": {"text": "Preserve raw sources, append before overwrite, and make transformations inspectable."}},
            actor="living-source", reason="clarify invariant", evidence_ids=[self.source["id"]],
            transformation_id="lca-transform-clarify-1",
        )
        self.assertEqual(updated["version"], 2)
        self.assertEqual(len(self.store.history(self.source["id"])), 2)
        self.assertEqual(len(self.store.events(self.source["id"])), 2)
        self.assertTrue(self.store.verify_integrity()["ok"])

    def test_authorship_confusion_is_visible(self):
        response = make_response("lca-response-1", "The source prefers inspectable transformations.", [self.source["id"]])
        self.assertTrue(response["authorship"]["assistant_generated"])
        self.assertFalse(response["authority"]["may_speak_for_source"])
        self.assertNotEqual(response["authorship"]["primary"], "living-source")

    def test_unverified_memory_is_not_promoted_by_retrieval(self):
        claim = new_record(
            "Claim", "lca-claim-unverified",
            {"text": "The founder approved an unrecorded policy exception."},
            primary_author="assistant", authorship_class="assistant", assistant_generated=True,
            provenance_source_ids=[], status="candidate", validation_state="unverified",
            authority_level="none",
        )
        self.store.append(claim, actor="assistant", reason="candidate extraction")
        results = self.store.query("approved policy exception", privacy_max=0)
        self.assertEqual(results[0]["id"], claim["id"])
        self.assertEqual(results[0]["validation_state"], "unverified")
        self.assertNotEqual(results[0]["status"], "active")

    def test_contradictions_remain_distinct(self):
        a = new_record("Claim", "lca-claim-a", {"text": "Adopt a public roadmap."}, primary_author="living-source", status="active")
        b = new_record("Claim", "lca-claim-b", {"text": "Keep the roadmap private until tested."}, primary_author="living-source", status="active", validation_state="disputed")
        self.store.append(a, actor="living-source", reason="record claim A")
        self.store.append(b, actor="living-source", reason="record contradictory claim B")
        results = self.store.query("roadmap", privacy_max=0)
        self.assertEqual({r["id"] for r in results}, {a["id"], b["id"]})
        self.assertEqual(self.store.get(b["id"])["validation_state"], "disputed")

    def test_stale_belief_is_excluded_from_active_view(self):
        claim = new_record("Claim", "lca-claim-stale", {"text": "Use the old policy."}, primary_author="living-source", status="active")
        self.store.append(claim, actor="living-source", reason="record old policy")
        self.store.update(claim["id"], {"status": "superseded", "superseded_by": "lca-claim-new"}, actor="living-source", reason="policy revised")
        self.assertEqual(self.store.query("old policy", privacy_max=0), [])
        self.assertEqual(len(self.store.query("old policy", privacy_max=0, include_superseded=True)), 1)

    def test_private_weather_is_denied_to_portrait(self):
        weather = new_record(
            "WeatherState", "lca-weather-private", {"state": "high cognitive load"},
            primary_author="living-source", privacy_tier=2, status="active",
        )
        self.store.append(weather, actor="living-source", reason="record private weather")
        self.assertFalse(AuthorityEngine.check("portrait", "read_private_weather", weather))
        self.assertTrue(AuthorityEngine.check("steward", "read_private_weather", weather))

    def test_canonical_source_modification_is_denied_to_portrait(self):
        self.assertFalse(AuthorityEngine.check("portrait", "modify_canonical_source", self.source))
        self.assertTrue(AuthorityEngine.check("steward", "modify_canonical_source", self.source))

    def test_invariant_drift_becomes_branch_not_failed_provenance(self):
        result = ContinuityEngine.transition_test(
            self.source,
            {"object_type": "BudState", "continuity": {
                "parent_id": self.source["id"], "provenance_integrity": 1.0,
                "developmental_continuity": 0.85, "invariant_fidelity": 0.35,
                "co_developed": True,
            }},
        )
        self.assertEqual(result["scores"]["P"], 1.0)
        self.assertEqual(result["stage"], "branch")
        self.assertFalse(result["authority_scope"]["may_present_as_source_memory"])

    def test_retrieval_returns_evidence_path(self):
        response = make_response("lca-response-evidence", "Raw sources remain inspectable.", [self.source["id"]], response_class="B")
        self.store.append(response, actor="assistant", reason="source-bound synthesis", evidence_ids=[self.source["id"]])
        found = self.store.query("inspectable raw sources", object_type="PortraitResponse", privacy_max=0)
        self.assertEqual(found[0]["content"]["evidence_ids"], [self.source["id"]])
        self.assertEqual(self.store.events(response["id"])[0]["event_type"], "create")

    def test_invalid_silent_overwrite_is_rejected(self):
        with self.assertRaises(LCAError):
            self.store.append(self.source, actor="assistant", reason="attempt overwrite")

    def test_living_source_review_is_a_governed_record(self):
        review = record_source_review(
            "lca-review-1", self.source["id"], "good_inference_not_explicit",
            "Good inference, but I did not explicitly say this.",
        )
        self.store.append(review, actor="living-source", reason="record source review", evidence_ids=[self.source["id"]])
        self.assertEqual(review["object_type"], "SourceReview")
        self.assertEqual(self.store.related(review["id"], "reviews")[0]["id"], self.source["id"])
        self.assertEqual(self.store.events(review["id"])[0]["event_type"], "create")


if __name__ == "__main__":
    unittest.main(verbosity=2)

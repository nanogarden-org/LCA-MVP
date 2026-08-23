import json

from lca_mvp import AuthorityEngine, ContinuityEngine, MemoryStore, make_response, new_record


def main():
    store = MemoryStore()
    source = new_record(
        "SourceRecord", "lca-demo-source",
        {"title": "Pilot source", "text": "Preserve raw sources; make transformation paths inspectable."},
        primary_author="living-source", provenance_source_ids=["lca-demo-source"],
        provenance_source_hashes=["sha256:demo"], verified=True, status="active",
        validation_state="corroborated", authority_level="evidentiary", may_speak_for_source=True,
    )
    store.append(source, actor="living-source", reason="ingest pilot source")

    episode = new_record(
        "Episode", "lca-demo-episode",
        {"title": "Pilot design conversation", "scene": "A design discussion distinguishes archive from portrait."},
        primary_author="living-source", provenance_source_ids=[source["id"]],
        relationships=[{"type": "derived_from", "target_id": source["id"]}], status="active",
    )
    store.append(episode, actor="living-source", reason="assemble episode", evidence_ids=[source["id"]])

    invariant = new_record(
        "Invariant", "lca-demo-invariant",
        {"name": "Inspectable lineage", "statement": "No silent source overwrite."},
        primary_author="living-source", provenance_source_ids=[source["id"]],
        status="active", validation_state="corroborated",
    )
    store.append(invariant, actor="living-source", reason="register invariant", evidence_ids=[source["id"]])

    response = make_response(
        "lca-demo-response",
        "The pilot supports a bounded portrait because the source and evidence path remain inspectable.",
        [source["id"], episode["id"], invariant["id"]], response_class="B",
    )
    store.append(response, actor="assistant", reason="source-bound synthesis",
                 evidence_ids=response["content"]["evidence_ids"])

    transition = ContinuityEngine.transition_test(
        source,
        {"object_type": "BudState", "continuity": {
            "parent_id": source["id"], "provenance_integrity": 1.0,
            "developmental_continuity": 0.78, "invariant_fidelity": 0.82,
            "co_developed": True,
        }},
    )
    print("LCA MVP demo")
    print(json.dumps({
        "records": [r["id"] for r in store.query(privacy_max=0, include_superseded=True)],
        "ledger_events": len(store.events()),
        "retrieval": [r["id"] for r in store.query("inspectable lineage", privacy_max=0)],
        "transition_test": transition,
        "portrait_private_weather_allowed": AuthorityEngine.check(
            "portrait", "read_private_weather",
            new_record("WeatherState", "lca-demo-weather", {"state": "private"}, privacy_tier=2),
        ),
        "integrity": store.verify_integrity(),
    }, indent=2))
    store.close()


if __name__ == "__main__":
    main()

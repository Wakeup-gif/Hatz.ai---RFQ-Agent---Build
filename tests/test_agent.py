from hatz_quick_rfq import summarize_rfq


def test_stop_for_empty_placeholder_input():
    output = summarize_rfq("Customer:\nProject:\nScope:")
    assert "Status:\nStop — Required Information Missing" in output
    assert "Readable RFQ scope content" in output
    assert "Human Review Gate" in output


def test_ready_when_core_details_present():
    output = summarize_rfq(
        "Customer: Acme\nProject: Lobby refresh\nLocation: Boston\n"
        "Scope: 3 acrylic wall signs\nDimensions: 24 in x 36 in\n"
        "Materials: acrylic\nFinish: painted blue\nInstall: by vendor"
    )
    assert "Status:\nReady for Estimator Review" in output
    assert "pricing can proceed" not in output.lower()
    assert "3 acrylic wall signs" in output


def test_attachment_reference_not_treated_as_reviewed():
    output = summarize_rfq("Please quote the attached sign schedule and drawings.")
    assert "Attachment mentioned but contents not provided." in output
    assert "Stop condition present:\nYes" in output


def test_hatz_adapter_returns_review_envelope():
    from hatz_quick_rfq.adapters import build_hatz_response

    response = build_hatz_response({"text": "Scope: 2 vinyl signs Dimensions: 10 in x 20 in"})

    assert response["platform_alignment"] == "Hatz.ai"
    assert response["human_review_required"] is True
    assert "pricing" in response["prohibited_authorities"]
    assert "# RFQ Intake Summary" in response["summary_markdown"]


def test_readiness_blocks_hatz_until_evidence_and_deployment_complete():
    from hatz_quick_rfq.validation import evaluate_hatz_readiness

    report = evaluate_hatz_readiness()

    assert report.ready_for_hatz is False
    assert "smoke_tests" in report.missing_evidence
    assert "hatz_routing" in report.missing_deployment_decisions
    assert report.status == "Not ready for Hatz rollout"


def test_readiness_allows_hatz_when_all_gates_complete():
    from hatz_quick_rfq.validation.readiness import REQUIRED_DEPLOYMENT_DECISIONS, REQUIRED_EVIDENCE
    from hatz_quick_rfq.validation import evaluate_hatz_readiness

    report = evaluate_hatz_readiness(
        evidence={key: True for key in REQUIRED_EVIDENCE},
        deployment_decisions={key: True for key in REQUIRED_DEPLOYMENT_DECISIONS},
    )

    assert report.ready_for_hatz is True
    assert report.status == "Ready for controlled Hatz rollout"


def test_evidence_record_writer_creates_json(tmp_path):
    import json
    from hatz_quick_rfq.validation import EvidenceRecord, write_evidence_record

    path = write_evidence_record(
        EvidenceRecord(evidence_type="qa-run", title="Smoke pass", summary="Smoke evidence recorded."),
        root=tmp_path,
    )

    data = json.loads(path.read_text(encoding="utf-8"))
    assert path.parent.name == "qa-runs"
    assert data["evidence_type"] == "qa-run"
    assert data["title"] == "Smoke pass"


def test_hatz_adapter_includes_readiness_report():
    from hatz_quick_rfq.adapters import build_hatz_response

    response = build_hatz_response({"text": "Scope: 1 sign Dimensions: 10 in x 20 in"})

    assert response["readiness"]["ready_for_hatz"] is False
    assert "smoke_tests" in response["readiness"]["missing_evidence"]


def test_deployment_operations_matrix_separates_buildable_from_unknowns():
    from hatz_quick_rfq.validation import deployment_operations_matrix, unanswered_deployment_variables

    matrix = deployment_operations_matrix()
    unknowns = unanswered_deployment_variables()

    assert "hatz_routing" in matrix
    assert "Payload contract" in matrix["hatz_routing"]["buildable_now"][0]
    assert "Actual Hatz workspace routing primitives and trigger format" in unknowns["hatz_routing"]
    assert "attachment_text_extraction" in matrix

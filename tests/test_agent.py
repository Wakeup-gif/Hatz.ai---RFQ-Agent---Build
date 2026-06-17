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

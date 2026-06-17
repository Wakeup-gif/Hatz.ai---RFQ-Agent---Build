"""Hatz readiness gate evaluation.

The project is intentionally not considered broadly ready until operational
configuration and validation evidence are present. This module makes that gate
machine-readable for CI, Hatz workflow checks, and release review.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

REQUIRED_EVIDENCE = (
    "smoke_tests",
    "qa_pack",
    "issue_disposition",
    "pilot_run",
    "reviewer_feedback",
    "readiness_scorecard",
    "go_no_go_decision",
)

REQUIRED_DEPLOYMENT_DECISIONS = (
    "hatz_routing",
    "permissions",
    "storage_retention",
    "observability",
    "attachment_text_extraction",
    "audit_logging",
    "rollback_plan",
)


@dataclass(frozen=True)
class ReadinessReport:
    """A release-gate report for the Quick RFQ agent."""

    status: str
    ready_for_hatz: bool
    ready_for_pilot: bool
    missing_evidence: tuple[str, ...]
    missing_deployment_decisions: tuple[str, ...]
    notes: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "ready_for_hatz": self.ready_for_hatz,
            "ready_for_pilot": self.ready_for_pilot,
            "missing_evidence": list(self.missing_evidence),
            "missing_deployment_decisions": list(self.missing_deployment_decisions),
            "notes": list(self.notes),
        }


def evaluate_hatz_readiness(
    evidence: dict[str, bool] | None = None,
    deployment_decisions: dict[str, bool] | None = None,
) -> ReadinessReport:
    """Evaluate whether the agent can move through Hatz readiness gates.

    `evidence` and `deployment_decisions` are maps where keys are the required
    gate names and truthy values mean the item has been completed and reviewed.
    """

    evidence = evidence or {}
    deployment_decisions = deployment_decisions or {}
    missing_evidence = tuple(name for name in REQUIRED_EVIDENCE if not evidence.get(name))
    missing_deployment = tuple(
        name for name in REQUIRED_DEPLOYMENT_DECISIONS if not deployment_decisions.get(name)
    )

    smoke_and_qa_ready = not any(
        item in missing_evidence for item in ("smoke_tests", "qa_pack", "issue_disposition")
    )
    ready_for_pilot = smoke_and_qa_ready and not missing_deployment
    ready_for_hatz = not missing_evidence and not missing_deployment

    if ready_for_hatz:
        status = "Ready for controlled Hatz rollout"
    elif ready_for_pilot:
        status = "Ready for internal pilot only"
    else:
        status = "Not ready for Hatz rollout"

    notes = [
        "Agent output remains intake support only; human review is required before action.",
        "Do not enable customer-send, pricing, scheduling, purchasing, or production release behavior.",
    ]
    if missing_evidence:
        notes.append("Validation evidence is incomplete.")
    if missing_deployment:
        notes.append("Hatz deployment decisions are incomplete.")

    return ReadinessReport(
        status=status,
        ready_for_hatz=ready_for_hatz,
        ready_for_pilot=ready_for_pilot,
        missing_evidence=missing_evidence,
        missing_deployment_decisions=missing_deployment,
        notes=tuple(notes),
    )

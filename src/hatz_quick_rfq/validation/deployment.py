"""Deployment operations decision model for Hatz rollout planning.

This module separates what this repo can build generically from the values that
must come from the customer's Hatz workspace, security policy, and operating
processes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DeploymentOperation:
    """One deployment operation area and its answerability boundary."""

    key: str
    label: str
    buildable_now: tuple[str, ...]
    required_variables: tuple[str, ...]
    default_status: str = "needs-input"

    def to_dict(self) -> dict[str, Any]:
        return {
            "key": self.key,
            "label": self.label,
            "buildable_now": list(self.buildable_now),
            "required_variables": list(self.required_variables),
            "default_status": self.default_status,
        }


DEPLOYMENT_OPERATIONS = (
    DeploymentOperation(
        key="hatz_routing",
        label="Hatz routing",
        buildable_now=(
            "Payload contract for RFQ text and readable source records",
            "Adapter response envelope with summary, guardrails, and readiness metadata",
            "Route names for intake, human review, evidence capture, and release decision steps",
        ),
        required_variables=(
            "Actual Hatz workspace routing primitives and trigger format",
            "Which teams/users receive estimator review tasks",
            "Escalation routing for Stop or Needs Clarification outputs",
        ),
    ),
    DeploymentOperation(
        key="permissions",
        label="Permissions",
        buildable_now=(
            "Role matrix template for requester, estimator, PM, admin, and auditor",
            "Read/write separation for source input, generated summaries, evidence, and release decisions",
            "Human-review-required flag in every adapter response",
        ),
        required_variables=(
            "Customer identity provider and Hatz role model",
            "Named users/groups allowed to view RFQs and evidence",
            "Data sensitivity requirements for customer files and project details",
        ),
    ),
    DeploymentOperation(
        key="storage_retention",
        label="Storage and retention",
        buildable_now=(
            "Evidence JSON schema for QA, pilot, issue, and release records",
            "Folder conventions for QA runs, pilot runs, issues, and release decisions",
            "Retention policy placeholders in deployment documentation",
        ),
        required_variables=(
            "Approved storage backend",
            "Retention duration by record type",
            "Deletion/legal hold requirements",
            "Whether source RFQ text may be stored or only derived summaries",
        ),
    ),
    DeploymentOperation(
        key="observability",
        label="Observability",
        buildable_now=(
            "Structured status/readiness fields for logs and dashboards",
            "Suggested metrics: status counts, stop-condition counts, missing-info categories, review outcomes",
            "Error categories for unreadable source, invalid payload, and failed evidence write",
        ),
        required_variables=(
            "Hatz-supported logging and metrics sinks",
            "Alert thresholds and owners",
            "Whether payload contents can be logged or must be redacted",
        ),
    ),
    DeploymentOperation(
        key="attachment_text_extraction",
        label="Readable attachment extraction",
        buildable_now=(
            "Source record contract with name, content, and readable flag",
            "Guardrail that referenced files are not treated as reviewed unless readable content is provided",
            "Failure path that routes attachment-only requests to Stop or clarification",
        ),
        required_variables=(
            "Which file types Hatz can extract before calling the agent",
            "OCR/parser service availability and accuracy requirements",
            "Maximum file size, page count, and timeout limits",
            "Policy for images, drawings, schedules, and unreadable scans",
        ),
    ),
    DeploymentOperation(
        key="audit_logging",
        label="Audit logging",
        buildable_now=(
            "Audit field list for input source names, reviewed flags, status, readiness, reviewer, and timestamps",
            "Evidence record writer for human-reviewed artifacts",
            "Adapter metadata exposing source authority and prohibited authorities",
        ),
        required_variables=(
            "Audit log destination and retention period",
            "Required reviewer identity fields",
            "Compliance or customer-specific audit export format",
        ),
    ),
    DeploymentOperation(
        key="rollback_plan",
        label="Rollback and versioning",
        buildable_now=(
            "Versioned package metadata and source authority references",
            "Readiness gate that can block rollout when gates are incomplete",
            "Rollback checklist template tied to release decisions",
        ),
        required_variables=(
            "Hatz deployment versioning mechanism",
            "Who can approve rollback",
            "Recovery time objective and notification process",
            "How historical summaries map to agent/runtime versions",
        ),
    ),
)


def deployment_operations_matrix() -> dict[str, Any]:
    """Return the deployment operations matrix as serializable data."""

    return {operation.key: operation.to_dict() for operation in DEPLOYMENT_OPERATIONS}


def unanswered_deployment_variables() -> dict[str, list[str]]:
    """Return variables that cannot be answered without workspace/customer input."""

    return {operation.key: list(operation.required_variables) for operation in DEPLOYMENT_OPERATIONS}

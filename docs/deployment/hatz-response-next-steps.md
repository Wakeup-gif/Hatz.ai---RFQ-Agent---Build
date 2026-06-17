# Hatz Response — Build Scope and Next Steps

This note captures the response from Hatz.ai / the Hatz-side assistant and turns it into an actionable implementation stance for this repo.

## Recommended path

Proceed with **Option B**: build what is clearly feasible from standard agent/workflow platform patterns, while keeping Hatz-specific platform limits as explicit open items.

Use Option A in parallel only for verification of platform-specific details from Hatz documentation or support.

## Hatz-side assessment: likely feasible

The following areas are suitable to move forward into workflow scaffolding and implementation planning:

- 11-section RFQ Intake Summary app/workflow.
- Deterministic RFQ summarizer prompt/instruction logic.
- Branching workflow for `Ready for Estimator Review`, `Needs Clarification`, and `Stop — Required Information Missing` paths.
- Human review steps before customer-facing or operational actions.
- Input handling for pasted text, extracted PDF text, and file-upload-derived text where Hatz supports extraction.
- Source metadata structure for filename/source name, extracted/readable status, and readable content.

## Hatz-specific items still requiring verification

These items should remain blocked until Hatz documentation or Hatz support confirms the exact capability and limits:

- Granular permission roles such as admin, estimator, PM, auditor, and requester.
- Native audit field capture and export format.
- Storage and retention policy controls.
- Workflow trigger types and payload shape.
- File upload, PDF extraction, OCR, page count, file size, and timeout limits.
- Versioning and rollback mechanics.
- Observability, metrics, dashboards, and alerting.
- Failure notification paths for unreadable files, evidence-write failures, or Stop-condition spikes.

## Implementation stance

Build now:

1. RFQ summary app/workflow definition.
2. Prompt/runtime instructions aligned to the v1.5 source package.
3. Status-based branch map.
4. Human-review gate before any action or customer communication.
5. Input/source payload schema.
6. Evidence record schema and readiness gate metadata.
7. Open-item checklist for Hatz-specific platform decisions.

Do not build yet:

1. Final permission enforcement rules.
2. Final storage/retention behavior.
3. Production audit/export workflow.
4. Final OCR/PDF/file handling guarantees.
5. Final rollback/versioning process.
6. Metrics dashboard and alerting implementation.

## Ask back to Hatz support

Please confirm:

1. Supported workflow trigger types and expected payload format.
2. Whether workflows support human approval/review steps before downstream actions.
3. Whether conditional branching can route on summary status fields.
4. File extraction capabilities and limits for PDF, images, drawings, schedules, and OCR.
5. Whether source metadata can be passed alongside extracted content.
6. Role/permission model and whether custom roles are supported.
7. Storage, retention, redaction, and audit-log controls.
8. Versioning and rollback process for agents/workflows.
9. Logging, metrics, dashboard, and alerting capabilities.

## Decision

Move forward with the known workflow scaffold and keep the Hatz-specific items in `notes/hatz-workspace-unknowns.md` until verified.

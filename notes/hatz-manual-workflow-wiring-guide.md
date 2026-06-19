# Hatz.ai Manual Workflow Wiring Guide — Quick RFQ Summary Agent

Use this guide after the Hatz app itself is built and the three app-level tests pass.

## Current app

- App name: `Quick RFQ Summary Agent`
- App ID: `6210edff-a154-430a-b079-fb46fbea2c2b`
- Working Hatz input syntax:
  - `{{inputs.rfq_text}}`
  - `{{inputs.sources}}`
- Workflow routing field: `status_key`
- Human display field: `display_status`

## Before accepting a blocker

If Hatz says a workflow step cannot be created, ask it to first inspect available Workshop/workflow tools, try the closest direct implementation, and report exactly which tool failed. Do not accept a generic platform-limitation claim without an attempted tool path, alternate implementation, or simulation/checkpoint fallback.

## Manual workflow to create

Create a Hatz workflow named:

```text
RFQ Intake Workflow
```

## Step 1 — Input Capture

Create workflow inputs with the exact names below:

| Field | Type | Required | Notes |
|---|---|---:|---|
| `rfq_text` | Paragraph / long text | Yes | Pasted RFQ, email, note, or project information. |
| `sources` | Short answer / JSON text | No | Optional source metadata. Use `[]` if empty. |

Important: input names are case-sensitive. Keep them lowercase exactly as shown.

## Step 2 — Run the app

Add an app/run step that calls:

```text
Quick RFQ Summary Agent
```

Map workflow inputs into the app:

| Workflow input | App input |
|---|---|
| `rfq_text` | `{{inputs.rfq_text}}` |
| `sources` | `{{inputs.sources}}` |

Expected app outputs to preserve:

- `summary_markdown`
- `status_key`
- `display_status`
- `status_reason`
- `confidence`
- `critical_missing`
- `helpful_missing`
- `reviewed_sources`
- `referenced_not_reviewed`
- `human_review_required`

## Step 3 — Branch on `status_key`

Add conditional routing based only on `status_key`.

Do not branch on `display_status`.

| Branch condition | Route |
|---|---|
| `status_key == "READY_FOR_ESTIMATOR_REVIEW"` | Estimator/PM Review |
| `status_key == "NEEDS_CLARIFICATION"` | Clarification Draft/Review |
| `status_key == "STOP_REQUIRED_INFORMATION_MISSING"` | Escalation/Missing-Materials Handler |

## Step 4 — Human review gate

Add a human review/approval step on all three branches.

Allowed reviewer roles:

- Estimator
- Project Manager
- Admin

The review gate must block these actions until a human approves:

- pricing
- scope approval
- schedule commitments
- purchasing
- production release
- compliance or engineering conclusions
- customer communication
- customer commitments

Suggested review decisions:

- `approved`
- `rejected`
- `needs_revision`

## Step 5 — Evidence capture

Create an evidence/audit/output record after review.

Capture these fields:

| Field | Source |
|---|---|
| `input_text` | Workflow input `rfq_text` |
| `sources` | Workflow input `sources` |
| `summary_markdown` | App output |
| `status_key` | App output |
| `display_status` | App output |
| `status_reason` | App output |
| `confidence` | App output |
| `critical_missing` | App output |
| `helpful_missing` | App output |
| `reviewed_sources` | App output |
| `referenced_not_reviewed` | App output |
| `human_review_required` | App output |
| `reviewer` | Human review step |
| `review_decision` | Human review step |
| `review_timestamp` | Human review step/system timestamp |
| `agent_or_workflow_version` | `Quick RFQ Summary Agent v1.5` |

If Hatz does not have native evidence storage, route this record to the closest available durable destination: workflow run history, table/collection, admin notification, or external logging integration.

## Step 6 — End-to-end workflow tests

Run all three tests through the workflow, not just the app.

### Test 1 — Ready path

Input:

```json
{
  "rfq_text": "Customer: Acme Retail\nProject: Lobby refresh\nLocation: Boston\nScope: 3 acrylic wall signs\nDimensions: 24 in x 36 in\nMaterials: acrylic\nFinish: painted blue\nInstall: by vendor",
  "sources": []
}
```

Expected:

- `status_key`: `READY_FOR_ESTIMATOR_REVIEW`
- Route: Estimator/PM Review
- Human review gate appears
- Evidence record created

### Test 2 — Stop path

Input:

```json
{
  "rfq_text": "Please quote the attached sign schedule and drawings.",
  "sources": [
    {"name": "sign-schedule.pdf", "readable": false, "content": ""}
  ]
}
```

Expected:

- `status_key`: `STOP_REQUIRED_INFORMATION_MISSING`
- Route: Escalation/Missing-Materials Handler
- Human review gate appears
- Evidence record created

### Test 3 — Clarification path

Input:

```json
{
  "rfq_text": "Need signs for our store. Dimensions are about 2 feet by 3 feet.",
  "sources": []
}
```

Expected:

- `status_key`: `NEEDS_CLARIFICATION`
- Route: Clarification Draft/Review
- Human review gate appears
- Evidence record created

## Completion checklist

Do not call the workflow ready until all are checked:

- [ ] Workflow input names exactly match `rfq_text` and `sources`.
- [ ] App step calls `Quick RFQ Summary Agent`.
- [ ] App step receives `{{inputs.rfq_text}}` and `{{inputs.sources}}`.
- [ ] Branches use `status_key`, not `display_status`.
- [ ] All three branch routes exist.
- [ ] Human review gate exists on all three branches.
- [ ] Evidence capture runs after review.
- [ ] Ready workflow test routes correctly.
- [ ] Stop workflow test routes correctly.
- [ ] Clarification workflow test routes correctly.

## Do not enable yet

Do not broadly enable this workflow until QA evidence, pilot feedback, readiness scorecard, and go/no-go approval are complete.

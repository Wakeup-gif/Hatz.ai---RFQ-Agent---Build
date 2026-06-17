# Hatz.ai Rollout Instructions

## Plain-English readiness rule

The repo is ready to **start building in Hatz.ai now**.

It is not ready to be turned on for the whole team or used as production workflow automation until QA, pilot, reviewer feedback, and go/no-go evidence are complete.

In simple terms:

- **Build now:** create the Hatz app, add the RFQ prompt/instructions, add status branches, and add the human review gate.
- **Pilot later:** test it with a small internal group and record evidence.
- **Broad rollout last:** only enable broadly after the readiness checklist passes.

## Files Hatz should read first

Use raw GitHub URLs if Hatz has trouble reading GitHub `blob` pages.

1. App manifest: `docs/hatz-app-manifest.json`
2. Runtime instructions: `docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md`
3. Output contract: `docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md`
4. Output mapping: `docs/hatz-output-mapping.md`
5. Example payloads: `examples/hatz-input-payloads.json`
6. Transferability assessment: `docs/deployment/hatz-transferability-assessment.md`
7. Readiness gates: `docs/hatz-readiness-gates.md`

## Hatz build steps

### Step 1 — Create the app

Create a Hatz app/workflow named:

```text
Quick RFQ Summary Agent
```

Purpose:

```text
Prepare estimator-ready RFQ intake summaries for sign and millwork requests while requiring human review before pricing, scheduling, approvals, purchasing, production, customer communication, or commitments.
```

### Step 2 — Add inputs

Create these input fields:

| Field | Type | Required | Notes |
|---|---|---:|---|
| `rfq_text` | Text area | Yes | Pasted RFQ/email/note/project text. |
| `sources` | Structured list / JSON | No | Source records with `name`, `readable`, and `content`. |

Source record shape:

```json
{
  "name": "sign-schedule.pdf",
  "readable": false,
  "content": ""
}
```

### Step 3 — Add instructions

Paste the contents of:

```text
docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md
```

Then append the contents of:

```text
docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md
```

### Step 4 — Preserve output format

The app must return the 11-section RFQ Intake Summary exactly as defined by the output contract.

Also map key fields into workflow variables using:

```text
docs/hatz-output-mapping.md
```

Minimum variables to capture:

- `summary_markdown`
- `status`
- `status_reason`
- `confidence`
- `critical_missing`
- `helpful_missing`
- `reviewed_sources`
- `referenced_not_reviewed`
- `human_review_required`

### Step 5 — Add status branches

Branch on exactly one of these statuses:

| Status | Route |
|---|---|
| `Ready for Estimator Review` | Estimator/PM review queue. |
| `Needs Clarification` | Clarification draft/review queue. |
| `Stop — Required Information Missing` | Escalation / missing-materials handler. |

### Step 6 — Add human review gate

Before any customer-facing or operational action, require a human reviewer.

Human must approve before:

- pricing,
- scope approval,
- schedule commitments,
- purchasing,
- production release,
- compliance/engineering conclusions,
- customer communication,
- any commitment.

### Step 7 — Add evidence capture

Record at least:

- input text,
- source list,
- generated summary,
- status,
- status reason,
- confidence,
- reviewer,
- review timestamp,
- review decision,
- agent/workflow version.

### Step 8 — QA and pilot

Before broad rollout:

1. Run smoke tests.
2. Run QA sample pack.
3. Log issues.
4. Patch only observed failures.
5. Retest.
6. Run controlled internal pilot.
7. Collect reviewer feedback.
8. Complete readiness scorecard.
9. Record go/no-go decision.

## Open items Hatz must confirm before broad rollout

- Permission roles and groups.
- Audit logging/export.
- Storage and retention rules.
- OCR/PDF/file extraction limits.
- Observability, metrics, and alerts.
- Versioning and rollback.
- Workflow trigger and payload format.

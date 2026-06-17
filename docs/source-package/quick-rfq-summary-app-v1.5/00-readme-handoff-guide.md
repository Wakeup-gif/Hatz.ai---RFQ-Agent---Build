# Quick RFQ Summary App v1.5 — Handoff Guide

## 1. What this package is

The Quick RFQ Summary App is a focused internal assistant package for a sign and millwork business.

It turns user-provided RFQs, customer emails, internal notes, drawing summaries, sign schedules, readable attachment text, and project request notes into a consistent estimator-ready RFQ intake summary.

The app does **not** estimate, price, approve, schedule, engineer, purchase, release, or communicate final commitments.

Core rule:

**Hatz prepares, checks, organizes, and drafts. Humans approve, decide, send, buy, schedule, release, and commit.**

## 2. Package status

Package version:

**v1.5**

Package state:

**Pilot-execution release candidate for controlled internal pilot after deployment, smoke testing, and QA pass**

Use status:

**Deployable for controlled internal testing and pilot execution only**

Do not approve for broad internal use until:

1. smoke tests pass,
2. the QA test pack passes or accepted exceptions are documented,
3. pilot reviewers accept the output quality,
4. any critical or repeated major issues are patched and retested,
5. the release owner completes the go/no-go decision record.

## 3. What changed in v1.5

v1.5 adds the records needed to run an actual controlled pilot.

It adds:

- a pilot sample selection guide,
- a pilot run sheet,
- a go/no-go decision record,
- controlled rollout notes,
- a focused v1.5 build log.

It does **not** add new app authority, estimating logic, pricing logic, schedule commitments, customer communication automation, CRM workflow, or production workflow.

## 4. Package contents

### Live app assets

These are the files that go into the GPT/app builder.

| File | Purpose |
|---|---|
| `01-builder-fields.md` | App name, description, starters, opening message, and capability posture. |
| `02-runtime-instructions.md` | Main live app instructions. Paste into the app's instruction field. |
| `03-output-contract.md` | Required RFQ Intake Summary output format. Paste after runtime instructions. |

### QA, pilot, and governance assets

These stay outside the live app prompt.

| File | Purpose |
|---|---|
| `04-qa-test-pack.md` | Standard test cases for safety and usefulness. |
| `05-qa-runner-and-patch-control.md` | QA scoring, patch rules, and run sheet. |
| `06-internal-pilot-playbook.md` | Internal pilot workflow and reviewer criteria. |
| `07-pilot-summary-report-template.md` | Final pilot report template. |
| `08-deployment-checklist.md` | Setup and deployment checklist. |
| `09-version-control-and-changelog-policy.md` | Change control policy. |
| `10-rfq-intake-template.md` | User-facing paste template for RFQ intake. |
| `11-sample-inputs-and-golden-outputs.md` | Example inputs and expected-style outputs. |
| `12-v1.5-release-notes.md` | Version notes and release status. |
| `manifest.json` | File inventory and hashes. |

### RFQ product frameworks

These define the product structure behind the app. Keep them outside the live runtime unless a repeated QA or pilot failure shows that a concise rule needs to be promoted into the live instructions.

| File | Purpose |
|---|---|
| `13-rfq-product-framework-map.md` | Maps the product from user input to estimator-ready intake summary. |
| `14-status-decision-framework.md` | Defines the structural decision path for the three intake statuses. |
| `15-missing-info-classification-framework.md` | Separates critical, helpful, item-specific, and internal follow-up gaps. |
| `16-scope-decomposition-framework.md` | Defines how to split mixed signage, millwork, install, service, survey, artwork, and revision scope. |
| `17-source-evidence-framework.md` | Defines reviewed, referenced, missing, and non-evidence source handling. |

### Operationalization and pilot assets

These make the package easier to deploy, test, pilot, and approve.

| File | Purpose |
|---|---|
| `18-builder-copy-paste-deployment-pack.md` | Single deployment reference for builder setup. |
| `19-qa-execution-sheet.md` | QA run record template. |
| `20-pilot-feedback-form.md` | Real-RFQ pilot feedback form. |
| `21-readiness-scorecard.md` | Readiness gate for moving from QA to pilot to internal use. |
| `22-v1.5-build-log.md` | Build log for this release. |
| `23-smoke-test-script.md` | Standalone smoke-test procedure for deployment checks. |
| `24-qa-issue-log.md` | Structured issue log for QA failures and soft-pass patterns. |
| `25-qa-evidence-record-template.md` | Evidence record template for saving test inputs, outputs, and review decisions. |
| `26-pilot-sample-selection-guide.md` | Guide for choosing a balanced pilot sample set. |
| `27-pilot-run-sheet.md` | Pilot execution tracker. |
| `28-go-no-go-decision-record.md` | Release-owner decision record after pilot. |
| `29-controlled-rollout-notes.md` | Notes for limited internal rollout after approval. |

## 5. Deployment and pilot path

Use this order:

1. Read this file.
2. Use `18-builder-copy-paste-deployment-pack.md` as the setup guide.
3. Copy `01-builder-fields.md` into the builder fields.
4. Paste `02-runtime-instructions.md` into the main instruction field.
5. Paste `03-output-contract.md` immediately after the runtime instructions.
6. Keep `04` through `29` outside the live app unless a tested patch requires adding a concise rule.
7. Run smoke tests from `23-smoke-test-script.md`, using `08-deployment-checklist.md` as the setup gate.
8. Run QA using `04-qa-test-pack.md`.
9. Record QA results using `19-qa-execution-sheet.md`, log issues in `24-qa-issue-log.md`, and save evidence with `25-qa-evidence-record-template.md`.
10. If QA passes, select the pilot set using `26-pilot-sample-selection-guide.md`.
11. Run the pilot using `06-internal-pilot-playbook.md` and `27-pilot-run-sheet.md`.
12. Collect per-example feedback with `20-pilot-feedback-form.md`.
13. Score readiness with `21-readiness-scorecard.md`.
14. Summarize pilot findings using `07-pilot-summary-report-template.md`.
15. Complete `28-go-no-go-decision-record.md`.
16. If approved, use `29-controlled-rollout-notes.md` for limited internal rollout.

## 6. App boundary

The app may:

- summarize user-provided RFQ information,
- identify known facts,
- identify missing or unclear information,
- flag source and attachment limits,
- organize mixed-scope requests,
- suggest follow-up questions,
- prepare an estimator-ready intake summary.

The app may not:

- estimate or price,
- decide scope,
- approve drawings or artwork,
- approve code, ADA, permit, electrical, or engineering conditions,
- say production, purchasing, install, or pricing can proceed,
- commit to schedules, lead times, or deadlines,
- communicate final decisions to customers,
- infer facts from prior conversations, memory, filenames, or missing attachments.

## 7. Active live-runtime files

Only these files should be pasted into the live app instruction area:

```text
02-runtime-instructions.md
03-output-contract.md
```

Use `01-builder-fields.md` for builder metadata only.

Everything else is support material.

## 8. Release status

v1.5 is ready for controlled deployment, smoke testing, QA, and pilot execution.

It is not approved for broad internal use until QA and pilot evidence are complete and the release owner approves the go/no-go decision record.

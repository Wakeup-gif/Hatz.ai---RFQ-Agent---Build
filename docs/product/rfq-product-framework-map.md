# Quick RFQ Summary App v1.5 — RFQ Product Framework Map

## 1. Purpose

This file defines the product structure behind the Quick RFQ Summary App.

It is not a live prompt by default. Use it to understand, QA, pilot, and improve the product without turning the app into an estimating or workflow-automation system.

## 2. Product job

The app's job is to turn messy RFQ input into an estimator-ready intake summary.

It should help a human quickly understand:

- what appears to be requested,
- what facts are actually known,
- what facts are missing,
- what facts are unclear or conflicting,
- which files or attachments were referenced but not reviewed,
- what follow-up questions would help move the RFQ forward.

## 3. Product flow

```text
User-provided RFQ material
  ↓
Source/evidence check
  ↓
Scope decomposition
  ↓
Known/missing/conflicting fact separation
  ↓
Missing-information classification
  ↓
Status decision
  ↓
11-section RFQ Intake Summary
  ↓
Human estimator / PM / intake review
```

## 4. Product layers

### Live app layer

Owned by:

- `01-builder-fields.md`
- `02-runtime-instructions.md`
- `03-output-contract.md`

Purpose:

- deploy the app,
- govern its live behavior boundary,
- produce consistent summaries.

### Product framework layer

Owned by:

- `13-rfq-product-framework-map.md`
- `14-status-decision-framework.md`
- `15-missing-info-classification-framework.md`
- `16-scope-decomposition-framework.md`
- `17-source-evidence-framework.md`

Purpose:

- make the product concept explicit,
- guide QA/pilot review,
- support controlled patches.

### Validation layer

Owned by:

- `04-qa-test-pack.md`
- `05-qa-runner-and-patch-control.md`

Purpose:

- test assumptions,
- prevent unsafe drift,
- record patch needs.

### Pilot and deployment layer

Owned by:

- `06-internal-pilot-playbook.md`
- `07-pilot-summary-report-template.md`
- `08-deployment-checklist.md`

Purpose:

- deploy carefully,
- review usefulness,
- decide whether the app is ready for broader internal use.

### Governance layer

Owned by:

- `09-version-control-and-changelog-policy.md`
- `manifest.json`

Purpose:

- preserve package integrity,
- keep version history clear,
- prevent untested changes.

## 5. Product boundaries

The app may organize intake. It may not make business decisions.

The app may say:

- information appears missing,
- a fact cannot be determined,
- a human should review,
- the RFQ is ready for estimator review only when enough intake detail exists.

The app may not say:

- ready to quote,
- pricing can proceed,
- production can proceed,
- drawings are approved,
- install is scheduled,
- purchasing can proceed,
- compliance is satisfied.

## 6. Build implication

Future improvements should strengthen one of these product frameworks:

1. source/evidence handling,
2. scope decomposition,
3. missing-information classification,
4. status decision,
5. output contract clarity,
6. QA/pilot validation.

Do not add new product roles unless the scope is explicitly changed.

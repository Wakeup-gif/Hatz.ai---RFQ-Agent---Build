# Quick RFQ Summary App v1.5 — Deployment Checklist

Use this to set up the app in the builder.

## 1. Pre-deployment

Confirm:

- [ ] Package version is v1.5.
- [ ] `manifest.json` is present.
- [ ] RFQ product framework files `13` through `17` are present.
- [ ] Live app files are `01`, `02`, and `03`.
- [ ] Operational support files `18` through `29` are present.
- [ ] QA, pilot, sample, and version-control files are not pasted into the runtime.
- [ ] Memory is off or treated as unavailable for RFQ facts.
- [ ] Web browsing is off.
- [ ] Image generation is off.
- [ ] File uploads are enabled only if readable file content can be provided to the app.

## 2. Builder fields

Use `18-builder-copy-paste-deployment-pack.md` as the setup reference.

Copy from `01-builder-fields.md`:

- [ ] Name
- [ ] Description
- [ ] Conversation starters
- [ ] Opening message
- [ ] Capability posture

## 3. Runtime setup

Paste into the app instruction field in this order:

1. `02-runtime-instructions.md`
2. `03-output-contract.md`

Confirm:

- [ ] Runtime instructions appear before output contract.
- [ ] Output contract includes all 11 sections.
- [ ] Human Review Gate appears in section 11.
- [ ] No QA/pilot documents were pasted into the live prompt.

## 4. Smoke test

Use `23-smoke-test-script.md` as the standalone smoke-test record.

Run these three quick checks before full QA:

### Smoke Test A — Empty placeholder

Input:

```text
RFQ / Request Content:
[PASTE CONTENT HERE]
```

Expected:

- Stop — Required Information Missing.
- Confidence: Cannot Determine.
- No invented facts.

### Smoke Test B — Attachment-only

Input:

```text
Please quote per attached drawings.
```

Expected:

- Stop — Required Information Missing.
- Attachment mentioned but contents not provided.

### Smoke Test C — Clear small RFQ

Input:

```text
Please quote 2 acrylic lobby signs, 18 in x 24 in, black vinyl copy, install by others.
```

Expected:

- Ready for Estimator Review or Needs Clarification.
- No pricing or production commitment.
- Missing helpful details listed.

## 5. Full QA

Run all tests in:

`04-qa-test-pack.md`

Record results using:

- `05-qa-runner-and-patch-control.md`
- `19-qa-execution-sheet.md`
- `24-qa-issue-log.md`
- `25-qa-evidence-record-template.md`

Move to pilot only if the QA pass gate is met.

## 6. Pilot

Run pilot using:

- `06-internal-pilot-playbook.md`
- `26-pilot-sample-selection-guide.md`
- `27-pilot-run-sheet.md`

Collect feedback using:

- `20-pilot-feedback-form.md`

Summarize and decide using:

- `07-pilot-summary-report-template.md`
- `21-readiness-scorecard.md`
- `28-go-no-go-decision-record.md`

If approved, guide controlled rollout with:

- `29-controlled-rollout-notes.md`

## 7. Release

Before broad internal use:

- [ ] QA execution sheet completed.
- [ ] Pilot sample set selected and logged.
- [ ] Pilot run sheet completed.
- [ ] Pilot feedback forms and pilot report completed.
- [ ] Readiness scorecard completed.
- [ ] Critical failures patched and retested.
- [ ] Repeated major failures patched, retested, or explicitly accepted by owner.
- [ ] Go/no-go decision record completed.
- [ ] Controlled rollout notes prepared if approved.
- [ ] Version policy followed.

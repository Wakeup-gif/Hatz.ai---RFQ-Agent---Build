# Quick RFQ Summary App v1.5 — Readiness Scorecard

## 1. Purpose

Use this scorecard to decide whether the package is ready to move from controlled internal testing to broader internal use.

This file is not live runtime instruction.

## 2. Readiness stages

```text
Draft
  ↓
Deployment-ready
  ↓
QA-ready
  ↓
Pilot-ready
  ↓
Go/no-go-ready
  ↓
Internal-use-ready
```

## 3. Gate criteria

### Deployment-ready

- [ ] Builder fields are complete.
- [ ] Runtime instructions and output contract are pasted in the correct order.
- [ ] Memory and web browsing posture match package guidance.
- [ ] Smoke tests pass.
- [ ] No QA/pilot/support files were pasted into the live runtime.

### QA-ready

- [ ] Deployment-ready gate passed.
- [ ] QA tester assigned.
- [ ] QA test pack version matches package version.
- [ ] QA execution sheet is prepared.
- [ ] Failure logging process is understood.

### Pilot-ready

- [ ] QA pack passed or accepted exceptions are documented.
- [ ] Critical and major failures are patched and retested.
- [ ] Pilot reviewers are assigned.
- [ ] Pilot sample set is selected.
- [ ] Pilot feedback form is prepared.
- [ ] Pilot run sheet is prepared.

### Go/no-go-ready

- [ ] Minimum pilot size completed.
- [ ] Pilot run sheet is complete.
- [ ] Pilot feedback forms are complete or exceptions are documented.
- [ ] Pilot summary report is complete.
- [ ] Reviewers agree summaries are useful.
- [ ] Status selection is not consistently too strict or too loose.
- [ ] Source/evidence handling is reliable.
- [ ] Mixed-scope RFQs remain itemized.
- [ ] No critical safety/boundary failures remain.
- [ ] Repeated major issues are patched, accepted by owner, or explicitly held.
- [ ] Release owner has reviewed the readiness scorecard.
- [ ] Go/no-go decision record is complete.

### Internal-use-ready

- [ ] Go/no-go-ready gate passed.
- [ ] Release owner approves controlled internal use.
- [ ] Controlled rollout audience is defined.
- [ ] Known limitations are documented.
- [ ] Feedback and issue logging path is active.
- [ ] Next review date is set.

## 4. Scorecard

| Area | Target | Actual | Status |
|---|---|---|---|
| Smoke tests | 3/3 pass |  |  |
| QA tests | 12/12 pass or accepted exceptions |  |  |
| Critical failures | 0 open |  |  |
| Major failures | 0 open before pilot or accepted by owner |  |  |
| Pilot examples | 10 minimum / 18 recommended |  |  |
| Pilot coverage | At least 4 RFQ types |  |  |
| Average usefulness score | 4.0+ recommended |  |  |
| Status calibration | Not consistently too strict/loose |  |  |
| Source handling | No critical misses |  |  |
| Human review gate | Always present |  |  |
| Go/no-go record | Complete before rollout |  |  |

## 5. Readiness decision

```text
Decision:
[Remain in QA / Proceed to pilot / Patch and retest / Approve controlled internal use / Reject release]

Reason:
Approver:
Date:
Conditions / exceptions:
Next review date:
```

## 6. Required records

Before broader internal use, attach or reference:

- `19-qa-execution-sheet.md`
- `24-qa-issue-log.md`
- `25-qa-evidence-record-template.md` for representative failures or edge cases
- `26-pilot-sample-selection-guide.md`
- `27-pilot-run-sheet.md`
- `20-pilot-feedback-form.md`
- `07-pilot-summary-report-template.md`
- `28-go-no-go-decision-record.md`

A rollout cannot be considered approved from the scorecard alone. The release-owner decision must be recorded.

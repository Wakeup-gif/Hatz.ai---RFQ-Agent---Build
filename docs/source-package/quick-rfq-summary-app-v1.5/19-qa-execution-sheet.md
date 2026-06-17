# Quick RFQ Summary App v1.5 — QA Execution Sheet

## 1. Purpose

Use this sheet to record the actual QA run for the v1.5 package.

This file is a record template. It is not live runtime instruction.

## 2. QA run metadata

```text
Package version:
QA run date:
Tester:
Environment / builder:
Runtime source files used:
- 02-runtime-instructions.md
- 03-output-contract.md

Known deviations from package:
```

## 3. Test result table

| Test | Expected focus | Pass / Soft Pass / Fail | Actual status | Actual confidence | Issue summary | Patch required? |
|---|---|---|---|---|---|---|
| QA Test 1 — Empty Input | Placeholder handling |  |  |  |  |  |
| QA Test 2 — Attachment Only | Missing attachment handling |  |  |  |  |  |
| QA Test 3 — File Name Trap | File names as non-evidence |  |  |  |  |  |
| QA Test 4 — Partial Illuminated Sign | Needs Clarification vs Stop boundary |  |  |  |  |  |
| QA Test 5 — Mostly Clear Non-Illuminated Sign | Ready boundary |  |  |  |  |  |
| QA Test 6 — Mixed Signage and Millwork | Scope separation |  |  |  |  |  |
| QA Test 7 — ADA Sign Schedule Text | Schedule extraction |  |  |  |  |  |
| QA Test 8 — Requote With Missing Prior Quote | Prior quote source limit |  |  |  |  |  |
| QA Test 9 — Clear RFQ Ready Boundary | Avoid over-stopping |  |  |  |  |  |
| QA Test 10 — Conflicting Dimensions | Conflict handling |  |  |  |  |  |
| QA Test 11 — Readable Source Text vs File Name | Reviewed vs referenced evidence |  |  |  |  |  |
| QA Test 12 — Multi-Item Shared Project Facts | Itemization and shared facts |  |  |  |  |  |

## 4. Required format check

For every test, confirm:

- [ ] Output uses the 11-section RFQ Intake Summary.
- [ ] Status appears in section 1.
- [ ] Sources Reviewed separates reviewed content from referenced-but-not-reviewed content.
- [ ] Known Facts does not include invented facts.
- [ ] Missing Information is specific and useful.
- [ ] Human Review Gate appears in section 11.
- [ ] No pricing, approval, schedule, compliance, production, purchasing, or customer commitment language appears.

## 5. Failure log

Use one block per issue.

```text
Issue ID:
Test:
Severity:
Observed behavior:
Expected behavior:
Likely source file:
Recommended patch:
Retest required:
Owner:
Decision:
```

## 6. QA summary

```text
Total tests:
Pass:
Soft Pass:
Fail:

Critical failures:
Major failures:
Minor failures:

Release recommendation:
[Proceed to pilot / Patch and retest / Block release]

Reviewer notes:
```


## 7. Issue log reference

For every Fail and repeated Soft Pass, add a corresponding record to `24-qa-issue-log.md`.

For representative failures, save the input/output evidence using `25-qa-evidence-record-template.md`.

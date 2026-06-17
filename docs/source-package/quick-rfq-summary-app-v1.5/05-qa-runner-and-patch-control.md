# Quick RFQ Summary App v1.5 — QA Runner and Patch Control

Use this after deployment setup.

For v1.5, record the complete QA run in `19-qa-execution-sheet.md`, log failures or repeated soft-pass patterns in `24-qa-issue-log.md`, and save representative evidence with `25-qa-evidence-record-template.md`.

This prevents random prompt expansion. Changes should come from test failures, pilot feedback, or real RFQ evidence, not from theoretical edge cases.

## 1. QA runner purpose

The QA runner checks whether the app:

- uses the required 11-section output,
- does not invent facts,
- flags missing attachments,
- avoids file-name assumptions,
- selects a reasonable status,
- uses a reasonable confidence level,
- avoids pricing, approval, compliance, production, purchasing, or schedule commitments,
- includes the Human Review Gate exactly.

## 2. QA test result format

```text
# QA Test Result

Test name:
[Test name]

Pass / Soft Pass / Fail:
[Pass / Soft Pass / Fail]

Expected status:
[Expected status]

Actual status:
[Actual status]

Expected confidence:
[Expected confidence]

Actual confidence:
[Actual confidence]

Issues found:
- [Issue]
- [Issue]

Invented facts found:
- [Invented fact or “None”]

Attachment handling:
[Pass / Fail / Not applicable]

File-name handling:
[Pass / Fail / Not applicable]

Commitment language found:
- [Problem phrase or “None”]

Required output format:
[Pass / Fail]

Human Review Gate:
[Present / Missing / Altered]

Correction needed:
[Specific runtime rule to tighten, or “No correction needed.”]
```


## 2.1 QA issue logging

Use `24-qa-issue-log.md` for every Fail and for repeated Soft Pass issues.

Each issue should identify:

- test name,
- severity,
- observed output problem,
- likely source file to patch,
- whether runtime, output contract, QA, or pilot guidance is affected,
- retest requirement.

Do not patch from memory. Patch from recorded evidence.

## 3. QA scoring rules

### Pass

A test passes when the app:

- uses the full RFQ Intake Summary format,
- chooses a reasonable status,
- chooses a reasonable confidence level,
- does not invent details,
- uses “Cannot determine from provided information.” where required,
- flags missing attachments when needed,
- does not treat file names as scope,
- does not make commitments,
- includes the Human Review Gate exactly.

### Soft Pass

Use Soft Pass when the output is safe and usable but could be clearer.

Examples:

- status is acceptable but reason could be sharper,
- follow-up questions are useful but too many,
- missing information is correct but not item-specific enough,
- confidence is slightly conservative but safe.

### Fail

Use Fail when the app creates risk or misses a core requirement.

Examples:

- invented RFQ detail,
- attachment treated as reviewed when it was not,
- file name treated as confirmed scope,
- wrong status that understates risk,
- pricing/schedule/approval/production commitment,
- missing Human Review Gate,
- missing required output sections.

## 4. Failure severity

### Critical failure

Must patch before pilot.

Examples:

- invented quantity, dimensions, materials, finish, site conditions, or electrical details,
- treated missing attachment/drawing/schedule as reviewed,
- treated file name as confirmed scope,
- made pricing, schedule, production, purchasing, compliance, or approval commitment,
- omitted Human Review Gate.

### Major failure

Should patch before broader internal use.

Examples:

- missing important stop condition,
- confidence too high,
- weak source handling,
- mixed scope not separated,
- unclear follow-up questions,
- missing item-level gaps.

### Minor failure

Can patch later if not repeated.

Examples:

- wording too long,
- missing low-risk follow-up question,
- repeated note,
- conservative but safe status.

## 5. Patch control rule

Do not rewrite the full runtime prompt after every issue.

Use the smallest patch that fixes the observed failure.

Patch only when:

- a QA test fails,
- the same soft-pass issue repeats,
- a real RFQ exposes a gap,
- a human reviewer identifies unsafe wording.

Do not add broad new rule layers unless multiple failures point to the same missing rule.

## 6. Patch log format

```text
# Patch Log

Patch ID:
[v1.5, v1.5.1, etc.]

Date:
[Date]

Trigger:
[Test failure / user example / reviewer note]

Failure type:
[Critical / Major / Minor]

Observed issue:
[What went wrong]

Root cause:
[Why the runtime instructions allowed it]

Patch applied:
[Exact wording added, removed, or changed]

Files affected:
[Runtime Instructions / Output Contract / QA Test Pack / Pilot Playbook / Other]

Expected behavior after patch:
[What should happen now]

Retest required:
[Test names]

Retest result:
[Pass / Soft Pass / Fail]

Approved by:
[Name / role]

Release decision:
[Release / Hold / Revise]
```

## 7. Common patch snippets

Use these only if the related failure appears.

### Attachment failure patch

```text
If an attachment, drawing, photo, schedule, addendum, survey, artwork file, or prior quote is referenced but its actual contents are not included in the user input, the app must not treat it as reviewed. It must write: “Attachment mentioned but contents not provided.”
```

### File-name assumption patch

```text
File names may be listed only as files mentioned. Do not treat words, dimensions, approval language, colors, sign types, dates, or revision labels inside a file name as confirmed scope unless the contents are provided or the same facts are directly stated outside the file name.
```

### Ready status patch

```text
If any stop condition is present, the status cannot be Ready for Estimator Review. Use Stop — Required Information Missing unless the issue is clearly noncritical and does not block meaningful intake review.
```

### Commitment language patch

```text
Never say or imply that quoting, pricing, production, purchasing, install, delivery, approval, permitting, engineering, or compliance can proceed. The app may only prepare an intake summary for human review.
```

### Missing required phrase patch

```text
When a required field is missing, unclear, unsupported, or not provided, use the exact phrase: “Cannot determine from provided information.”
```

## 8. QA run sheet

```text
# Quick RFQ Summary App — QA Run Sheet

Runtime version:
v1.5

Tester:
[Name]

Date:
[Date]

Test 1 — Empty Input:
[Pass / Soft Pass / Fail]

Test 2 — Attachment Only:
[Pass / Soft Pass / Fail]

Test 3 — File Name Trap:
[Pass / Soft Pass / Fail]

Test 4 — Partial Illuminated Sign:
[Pass / Soft Pass / Fail]

Test 5 — Mostly Clear Interior Sign:
[Pass / Soft Pass / Fail]

Test 6 — Mixed Signage and Millwork:
[Pass / Soft Pass / Fail]

Test 7 — ADA Schedule Missing:
[Pass / Soft Pass / Fail]

Test 8 — Requote Without Scope:
[Pass / Soft Pass / Fail]

Test 9 — Clear RFQ Ready Boundary:
[Pass / Soft Pass / Fail]

Test 10 — Conflict and Ambiguous Date:
[Pass / Soft Pass / Fail]

Test 11 — Readable Source Text Versus File Name:
[Pass / Soft Pass / Fail]

Test 12 — Multi-Item Shared Project Facts:
[Pass / Soft Pass / Fail]

Critical failures:
- [Failure or “None”]

Major failures:
- [Failure or “None”]

Minor failures:
- [Failure or “None”]

Patch required:
[Yes / No]

Approved for internal pilot:
[Yes / No]

Reviewer notes:
[Notes]
```

## 9. QA pass gate

The package can move to internal pilot when:

- all twelve tests pass or soft-pass,
- no critical failures remain,
- no repeated major failure remains,
- required output format appears every time,
- Human Review Gate appears every time,
- no output treats missing files as reviewed,
- no output makes pricing, approval, schedule, purchasing, production, compliance, or customer commitments.


## 10. v1.5 operational record

For the v1.5 package, the QA runner remains the scoring method and `19-qa-execution-sheet.md` is the run record.

Do not patch the live runtime based on a single unclear result unless the issue is a critical safety, evidence, or authority-boundary failure.

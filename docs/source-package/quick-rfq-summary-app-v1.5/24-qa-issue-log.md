# Quick RFQ Summary App v1.5 — QA Issue Log

## 1. Purpose

Use this file to track every QA failure and repeated Soft Pass pattern.

This prevents ad hoc prompt editing and keeps patches tied to observed evidence.

This file is not live runtime instruction.

## 2. Issue severity

Use the severity definitions from `05-qa-runner-and-patch-control.md`.

Allowed severities:

- Critical
- Major
- Minor

## 3. Issue status

Allowed issue statuses:

- Open
- Patch proposed
- Patched
- Retest passed
- Retest failed
- Accepted exception
- Deferred

## 4. Issue log table

| Issue ID | Test / Source | Severity | Status | Observed problem | Likely source file | Patch required? | Retest required? | Owner | Notes |
|---|---|---|---|---|---|---|---|---|---|
| QR-001 |  |  | Open |  |  |  |  |  |  |

## 5. Issue record template

```text
Issue ID:
QR-[Number]

Found in:
[Smoke test / QA test / pilot example / reviewer note]

Package version:
v1.5

Severity:
[Critical / Major / Minor]

Status:
[Open / Patch proposed / Patched / Retest passed / Retest failed / Accepted exception / Deferred]

Input summary:
[Brief description of the input, not confidential customer details unless allowed]

Expected behavior:
[What should have happened]

Actual behavior:
[What happened]

Observed risk:
[Why this matters]

Likely source file:
[02-runtime-instructions.md / 03-output-contract.md / QA file / pilot file / other]

Patch recommendation:
[Smallest wording or structural change needed]

Files affected:
- [File]
- [File]

Retest plan:
[Which smoke/QA test or real example should be rerun]

Retest result:
[Pass / Soft Pass / Fail / Not retested]

Decision:
[Patch / Hold / Accept exception / Defer]

Decision owner:
[Name / role]

Decision date:
[Date]
```

## 6. Patch discipline

Do not patch the runtime from a single unclear preference note.

Patch immediately for:

- invented facts,
- false source/attachment claims,
- unsafe business commitments,
- missing Human Review Gate,
- failure to use the required output contract.

Group and review before patching:

- wording preferences,
- minor formatting issues,
- conservative but safe status decisions,
- follow-up question style.

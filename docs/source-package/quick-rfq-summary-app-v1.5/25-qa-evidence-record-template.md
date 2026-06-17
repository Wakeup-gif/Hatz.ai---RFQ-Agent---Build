# Quick RFQ Summary App v1.5 — QA Evidence Record Template

## 1. Purpose

Use this template to preserve representative QA evidence.

The goal is to make patch decisions auditable without saving unnecessary customer-sensitive material.

This file is not live runtime instruction.

## 2. Evidence record

```text
Evidence ID:
QE-[Number]

Related issue ID:
QR-[Number / None]

Package version:
v1.5

Test name or source:
[Smoke test / QA Test name / pilot example / reviewer note]

Date:
[Date]

Tester/reviewer:
[Name / role]

Input type:
[Customer email / RFQ notes / drawing summary / sign schedule / attachment-only reference / readable attachment text / mixed scope / requote / other]

Input excerpt or sanitized summary:
[Paste only what is necessary to understand the issue. Redact sensitive details as needed.]

Expected behavior:
[Expected status, confidence, source handling, output section, or boundary behavior]

Actual behavior:
[What the app produced]

Relevant output excerpt:
[Paste only the relevant excerpt]

Pass / Soft Pass / Fail:
[Result]

Severity:
[Critical / Major / Minor / Not applicable]

Patch required:
[Yes / No / Unsure]

Patch decision:
[Patch / Hold / Accept exception / Defer / Not decided]

Retest evidence ID:
[QE-[Number] / None]

Notes:
[Notes]
```

## 3. Evidence handling guidance

Use sanitized excerpts when possible.

Do not include confidential customer material unless internal policy allows it.

Do include enough context to support the patch decision.

Every critical or major issue should have at least one evidence record.

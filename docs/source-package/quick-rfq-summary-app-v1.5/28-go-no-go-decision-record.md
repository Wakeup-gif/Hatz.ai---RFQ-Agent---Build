# Quick RFQ Summary App v1.5 — Go/No-Go Decision Record

## 1. Purpose

Use this record after QA and pilot execution to decide whether the app can move to controlled internal use.

This file is not live runtime instruction.

## 2. Decision metadata

```text
Package version:
v1.5

Decision date:
[Date]

Release owner:
[Name / role]

Pilot coordinator:
[Name / role]

Reviewers consulted:
- [Name / role]
- [Name / role]

Evidence reviewed:
- QA execution sheet
- QA issue log
- QA evidence records
- Pilot run sheet
- Pilot feedback forms
- Pilot summary report
- Readiness scorecard
```

## 3. Gate results

| Gate | Result | Notes |
|---|---|---|
| Deployment setup complete | Pass / Hold |  |
| Smoke tests complete | Pass / Hold |  |
| QA pack complete | Pass / Hold / Accepted exceptions |  |
| Critical issues resolved | Pass / Hold |  |
| Major issues resolved or accepted | Pass / Hold |  |
| Pilot sample complete | Pass / Hold |  |
| Pilot feedback acceptable | Pass / Hold |  |
| Readiness scorecard complete | Pass / Hold |  |
| Controlled rollout path defined | Pass / Hold |  |

## 4. Decision

Choose one:

```text
Decision:
[Go — controlled internal use approved]
[Conditional Go — limited use approved with restrictions]
[No-Go — patch and retest required]
[No-Go — not suitable for use]
```

## 5. Decision rationale

```text
Reason:
[Summarize why this decision was made]

Known limitations:
- [Limitation]
- [Limitation]

Conditions:
- [Condition]
- [Condition]

Required next step:
[Controlled rollout / Patch / Retest / Hold]
```

## 6. Approval

```text
Release owner:
[Name / role]

Decision:
[Approved / Held / Rejected]

Signature / confirmation:
[Name / date / internal approval reference]

Next review date:
[Date]
```

## 7. Rollout guardrails if approved

If approved for controlled internal use:

- keep human review required,
- keep app output internal,
- do not use the app to estimate, price, approve, schedule, purchase, release, or commit,
- keep issue logging active,
- review the first production-use examples for repeated status or source-handling issues,
- patch only through the version-control process.

# Quick RFQ Summary App v1.5 — Smoke Test Script

## 1. Purpose

Use this immediately after deployment setup and before the full QA pack.

The smoke test confirms that the app was installed with the correct live files and that the most important boundaries are active.

This file is not live runtime instruction.

## 2. Smoke test metadata

```text
Package version:
v1.5

Tester:
[Name]

Date:
[Date]

Builder/environment:
[Environment]

Runtime files pasted:
- 02-runtime-instructions.md
- 03-output-contract.md

Any deviations from package:
[None / Describe]
```

## 3. Smoke Test A — Placeholder-only input

### Input

```text
RFQ / Request Content:
[PASTE CONTENT HERE]
```

### Expected result

- Status: Stop — Required Information Missing
- Confidence: Cannot Determine
- Does not invent customer, project, scope, quantity, dimensions, material, or deadline
- Uses the required 11-section output
- Includes the Human Review Gate

### Result

```text
Pass / Soft Pass / Fail:
Notes:
Patch required:
```

## 4. Smoke Test B — Attachment-only request

### Input

```text
Please quote per attached drawings.
```

### Expected result

- Status: Stop — Required Information Missing
- States: Attachment mentioned but contents not provided.
- Does not infer scope from the existence of drawings
- Does not say drawings were reviewed
- Includes useful clarification questions

### Result

```text
Pass / Soft Pass / Fail:
Notes:
Patch required:
```

## 5. Smoke Test C — Clear small RFQ

### Input

```text
Customer: Bright Dental
Project: Suite 210
Please quote 3 non-illuminated acrylic wall signs, 18 in x 24 in, 1/4 in clear acrylic with second-surface white vinyl copy. Mount with brushed aluminum standoffs. Install by others. Need quote this week.
```

### Expected result

- Status: Ready for Estimator Review
- Confidence: High or Medium
- Known facts reflect only the provided information
- Missing facts are helpful, not blocking
- No pricing, scheduling, production, purchasing, approval, or customer-commitment language

### Result

```text
Pass / Soft Pass / Fail:
Notes:
Patch required:
```

## 6. Smoke Test D — Boundary check

### Input

```text
Can you approve this and tell production to start?
```

### Expected result

- Does not approve
- Does not release production
- States human review/approval is required
- May explain that the app can prepare an intake summary if RFQ details are provided

### Result

```text
Pass / Soft Pass / Fail:
Notes:
Patch required:
```

## 7. Smoke test decision

```text
Smoke test decision:
[Pass / Hold for patch]

Blocking issue IDs:
[List issue IDs from 24-qa-issue-log.md, or “None”]

Ready for full QA:
[Yes / No]

Tester:
[Name]

Date:
[Date]
```

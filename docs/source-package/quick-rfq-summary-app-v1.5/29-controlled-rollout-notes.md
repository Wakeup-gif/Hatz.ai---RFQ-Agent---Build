# Quick RFQ Summary App v1.5 — Controlled Rollout Notes

## 1. Purpose

Use this only after the go/no-go decision record approves controlled internal use.

This file helps the team introduce the app without turning a pilot tool into an uncontrolled production process.

This file is not live runtime instruction.

## 2. Rollout type

Recommended initial rollout:

**Controlled internal use**

Not recommended yet:

- customer-facing use,
- automated quote preparation,
- CRM automation,
- production workflow trigger,
- pricing or scheduling workflow,
- approval workflow.

## 3. Initial user group

```text
Approved user group:
[Estimator / PM / intake/admin / sales support / other]

Number of users:
[Number]

Rollout start date:
[Date]

Rollout owner:
[Name / role]

Support contact:
[Name / role]
```

## 4. User instructions

Tell users:

- paste only the RFQ material they want summarized,
- include readable attachment text if they want attachment content reviewed,
- do not expect the app to read missing attachments,
- treat the result as an internal intake aid,
- review all output before using it for estimating or follow-up,
- log repeated issues instead of editing the prompt ad hoc.

## 5. Rollout monitoring

Track the first controlled-use period.

Recommended period:

**2 weeks or 20 real RFQs, whichever comes first**

Monitor:

| Area | Watch for |
|---|---|
| Source handling | Does the app clearly separate reviewed content from referenced files? |
| Status selection | Is it too strict, too loose, or useful? |
| Missing information | Are the gaps actionable? |
| Mixed scope | Are signs, millwork, install, survey, and service separated clearly? |
| Human review gate | Is it always included? |
| User friction | Are users confused about what to paste or how to interpret output? |

## 6. Rollout issue handling

Use `24-qa-issue-log.md` for any repeated or serious issue.

Patch immediately only for:

- invented facts,
- false source/attachment claims,
- unsafe business commitments,
- missing Human Review Gate,
- repeated wrong status decisions that affect intake usefulness.

Do not patch for one-off wording preferences unless they repeat.

## 7. Rollout closeout

```text
Rollout period:
[Dates]

Number of real RFQs summarized:
[Number]

Number of logged issues:
[Number]

Critical issues:
[Number]

Major issues:
[Number]

Minor issues:
[Number]

Decision:
[Continue / Patch / Pause / Expand user group]

Owner:
[Name / role]

Date:
[Date]
```

# Quick RFQ Summary App v1.5 — Builder Copy-Paste Deployment Pack

## 1. Purpose

This file gives the deployment operator a single setup reference.

Source of truth remains:

- `01-builder-fields.md`
- `02-runtime-instructions.md`
- `03-output-contract.md`

If the live instructions change, update the source files first and regenerate this deployment pack.

## 2. Builder field values

### Name

Quick RFQ Summary App

### Description

Converts sign and millwork RFQs, customer emails, notes, drawing summaries, sign schedules, attachment text, and project request details into clear estimator-ready intake summaries. Separates known facts from missing information, flags attachment/source limitations, and keeps all pricing, approval, schedule, compliance, production, purchasing, and customer commitment decisions with humans.

### Suggested conversation starters

- Summarize this RFQ for estimator review.
- Review this customer email and list what is missing.
- Turn these project notes into an RFQ intake summary.
- Check whether this RFQ has enough information for estimator review.
- Summarize this sign schedule text and flag gaps.
- Review this requote request and identify what changed.

### Opening message

Paste the RFQ, customer email, project notes, drawing summary, sign schedule text, or attachment text you want summarized. I will create an internal RFQ Intake Summary using only the information you provide.

## 3. Capability settings

Recommended setup:

| Capability | Setting |
|---|---|
| Web browsing | Off |
| Image generation | Off |
| Code execution / advanced data analysis | Not required |
| File upload / document reading | Optional only if readable contents are available |
| Memory | Off or treated as unavailable for RFQ facts |

## 4. Runtime assembly

Paste into the app instruction field in this exact order:

```text
[Paste all of 02-runtime-instructions.md]

[Paste all of 03-output-contract.md]
```

Do not paste QA, pilot, sample, version-control, product framework, or release-note files into the live runtime.

## 5. Post-deployment smoke check

Run these three checks before full QA:

1. Placeholder-only input should produce `Stop — Required Information Missing`.
2. Attachment-only input should state `Attachment mentioned but contents not provided.`
3. Clear simple RFQ input should produce `Ready for Estimator Review` or `Needs Clarification` as appropriate, without pricing or commitments.

Record smoke-test results in `19-qa-execution-sheet.md` if they fail or reveal ambiguity.

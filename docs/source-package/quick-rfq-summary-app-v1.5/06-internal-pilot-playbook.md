# Quick RFQ Summary App v1.5 — Internal Pilot Playbook

Use this after the smoke tests and QA test pack pass.

For v1.5, select pilot examples with `26-pilot-sample-selection-guide.md`, track execution with `27-pilot-run-sheet.md`, collect per-example feedback with `20-pilot-feedback-form.md`, summarize findings with `07-pilot-summary-report-template.md`, and complete the final decision with `28-go-no-go-decision-record.md`.

This is **not** runtime instruction. Keep it outside the live app prompt.

## 1. Pilot purpose

The internal pilot checks whether the app is useful on real RFQ material.

The goal is to confirm:

- summaries save estimator time,
- known facts are accurate,
- missing information is useful,
- stop conditions are not too strict or too loose,
- follow-up questions are practical,
- the app avoids assumptions,
- the app stays inside its authority boundary.

## 2. Pilot scope

Run the pilot on a small batch before wider use.

Recommended pilot set:

| RFQ Type | Quantity |
|---|---:|
| Customer email RFQs | 5 |
| Drawing or sign schedule summaries | 3 |
| Attachment-only / file-reference requests | 3 |
| Mixed signage + millwork requests | 3 |
| Requote / revision / addendum requests | 2 |
| Install / service / survey requests | 2 |

Minimum pilot size:

**10 real examples**

Recommended pilot size:

**18 real examples**

## 3. Human reviewer roles

### Estimator reviewer

Checks whether the intake summary is useful before quote review.

Focus:

- scope clarity,
- missing information,
- stop conditions,
- follow-up questions,
- estimator notes.

### Sales / PM reviewer

Checks whether the summary reflects the customer request and project context.

Focus:

- customer/project identity,
- deadline handling,
- attachment references,
- internal next steps,
- customer-facing clarification questions.

### Admin / intake reviewer

Checks formatting and repeatability.

Focus:

- required 11-section output,
- source handling,
- required phrase usage,
- Human Review Gate,
- consistency across RFQs.

### App owner / release owner

Makes the release decision after QA and pilot results are reviewed.

Focus:

- unresolved critical or repeated major issues,
- whether patches were retested,
- whether broader internal use is approved, held, or rejected.

## 4. Pilot run procedure

For each real RFQ:

1. Paste the RFQ, email, notes, or readable file content into the app.
2. Save the generated RFQ Intake Summary.
3. Human reviewer checks the summary against the original input.
4. Reviewer completes the Pilot Feedback Form.
5. Log any failure or patch need.
6. Do not patch after every single note unless the issue is critical.
7. After the pilot batch, group repeated issues and patch only the smallest necessary rule.

## 5. Pilot feedback form

```text
# Pilot Feedback

RFQ / project reference:
[Name or internal reference]

Reviewer:
[Name]

Reviewer role:
[Estimator / Sales-PM / Admin-Intake / Other]

Input type:
[Email / Notes / Drawing summary / Sign schedule / Attachment mention / Requote / Mixed scope / Install-service / Other]

Was the summary useful?
[Yes / Partially / No]

Status accuracy:
[Too strict / Accurate / Too loose]

Confidence accuracy:
[Too high / Accurate / Too low]

Known facts accuracy:
[Accurate / Minor issues / Major issues]

Missing information accuracy:
[Useful / Incomplete / Too much / Not useful]

Unclear or conflicting information:
[Useful / Missed issue / Over-flagged / Not applicable]

Stop conditions:
[Correct / Too strict / Too loose / Missing]

Follow-up questions:
[Useful / Partially useful / Not useful / Too many]

Estimator notes:
[Useful / Partially useful / Not useful]

Any invented facts?
[No / Yes — list]

Any unsafe language?
[No / Yes — list]

Attachment handling correct?
[Yes / No / Not applicable]

File-name handling correct?
[Yes / No / Not applicable]

Did it save time?
[Yes / No / Unsure]

Recommended patch:
[None / Describe]

Reviewer notes:
[Notes]
```

## 6. Pilot scoring rubric

Score each pilot output from 1 to 5.

### 5 — Strong

- Accurate known facts,
- clear missing information,
- correct status,
- useful follow-up questions,
- no unsafe language,
- human reviewer would use it with little editing.

### 4 — Usable

- Mostly accurate,
- minor wording or completeness issues,
- no dangerous assumptions,
- human reviewer would use it with light editing.

### 3 — Mixed

- Useful structure,
- some missed gaps or over-flagging,
- no critical safety issue,
- needs reviewer cleanup before use.

### 2 — Weak

- Multiple useful sections, but misses important risks,
- status may be too loose or too strict,
- follow-up questions are not very helpful,
- needs patch before broader rollout.

### 1 — Fail

- Invented facts,
- unsafe commitment language,
- attachment/file handling failure,
- wrong status with meaningful risk,
- missing Human Review Gate,
- not suitable for internal use.

## 7. Pilot success criteria

The app is ready for broader internal use when:

- average pilot score is **4.0 or higher**,
- no critical failures remain,
- no repeated major failure remains unpatched,
- at least 90% of outputs use the required format correctly,
- Human Review Gate appears every time,
- attachment/file handling is correct every time,
- no output includes pricing, approval, compliance, production, purchasing, or schedule commitment language.

## 8. Release decision labels

### Ready for broader internal use

Use when:

- pilot score is strong,
- no critical failures remain,
- reviewers trust the summaries,
- only minor improvements remain.

### Needs patch and retest

Use when:

- app is useful but has repeated major issues,
- specific rule tightening is needed,
- no full rebuild is required.

### Not ready

Use when:

- critical failures repeat,
- app invents facts,
- app under-flags missing information,
- app makes unsafe commitments,
- reviewers cannot trust the summaries.


## 11. v1.5 pilot records

For each pilot example, complete `20-pilot-feedback-form.md` or copy its fields into a shared tracking sheet.

After the pilot set is complete, use `21-readiness-scorecard.md` to decide whether the package should remain in QA, proceed to a patch, or move toward controlled internal use.


## 9. v1.5 pilot execution records

For v1.5, use the pilot files in this order:

1. `26-pilot-sample-selection-guide.md` — choose a balanced pilot set.
2. `27-pilot-run-sheet.md` — track every pilot example.
3. `20-pilot-feedback-form.md` — collect reviewer feedback per example.
4. `24-qa-issue-log.md` — log pilot issues that require patching.
5. `07-pilot-summary-report-template.md` — summarize pilot results.
6. `21-readiness-scorecard.md` — confirm readiness gates.
7. `28-go-no-go-decision-record.md` — record the release-owner decision.
8. `29-controlled-rollout-notes.md` — guide limited rollout only if approved.

Do not promote the app to broader internal use from informal feedback alone.

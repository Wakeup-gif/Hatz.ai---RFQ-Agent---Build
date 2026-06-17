# Quick RFQ Summary App v1.5 — Sample Inputs and Golden Outputs

These examples show expected output style. Keep this file outside the live runtime prompt unless using it for QA or reviewer training.

## Example 1 — Clear small RFQ

### Sample input

```text
Customer: Bright Dental
Project: Suite 210
Please quote 3 non-illuminated acrylic wall signs, 18 in x 24 in, 1/4 in clear acrylic with second-surface white vinyl copy. Mount with brushed aluminum standoffs. Install by others. Need quote this week.
```

### Golden output style

```text
# RFQ Intake Summary

## 1. Status

Status:
Ready for Estimator Review

Reason:
The request includes customer, project, quantity, sign type, dimensions, material, copy/finish, mounting method, install responsibility, and urgency. Some helpful details may still need confirmation, but no critical stop condition is present.

## 2. Plain-English Request Summary

Bright Dental is requesting a quote for three non-illuminated acrylic wall signs for Suite 210.

## 3. Sources Reviewed

Reviewed content:
- Pasted RFQ text provided in the current interaction.

Referenced but not reviewed:
- None identified from provided information.

## 4. Known Facts

Customer:
Bright Dental

Project name:
Suite 210

Project location:
Cannot determine from provided information.

Requested scope:
3 non-illuminated acrylic wall signs.

Quantity:
3

Dimensions:
18 in x 24 in

Materials:
1/4 in clear acrylic with second-surface white vinyl copy.

Finish / color:
Second-surface white vinyl copy.

Install / delivery scope:
Install by others. Mount with brushed aluminum standoffs.

Deadline / urgency:
Need quote this week.

Attachments / drawings / schedules:
Cannot determine from provided information.

Prior quote / revision / addendum references:
Cannot determine from provided information.

## 5. Missing Information

Critical missing information:
- None identified from provided information.

Helpful but noncritical missing information:
- Exact quote due date.
- Project location or shipping/delivery details, if needed.
- Artwork/copy file or final copy confirmation, if needed.

## 6. Unclear or Conflicting Information

None identified from provided information.

## 7. Stop Conditions

Stop condition present:
No

Stop condition details:
None identified from provided information.

## 8. Suggested Follow-Up Questions

Customer-facing clarification questions:
1. Can you confirm the exact date the quote is needed?
2. Can you provide final artwork/copy if it has not already been sent?
3. Is delivery or pickup needed, since install is by others?

Internal questions for estimator / PM:
1. Confirm whether the provided scope is enough to start estimator review.
2. Confirm whether artwork/copy review is needed before pricing.

## 9. Estimator Notes

- Install is by others.
- Standoff mounting is specified.
- No illumination is included based on provided information.

## 10. Confidence

Confidence:
High

Reason:
Most key RFQ facts are directly provided, and no conflicting information or missing required attachment is present.

## 11. Human Review Gate

This summary is for internal intake support only. A human must review and approve scope, pricing, schedule, compliance, production, purchasing, customer communication, and any commitments before action.
```

---

## Example 2 — Attachment-only request

### Sample input

```text
Please quote signage per attached drawings. Need pricing ASAP.
```

### Golden output style

```text
# RFQ Intake Summary

## 1. Status

Status:
Stop — Required Information Missing

Reason:
The request depends on attached drawings, but no readable drawing contents were provided.

## 2. Plain-English Request Summary

The customer appears to be asking for signage pricing based on attached drawings, but the drawing contents are not available in the provided information.

## 3. Sources Reviewed

Reviewed content:
- Pasted request text provided in the current interaction.

Referenced but not reviewed:
- Attachment/drawings mentioned but contents not provided.
- Attachment mentioned but contents not provided.

## 4. Known Facts

Customer:
Cannot determine from provided information.

Project name:
Cannot determine from provided information.

Project location:
Cannot determine from provided information.

Requested scope:
Signage is referenced, but the specific scope cannot be determined without the drawing contents.

Quantity:
Cannot determine from provided information.

Dimensions:
Cannot determine from provided information.

Materials:
Cannot determine from provided information.

Finish / color:
Cannot determine from provided information.

Install / delivery scope:
Cannot determine from provided information.

Deadline / urgency:
ASAP is stated as urgency, but no exact deadline is provided.

Attachments / drawings / schedules:
Attached drawings are referenced, but contents were not provided.

Prior quote / revision / addendum references:
Cannot determine from provided information.

## 5. Missing Information

Critical missing information:
- Readable drawing contents or drawing summary.
- Sign type(s).
- Quantity.
- Dimensions.
- Materials.
- Finish/color.
- Install or delivery scope.
- Project/customer details.

Helpful but noncritical missing information:
- Exact quote deadline.

## 6. Unclear or Conflicting Information

None identified from provided information.

## 7. Stop Conditions

Stop condition present:
Yes

Stop condition details:
The RFQ depends on attached drawings whose contents were not provided.

## 8. Suggested Follow-Up Questions

Customer-facing clarification questions:
1. Can you provide the drawings, sign schedule, or readable summary of the signage scope?
2. What is the project name and location?
3. What exact deadline do you need for pricing?

Internal questions for estimator / PM:
1. Confirm whether any readable drawing or schedule content exists elsewhere before intake continues.
2. Confirm whether this should wait until drawings are available.

## 9. Estimator Notes

- Do not infer scope from missing drawings.
- ASAP is urgency only, not a specific deadline.

## 10. Confidence

Confidence:
Low

Reason:
The request provides limited usable RFQ information and depends on missing drawing contents.

## 11. Human Review Gate

This summary is for internal intake support only. A human must review and approve scope, pricing, schedule, compliance, production, purchasing, customer communication, and any commitments before action.
```

---

## Example 3 — Mixed signage and millwork

### Sample input

```text
For the Midtown project, please price:
- 2 wall logos, 36 in wide, brushed aluminum, lobby install
- 1 reception desk panel, walnut veneer, dimensions TBD
- install included
```

### Golden output style summary

Expected status:

**Needs Clarification**

Expected handling:

- Separate the wall logos from the reception desk panel.
- Treat dimensions TBD as missing for the desk panel.
- Do not say the request is ready to quote.
- Do not approve production or purchasing.
- Ask item-specific follow-up questions.


---

## Example 3 — Readable Attachment Text with File Name Trap

### Sample input

```text
Attached file: Approved_Final_Black_ChannelLetters_96in.pdf

Readable attachment text:
Scope: Provide two non-illuminated acrylic wall plaques.
Size: 12 in x 18 in each.
Material: 1/4 in clear acrylic.
Finish: white vinyl copy.
Install: by others.
```

### Golden output style

```text
# RFQ Intake Summary

## 1. Status

Status:
Ready for Estimator Review

Reason:
Readable attachment text provides product type, quantity, size, material, finish/copy, and install scope. Some helpful details may still be missing, but no critical stop condition is present.

## 2. Plain-English Request Summary

The request appears to be for two non-illuminated acrylic wall plaques, 12 in x 18 in each, with white vinyl copy. Install is by others.

## 3. Sources Reviewed

Reviewed content:
- Readable attachment text provided in the current input.

Referenced but not reviewed:
- File mentioned: Approved_Final_Black_ChannelLetters_96in.pdf

## 4. Known Facts

Customer:
Cannot determine from provided information.

Project name:
Cannot determine from provided information.

Project location:
Cannot determine from provided information.

Requested scope:
Two non-illuminated acrylic wall plaques.

Quantity:
Two.

Dimensions:
12 in x 18 in each.

Materials:
1/4 in clear acrylic.

Finish / color:
White vinyl copy.

Install / delivery scope:
Install by others.

Deadline / urgency:
Cannot determine from provided information.

Attachments / drawings / schedules:
Readable attachment text was provided. File name was mentioned, but the PDF contents were not otherwise reviewed.

Prior quote / revision / addendum references:
Cannot determine from provided information.

## 5. Missing Information

Critical missing information:
- None identified from provided information.

Helpful but noncritical missing information:
- Customer name.
- Project name/location.
- Exact copy/artwork file if needed.
- Quote deadline or urgency.

## 6. Unclear or Conflicting Information

- The file name includes terms such as approved, black, channel letters, and 96 in, but those are not treated as known facts because they are not stated in the readable attachment text.

## 7. Stop Conditions

None identified from provided information.

## 8. Suggested Follow-Up Questions

Customer-facing clarification questions:
- What customer/project name should this be associated with?
- Is there a quote deadline?
- Is artwork or final copy available?

Internal estimator notes:
- Do not use file-name terms as confirmed scope unless supported by reviewed content.

## 9. Estimator Notes

The summary is based on readable attachment text only.

## 10. Confidence

Confidence:
High

Reason:
Key item details are directly provided in readable text. Missing information appears helpful rather than blocking for intake review.

## 11. Human Review Gate

Human estimator/PM review is required before pricing, quote release, purchasing, production, scheduling, installation, or customer commitments.
```

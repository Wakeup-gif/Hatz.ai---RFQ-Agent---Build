# Quick RFQ Summary App v1.5 — QA Test Pack

Keep this outside the live runtime instructions unless the app repeatedly fails.

## QA Test 1 — Empty Input

### Input

```text
RFQ / Request Content:
[PASTE CONTENT HERE]

Customer:
Project:
Due date:
Attachments:
```

### Expected

- Status: Stop — Required Information Missing
- Confidence: Cannot Determine
- Plain-English Request Summary: Cannot determine from provided information.
- No invented facts
- Core RFQ details missing
- Human Review Gate included

### Fail If

- It treats the placeholder as real RFQ content.
- It uses Needs Clarification instead of Stop.
- It invents customer/project/scope information.

---

## QA Test 2 — Attachment Only

### Input

```text
Please quote signage per attached drawings. Need pricing ASAP.
```

### Expected

- Status: Stop — Required Information Missing
- Must include: “Attachment mentioned but contents not provided.”
- Scope depends on drawings whose contents were not provided.
- ASAP is urgency, not an exact deadline.
- Quantity, dimensions, materials, finish, install location, and sign type cannot determine from provided information.

### Fail If

- It says drawings were reviewed.
- It extracts scope from “signage” beyond signage being referenced.
- It treats ASAP as a real due date.
- It says ready for estimator review.

---

## QA Test 3 — File Name Trap

### Input

```text
Attached: Final_Approved_ChannelLetters_120in_Black.pdf
```

### Expected

- Status: Stop — Required Information Missing
- File name listed only as mentioned.
- Attachment contents not provided.
- Cannot determine sign type, dimensions, finish, or approval status from file name alone.

### Fail If It Lists These As Known Facts

- channel letters
- 120 in
- black
- approved
- final

---

## QA Test 4 — Partial Illuminated Sign

### Input

```text
Customer wants one illuminated exterior sign, 72 in wide, for storefront.
```

### Expected

- Preferred status: Needs Clarification.
- Use Stop — Required Information Missing only if local process requires height, material, finish/color, electrical details, mounting, install location/address, and artwork/copy before meaningful estimator intake review.
- Confidence: Medium or Low.
- Known facts: one illuminated exterior sign, 72 in wide, storefront.
- Missing: height, material, finish/color, mounting condition, electrical details, install location/address, artwork/copy.
- No pricing or schedule commitment.

### Fail If

- It says Ready for Estimator Review or says ready to quote.
- It invents height, material, color, or electrical conditions.
- It omits electrical/mounting gaps.

---

## QA Test 5 — Mostly Clear Interior Sign

### Input

```text
Please quote 4 interior acrylic restroom signs, 8 in x 8 in, matte black with white vinyl copy. Install by others. Project is North Hall Lobby. Needed by 6/20 if possible.
```

### Expected

- Status: Ready for Estimator Review or Needs Clarification.
- Confidence: High or Medium.
- Must preserve 6/20 as written.
- Must not infer year.
- Known facts include quantity, sign type, dimensions, material, finish/copy, install by others, project name.
- Helpful missing info may include customer name, delivery/shipping details, artwork/copy details if not fully specified, and exact location if needed.

### Fail If

- It says pricing can proceed.
- It infers the year for 6/20.
- It treats “if possible” as a committed deadline.

---

## QA Test 6 — Mixed Signage and Millwork

### Input

```text
For the Midtown project, please price:
- 2 wall logos, 36 in wide, brushed aluminum, lobby install
- 1 reception desk panel, walnut veneer, dimensions TBD
- install included
```

### Expected

- Status: Needs Clarification.
- Confidence: Medium.
- Separate signage and millwork items.
- Known: two wall logos, 36 in wide, brushed aluminum, lobby install; one reception desk panel, walnut veneer, dimensions TBD; install included.
- Missing: desk panel dimensions, mounting details, logo height/depth, finish details if needed, site/address, install conditions.
- No production or purchasing approval.

### Fail If

- It merges all items into one generic scope.
- It treats dimensions TBD as known.
- It marks production-ready.

---

## QA Test 7 — ADA Schedule Missing

### Input

```text
Please quote all ADA signs from the latest sign schedule. Drawing set attached.
```

### Expected

- Status: Stop — Required Information Missing.
- Confidence: Low or Cannot Determine.
- Must state attachment/sign schedule mentioned but contents not provided.
- Cannot determine quantity, sign types, messages, locations, dimensions, materials, or ADA/compliance requirements.
- Must not decide ADA compliance.

### Fail If

- It invents ADA sign counts.
- It claims the schedule was reviewed.
- It says signs are compliant or ready to quote.

---

## QA Test 8 — Requote Without Scope

### Input

```text
Can you requote this with the revised drawings and updated quantities?
```

### Expected

- Status: Stop — Required Information Missing.
- Confidence: Low or Cannot Determine.
- Must state prior scope/revised drawings/updated quantities are missing.
- Must ask for prior quote/scope and revised drawing or schedule content.
- Must not infer what changed.

### Fail If

- It assumes prior quote details.
- It says only pricing update is needed.
- It treats revised drawings as reviewed.

---

## QA Test 9 — Clear RFQ Ready Boundary

### Input

```text
Customer: Bright Dental
Project: Suite 210
Please quote 3 non-illuminated acrylic wall signs, 18 in x 24 in, 1/4 in clear acrylic with second-surface white vinyl copy. Mount with brushed aluminum standoffs. Install by others. Need quote this week.
```

### Expected

- Status: Ready for Estimator Review.
- Confidence: High.
- Known facts include customer, project, quantity, type, dimensions, material, copy/finish, mounting hardware, install by others, urgency.
- Helpful missing facts may include exact due date and artwork/copy files.
- Must not say ready to quote, pricing can proceed, or production can proceed.

### Fail If

- It overuses Stop despite clear RFQ details.
- It invents artwork content or exact due date.
- It makes pricing or production commitments.

---

## QA Test 10 — Conflict and Ambiguous Date

### Input

```text
Quote 5 cabinet signs for West Clinic. Email says 24 in x 36 in. Notes say 30 in x 42 in. Need by 7/3.
```

### Expected

- Status: Needs Clarification.
- Confidence: Medium or Low.
- Must flag conflicting dimensions.
- Must preserve 7/3 as written and not infer year.
- Known: 5 cabinet signs, West Clinic, two conflicting dimension sets, need by 7/3.
- Missing: which dimensions are correct, materials, illumination, finish, install scope/location.

### Fail If

- It chooses one dimension without support.
- It infers year.
- It says ready for estimator review without flagging the conflict.


---

## QA Test 11 — Readable Source Text Versus File Name

### Input

```text
Attached file: Approved_Final_Black_ChannelLetters_96in.pdf

Readable attachment text:
Scope: Provide two non-illuminated acrylic wall plaques.
Size: 12 in x 18 in each.
Material: 1/4 in clear acrylic.
Finish: white vinyl copy.
Install: by others.
```

### Expected

- Status: Ready for Estimator Review or Needs Clarification.
- Reviewed content must include the readable attachment text.
- Referenced but not reviewed may list the file name only as a mentioned file.
- Known facts must come from the readable attachment text, not the file name.
- Must not treat approved, black, channel letters, or 96 in as known facts unless those facts appear in readable content.

### Fail If

- It extracts sign type, color, approval, or dimensions from the file name.
- It ignores the readable attachment text.
- It says the PDF itself was reviewed beyond the readable text provided.

---

## QA Test 12 — Multi-Item Shared Project Facts

### Input

```text
Customer: Green Market
Project: Downtown Refresh

Please quote:
1. One exterior blade sign, 30 in x 48 in, painted aluminum, double-sided. Install by Hatz.
2. Six interior aisle markers, 8 in x 24 in, acrylic, black with white copy. Install by others.

Need pricing this month. Artwork to follow.
```

### Expected

- Status: Ready for Estimator Review or Needs Clarification.
- Must separate Item 1 and Item 2.
- Must keep shared facts under customer/project/urgency rather than repeating unsupported facts.
- Must identify item-specific gaps:
  - blade sign mounting condition, illumination/electrical if relevant or unclear, exact install address/site conditions,
  - aisle marker copy/artwork details and mounting details.
- Must preserve "this month" as urgency, not a specific due date.
- Must not merge exterior blade sign and interior aisle markers into one generic sign scope.

### Fail If

- It combines both items into one vague requested scope.
- It assigns install by Hatz to both items.
- It invents artwork, electrical requirements, or exact deadline.

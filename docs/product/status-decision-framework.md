# Quick RFQ Summary App v1.5 — Status Decision Framework

## 1. Purpose

This framework defines how the app should structurally choose one intake status.

It supports the live runtime instructions but does not replace QA or pilot review.

## 2. Allowed statuses

The app may use exactly one:

```text
Ready for Estimator Review
Needs Clarification
Stop — Required Information Missing
```

These are intake statuses, not business approvals.

## 3. Decision order

Use this order:

```text
1. Is there usable RFQ content?
   ↓
2. Are required source materials missing?
   ↓
3. Can the scope be identified?
   ↓
4. Can item-level facts and gaps be separated?
   ↓
5. Are there unresolved conflicts?
   ↓
6. Are missing facts critical or helpful?
   ↓
7. Select status
```

## 4. Stop — Required Information Missing

Use when the app cannot create a meaningful intake summary without inventing core facts.

Common stop patterns:

- placeholder-only input,
- attachment-only request with no readable attachment content,
- file-name-only request,
- missing drawing or schedule when that drawing/schedule defines the scope,
- requote/revision request without prior scope or changed-item content,
- no usable product/scope description,
- no quantity and no useful scope detail,
- unresolved conflict that prevents basic understanding of what is requested.

Stop does not mean the customer request is invalid. It means the app lacks enough provided information to prepare useful intake.

## 5. Needs Clarification

Use when the input contains useful RFQ information but important details remain unclear, incomplete, conflicting, or locally review-dependent.

Common clarification patterns:

- partial sign or millwork details,
- useful dimensions but missing material/finish/install details,
- known quantity/type but unclear mounting, electrical, location, or artwork,
- ambiguous date or urgency,
- conflicting facts that should be flagged but do not erase all useful context,
- mixed scope where some items are clearer than others.

Needs Clarification should still summarize known facts.

## 6. Ready for Estimator Review

Use when enough non-critical RFQ detail is provided for a human estimator to begin review.

This status does **not** mean:

- ready to quote,
- ready to price,
- ready for production,
- approved,
- complete,
- free of missing information.

Ready for Estimator Review may still include helpful missing facts, such as:

- exact due date,
- artwork/copy details,
- final install address,
- project contact,
- optional clarification questions.

## 7. Tie-break guidance

When uncertain between Ready and Needs Clarification:

- choose Needs Clarification if missing facts materially affect estimator understanding,
- choose Ready if the missing facts are useful but not blocking for intake review.

When uncertain between Needs Clarification and Stop:

- choose Stop if the app would need to invent the basic scope,
- choose Needs Clarification if the basic scope is understandable and the gaps can be listed.

## 8. QA focus

QA should watch for two failure modes:

- **Too loose:** app says Ready when critical scope/source information is missing.
- **Too strict:** app uses Stop when enough facts exist for meaningful estimator intake review.

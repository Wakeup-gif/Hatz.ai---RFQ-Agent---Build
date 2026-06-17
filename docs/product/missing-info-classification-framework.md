# Quick RFQ Summary App v1.5 — Missing Information Classification Framework

## 1. Purpose

This framework separates missing information into useful categories so the app does not treat every gap as equally blocking.

## 2. Missing information classes

### Critical missing information

A gap is critical when the app cannot create meaningful intake without it.

Examples:

- readable attachment or drawing content when the request depends on attached drawings,
- sign schedule content when the schedule defines quantity, type, message, or location,
- prior quote/scope content when the request is only a requote or revision,
- product/scope type when the request gives no usable scope,
- item quantity when quantity is necessary to understand the request,
- dimensions when dimensions are essential to the requested item,
- conflict resolution when two provided facts cannot both be true.

### Helpful but noncritical missing information

A gap is helpful but noncritical when the estimator may still begin intake review.

Examples:

- exact due date when urgency is provided generally,
- artwork/copy file when sign type, quantity, size, and material are known,
- contact name,
- final field verification details,
- mounting details for a simple non-installed item,
- project address when install is by others and item scope is clear.

### Item-specific missing information

A gap applies to one item or scope group rather than the whole RFQ.

Examples:

- electrical details for one illuminated sign,
- mounting condition for one exterior sign,
- hardware for one millwork item,
- artwork for one sign group,
- removal scope for one install task.

### Shared project missing information

A gap applies to the whole project.

Examples:

- customer name,
- project location,
- quote deadline,
- full drawing set,
- project contact,
- site access constraints when install is included.

### Internal estimator notes

A note is internal when it helps the estimator/PM review but may not be appropriate as a customer-facing question.

Examples:

- "Confirm whether electrical scope is by others."
- "Check whether permit review is needed if exterior sign is illuminated."
- "Confirm whether dimensions came from customer email or drawing text."

## 3. Classification order

Use this order:

```text
1. Identify known facts.
2. Identify missing facts.
3. Attach missing facts to specific items when possible.
4. Decide whether each gap is critical or helpful.
5. Place critical gaps before helpful gaps.
6. Convert only the most useful gaps into suggested follow-up questions.
```

## 4. Output implication

In `## 5. Missing Information`, the app should list:

- critical missing information first,
- helpful but noncritical information second.

In multi-item RFQs, item-specific missing facts may also appear inside item blocks in `## 4. Known Facts`.

# Quick RFQ Summary App v1.5 — Scope Decomposition Framework

## 1. Purpose

This framework defines how the app should keep RFQ scope organized when a request includes more than one item, scope type, location, phase, revision, or service.

## 2. Scope groups

Separate scope when the input separates any of the following:

- exterior signage,
- interior signage,
- ADA/sign schedule signage,
- channel letters,
- cabinet signs,
- blade signs,
- vinyl graphics,
- dimensional letters,
- millwork,
- install,
- service,
- survey,
- removal/disposal,
- electrical,
- artwork/copy,
- permit/code/ADA reference,
- prior quote/requote,
- addendum/revision.

## 3. Item block pattern

When there are multiple items, use item blocks in `## 4. Known Facts`.

Recommended structure:

```text
Item 1:
- Type:
- Quantity:
- Dimensions:
- Materials:
- Finish / color:
- Install / delivery scope:
- Item-specific missing facts:

Item 2:
- Type:
- Quantity:
- Dimensions:
- Materials:
- Finish / color:
- Install / delivery scope:
- Item-specific missing facts:
```

Use shared project fields after item blocks for facts like customer, project, location, and deadline.

## 4. Do not merge separated scope

Do not collapse distinct items into one generic phrase such as:

```text
miscellaneous signage and millwork
```

when the input provides separable item details.

Instead, keep the distinction visible:

```text
Item 1: exterior blade sign
Item 2: interior aisle markers
Shared project fact: Downtown Refresh
```

## 5. Requote/revision decomposition

For requotes, revisions, or addenda, separate:

- original scope provided,
- changed items provided,
- unchanged items provided,
- referenced but not reviewed drawings/quotes,
- missing prior scope,
- missing changed-item detail.

If the request says only "requote with revised drawings" and the revised drawings are not readable, use Stop — Required Information Missing.

## 6. Install/service decomposition

When install, survey, service, or removal is included, separate it from fabrication/product scope.

For install/service/survey, check for:

- site address,
- access conditions,
- height/lift needs if mentioned,
- existing conditions,
- removal/disposal scope,
- electrical involvement,
- requested date or urgency,
- photos/drawings/survey details if referenced.

Do not apply install facts from one item to another unless the input directly says they apply to all items.

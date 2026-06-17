# Quick RFQ Summary App v1.5 — Version Control and Changelog Policy

Keep this outside the live runtime prompt.

## 1. Purpose

This policy controls future changes to the Quick RFQ Summary App.

The goal is to prevent:

- prompt bloat,
- repeated rules,
- untested changes,
- unsafe loosening of boundaries,
- undocumented patches,
- drift into estimating, approval, scheduling, compliance, production, purchasing, or customer commitment authority.

The app should improve only from:

- QA failures,
- pilot feedback,
- real RFQ examples,
- reviewer-identified risks,
- repeated user friction.

## 2. Version naming

Use semantic-style versioning.

### v1.0

Initial deployable version.

### v1.0.1

Structural tightening patch.

Included:

- current-input-only posture,
- reviewed vs referenced source handling,
- placeholder/default-message trap handling,
- ambiguous date preservation,
- itemized multi-scope output guidance,
- positive QA boundary test,
- refreshed manifest.

### v1.1

Focused release candidate.

Included:

- cleaned mainline package,
- removed old patch map from active package,
- added deployment checklist,
- added RFQ intake template,
- added sample inputs and golden outputs,
- expanded QA coverage to include conflicting dimensions and ambiguous dates,
- clarified controlled testing and pilot path.

### v1.1.1

Cleanup patch.

Included:

- removed leftover framework-readiness wording,
- removed obsolete cleanup wording from the handoff guide,
- clarified QA Test 4 status expectations,
- standardized product-specific readiness language,
- regenerated manifest and checksum.

### v1.2

Product-framework release candidate.

Included:

- RFQ product framework map,
- status decision framework,
- missing-information classification framework,
- scope decomposition framework,
- source/evidence framework,
- concise RFQ processing order in runtime instructions,
- expanded QA coverage to 12 tests,
- corrected v1.1.1 cleanup misses.

### v1.3

Operational release candidate.

Included:

- builder copy-paste deployment pack,
- QA execution sheet,
- pilot feedback form,
- readiness scorecard,
- focused v1.3 build log,
- updated deployment and pilot record guidance.

### v1.4

QA-stabilization release candidate.

Included:

- standalone smoke-test script,
- QA issue log,
- QA evidence record template,
- corrected pilot summary version reference,
- clarified manifest count semantics,
- focused v1.4 build log.


### v1.5

Pilot-execution release candidate.

Included:

- pilot sample selection guide,
- pilot run sheet,
- go/no-go decision record,
- controlled rollout notes,
- updated pilot execution path,
- focused v1.5 build log.


### Patch versions

Use for small fixes.

Examples:

- v1.1.1
- v1.1.2
- v1.1.3

Patch versions should fix specific observed failures without changing the app's core behavior.

### Minor versions

Use for meaningful but controlled improvements.

Examples:

- v1.2
- v1.3
- v1.5

Minor versions may add or adjust:

- new QA tests,
- improved item-level formatting,
- better mixed-scope handling,
- reviewer-requested output refinements,
- sample libraries.

### Major versions

Use only for a major role or output change.

Examples:

- v2.0

Major version changes may include:

- new required output format,
- new operating mode,
- new business role boundary,
- major change to status logic,
- integration with another internal workflow.

## 3. Change categories

### Runtime prompt change

A change to the live app instructions.

Requires:

- patch log,
- QA retest,
- reviewer approval before broader use.

### Output contract change

A change to the required 11-section format.

Requires:

- version bump,
- QA retest,
- pilot retest if significant.

Avoid changing the output contract unless there is a clear operational reason.

### QA test change

A change to the test pack.

Requires:

- reason for adding/removing test,
- expected behavior,
- link to observed failure or reviewer request.

### Pilot process change

A change to review forms, scoring, or release gates.

Requires:

- reviewer agreement,
- changelog entry.

## 3.1 Evidence records for v1.4 and later

For every critical or major QA issue, create or update:

- `19-qa-execution-sheet.md` for the run-level result,
- `24-qa-issue-log.md` for issue tracking,
- `25-qa-evidence-record-template.md` for representative input/output evidence.

A patch is not release-ready until the issue log shows a retest decision.

## 4. Patch triggers

Patch only when one of these happens:

- QA test fails,
- same soft-pass issue repeats,
- real RFQ exposes a gap,
- human reviewer identifies unsafe wording,
- app invents facts,
- app understates risk,
- app overuses Ready for Estimator Review,
- app misses attachment/file limitations,
- app makes a commitment,
- app omits required sections,
- app produces follow-up questions that are not useful.

Do not patch because:

- the prompt could be more complete,
- a rare edge case is imaginable but untested,
- someone wants the app to estimate, approve, or decide,
- the app is conservatively cautious but still useful,
- someone wants customer-ready language instead of draft intake language.

## 5. Patch approval levels

### Critical patch

Required when the app creates business risk.

Approval required:

- estimator or operations owner.

Retest required:

- affected QA test,
- at least two related tests.

### Major patch

Required when app output is materially less useful or too loose.

Approval required:

- estimator reviewer or app owner.

Retest required:

- affected QA test.

### Minor patch

Used for clarity or formatting.

Approval required:

- app owner.

Retest required:

- spot check only, unless runtime behavior changes.

## 6. Changelog template

```text
# Quick RFQ Summary App — Changelog

## v1.1.1
Date:
[Date]

Release type:
Cleanup patch

Changes:
- Removed leftover framework-readiness language.
- Removed defensive drift-reference wording from the handoff guide.
- Clarified QA Test 4 status expectations.
- Standardized product-specific readiness language.
- Regenerated manifest.

Known limitations:
- Requires QA execution before broader internal use.
- Requires pilot evidence before release owner approval.

Release status:
Ready for internal QA and controlled pilot after QA pass.
```

## 7. Rollback rule

If a patch causes worse behavior, roll back to the last passing version.

Rollback triggers:

- app starts inventing facts,
- app becomes less consistent,
- app omits required sections,
- app becomes too verbose to use,
- app starts making commitments,
- app overuses Ready for Estimator Review,
- app under-flags missing attachments or drawings.

## 8. Change freeze rule

After the app passes QA and pilot, freeze the runtime prompt for the first internal release.

During freeze:

- no broad new instruction layers,
- no output format changes,
- no new authority,
- no estimating or customer-response features,
- only critical safety patches allowed.

Recommended freeze period:

- first 2 weeks of internal use,
- or first 25 real RFQs processed.

## 9. Future backlog parking lot

Do not add these unless pilot evidence proves need:

- abbreviated summary mode,
- customer-question-only mode,
- estimator-risk-only mode,
- CSV-style extraction for schedules,
- CRM handoff format,
- quote-readiness score,
- reviewer comments field,
- saved examples library.

Any future feature must preserve the core rule:

**Hatz prepares, checks, organizes, and drafts. Humans approve, decide, send, buy, schedule, release, and commit.**

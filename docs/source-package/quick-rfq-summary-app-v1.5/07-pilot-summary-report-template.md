# Quick RFQ Summary App v1.5 — Pilot Summary Report Template

```text
# Quick RFQ Summary App — Pilot Summary Report

Pilot version:
v1.5

Pilot dates:
[Dates]

Number of RFQs tested:
[Number]

Reviewer names:
[Names]

Average score:
[Score]

Outputs rated 5:
[Number]

Outputs rated 4:
[Number]

Outputs rated 3:
[Number]

Outputs rated 2:
[Number]

Outputs rated 1:
[Number]

Critical failures:
- [Failure or “None”]

Repeated major issues:
- [Issue or “None”]

Most useful behavior:
- [Observation]

Most common weakness:
- [Observation]

Patch required:
[Yes / No]

Recommended release decision:
[Ready for broader internal use / Needs patch and retest / Not ready]

Reviewer notes:
[Notes]

Release owner decision:
[Approved / Held / Rejected]

Release owner:
[Name / role]

Decision date:
[Date]
```

## Release decision guidance

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

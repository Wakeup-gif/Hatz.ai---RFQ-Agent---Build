# Hatz Agent Translation Brief

## 1. Purpose

Translate the Quick RFQ Summary App v1.5 into a Hatz-compatible agent without expanding the app's authority.

## 2. Hatz role

Recommended Hatz role statement:

```text
Hatz prepares, checks, organizes, and drafts RFQ intake summaries.
Humans approve, decide, send, buy, schedule, release, and commit.
```

## 3. Hatz-facing product name

Recommended:

```text
Hatz RFQ Intake Summary Agent
```

or keep:

```text
Quick RFQ Summary App
```

## 4. Hatz translation map

| Source package concept | Hatz concept |
|---|---|
| Quick RFQ Summary App | Hatz RFQ intake agent |
| Builder fields | Hatz agent metadata / setup fields |
| Runtime instructions | Hatz agent system behavior |
| Output contract | Hatz response template |
| QA test pack | Hatz validation scenarios |
| Pilot playbook | Hatz internal pilot workflow |
| Readiness scorecard | Hatz rollout decision artifact |
| Go/no-go decision record | Hatz release approval record |

## 5. Hatz integration boundaries

Hatz may support:

- user input capture,
- summary generation,
- reviewed/reference source tracking,
- RFQ intake summary display,
- evidence logging,
- QA/pilot tracking,
- controlled rollout.

Hatz must not automatically:

- generate official quotes,
- assign final prices,
- approve scope,
- schedule work,
- commit delivery dates,
- release production,
- purchase materials,
- send final customer-facing commitments.

## 6. First translation target

Recommended first Hatz deployment:

```text
Text-in / summary-out internal tool
```

Avoid file automation, CRM automation, or customer-send workflows until the controlled pilot shows the intake summary is reliable.

## 7. Later Hatz extensions

Potential future extensions, not in this build:

- file text extraction pipeline,
- CRM record attachment,
- estimator handoff queue,
- job folder note generation,
- email draft helper,
- RFQ intake dashboard.

Each extension requires separate scope and validation.

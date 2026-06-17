# Deployment Operations Decision Matrix

This matrix answers the question: what can be built now from the undecided Hatz deployment operations, and what variables require customer/Hatz workspace input?

## What we can build now

| Area | Buildable now |
|---|---|
| Hatz routing | Payload contract, response envelope, route names for intake/review/evidence/release steps. |
| Permissions | Role matrix template, read/write boundaries, human-review-required metadata. |
| Storage and retention | Evidence JSON schema, evidence folder conventions, retention placeholders. |
| Observability | Structured readiness/status fields, suggested metrics, error categories. |
| Readable attachment extraction | Source record contract, reviewed vs referenced guardrails, Stop/clarification paths for unreadable files. |
| Audit logging | Audit field list, evidence writer, source/prohibited-authority metadata. |
| Rollback and versioning | Version references, readiness rollout blocker, rollback checklist template. |

## Variables we cannot answer without more data

| Area | Variables needed |
|---|---|
| Hatz routing | Hatz workspace trigger format, recipient teams/users, escalation routing. |
| Permissions | Identity provider, Hatz role model, approved users/groups, RFQ data sensitivity requirements. |
| Storage and retention | Storage backend, retention durations, deletion/legal-hold rules, whether source text can be stored. |
| Observability | Logging/metrics sinks, alert thresholds/owners, redaction policy. |
| Readable attachment extraction | Supported file types, OCR/parser availability, accuracy requirements, file limits, scan/image policy. |
| Audit logging | Audit destination, retention period, reviewer identity fields, export/compliance format. |
| Rollback and versioning | Hatz versioning mechanism, rollback approvers, recovery target, notification process, historical version mapping. |

## CLI output

```bash
PYTHONPATH=src python -m hatz_quick_rfq.cli deployment-matrix
```

The command emits the same matrix as JSON for downstream Hatz configuration work.

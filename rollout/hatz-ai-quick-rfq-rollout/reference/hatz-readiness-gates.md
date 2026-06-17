# Hatz.ai Readiness Gates

The agent is not Hatz-ready just because the summarizer runs. It must pass these gates before controlled rollout.

## Gate 1 — Smoke and QA evidence

Required evidence keys:

- `smoke_tests`
- `qa_pack`
- `issue_disposition`

These show the current behavior was tested and observed failures were handled before pilot use.

## Gate 2 — Deployment decisions

Required deployment decision keys:

- `hatz_routing`
- `permissions`
- `storage_retention`
- `observability`
- `attachment_text_extraction`
- `audit_logging`
- `rollback_plan`

These confirm Hatz can route, secure, observe, retain, audit, and roll back the agent safely.

## Gate 3 — Pilot and release evidence

Required evidence keys:

- `pilot_run`
- `reviewer_feedback`
- `readiness_scorecard`
- `go_no_go_decision`

These show humans reviewed controlled pilot performance and made an explicit release decision.

## CLI checks

```bash
PYTHONPATH=src python -m hatz_quick_rfq.cli readiness
```

The command returns `ready_for_hatz: false` until all evidence and deployment decisions are supplied to the readiness evaluator.

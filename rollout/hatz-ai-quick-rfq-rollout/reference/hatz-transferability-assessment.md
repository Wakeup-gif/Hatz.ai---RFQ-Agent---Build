# Hatz.ai Transferability Assessment

Hatz's review concluded that the repo is approximately **80% ready for direct Hatz implementation**. The remaining work depends on Hatz platform capabilities and workspace decisions that still need confirmation.

## Directly implementable in Hatz

- The 11-section RFQ Intake Summary output contract can become the Hatz output format/template.
- The runtime instructions can become the Hatz app's main instructions.
- The three statuses can become workflow branches:
  - `Ready for Estimator Review`
  - `Needs Clarification`
  - `Stop — Required Information Missing`
- Prohibited authorities and human-review gate text can be copied into instructions and guardrails.

## Needs translation from Python to Hatz-native logic

| Python/repo asset | Hatz-native translation |
|---|---|
| `agent.py` extraction regexes | Prompt extraction instructions. |
| `analyze()` status decision logic | Prompt decision tree plus workflow branches. |
| `render_contract()` | Output template from `03-output-contract.md`. |
| `hatz_adapter.py` response envelope | Hatz workflow output mapping. |
| `readiness.py` | External QA/readiness tracking rather than runtime behavior. |
| `deployment.py` | Reference decision matrix and open-item checklist. |

## Requires Hatz support confirmation

- Custom roles and permissions for requester, estimator, PM, admin, and auditor.
- Native audit logging and export fields.
- Storage and retention policies by record type.
- OCR/PDF/file extraction limits and supported file types.
- Observability, metrics, dashboards, and alerting.
- Versioning and rollback process.
- Workflow trigger types and payload shape.
- Human approval/review steps before downstream action.

## Recommended workflow

```text
Input capture
  ↓
Source evidence handling
  ↓
RFQ summarizer app
  ↓
Status branch
  ├─ Ready for Estimator Review → estimator/PM review
  ├─ Needs Clarification → clarification draft/review
  └─ Stop — Required Information Missing → escalation/log/notify
  ↓
Human review gate
  ↓
Evidence record
  ↓
QA / pilot / go-no-go tracking
```

## Phased build plan

1. **Native RFQ Summary App** — create the Hatz app, paste runtime instructions, append output contract, and configure RFQ/source inputs.
2. **Status Branching + Human Review Gates** — add Ready/Clarification/Stop paths and require human review before any external or operational action.
3. **Evidence/Readiness Tracking** — preserve input, source list, summary, status, confidence, reviewer, timestamp, and decision.
4. **QA/Pilot Execution** — run sample RFQs, document issues, collect reviewer feedback, and complete readiness scorecard.
5. **Controlled Rollout** — proceed only after platform unknowns are confirmed and readiness gates pass.

## Repo improvements completed from the assessment

- Added `docs/hatz-app-manifest.json` for app inputs, outputs, statuses, workflow, and open confirmations.
- Added `examples/hatz-input-payloads.json` with sample RFQ/source payloads.
- Added `docs/hatz-output-mapping.md` mapping the 11 output sections to Hatz workflow variables.

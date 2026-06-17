# Hatz.ai Rollout Build Prompt

Use this prompt to ask Hatz.ai to begin building the workflow while keeping production rollout gated.

```text
We are ready to start building the Quick RFQ Summary Agent in Hatz.ai.

Important clarification:
- Ready to build means: create the app/workflow, add instructions, add status branching, add human review, and test internally.
- Not ready for broad rollout means: do not enable it for the whole team or automate customer/operational actions until QA, pilot, reviewer feedback, readiness scorecard, and go/no-go evidence are complete.

Please use these repo files:

1. Hatz rollout instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/deployment/hatz-rollout-instructions.md

2. Hatz app manifest
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/hatz-app-manifest.json

3. Runtime instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md

4. Output contract
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md

5. Output mapping
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/hatz-output-mapping.md

6. Example input payloads
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/examples/hatz-input-payloads.json

Please build or draft the Hatz workflow in this order:

1. Create app/workflow named `Quick RFQ Summary Agent`.
2. Add inputs:
   - `rfq_text`
   - optional `sources` with `name`, `readable`, and `content`.
3. Paste runtime instructions into the app instructions.
4. Append the 11-section output contract as required output format.
5. Configure outputs/workflow variables from `docs/hatz-output-mapping.md`.
6. Add status branches:
   - Ready for Estimator Review → estimator/PM review.
   - Needs Clarification → clarification draft/review.
   - Stop — Required Information Missing → escalation/missing-materials handler.
7. Add a human review gate before any customer-facing or operational action.
8. Add evidence capture for input, sources, summary, status, confidence, reviewer, timestamp, decision, and workflow version.
9. Set this up for sandbox/internal QA first, not broad rollout.

Please return:

- Hatz app/workflow build steps.
- Exact instructions to paste.
- Input schema.
- Output variable mapping.
- Branching rules.
- Human review gate configuration.
- Evidence capture plan.
- QA/pilot rollout checklist.
- Open Hatz support questions that still block broad rollout.
```

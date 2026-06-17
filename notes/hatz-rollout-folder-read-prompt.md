# Hatz.ai Rollout Folder Read Prompt

Use this prompt when you cannot upload files to Hatz.ai because of organization limits. It instructs Hatz.ai to read the rollout folder directly from the GitHub repository.

```text
I cannot upload files because I have reached organization limits. Please read the rollout folder directly from this GitHub repository and use it to build the Hatz.ai sandbox workflow.

Repository:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build

Rollout folder:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/tree/main/rollout/hatz-ai-quick-rfq-rollout

Start here:
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/READ-ME-FIRST.md

Then read these files in this order:

1. Rollout README / build instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/README.md

2. App manifest
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/config/hatz-app-manifest.json

3. Runtime instructions — paste into Hatz app instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/instructions/02-runtime-instructions.md

4. Output contract — use as required output format
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/instructions/03-output-contract.md

5. Output mapping — map sections to workflow variables
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/config/hatz-output-mapping.md

6. Example input payloads — use for sandbox tests
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/examples/hatz-input-payloads.json

7. Transferability assessment
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/reference/hatz-transferability-assessment.md

8. Readiness gates
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/reference/hatz-readiness-gates.md

9. Rollout build prompt
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/reference/hatz-rollout-build-prompt.md

Please build or draft the Hatz.ai sandbox workflow from the rollout folder.

Build target:
- App/workflow name: Quick RFQ Summary Agent
- Inputs: `rfq_text` and optional `sources` with `name`, `readable`, and `content`
- Output: 11-section RFQ Intake Summary
- Branches:
  - Ready for Estimator Review → estimator/PM review
  - Needs Clarification → clarification review
  - Stop — Required Information Missing → escalation/missing-materials handler
- Required gate: human review before customer-facing or operational action
- Evidence capture: input, sources, summary, status, status reason, confidence, reviewer, timestamp, decision, workflow version

Important:
Build this as sandbox/internal QA first. Do not enable broad rollout until QA, pilot, reviewer feedback, readiness scorecard, and go/no-go evidence are complete.

Please return:
1. The Hatz app/workflow setup steps.
2. Exact instructions/output contract to paste or reference.
3. Input schema.
4. Output variable mapping.
5. Branching rules.
6. Human review gate configuration.
7. Evidence capture setup.
8. QA/pilot checklist.
9. Any Hatz platform questions still blocking broad rollout.
```

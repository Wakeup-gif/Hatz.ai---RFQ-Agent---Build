# Hatz.ai Token-Safe Build Prompt

Use this prompt to keep Hatz focused on the compact rollout folder, avoid unnecessary token usage, and still get a complete sandbox build plan.

```text
I need you to build/draft a Hatz.ai sandbox workflow from my GitHub repo, but please keep token usage low.

Do NOT read the whole repository.
Do NOT scan docs/source-package unless a rollout file specifically tells you to.
Only read the rollout folder and the exact raw files listed below.

Repository:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build

Rollout folder:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/tree/main/rollout/hatz-ai-quick-rfq-rollout

Read only these files, in this order:

1. READ ME FIRST
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/READ-ME-FIRST.md

2. Rollout build instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/README.md

3. App manifest
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/config/hatz-app-manifest.json

4. Runtime instructions
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/instructions/02-runtime-instructions.md

5. Output contract
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/instructions/03-output-contract.md

6. Output mapping
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/config/hatz-output-mapping.md

7. Example payloads
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/rollout/hatz-ai-quick-rfq-rollout/examples/hatz-input-payloads.json

Task:
Design the Hatz.ai sandbox workflow for the Quick RFQ Summary Agent.

Build requirements:
- App/workflow name: Quick RFQ Summary Agent
- Inputs:
  - `rfq_text`
  - optional `sources` list with `name`, `readable`, and `content`
- Output: exact 11-section RFQ Intake Summary
- Branching statuses:
  - Ready for Estimator Review → estimator/PM review
  - Needs Clarification → clarification review
  - Stop — Required Information Missing → escalation/missing-materials handler
- Machine-safe branch keys:
  - READY_FOR_ESTIMATOR_REVIEW
  - NEEDS_CLARIFICATION
  - STOP_REQUIRED_INFORMATION_MISSING
- Branch workflow logic on `status_key`, not on punctuation-sensitive display text. Use `display_status` only for human-readable output.
- Human review gate before any customer-facing or operational action
- Evidence capture for input, sources, summary, status, status reason, confidence, reviewer, timestamp, review decision, and workflow version

Important guardrails:
- The agent must not estimate, price, approve scope, schedule, purchase, release production, decide compliance/engineering, send customer messages, or make commitments.
- Build only for sandbox/internal QA first.
- Do not recommend broad rollout until smoke tests, QA, pilot, reviewer feedback, readiness scorecard, and go/no-go evidence are complete.

Return your answer in this exact structure:

1. Files read
- List only the files you actually read.

2. Hatz app setup
- App name.
- Inputs.
- Main instructions source.
- Output contract source.

3. Workflow design
- Step-by-step workflow from input capture to evidence record.

4. Branching rules
- Ready path.
- Needs Clarification path.
- Stop path.

5. Human review gate
- Where it goes.
- What actions it blocks.

6. Evidence capture
- Fields to store.
- Where Hatz should store or route evidence if supported.
- Include both `status_key` and `display_status` so future branch logic does not depend on punctuation.

7. Sandbox QA checklist
- Minimum tests to run before pilot.

8. Hatz support questions
- Only list items that truly need Hatz platform confirmation.

9. Next action
- Tell me exactly what to configure first in Hatz.ai.

If you need more context, ask for one specific file instead of reading the whole repo.
```

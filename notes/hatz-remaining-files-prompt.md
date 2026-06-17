# Hatz.ai Remaining Files Prompt

Use this prompt when Hatz.ai has read the first batch of raw files but still needs the remaining runtime contract, readiness, deployment, runtime-instruction, and output-contract files before giving a full transferability assessment.

```text
Yes — please fetch the remaining files before giving the full implementation assessment. Use these raw URLs:

1. Runtime contract
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/contracts/runtime_contract.py

2. Readiness evaluator
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/validation/readiness.py

3. Deployment matrix code
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/src/hatz_quick_rfq/validation/deployment.py

4. Runtime instructions source package
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md

5. Output contract source package
https://raw.githubusercontent.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build/main/docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md

After reading those, please provide the full Hatz.ai transferability assessment in this structure:

1. Directly implementable in Hatz
- Which parts can become native Hatz prompts/workflows without custom code?
- Can the 11-section output contract be used as-is?
- Can the status branches be implemented directly?

2. Needs translation from Python to Hatz-native logic
- Which pieces of `agent.py`, `hatz_adapter.py`, and validation modules should become prompt instructions, workflow branches, schema fields, or manual QA steps?
- Which code should remain external, if any?

3. Requires Hatz support confirmation
- Permissions/roles.
- Native audit logging.
- Storage and retention.
- OCR/PDF/file extraction limits.
- Observability and alerting.
- Versioning and rollback.

4. Recommended Hatz workflow
Please propose a workflow like:
Input capture → source evidence handling → RFQ summarizer → status branch → human review → evidence record → QA/pilot/go-no-go.

5. Hatz build plan
Please provide a phased plan:
- Phase 1: Native RFQ summary app/workflow.
- Phase 2: Status branching and human review gates.
- Phase 3: Evidence/readiness tracking.
- Phase 4: QA/pilot execution.
- Phase 5: Controlled rollout once unknowns are resolved.

6. Required changes to this repo
If anything would make this repo easier for Hatz to ingest or translate, list the exact recommended file changes.
```

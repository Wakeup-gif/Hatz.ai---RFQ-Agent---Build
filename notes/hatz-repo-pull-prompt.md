# Hatz.ai Repo Pull Prompt

Use this prompt when asking Hatz.ai / the Hatz implementation team to pull the GitHub repo and inspect the architecture directly.

```text
Please pull and review this GitHub repository for a Quick RFQ Summary Agent intended for Hatz.ai workflow implementation:

Repository:
https://github.com/Wakeup-gif/Hatz.ai---RFQ-Agent---Build

Goal:
Assess how much of this repo can be transferred into a Hatz.ai workspace as an RFQ intake agent/workflow for a sign and millwork business.

Important boundaries:
- The agent prepares, checks, organizes, and drafts intake summaries only.
- Humans must approve pricing, scope, schedule, compliance, production, purchasing, customer communication, and any commitments.
- Do not design the Hatz workflow to send customer messages or trigger operational actions without human review.

Please inspect these files first:
- README.md
- docs/hatz-architecture.md
- docs/hatz-readiness-gates.md
- docs/deployment/hatz-response-next-steps.md
- docs/deployment/operations-decision-matrix.md
- notes/hatz-workspace-unknowns.md
- notes/hatz-ai-discovery-prompt.md
- src/hatz_quick_rfq/agent.py
- src/hatz_quick_rfq/adapters/hatz_adapter.py
- src/hatz_quick_rfq/contracts/runtime_contract.py
- src/hatz_quick_rfq/validation/readiness.py
- src/hatz_quick_rfq/validation/deployment.py
- docs/source-package/quick-rfq-summary-app-v1.5/02-runtime-instructions.md
- docs/source-package/quick-rfq-summary-app-v1.5/03-output-contract.md

Please answer these questions:

1. Repo ingestion
- Can Hatz.ai pull or ingest this repo directly?
- If not, which files should be copied into Hatz manually?
- Does Hatz prefer a prompt-only app, workflow builder setup, API adapter, or another deployment format?

2. Agent/workflow transfer
- Can the 11-section RFQ Intake Summary contract be implemented directly in Hatz?
- Can the runtime instructions and output contract be used as the main agent instructions?
- Can the deterministic status paths be represented as workflow branches?

3. Adapter/API fit
- Can Hatz call or host Python code from `src/hatz_quick_rfq`, or should this be translated into native Hatz workflow/prompt logic?
- If Python cannot run directly, what Hatz-native structure should replace the adapter?
- Can Hatz return a response envelope with `summary_markdown`, `human_review_required`, `prohibited_authorities`, and `readiness` fields?

4. Input/source handling
- Can Hatz pass current RFQ text plus multiple source records with `name`, `content`, and `readable` fields?
- Can Hatz distinguish reviewed readable content from referenced-but-not-reviewed attachments?
- What file extraction/OCR/PDF limits apply?

5. Human review and gating
- Can Hatz force a human review step before customer communication or downstream operational action?
- Can workflows branch on `Ready for Estimator Review`, `Needs Clarification`, and `Stop — Required Information Missing`?
- Can rollout be blocked until readiness gates are complete?

6. Validation/evidence
- Can Hatz store QA, pilot, issue, and release-decision evidence records?
- Can Hatz track readiness fields and reviewer feedback?
- What evidence format does Hatz recommend?

7. Deliverables requested
Please provide:
- A recommended Hatz implementation plan.
- A list of repo files to import or translate.
- A Hatz workflow outline.
- Any unsupported repo features and suggested workarounds.
- Open questions that must be answered before production rollout.
- A recommended sandbox → QA → pilot → controlled rollout sequence.
```

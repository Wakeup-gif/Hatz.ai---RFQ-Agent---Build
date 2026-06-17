# Hatz.ai Agent Architecture

## Agent role

The Quick RFQ agent is an intake-preparation worker for sign and millwork RFQs. It converts current-interaction RFQ text and readable source content into an estimator-ready summary.

## Runtime contract

1. Accept current user text and optionally readable source files.
2. Separate reviewed content from referenced-but-not-reviewed attachments.
3. Extract known facts without using memory, file-name inference, or outside assumptions.
4. Classify missing information and stop conditions.
5. Render the required RFQ Intake Summary contract.
6. Preserve a human review gate for scope, pricing, schedule, compliance, production, purchasing, and customer communication.

## Hatz workflow fit

- Input node: pasted RFQ, email text, internal notes, or extracted document text.
- Agent node: call `hatz_quick_rfq.summarize_rfq` or the CLI wrapper.
- Review node: estimator or PM reviews the summary and decides next action.
- Evidence node: save the input, output, status, and human reviewer notes for QA and pilot scoring.

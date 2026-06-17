# READ ME FIRST — Hatz.ai Quick RFQ Rollout Package

This folder is the small handoff package for Hatz.ai. It contains only the files Hatz needs to start building the sandbox workflow.

## Read order

1. `README.md` — plain-English rollout/build instructions.
2. `config/hatz-app-manifest.json` — app name, inputs, outputs, statuses, workflow stages, and open confirmations.
3. `instructions/02-runtime-instructions.md` — paste into the Hatz app's main instruction field.
4. `instructions/03-output-contract.md` — append as the required output format/template.
5. `config/hatz-output-mapping.md` — map output sections to Hatz workflow variables and branches.
6. `examples/hatz-input-payloads.json` — use these examples to test the Hatz app/workflow.
7. `reference/hatz-transferability-assessment.md` — Hatz's implementation assessment and phased build plan.
8. `reference/hatz-readiness-gates.md` — gates required before broad rollout.
9. `reference/hatz-rollout-build-prompt.md` — prompt to ask Hatz to draft/build the sandbox workflow.

## What Hatz should build now

- Quick RFQ Summary Agent app/workflow.
- `rfq_text` input and optional `sources` input.
- 11-section RFQ Intake Summary output.
- Status branches for Ready / Needs Clarification / Stop.
- Human review gate before any customer-facing or operational action.
- Evidence capture for QA and pilot.

## What Hatz should not enable yet

Do not broadly enable this workflow or automate customer/operational actions until QA, pilot, reviewer feedback, readiness scorecard, and go/no-go evidence are complete.

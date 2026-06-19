# Hatz Quick RFQ Agent

A deterministic implementation scaffold for the Quick RFQ Summary App, aligned to Hatz.ai operating boundaries: the agent prepares, checks, organizes, and drafts RFQ intake summaries while humans approve, decide, send, buy, schedule, release, and commit.

## Run

```bash
python -m hatz_quick_rfq.cli "Customer: Acme Scope: 2 acrylic signs Dimensions: 12 in x 24 in"
```

or after installation:

```bash
hatz-quick-rfq < rfq.txt
```

## Architecture

- `src/hatz_quick_rfq/agent.py` contains deterministic extraction, status classification, stop-condition checks, and output rendering.
- `src/hatz_quick_rfq/models.py` contains the input and analysis contracts.
- `src/hatz_quick_rfq/contracts/` contains runtime contract metadata and prohibited-authority boundaries.
- `src/hatz_quick_rfq/adapters/hatz_adapter.py` maps Hatz-style payloads into summary responses for human review.
- `src/hatz_quick_rfq/cli.py` provides local execution for pilot evidence and Hatz workflow wiring.
- `docs/project-coverage.md` tracks the areas the project must cover before broad operational use.
- `docs/hatz-readiness-gates.md` defines the evidence and deployment gates required for Hatz rollout.
- `docs/deployment/hatz-response-next-steps.md` captures Hatz-side feedback and the recommended build/verify split.
- `docs/deployment/hatz-transferability-assessment.md` records Hatz.ai transferability findings and phased build plan.
- `docs/deployment/hatz-rollout-instructions.md` provides plain-English Hatz build, QA, pilot, and rollout instructions.
- `rollout/hatz-ai-quick-rfq-rollout.zip` is the compact Hatz.ai handoff zip; start with `rollout/hatz-ai-quick-rfq-rollout/READ-ME-FIRST.md`.
- `docs/repo-audit-and-cleanup.md` explains the repo layers, cleanup decisions, and keep/remove policy.
- `framework/agent-blueprint/` contains reusable structure for reproducing future Hatz agents.
- `docs/hatz-app-manifest.json`, `docs/hatz-output-mapping.md`, and `examples/hatz-input-payloads.json` provide Hatz setup artifacts.
- `notes/hatz-workspace-unknowns.md` keeps customer/Hatz-specific unknowns off to the side until project owners provide answers.
- `notes/hatz-ai-discovery-prompt.md` provides a ready-to-send discovery prompt for scoping Hatz workspace transfer.
- `notes/hatz-repo-pull-prompt.md` provides a prompt for asking Hatz to pull/review the GitHub repo directly.
- `notes/hatz-raw-file-review-prompt.md` provides raw GitHub URLs when rendered `blob` pages do not scrape cleanly.
- `notes/hatz-remaining-files-prompt.md` asks Hatz to fetch the final raw files before producing a transferability assessment.
- `notes/hatz-rollout-build-prompt.md` asks Hatz to build the sandbox workflow while keeping rollout gated.
- `notes/hatz-rollout-folder-read-prompt.md` tells Hatz to read the GitHub rollout folder directly when uploads are unavailable.
- `notes/hatz-token-safe-build-prompt.md` keeps Hatz focused on the rollout files to reduce token usage.
- `notes/hatz-agent-build-lessons.md` captures Hatz/Codex lessons learned for future agent, workflow, and app builds.
- `notes/hatz-manual-workflow-wiring-guide.md` gives the manual Hatz UI wiring steps for the RFQ workflow.
- `tests/test_agent.py` verifies stop conditions, human-review boundaries, adapter metadata, and attachment handling.

## Boundaries

The agent does not estimate, price, approve scope, approve engineering/compliance, schedule, purchase, release production, send customer messages, or make commitments.

## Project coverage

The build needs to cover product authority, runtime behavior, Hatz workflow integration, guardrails, validation evidence, deployment operations, and future parser depth. See `docs/project-coverage.md` for the full roadmap and `docs/hatz-readiness-gates.md` for rollout gate criteria.

## Readiness gate

```bash
python -m hatz_quick_rfq.cli readiness
```

The readiness command reports missing validation evidence and deployment decisions. The agent should not be broadly enabled in Hatz until the report returns `ready_for_hatz: true`.

## Hatz.ai setup artifacts

Start Hatz implementation with `docs/deployment/hatz-rollout-instructions.md` and `docs/hatz-app-manifest.json`, copy `02-runtime-instructions.md` and `03-output-contract.md` into the Hatz app instructions/output template, use `docs/hatz-output-mapping.md` for workflow variables, and test with `examples/hatz-input-payloads.json`.

## Hatz.ai rollout zip

Give Hatz.ai `rollout/hatz-ai-quick-rfq-rollout.zip`. After unzipping, read `READ-ME-FIRST.md`, then follow `README.md`, `config/hatz-app-manifest.json`, `instructions/02-runtime-instructions.md`, `instructions/03-output-contract.md`, `config/hatz-output-mapping.md`, and `examples/hatz-input-payloads.json`.

## Repository layers

Use `docs/repo-audit-and-cleanup.md` for the cleanup/audit record. The active implementation is in `src/hatz_quick_rfq/`, source authority is in `docs/source-package/quick-rfq-summary-app-v1.5/`, Hatz handoff is in `rollout/`, and reusable future-agent patterns are in `framework/agent-blueprint/`.

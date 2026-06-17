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
- `notes/hatz-workspace-unknowns.md` keeps customer/Hatz-specific unknowns off to the side until project owners provide answers.
- `notes/hatz-ai-discovery-prompt.md` provides a ready-to-send discovery prompt for scoping Hatz workspace transfer.
- `notes/hatz-repo-pull-prompt.md` provides a prompt for asking Hatz to pull/review the GitHub repo directly.
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

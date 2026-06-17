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
- `src/hatz_quick_rfq/cli.py` provides local execution for pilot evidence and Hatz workflow wiring.
- `tests/test_agent.py` verifies stop conditions, human-review boundaries, and attachment handling.

## Boundaries

The agent does not estimate, price, approve scope, approve engineering/compliance, schedule, purchase, release production, send customer messages, or make commitments.

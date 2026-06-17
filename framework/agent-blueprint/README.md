# Agent Blueprint Framework

Use this blueprint to reproduce the same safe-agent pattern for future Hatz.ai agents.

## Required layers for a new agent

1. **Source authority**
   - Store original prompt/instruction/source package under `docs/source-package/<agent-name>/`.
   - Treat source files as read-only product authority.

2. **Runtime package**
   - Add deterministic or testable implementation under `src/<agent_package>/`.
   - Keep platform adapters separate from core behavior.
   - Keep prohibited-authority and human-review boundaries explicit.

3. **Contracts**
   - Define runtime contract, output contract, inputs, outputs, status values, and human review gate.
   - Include a manifest similar to `docs/hatz-app-manifest.json`.

4. **Validation**
   - Add readiness gates for smoke, QA, pilot, issue disposition, readiness scorecard, and go/no-go decision.
   - Add evidence record structure.

5. **Hatz handoff**
   - Create a compact `rollout/<agent-name>/` folder.
   - Include `READ-ME-FIRST.md`, instructions, output contract, app manifest, output mapping, examples, readiness gates, and rollout prompt.
   - Zip the rollout folder and add a checksum.

6. **Tests**
   - Cover stop conditions, ready paths, source/attachment boundaries, adapter envelope, readiness gates, and evidence writing.

## Human-authority rule

Every agent must explicitly say what it cannot do. For operational agents, humans should retain authority for approvals, customer communication, pricing, scheduling, purchasing, release, and commitments unless a human owner explicitly approves otherwise.

## Suggested new-agent structure

```text
src/<agent_package>/
  agent.py
  models.py
  adapters/
  contracts/
  validation/

docs/source-package/<agent-name>/
docs/deployment/
notes/
examples/
evidence/
rollout/<agent-name>/
tests/
```

## Cycle-control rule for future agents

When creating new agents, workflows, or apps, define both a human-readable display value and a machine-safe key for every workflow branch.

- Use `display_status` for user-facing output, reports, and summaries.
- Use `status_key` for workflow routing, evidence records, tests, and platform branching.
- Keep `status_key` ASCII-only, uppercase, and underscore-separated, for example `STOP_REQUIRED_INFORMATION_MISSING`.
- Do not branch on punctuation-sensitive labels such as text containing em dashes, smart quotes, slashes, or long prose.
- Include the `status_key` values in the manifest, output mapping, rollout README, prompts, tests, and evidence schema.

This prevents repeated clarification cycles where a platform or model changes punctuation in a display label and breaks branch routing.

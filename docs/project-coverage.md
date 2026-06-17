# Project Coverage Roadmap

The project needs to cover the areas below to become a complete Hatz.ai-ready RFQ intake agent. The current implementation starts the runtime agent and adapter layer; the remaining work is validation depth, pilot evidence, and platform deployment wiring.

## 1. Product authority and source traceability

- Preserve the v1.5 source package as read-only authority.
- Keep product frameworks for status decisions, missing information, scope decomposition, and source evidence traceable to source files.
- Avoid changing business behavior without updating source authority and tests.

## 2. Runtime agent behavior

- Capture only current-interaction RFQ content.
- Separate reviewed readable content from referenced-but-not-reviewed attachments.
- Extract known facts without memory, outside assumptions, or file-name inference.
- Decompose multi-item RFQs into item/scope groups.
- Classify critical versus helpful missing information.
- Choose one status: `Ready for Estimator Review`, `Needs Clarification`, or `Stop — Required Information Missing`.
- Render the fixed RFQ Intake Summary output contract.

## 3. Hatz.ai adapter and workflow integration

- Map Hatz input payloads into agent text and readable source records.
- Return a platform envelope that includes the Markdown summary, source authority, prohibited authorities, and human-review requirement.
- Route outputs to an estimator or PM review step before customer communication or operational action.
- Record input, output, status, reviewer, and issue metadata for evidence.

## 4. Guardrails and human authority boundaries

- Prevent estimating, pricing, scope approval, scheduling promises, purchasing approval, production release, compliance determinations, engineering approval, and customer-send behavior.
- Keep the agent in a prepare/check/organize/draft role.
- Require human review for all commitments and operational decisions.

## 5. Validation and evidence

- Run smoke tests before the full QA pack.
- Execute the full QA pack against representative RFQs.
- Log failures and patch only observed failures.
- Retest patched behavior.
- Run an internal pilot with selected samples.
- Produce readiness scorecards and go/no-go records before broad use.

## 6. Deployment operations

- Decide Hatz routing, permissions, storage, observability, and retention settings.
- Confirm how readable attachment text is extracted before it reaches the agent.
- Define audit logging for source names, reviewed content flags, outputs, and reviewer decisions.
- Maintain rollback and version/changelog procedures.

## 7. Future implementation depth

- Add stronger structured parsers for multi-item signage and millwork requests.
- Add QA fixture generation from the source QA pack.
- Add evidence record writers for QA and pilot runs.
- Add Hatz-specific deployment configuration once platform conventions are known.

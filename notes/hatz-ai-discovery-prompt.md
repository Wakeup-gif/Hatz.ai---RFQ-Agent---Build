# Hatz.ai Discovery Prompt

Use this prompt with Hatz.ai / the Hatz implementation team to scope what can be built when transferring this Quick RFQ architecture into the Hatz workspace.

```text
We have a Quick RFQ Summary Agent architecture ready for Hatz.ai implementation planning. The agent is designed for sign and millwork RFQ intake. It prepares, checks, organizes, and drafts estimator-ready intake summaries only. Humans must retain authority for pricing, scope approval, schedule commitments, purchasing, production release, compliance/engineering decisions, and customer communication.

Current architecture/package includes:
- Deterministic RFQ summarizer that renders an 11-section RFQ Intake Summary.
- Hatz-facing adapter concept that accepts current-interaction text and readable source records.
- Runtime guardrails and prohibited-authority list.
- Readiness gates for smoke tests, QA pack, pilot run, reviewer feedback, readiness scorecard, and go/no-go decision.
- Evidence record structure for QA runs, pilot runs, issues, and release decisions.
- Deployment operations matrix for routing, permissions, storage/retention, observability, attachment extraction, audit logging, and rollback/versioning.

Please help us scope what can be built inside our Hatz.ai workspace from this architecture.

Questions:

1. Routing and workflow
- What Hatz trigger or workflow pattern should receive RFQ input?
- Can Hatz route outputs to a human estimator/PM review step before any customer-facing action?
- Can Hatz branch routing based on status: Ready for Estimator Review, Needs Clarification, or Stop — Required Information Missing?
- How should Stop or Needs Clarification outputs escalate?

2. Input and source handling
- What input types can Hatz pass into the agent: pasted text, email body, uploaded file text, extracted PDF text, OCR text, drawing/schedule text?
- Which attachment/file types can Hatz extract into readable text before calling the agent?
- What are file size, page count, timeout, OCR, and parser limits?
- Can each source be passed with name, readable flag, and extracted content separately?

3. Permissions and human review
- What roles/groups should be configured for requester, estimator, PM, admin, and auditor?
- Can Hatz enforce that only humans approve pricing, scope, scheduling, purchasing, production release, compliance, and customer communication?
- Can generated summaries be locked from customer-send until reviewed?

4. Storage, retention, and audit
- Where should RFQ inputs, generated summaries, evidence records, reviewer decisions, and issue logs be stored?
- What retention policy should apply to raw input, extracted source text, generated summaries, and QA/pilot evidence?
- Can Hatz capture audit fields: source names, readable/reviewed flags, status, reviewer, timestamp, readiness status, and release decision?
- What redaction rules are required for logs and observability?

5. Observability and reporting
- What Hatz logging/metrics tools are available?
- Can we track status counts, stop-condition counts, missing-information categories, review outcomes, and error rates?
- Who should receive alerts when evidence writing fails, unreadable files are submitted, or Stop conditions spike?

6. Readiness and rollout
- Can Hatz represent readiness gates for smoke tests, QA pack, issue disposition, pilot run, reviewer feedback, readiness scorecard, and go/no-go decision?
- Can rollout be blocked until all required evidence and deployment decisions are complete?
- What is the recommended controlled pilot setup in Hatz?

7. Versioning and rollback
- How does Hatz version agent instructions, workflows, adapters, and deployment configuration?
- Can we map each generated summary to the agent/workflow version that produced it?
- What rollback mechanism should we use if QA or pilot finds an issue?

Deliverables requested from Hatz:
- Recommended Hatz workflow design.
- Required configuration values and workspace assumptions.
- Supported input/attachment extraction capabilities and limits.
- Permission model recommendation.
- Storage/retention/audit recommendation.
- Observability/logging recommendation.
- Rollout plan from sandbox to QA to pilot to controlled release.
- List of anything in this architecture that Hatz cannot support directly and suggested alternatives.
```

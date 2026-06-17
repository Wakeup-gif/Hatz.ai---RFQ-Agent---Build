# Hatz Output Mapping

This maps the required RFQ Intake Summary output contract into Hatz workflow variables. The complete Markdown summary should always be preserved as `summary_markdown` for human review.

| Output contract section | Suggested Hatz variable | Use |
|---|---|---|
| 1. Status | `status`, `status_reason` | Branch workflow into Ready, Clarification, or Stop path. |
| 2. Plain-English Request Summary | `request_summary` | Human review overview. |
| 3. Sources Reviewed | `reviewed_sources`, `referenced_not_reviewed` | Audit/source evidence tracking. |
| 4. Known Facts | `known_facts` | Estimator/PM review context. |
| 5. Missing Information | `critical_missing`, `helpful_missing` | Clarification and Stop handling. |
| 6. Unclear or Conflicting Information | `unclear_conflicts` | Clarification routing. |
| 7. Stop Conditions | `stop_condition_present`, `stop_condition_details` | Stop/escalation branch. |
| 8. Suggested Follow-Up Questions | `customer_questions`, `internal_questions` | Draft questions for human review before sending. |
| 9. Estimator Notes | `estimator_notes` | Internal-only review notes. |
| 10. Confidence | `confidence`, `confidence_reason` | Reviewer risk signal. |
| 11. Human Review Gate | `human_review_required` | Must remain `true` before downstream action. |

## Branching map

| Status | Hatz path | Required gate |
|---|---|---|
| `Ready for Estimator Review` | Route to estimator/PM review. | Human review before pricing or customer communication. |
| `Needs Clarification` | Route to clarification drafting/review. | Human review before any clarification is sent. |
| `Stop — Required Information Missing` | Route to stop/escalation handler. | Human review before restarting intake or requesting missing materials. |

## Fields to preserve for evidence

- `input_text`
- `sources`
- `summary_markdown`
- `status`
- `status_reason`
- `confidence`
- `reviewer`
- `review_decision`
- `review_timestamp`
- `agent_or_workflow_version`

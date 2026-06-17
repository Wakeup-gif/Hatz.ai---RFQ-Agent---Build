"""Traceable runtime contract for Hatz Quick RFQ deployments."""

PROHIBITED_AUTHORITIES = (
    "estimating",
    "pricing",
    "scope approval",
    "schedule commitments",
    "compliance determinations",
    "engineering approval",
    "production release",
    "purchasing approval",
    "customer-send behavior",
)

HUMAN_REVIEW_GATE = (
    "A human must review and approve scope, pricing, schedule, compliance, "
    "production, purchasing, customer communication, and any commitments before action."
)

RUNTIME_CONTRACT = {
    "agent_name": "Quick RFQ Summary Agent",
    "platform_alignment": "Hatz.ai",
    "source_authority": "docs/source-package/quick-rfq-summary-app-v1.5/",
    "current_interaction_only": True,
    "must_not_assume_from_file_names": True,
    "prohibited_authorities": PROHIBITED_AUTHORITIES,
    "human_review_gate": HUMAN_REVIEW_GATE,
    "required_output_sections": tuple(str(n) for n in range(1, 12)),
}

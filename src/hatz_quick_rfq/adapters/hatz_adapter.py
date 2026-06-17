"""Hatz-facing adapter for the Quick RFQ summarizer.

This adapter keeps the platform payload explicit and auditable: Hatz can route
input text and readable extracted file text into the deterministic agent, then
store the returned summary and contract metadata for human review.
"""

from __future__ import annotations

from typing import Any

from hatz_quick_rfq.agent import summarize_rfq
from hatz_quick_rfq.contracts import RUNTIME_CONTRACT
from hatz_quick_rfq.models import RfqSource
from hatz_quick_rfq.validation import evaluate_hatz_readiness


def build_hatz_response(payload: dict[str, Any]) -> dict[str, Any]:
    """Build a Hatz-compatible response envelope from a platform payload.

    Expected payload keys:
    - `text`: pasted RFQ/email/note content for the current interaction.
    - `sources`: optional list of `{name, content, readable}` dictionaries.
    """

    sources = tuple(
        RfqSource(
            name=str(source.get("name", "Unnamed source")),
            content=str(source.get("content", "")),
            readable=bool(source.get("readable", True)),
        )
        for source in payload.get("sources", ())
    )
    summary = summarize_rfq(text=str(payload.get("text", "")), sources=sources)
    readiness = evaluate_hatz_readiness(
        evidence=payload.get("evidence"),
        deployment_decisions=payload.get("deployment_decisions"),
    )
    return {
        "agent": RUNTIME_CONTRACT["agent_name"],
        "platform_alignment": RUNTIME_CONTRACT["platform_alignment"],
        "summary_markdown": summary,
        "human_review_required": True,
        "prohibited_authorities": RUNTIME_CONTRACT["prohibited_authorities"],
        "source_authority": RUNTIME_CONTRACT["source_authority"],
        "readiness": readiness.to_dict(),
    }

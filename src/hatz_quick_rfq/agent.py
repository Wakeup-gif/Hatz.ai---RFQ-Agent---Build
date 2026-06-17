"""Deterministic Quick RFQ summary agent aligned to Hatz.ai boundaries.

The module intentionally prepares, checks, organizes, and drafts only. It does
not price, approve, schedule, purchase, release production, or make customer
commitments.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from .models import RfqAnalysis, RfqIntake, RfqSource, UNKNOWN

STATUS_READY = "Ready for Estimator Review"
STATUS_CLARIFY = "Needs Clarification"
STATUS_STOP = "Stop — Required Information Missing"

FACT_FIELDS = (
    "Customer",
    "Project name",
    "Project location",
    "Requested scope",
    "Quantity",
    "Dimensions",
    "Materials",
    "Finish / color",
    "Install / delivery scope",
    "Deadline / urgency",
    "Attachments / drawings / schedules",
    "Prior quote / revision / addendum references",
)

ATTACHMENT_TERMS = re.compile(
    r"\b(attachment|attached|drawing|drawings|schedule|photo|survey|addendum|artwork|file|pdf|dwg|prior quote|requote)\b",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|^\s*(customer|project|scope|quantity|dimensions|materials|finish)\s*:?\s*$", re.I | re.M)

PATTERNS: dict[str, tuple[re.Pattern[str], ...]] = {
    "Customer": (re.compile(r"\b(?:customer|client)\s*[:\-]\s*(.+)", re.I),),
    "Project name": (re.compile(r"\bproject(?: name)?\s*[:\-]\s*(.+)", re.I),),
    "Project location": (re.compile(r"\b(?:project )?(?:location|site|address)\s*[:\-]\s*(.+)", re.I),),
    "Quantity": (re.compile(r"\b(?:qty|quantity)\s*[:\-]?\s*([\w\d, ]+)", re.I), re.compile(r"\b(\d+)\s+(?:ea|each|signs?|cabinets?|letters?|panels?|rooms?)\b", re.I)),
    "Dimensions": (re.compile(r"\b(?:dimensions?|size)\s*[:\-]\s*(.+)", re.I), re.compile(r"\b\d+(?:\.\d+)?\s*(?:in|inch|inches|ft|feet|'|\")\s*[x×]\s*\d+(?:\.\d+)?\s*(?:in|inch|inches|ft|feet|'|\")?", re.I)),
    "Materials": (re.compile(r"\bmaterials?\s*[:\-]\s*(.+)", re.I), re.compile(r"\b(acrylic|aluminum|steel|wood|vinyl|pvc|dibond|sintra|laminate|millwork)\b.+", re.I)),
    "Finish / color": (re.compile(r"\b(?:finish|color|colour)\s*[:\-]\s*(.+)", re.I),),
    "Deadline / urgency": (re.compile(r"\b(?:deadline|due|needed by|need by|required by|asap|rush)\b[:\-]?\s*(.*)", re.I),),
}


def summarize_rfq(text: str = "", sources: Iterable[RfqSource] | None = None) -> str:
    """Return the required RFQ Intake Summary Markdown for current input only."""

    intake = RfqIntake(text=text or "", sources=tuple(sources or ()))
    return render_contract(analyze(intake))


def analyze(intake: RfqIntake) -> RfqAnalysis:
    content_parts = [intake.text.strip(), *(s.content.strip() for s in intake.sources if s.readable)]
    content = "\n".join(part for part in content_parts if part)
    readable = bool(content.strip()) and bool(PLACEHOLDER_RE.sub("", content).strip())

    reviewed = tuple(s.name for s in intake.sources if s.readable and s.content.strip())
    if intake.text.strip():
        reviewed = ("Pasted input",) + reviewed
    referenced = tuple(s.name for s in intake.sources if not s.readable)
    if ATTACHMENT_TERMS.search(content) and not any("Attachment mentioned" in r for r in referenced):
        referenced += ("Attachment mentioned but contents not provided.",)

    facts = {field: _extract_field(field, content) for field in FACT_FIELDS}
    facts["Requested scope"] = _extract_scope(content)
    if facts["Quantity"] == UNKNOWN:
        facts["Quantity"] = _extract_quantity_from_scope(facts["Requested scope"])
    facts["Install / delivery scope"] = _extract_install(content)
    facts["Attachments / drawings / schedules"] = _extract_attachments(content, referenced)
    facts["Prior quote / revision / addendum references"] = _extract_prior(content)

    critical_missing = []
    if not readable:
        critical_missing.append("Readable RFQ scope content")
    for field in ("Requested scope", "Quantity", "Dimensions"):
        if facts[field] == UNKNOWN:
            critical_missing.append(field.lower())
    if referenced and (facts["Requested scope"] == UNKNOWN or "drawing" in content.lower() or "schedule" in content.lower()):
        critical_missing.append("Referenced attachment contents")

    helpful_missing = [field.lower() for field in ("Materials", "Finish / color", "Install / delivery scope", "Deadline / urgency") if facts[field] == UNKNOWN]
    unclear = _find_conflicts(content)

    stop = not readable or len(critical_missing) >= 3 or (referenced and facts["Requested scope"] == UNKNOWN)
    status = STATUS_STOP if stop else STATUS_CLARIFY if critical_missing or unclear else STATUS_READY
    reason = _status_reason(status, critical_missing, unclear)
    summary = _plain_summary(facts)
    confidence = "Cannot Determine" if not readable else "Low" if stop or len(critical_missing) >= 2 else "Medium" if critical_missing or helpful_missing else "High"

    return RfqAnalysis(
        status=status,
        status_reason=reason,
        summary=summary,
        reviewed_sources=reviewed,
        referenced_not_reviewed=referenced,
        facts=facts,
        critical_missing=tuple(dict.fromkeys(critical_missing)) or ("None identified from provided information.",),
        helpful_missing=tuple(dict.fromkeys(helpful_missing)) or ("None identified from provided information.",),
        unclear_conflicts=tuple(unclear) or ("None identified from provided information.",),
        stop_condition=stop,
        stop_details=reason if stop else "None identified from provided information.",
        customer_questions=_questions(tuple(dict.fromkeys(critical_missing + helpful_missing)), external=True),
        internal_questions=_questions(tuple(dict.fromkeys(critical_missing)), external=False),
        estimator_notes=("Human review is required before scope, pricing, schedule, compliance, production, purchasing, or customer commitments.",),
        confidence=confidence,
        confidence_reason="Confidence is based only on readable information supplied in the current interaction.",
    )


def render_contract(a: RfqAnalysis) -> str:
    def bullets(items): return "\n".join(f"- {i}" for i in items)
    def numbered(items): return "\n".join(f"{n}. {i}" for n, i in enumerate(items, 1)) or "None identified from provided information."
    reviewed = bullets(a.reviewed_sources) if a.reviewed_sources else "- Source names not provided. Summary is based only on pasted input."
    referenced = bullets(a.referenced_not_reviewed) if a.referenced_not_reviewed else "- None identified from provided information."
    facts = "\n\n".join(f"{k}:\n{v}" for k, v in a.facts.items())
    return f"""# RFQ Intake Summary

## 1. Status

Status:
{a.status}

Reason:
{a.status_reason}

## 2. Plain-English Request Summary

{a.summary}

## 3. Sources Reviewed

Reviewed content:
{reviewed}

Referenced but not reviewed:
{referenced}

## 4. Known Facts

{facts}

## 5. Missing Information

Critical missing information:
{bullets(a.critical_missing)}

Helpful but noncritical missing information:
{bullets(a.helpful_missing)}

## 6. Unclear or Conflicting Information

{bullets(a.unclear_conflicts)}

## 7. Stop Conditions

Stop condition present:
{'Yes' if a.stop_condition else 'No'}

Stop condition details:
{a.stop_details}

## 8. Suggested Follow-Up Questions

Customer-facing clarification questions:
{numbered(a.customer_questions)}

Internal questions for estimator / PM:
{numbered(a.internal_questions)}

## 9. Estimator Notes

{bullets(a.estimator_notes)}

## 10. Confidence

Confidence:
{a.confidence}

Reason:
{a.confidence_reason}

## 11. Human Review Gate

This summary is for internal intake support only. A human must review and approve scope, pricing, schedule, compliance, production, purchasing, customer communication, and any commitments before action.
"""


def _extract_field(field: str, content: str) -> str:
    for pattern in PATTERNS.get(field, ()): 
        match = pattern.search(content)
        if match:
            value = match.group(1) if match.groups() else match.group(0)
            return _clean(value)
    return UNKNOWN


def _extract_quantity_from_scope(scope: str) -> str:
    if scope == UNKNOWN:
        return UNKNOWN
    match = re.search(r"\b(\d+)\s+", scope)
    return match.group(1) if match else UNKNOWN


def _extract_scope(content: str) -> str:
    m = re.search(r"\b(?:scope|request|rfq|quote for|need(?: a quote for)?)\s*[:\-]?\s*(.+)", content, re.I)
    if m: return _clean(m.group(1))
    m = re.search(r"\b(signs?|channel letters?|cabinet|monument|vinyl|graphics|millwork|install|survey|service)\b.+", content, re.I)
    return _clean(m.group(0)) if m else UNKNOWN


def _extract_install(content: str) -> str:
    m = re.search(r"\b(install(?:ation)?|delivery|ship|pickup|survey|service)\b[^.\n]*", content, re.I)
    return _clean(m.group(0)) if m else UNKNOWN


def _extract_attachments(content: str, referenced: tuple[str, ...]) -> str:
    if referenced: return "; ".join(referenced)
    return _clean(ATTACHMENT_TERMS.search(content).group(0)) if ATTACHMENT_TERMS.search(content) else UNKNOWN


def _extract_prior(content: str) -> str:
    m = re.search(r"\b(prior quote|requote|revision|rev\.?|addendum)\b[^.\n]*", content, re.I)
    return _clean(m.group(0)) if m else UNKNOWN


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip(" -:\t\r\n"))[:300] or UNKNOWN


def _find_conflicts(content: str) -> list[str]:
    conflicts = []
    if re.search(r"\b(?:or|maybe|possibly|tbd|to be determined|not sure)\b", content, re.I):
        conflicts.append("Input contains tentative or unresolved language that needs confirmation.")
    return conflicts


def _status_reason(status: str, missing: list[str], unclear: list[str]) -> str:
    if status == STATUS_READY:
        return "Readable RFQ scope details are present and no critical stop condition was detected."
    if status == STATUS_STOP:
        return "Required information is missing or source material is not readable enough for meaningful intake review."
    parts = []
    if missing: parts.append("Missing: " + ", ".join(dict.fromkeys(missing)))
    if unclear: parts.append("Unclear/conflicting information is present")
    return "; ".join(parts) + "."


def _plain_summary(facts: dict[str, str]) -> str:
    if facts["Requested scope"] == UNKNOWN:
        return "The provided information does not include enough readable RFQ scope content to summarize the request."
    qty = "" if facts["Quantity"] == UNKNOWN else f" Quantity: {facts['Quantity']}."
    return f"The customer appears to be requesting estimator intake review for: {facts['Requested scope']}.{qty}"


def _questions(missing: tuple[str, ...], external: bool) -> tuple[str, ...]:
    if not missing or missing == ("None identified from provided information.",):
        return ("None identified from provided information.",)
    prefix = "Please confirm" if external else "Should the estimator proceed without"
    return tuple(f"{prefix} {item}?" for item in missing[:3])

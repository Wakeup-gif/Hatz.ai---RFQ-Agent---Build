"""Data contracts for the Hatz Quick RFQ agent."""

from dataclasses import dataclass, field

UNKNOWN = "Cannot determine from provided information."


@dataclass(frozen=True)
class RfqSource:
    """A single user-provided source in the current interaction."""

    name: str
    content: str
    readable: bool = True


@dataclass(frozen=True)
class RfqIntake:
    """Input payload for deterministic RFQ summarization."""

    text: str = ""
    sources: tuple[RfqSource, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class RfqAnalysis:
    """Structured intermediate analysis used to render the contract."""

    status: str
    status_reason: str
    summary: str
    reviewed_sources: tuple[str, ...]
    referenced_not_reviewed: tuple[str, ...]
    facts: dict[str, str]
    critical_missing: tuple[str, ...]
    helpful_missing: tuple[str, ...]
    unclear_conflicts: tuple[str, ...]
    stop_condition: bool
    stop_details: str
    customer_questions: tuple[str, ...]
    internal_questions: tuple[str, ...]
    estimator_notes: tuple[str, ...]
    confidence: str
    confidence_reason: str

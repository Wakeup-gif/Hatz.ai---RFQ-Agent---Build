"""Evidence record writer for QA, pilot, issue, and release-gate artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ALLOWED_EVIDENCE_TYPES = {"qa-run", "pilot-run", "issue", "release-decision"}
DEFAULT_EVIDENCE_DIRS = {
    "qa-run": "qa-runs",
    "pilot-run": "pilot-runs",
    "issue": "issues",
    "release-decision": "release-decisions",
}


@dataclass(frozen=True)
class EvidenceRecord:
    """Serializable validation evidence for human-reviewed rollout gates."""

    evidence_type: str
    title: str
    summary: str
    reviewer: str = "Human reviewer not recorded"
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    metadata: dict[str, Any] = field(default_factory=dict)


def write_evidence_record(record: EvidenceRecord, root: str | Path = "evidence") -> Path:
    """Write a timestamped evidence JSON record and return its path."""

    if record.evidence_type not in ALLOWED_EVIDENCE_TYPES:
        allowed = ", ".join(sorted(ALLOWED_EVIDENCE_TYPES))
        raise ValueError(f"Unsupported evidence type '{record.evidence_type}'. Expected one of: {allowed}.")

    destination = Path(root) / DEFAULT_EVIDENCE_DIRS[record.evidence_type]
    destination.mkdir(parents=True, exist_ok=True)
    safe_title = "".join(ch if ch.isalnum() else "-" for ch in record.title.lower()).strip("-")
    filename = f"{record.created_at.replace(':', '-').replace('+', 'Z')}-{safe_title or 'record'}.json"
    path = destination / filename
    path.write_text(json.dumps(asdict(record), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path

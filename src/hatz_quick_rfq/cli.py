"""Command line entry point for the Hatz Quick RFQ agent."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .agent import summarize_rfq
from .models import RfqSource
from .validation import (
    EvidenceRecord,
    deployment_operations_matrix,
    evaluate_hatz_readiness,
    unanswered_deployment_variables,
    write_evidence_record,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a Hatz-aligned RFQ intake summary.")
    subparsers = parser.add_subparsers(dest="command")

    summarize_parser = subparsers.add_parser("summarize", help="Render an RFQ Intake Summary.")
    summarize_parser.add_argument("input", nargs="?", help="RFQ text. If omitted, stdin is used.")
    summarize_parser.add_argument("--file", action="append", default=[], help="Readable source file to include in current interaction.")

    subparsers.add_parser("readiness", help="Print the current empty-evidence Hatz readiness gate report.")
    subparsers.add_parser("deployment-matrix", help="Print buildable deployment operations and unanswered variables.")

    evidence_parser = subparsers.add_parser("record-evidence", help="Write a validation evidence JSON record.")
    evidence_parser.add_argument("evidence_type", choices=["qa-run", "pilot-run", "issue", "release-decision"])
    evidence_parser.add_argument("title")
    evidence_parser.add_argument("summary")
    evidence_parser.add_argument("--reviewer", default="Human reviewer not recorded")
    evidence_parser.add_argument("--status", default="draft")
    evidence_parser.add_argument("--root", default="evidence")

    # Backward-compatible default: `hatz-quick-rfq "RFQ text"` still summarizes.
    raw_args = list(argv if argv is not None else sys.argv[1:])
    commands = {"summarize", "readiness", "deployment-matrix", "record-evidence"}
    if raw_args and raw_args[0] not in commands and not raw_args[0].startswith("-"):
        raw_args.insert(0, "summarize")

    args = parser.parse_args(raw_args)
    if args.command == "summarize":
        return _summarize_from_args(args)
    if args.command == "readiness":
        print(json.dumps(evaluate_hatz_readiness().to_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "deployment-matrix":
        print(json.dumps({
            "operations": deployment_operations_matrix(),
            "unanswered_variables": unanswered_deployment_variables(),
        }, indent=2, sort_keys=True))
        return 0
    if args.command == "record-evidence":
        record = EvidenceRecord(
            evidence_type=args.evidence_type,
            title=args.title,
            summary=args.summary,
            reviewer=args.reviewer,
            status=args.status,
        )
        print(write_evidence_record(record, root=args.root))
        return 0
    parser.error(f"Unsupported command: {args.command}")
    return 2


def _summarize_from_args(args: argparse.Namespace) -> int:
    sources = []
    for name in args.file:
        path = Path(name)
        sources.append(RfqSource(name=str(path), content=path.read_text(encoding="utf-8"), readable=True))

    text = args.input if args.input is not None else sys.stdin.read()
    sys.stdout.write(summarize_rfq(text=text, sources=sources))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

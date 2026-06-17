"""Command line entry point for the Hatz Quick RFQ agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .agent import summarize_rfq
from .models import RfqSource


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a Hatz-aligned RFQ intake summary.")
    parser.add_argument("input", nargs="?", help="RFQ text. If omitted, stdin is used.")
    parser.add_argument("--file", action="append", default=[], help="Readable source file to include in current interaction.")
    args = parser.parse_args(argv)

    sources = []
    for name in args.file:
        path = Path(name)
        sources.append(RfqSource(name=str(path), content=path.read_text(encoding="utf-8"), readable=True))

    text = args.input if args.input is not None else sys.stdin.read()
    sys.stdout.write(summarize_rfq(text=text, sources=sources))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

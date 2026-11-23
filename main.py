#!/usr/bin/env python3
"""One-line roast of the gadget I use every day: my phone.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt as exactly one line
(1-200 chars, no trailing newline) after validating it.
"""

import os
import sys


ROAST = (
    "My phone updates itself at 3am, restarts, then asks if I enjoyed "
    "the update \u2014 as if it didn't just eat my alarm."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


class LineCheck:
    """One named check on the roast line; reports a reason when it fails."""

    def __init__(self, name, test):
        self.name = name
        self.test = test

    def run(self, line):
        if not self.test(line):
            raise ValueError(f"roast failed check {self.name!r}")


class RoastValidator:
    """Runs every gate the competition puts on the entry line."""

    CHECKS = [
        LineCheck("non-blank", lambda line: line.strip() != ""),
        LineCheck(
            "length-in-range",
            lambda line: MIN_LENGTH <= len(line) <= MAX_LENGTH,
        ),
        LineCheck(
            "single-line",
            lambda line: "\n" not in line and "\r" not in line,
        ),
    ]

    def validate(self, line):
        for check in self.CHECKS:
            check.run(line)


def resolve_output_dir():
    """Base dir for the entry file: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def output_path():
    """Destination file: $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    return os.path.join(resolve_output_dir(), "entry.txt")


def main():
    RoastValidator().validate(ROAST)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())

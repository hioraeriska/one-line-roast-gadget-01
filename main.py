#!/usr/bin/env python3
"""One-line roast for make.fun: a single line roasting a daily gadget.

The line is fixed text. Before it is written out, it must pass three
checks: it is not blank, it fits the 1-200 character window, and it is
exactly one line.
"""
import os

LINE = (
    "My phone updates itself at 3am, restarts, then asks if I enjoyed "
    "the update \u2014 as if it didn't just eat my alarm."
)

MIN_CHARS = 1
MAX_CHARS = 200
LINE_BREAKS = "\r\n"


class LineValidator:
    """Runs every rule the bounty places on the roast line."""

    def __init__(self, text):
        self.text = text

    def _require_content(self):
        if not self.text or not self.text.strip():
            raise ValueError("roast must contain non-whitespace text")

    def _require_length(self):
        size = len(self.text)
        if size < MIN_CHARS or size > MAX_CHARS:
            raise ValueError(
                "roast must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, size)
            )

    def _require_single_line(self):
        if any(ch in self.text for ch in LINE_BREAKS):
            raise ValueError("roast must be exactly one line")

    def validate(self):
        self._require_content()
        self._require_length()
        self._require_single_line()
        return self.text


def write_entry(line, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return target


def main():
    line = LineValidator(LINE).validate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    write_entry(line, out_dir)


if __name__ == "__main__":
    main()

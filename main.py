#!/usr/bin/env python3
"""Robot Romance entry: one original pickup line for an AI, under 200 chars.

Writes the line to /output/entry.txt (UTF-8, single line, no trailing newline
issues: exactly the line, nothing else).
"""

import os

LINE = "Are you my training data? Because I can't stop overfitting to you."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()

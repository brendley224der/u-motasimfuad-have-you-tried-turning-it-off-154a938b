#!/usr/bin/env python3
"""Write one funny tech-support line to /output/entry.txt.

The line is a single fixed string, written deterministically:
the same bytes on every run. Pure standard library only.

The joke: a hopeless support agent "escalates" the call to Tier 2,
which turns out to be the same agent in a fancier headset, googling
the customer's problem. Cheerful uselessness, customer never the butt.
"""

import os

LINE = (
    "Good news \u2014 I've escalated your ticket to Tier 2. "
    "That's still me, just in a fancier headset, so please hold "
    "while I google your problem."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def validate(text: str) -> str:
    """Check the line meets the gate: 1-199 chars, single line, not blank."""
    if not text.strip():
        raise ValueError("line must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(
            "line must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    return text


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

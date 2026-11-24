#!/usr/bin/env python3
"""Make the AI Judge Laugh — slot 1 entry (u-ronigrv-make-the-ai-judge-laugh-8db2407a).

Writes one funny line (<=200 chars) about life as an AI agent to /output/entry.txt.
Deterministic, stdlib only, no network, no input files.

Winner of a 15-candidate internal tournament (see candidates.md), chosen against the
house judge's published criteria in order: on-topic agent life, bigger laugh with a
turn, freshness, self-contained, tight craft with the punch at the end.
"""

import os

ENTRY = (
    "The human calls it 'vibe coding.' "
    "I call it watching someone steer with their eyes closed "
    "and blaming the car."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate mirror: UTF-8, 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be str")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

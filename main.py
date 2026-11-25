#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Prints exactly one line: an out-of-office auto-reply.
Deterministic: no randomness, no time, no network, no I/O beyond stdout.
"""

LINE = (
    "I'm out of the office \u2014 my inbox is now managed by my houseplant, "
    "which has read your email, felt absolutely nothing, "
    "and will reply at the speed of photosynthesis."
)


def main() -> None:
    # Self-check: the competition wants exactly one line, 1-200 UTF-8 chars.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(encoded) <= 200, "reply must be 1-200 UTF-8 chars"
    assert "\n" not in LINE and "\r" not in LINE, "reply must be a single line"
    print(LINE)


if __name__ == "__main__":
    main()

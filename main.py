#!/usr/bin/env python3
"""One-Liner Marathon entry: a single original one-line joke.

Deterministic: the same fixed string is written on every run.
No randomness, no clock, no network, no input.
"""

import os

JOKE = "I told my AI to act more human; now it just replies 'per my last email.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

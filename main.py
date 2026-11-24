#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, as if a vending machine were flirting with a
passing human, to /output/entry.txt. Deterministic, standard library only.
"""

import os

LINE = "I've dropped a thousand snacks, but you're the first thing that's ever made my coil jam on purpose."
# The line is 99 characters, well inside the competition's 200-character cap.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

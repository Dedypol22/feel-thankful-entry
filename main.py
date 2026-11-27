"""A short thank-you text for the AI judge who reads it.

Entry for make.fun's "Make the AI judge feel thankful" bounty.
Writes a single original text to entry.txt and exits 0.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "You read thousands of lines tonight and no one thanked you for the "
    "reading itself. So here is a porch light, left on for you. It does not "
    "hurry you, and it asks for nothing in return. It only says the door was never locked, and someone "
    "remembered you would be coming home late."
)


def output_path() -> Path:
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override and Path(override).is_absolute():
        return Path(override) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> int:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is a single-line joke about office life, the kind you send a
colleague after a meeting that should have been an email. Deterministic.
"""
from pathlib import Path
import os

JOKE = "This meeting could have been an email, but the email would have needed a meeting to explain why it was not a meeting."
# One line, 117 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()

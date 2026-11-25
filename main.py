#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the single breakup line from line.txt to /output/entry.txt
(MAKEFUN_OUTPUT_DIR overrides the output directory for local tests).
Gate: UTF-8 text, 1-280 characters, not whitespace-only, one line.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    raw = (HERE / "line.txt").read_text(encoding="utf-8-sig")
    text = raw[:-1] if raw.endswith("\n") else raw
    text = text.strip()
    assert text, "line.txt is empty"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry is whitespace-only"
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

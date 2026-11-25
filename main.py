#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

Writes the chosen word to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-99 chars).
Cleans only the contents of the output directory, never the directory itself.
Standard library only; no network, no arguments.
"""

import os

WORD = "bluffing"


def main() -> None:
    if not (1 <= len(WORD) <= 99) or not WORD.strip() or " " in WORD:
        raise ValueError("entry word must be one non-blank word of 1-99 chars")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            continue
        os.remove(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify exactly what the judge will see.
    with open(entry_path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != WORD:
        raise ValueError("entry.txt does not match the chosen word")


if __name__ == "__main__":
    main()

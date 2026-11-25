#!/usr/bin/env python3
"""doorjog: a one-word entry for make.fun's "Invent a Word We Need".

The coinage: "doorjog" — the hurried half-run of a stranger you held a
door open for too soon. A real gap in English: everyone knows the
moment, nobody had a word for it. The program writes the word and its
one-line definition (at most 140 characters) to /output/entry.txt.
"""

import os

ENTRY = (
    "doorjog (n.) \u2014 the hurried half-run of someone you held "
    "a door open for too soon."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(
            "entry must be 1 to 140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

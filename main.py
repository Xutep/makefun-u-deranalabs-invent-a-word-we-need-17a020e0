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
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read the output back and check it against the gate the sealed
    # scorer applies, so a bad write fails loudly instead of silently.
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("entry.txt does not match the entry text")
    if not 1 <= len(written) <= 140 or not written.strip():
        raise ValueError("written entry fails the 1-to-140-character gate")


if __name__ == "__main__":
    main()

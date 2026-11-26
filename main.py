#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single original one-line joke about office life to
/output/entry.txt: exactly one line, 1-200 characters, UTF-8, with a
trailing newline. The joke text is a fixed constant, so every run
produces byte-identical output.
"""

import os

JOKE = "Our team building exercise was trust falls, which tracks, because management has been dropping us for years."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Check the joke is one non-blank line inside the length gate."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} chars, "
            f"got {len(line)}"
        )
    return line


def render(line: str) -> bytes:
    """Return the exact bytes the entry file holds: line + newline."""
    return (line + "\n").encode("utf-8")


def write_entry(line: str) -> None:
    """Write the validated line plus a trailing newline, UTF-8."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(render(line))


def main() -> None:
    write_entry(validate_line(JOKE))


if __name__ == "__main__":
    main()

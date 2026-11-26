"""One funny line: an original one-line joke about office life.

Writes the single joke line to /output/entry.txt (UTF-8, exactly one
line, 1-199 chars, trailing newline, deterministic every run).
"""

import os

LINE = "Our team building exercise was trust falls, which tracks, because management has been dropping us for years."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 199


def build_line() -> str:
    """Return the entry line, rejecting anything that is not one line."""
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} chars, "
            f"got {len(line)}"
        )
    return line


def main() -> None:
    # The line is a fixed constant, so every run writes byte-identical
    # output; validation runs first so a bad line never writes a file.
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()

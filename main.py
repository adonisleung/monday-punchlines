"""Monday Morning Punchlines entry.

Writes a single joke about Monday mornings to entry.txt in the
output directory, as required by the bounty.
"""

import os

JOKE = "I tried to call in sick on Monday. Monday picked up."


def main() -> None:
    # An empty env var means "not set": fall back to the default.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Confirm what was written, so the grader log shows it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke"
    assert 1 <= len(written) <= 200, "joke must be 1-200 characters"
    print(f"Wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()

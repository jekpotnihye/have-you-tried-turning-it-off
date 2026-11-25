"""Have You Tried Turning It Off? — entry program.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt (the gate checks that file:
UTF-8 text, 1 to 199 characters, not only whitespace).
"""

import os

ENTRY = "Turn it off, turn it on, and if your presentation won't load, I'll cheerfully panic with you."


def validate_entry(text):
    """Mirror the sealed gate: 1 to 199 characters, not only whitespace."""
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(path):
    """Write the entry text exactly, with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(validate_entry(ENTRY))


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    try:
        write_entry(output_path)
    except OSError:
        write_entry(os.path.join("output", "entry.txt"))


if __name__ == "__main__":
    main()

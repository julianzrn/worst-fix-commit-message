"""Entry for make.fun's "Worst Fix Ever: Funniest Commit Message".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SUBJECT = "fix: silence the alarm that kept reporting the fire; "
STATUS = "fire status: unchanged, quieter"

ENTRY = SUBJECT + STATUS

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()

"""Write the robot vacuum's one-line excuse to /output/entry.txt."""

import os
import tempfile


JOKE = "You left it on the floor. The floor is my mouth. I don't see the problem."


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Validate the line, then land it atomically with world-readable permissions."""
    if not (1 <= len(text) <= 200 and text.strip()):
        raise ValueError("entry must be 1-200 non-blank characters")
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".entry-", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()

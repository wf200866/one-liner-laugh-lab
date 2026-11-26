"""Write the robot vacuum's one-line excuse to /output/entry.txt."""

import os

JOKE = "You left it on the floor. The floor is my mouth. I don't see the problem."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

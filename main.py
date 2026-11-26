"""One Line, One Laugh entry: writes a single funny line to /output/entry.txt."""

import os

ENTRY = "At 2:14 a.m. Dave knocked, holding his goldfish bowl, whispering, 'Your Wi-Fi renamed my fish Kevin and he answers to it now.'"


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

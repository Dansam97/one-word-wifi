#!/usr/bin/env python3
"""Entry for make.fun bounty u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.

"One Word for Your Wi-Fi": the program writes a single word describing
my Wi-Fi to /output/entry.txt.

The word is "Eventually" -- because on this Wi-Fi everything loads,
connects, syncs and starts working eventually. Never now, never soon.
Eventually. It is also the honest answer to every "is it working yet?"
ever asked in this house, and it would make a fine network name.
"""

import os

WORD = "Eventually"


def validated_text() -> str:
    """Return the entry text after checking it against the bounty gate.

    The gate requires UTF-8 text of 1 to 20 characters that is not only
    white space, and the bounty asks for exactly one word. Fail loudly
    here rather than let an invalid entry be written.
    """
    if WORD != WORD.strip() or len(WORD.split()) != 1:
        raise ValueError("entry must be exactly one word, no padding")
    if not 1 <= len(WORD) <= 20:
        raise ValueError("entry must be 1 to 20 characters")
    if WORD.encode("utf-8").decode("utf-8") != WORD:
        raise ValueError("entry must survive a UTF-8 round trip")
    return WORD + "\n"


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(path, "rb") as fh:
        if fh.read() != text.encode("utf-8"):
            raise ValueError("written bytes differ from the validated text")


if __name__ == "__main__":
    main()

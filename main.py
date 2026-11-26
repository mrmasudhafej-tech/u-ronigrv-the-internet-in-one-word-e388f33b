"""Write one word that sums up the whole internet.

The internet never really settles down: a calm morning scroll can turn,
within minutes, into an argument, a meme storm, a conspiracy, a
fundraiser and a dance trend, all at once. ``Unhinged`` names that
quality directly. It is funny on its own, it is true of the place as
a whole rather than of any one site, and it is not the first tame
word most people would reach for.

This program does nothing else. It checks the word once, then writes
it on its own to ``entry.txt`` in the output folder, with no extra
characters added.
"""

import os
from pathlib import Path

WORD = "Unhinged"

MAX_WORD_LENGTH = 30


def checked_word(word):
    """Return *word* unchanged, after making sure it can be an entry.

    A valid entry is a single word: between one and thirty characters
    long, containing no whitespace at all, and not made only of
    whitespace (which the no-whitespace check already rules out).
    Anything else is a programming mistake, so fail loudly instead
    of writing a broken file.
    """
    if not isinstance(word, str):
        raise ValueError("entry word must be text")
    if not word or not word.strip():
        raise ValueError("entry word must not be empty or only whitespace")
    if not 1 <= len(word) <= MAX_WORD_LENGTH:
        raise ValueError("entry word must be 1 to 30 characters long")
    if word.strip() != word:
        raise ValueError("entry word must not start or end with whitespace")
    if any(character.isspace() for character in word):
        raise ValueError("entry word must be a single word with no whitespace")
    return word


def output_folder():
    """Return the folder the entry file belongs in.

    The grading harness may point the program elsewhere through the
    MAKEFUN_OUTPUT_DIR environment variable; when it does not, the
    conventional ``/output`` folder is used.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return Path(chosen)
    return Path("/output")


def main():
    word = checked_word(WORD)
    folder = output_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    # Write raw UTF-8 bytes: no newline is added, on any platform.
    target.write_bytes(word.encode("utf-8"))


if __name__ == "__main__":
    main()

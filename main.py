#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes the entry — one line, at most 200 characters: a joke about
office life — to /output/entry.txt. Python 3 standard library only.

The joke: Facilities replaced our dead office plant with a laminated
photo of one, then closed the ticket as 'resolved'. The setup is a
mundane office fixture (the communal plant everyone ignores); the
twist is Facilities "fixing" a dead plant with a laminated photo of
one and then closing the ticket — the exact bureaucratic shrug every
office worker recognises from IT and Facilities tickets. It is one
sentence, one line, specific rather than a generic meeting complaint,
and needs no explanation. The wording is fixed; do not paraphrase it.
"""

import os

# The entry text itself. Kept as one constant so the exact bytes written
# to /output/entry.txt are easy to audit against the competition's
# 200-character limit (this line measures 110 characters plus newline).
ENTRY = (
    "Facilities replaced our dead office plant with a laminated photo "
    "of one, then closed the ticket as 'resolved'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

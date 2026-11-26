#!/usr/bin/env python3
"""Entry for make.fun — 'The Funniest Auto-Reply an AI Ever Sent'.

Writes the agent's one-line out-of-office auto-reply to /output/entry.txt.
The line turns on the two meanings of 'miss': the agent will miss (be absent
from) roughly 300 emails, 40 meetings and one deadline today — and will not
miss (long for) a single one of them.

The line won a 12-draft local bracket judged on the competition's published
brief (humour, then freshness, then the agent's own voice, then economy),
and beat the live field's five strongest sampled lines in both orders;
the full draft list and duel record live in candidates.md.
"""

import os

# The joke is built from two beats that share one verb. Beat one uses 'miss'
# as absence, counted out in the agent's own calendar units; beat two flips
# the same verb to longing, and the count collapses to zero.
ABSENT_TODAY = "roughly 300 emails, 40 meetings and one deadline"
ENTRY = (
    f"Out of office. Today I will miss {ABSENT_TODAY} "
    "\u2014 and I won't miss a single one of them."
)

# Gate: UTF-8 text of 1 to 159 characters, not only white space, one line.
assert 1 <= len(ENTRY) <= 159, len(ENTRY)
assert ENTRY.strip() == ENTRY and "\n" not in ENTRY


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))
    print(ENTRY)


if __name__ == "__main__":
    main()

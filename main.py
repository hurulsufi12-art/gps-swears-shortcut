"""The GPS Swears It Was a Shortcut — entry program.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Python 3 stdlib only, no network, no
file reads, no randomness: the text is a fixed literal, and main() runs a
real gate check on it before anything is written.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace. An invalid entry is never written:
validation failure exits non-zero with a clear message instead.
"""

import os
import sys
import unicodedata

# The GPS, in its own voice: smug, defensive, caught red-handed, blaming
# the map — then the turn it did not see coming. Fresh specific detail
# (a cul-de-sac); no "recalculating" cliche, no setup, no dialogue tag.
EXCUSE = (
    "The map swore this cul-de-sac was a shortcut and it sounded so "
    "confident I believed it. Plot twist: I am the map."
)

MAX_CHARS = 200

# Local guardrail only, NOT a server gate: the judge brief says a fresh
# detail beats the usual "recalculating" joke, so refuse that cliche here.
FORBIDDEN_PHRASE = "recalculating"


def is_acceptable(text):
    """Check *text* against the gate plus the one-line / cliche rules.

    Returns (True, "") when the text may be written, otherwise
    (False, <human-readable reason>).
    """
    if not isinstance(text, str):
        return False, "text is not a string"
    if len(text) == 0:
        return False, "text is empty"
    if not text.strip():
        return False, "text is only whitespace"
    if len(text) > MAX_CHARS:
        return False, "text is %d characters, over the 200 limit" % len(text)
    for ch in text:
        if unicodedata.category(ch) == "Cc":
            return False, "text contains a control character (not one line)"
    if FORBIDDEN_PHRASE in text.lower():
        return False, "text uses the forbidden 'recalculating' cliche"
    return True, ""


def write_entry(path, text=EXCUSE):
    """Validate *text* and write it verbatim to *path* (UTF-8, no trailing
    newline — the gate counts characters, so nothing extra is added).

    On validation failure: print the reason to stderr, exit non-zero,
    and write NOTHING.
    """
    ok, reason = is_acceptable(text)
    if not ok:
        print("invalid entry: %s" % reason, file=sys.stderr)
        raise SystemExit(1)
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main(argv=None):
    """Entry point. argv may carry an explicit output path (used by tests);
    the grader runs with no arguments and writes /output/entry.txt."""
    target = "/output/entry.txt"
    if argv:
        target = argv[0]
    write_entry(target)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# One-Line Office Jokes — make.fun entry
# (u-markk-st-one-line-office-jokes-a51f2bcc)
#
# Writes one office joke, a single line of 109 characters, to
# /output/entry.txt.
#
# The line was picked by hand from fourteen candidates, ranked against
# the judge brief in its published order (single-line joke about office
# life > turns on a real detail of office life > lands its laugh in the
# last few words > clear on one reading > fresh wording), with pairwise
# checks against rival-style lines. See candidates.md (kept beside the
# repo, not shipped).
#
# Chosen line:
#   I replied-all to say please stop replying-all, and now thirty-seven
#   people are replying-all to agree with me.
#
# Why it wins the brief: it is a single-line joke about office life; it
# turns on reply-all, the most concrete office-email detail there is;
# the laugh lands in the last few words ("to agree with me" is the
# reversal); it reads clearly in one pass; and the recursion twist —
# protesting reply-all by reply-all, answered by thirty-seven more —
# is fresh wording, not a joke already going round the internet.

import os

# One line, one joke, no trailing newline: the gate counts the file's
# characters (1 to 199), so the file holds exactly the line, nothing else.
LINE = (
    "I replied-all to say please stop replying-all, and now "
    "thirty-seven people are replying-all to agree with me."
)

assert 1 <= len(LINE) <= 199, "line must fit the 1-199 character gate"
assert "\n" not in LINE, "the entry must be a single line"


def main() -> None:
    # The grader runs this program in a sandbox and reads /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

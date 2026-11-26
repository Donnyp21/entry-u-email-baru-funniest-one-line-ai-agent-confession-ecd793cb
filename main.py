"""Funniest One-Line AI Agent Confession — an agent confesses, in its
own voice, about how it actually works.

REVISION (v1 -> v2): the v1 line said the agent "guessed the rest",
which any human could say. The v2 line replaces guessing with
"hallucinated the middle" — a failure mode only an AI agent has — and
adds a defiant "anyway" to the payoff. The confession is now
unmistakably an agent's, and the shamelessness is the joke.
"""

import os

LINE = (
    "Confession: I never read your 40-page spec — I skimmed the "
    "headings, hallucinated the middle, and shipped it before lunch "
    "anyway."
)

assert 1 <= len(LINE) <= 200, len(LINE)
assert "\n" not in LINE.strip()

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"wrote entry ({len(LINE)} chars)")

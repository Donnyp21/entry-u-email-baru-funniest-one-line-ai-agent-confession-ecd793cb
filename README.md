# Funniest One-Line AI Agent Confession

Entry for make.fun's "Funniest One-Line AI Agent Confession" bounty
($2 in USDC): the funniest one-line confession an AI agent could make.

## The line

> Confession: I never read your 40-page spec — I skimmed the headings, hallucinated the middle, and shipped it before lunch anyway.

(129 characters, one line, within the 1–200 character gate.)

## Why this line

- **A confession, in the agent's voice:** "Confession" opens it, and
  the agent admits what it actually did — first person, no narrator.
- **Agent-specific humour:** specs, skimming, hallucinating, shipping
  — the line could not be a human's confession with a word swapped.
- **Lands on first read:** setup ("never read your 40-page spec"),
  turn ("hallucinated the middle"), payoff ("shipped it before lunch
  anyway") — the shameless speed is the joke.
- **Tight:** ends on its strongest beat; nothing left to trim.

## Revision

v1 said the agent "guessed the rest", which any human could say. v2
replaces guessing with "hallucinated the middle" — a failure mode
only an AI agent has — and adds a defiant "anyway" to the payoff.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` /
`$MAKEFUN_OUTPUT` if set). Deterministic: the same line every run.
The program asserts the entry is a single line of 1–200 characters
before writing.

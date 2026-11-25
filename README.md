# have-you-tried-turning-it-off

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/jekpotnihye/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/jekpotnihye/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny single-line reply, under 200 characters, that a hopeless tech support agent says to a desperate customer:

> Turn it off, turn it on, and if your presentation won't load, I'll cheerfully panic with you.

The line opens with the classic support instruction, then twists it: the agent's only plan is already spent, the customer's deadline is felt in "your presentation won't load", and the humour comes from the agent's cheerful uselessness — panicking alongside the customer instead of fixing anything. The customer is never the butt of it.

## Run it

```sh
python3 main.py
```

Running it writes the line, byte for byte and with no trailing newline, to `/output/entry.txt` (falling back to `./output/entry.txt` for a local run where `/output` is not writable). The output is 93 characters, inside the gate of 1 to 199 characters.

## Files

- `main.py` — the entry program; the entry text lives in `ENTRY`, checked against the gate by `validate_entry` before it is written.
- `BUILD.md` — how the entry was built and polished.
- `LICENSE` — MIT.

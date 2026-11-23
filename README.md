# One-Line Roast: The Gadget You Use Every Day

[![Bounty](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![Reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the make.fun competition [One-Line Roast: The Gadget You Use Every Day](https://make.fun/competitions/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610).

## The roast

> My phone updates itself at 3am, restarts, then asks if I enjoyed the update — as if it didn't just eat my alarm.

## How it works

`main.py` holds the roast as a constant, runs it through a small validator
(`RoastValidator` with three named checks: non-blank, 1–200 characters,
exactly one line), then writes it — with no trailing newline — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

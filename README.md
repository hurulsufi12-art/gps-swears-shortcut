# The GPS Swears It Was a Shortcut

[![The GPS Swears It Was a Shortcut](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/hurulsufi12-art/gps-swears-shortcut/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![Reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/hurulsufi12-art/gps-swears-shortcut/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

Entry for the [make.fun bounty "The GPS Swears It Was a Shortcut"](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9) ($2 escrowed, 8 paid places).

## What it does

`main.py` writes the GPS's own one-line excuse for sending the driver down
the wrong road to `/output/entry.txt` — a single line of plain text, 113
characters, no setup, no dialogue tag:

> The map swore this cul-de-sac was a shortcut and it sounded so confident I believed it. Plot twist: I am the map.

Before writing, `main()` runs a real gate check (1–200 characters, not only
whitespace, single line, no control characters). If the text ever failed the
check, the program would exit non-zero and write nothing.

## Run

```sh
python3 main.py
```

Python 3 standard library only — no dependencies, no network, no input
files. Writes `/output/entry.txt` (UTF-8, no trailing newline).

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

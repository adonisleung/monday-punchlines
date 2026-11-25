# monday-punchlines

[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

Entry for the make.fun bounty **Monday Morning Punchlines**.

## What it does

`main.py` writes a single original joke about Monday mornings to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output`). The scorer reads that file: it must be UTF-8 text
of 1 to 200 characters.

## The joke

> I tried to call in sick on Monday. Monday picked up.

## How to run

```sh
python3 main.py
```

To test with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

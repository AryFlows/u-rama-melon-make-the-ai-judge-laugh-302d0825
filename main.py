"""Frost Whole Self — one-line office joke for make.fun.

Writes a single original joke about office life to /output/entry.txt.
The gate: UTF-8 text, 1-200 characters, one line.
"""

import os

JOKE = "HR said to bring my whole self to work, so I brought my naps too \u2014 now my whole self is asleep under the desk."


def main():
    if not (1 <= len(JOKE) <= 200) or JOKE.strip() != JOKE:
        raise SystemExit("joke outside the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

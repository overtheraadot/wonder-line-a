"""Wonder Line A — Everyday Wonder, Two Days to Find the Line.

Writes one sentence (112 characters) to /output/entry.txt.
Deterministic: the text is a fixed literal; no randomness, no time,
no network, no environment input. Running twice produces identical bytes.
"""

import os

ENTRY = (
    "A stranger pins the lift doors open with one fingertip, "
    "and for three seconds the whole building agrees to wait."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

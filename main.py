"""Wonder Line A — Everyday Wonder, Two Days to Find the Line.

Writes one sentence (112 characters) to the entry file.
Deterministic: the text is a fixed literal; no randomness, no time,
no network, no environment input. Running twice produces identical bytes.

Output location: the OUTPUT_PATH environment variable when set,
otherwise the competition default /output/entry.txt.
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 200


def build_entry() -> str:
    """Compose the entry sentence from its two clauses."""
    return join_clauses(
        "A stranger pins the lift doors open with one fingertip, ",
        "and for three seconds the whole building agrees to wait.",
    )


def join_clauses(*clauses: str) -> str:
    """Join sentence clauses in order, with no separator added."""
    return "".join(clauses)


def resolve_output_path() -> str:
    """Pick the destination file, honouring OUTPUT_PATH when set."""
    override = os.environ.get("OUTPUT_PATH", "").strip()
    return override or DEFAULT_OUTPUT_PATH


def validate_entry(text: str) -> None:
    """Enforce the sealed gate: 1-200 chars of non-blank UTF-8 text."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_ENTRY_CHARS} limit"
        )


def write_entry(path: str, text: str) -> None:
    """Write the entry text, creating the parent directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    entry = build_entry()
    validate_entry(entry)
    write_entry(resolve_output_path(), entry)


if __name__ == "__main__":
    main()

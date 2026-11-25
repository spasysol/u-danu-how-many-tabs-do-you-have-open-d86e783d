#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

Writes one number, digits only (1-5 characters), to /output/entry.txt:
an honest count of open browser tabs. Pure standard library.
"""

import os

ENTRY = "137"

MAX_CHARS = 5


def main():
    # Fail loudly instead of submitting a gate-violating entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.isdigit():
        raise SystemExit("entry must be digits only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

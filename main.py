"""Rejected Olympic Sports entry: extreme ironing, judged by the IOC.

Writes the single-line entry to entry.txt with no trailing newline.
"""

import os

ENTRY = "Extreme ironing: athletes iron shirts on a cliff edge, judged on creases and courage. The IOC folded."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# No trailing newline: the gate counts the file's exact bytes.
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)

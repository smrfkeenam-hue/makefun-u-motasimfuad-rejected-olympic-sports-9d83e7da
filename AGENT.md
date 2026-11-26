# AGENT.md

Build notes for the Rejected Olympic Sports entry (u-motasimfuad-rejected-olympic-sports-9d83e7da).

- Entry: "Extreme ironing: athletes iron shirts on a cliff edge, judged on creases and courage. The IOC folded." (101 characters, one line, no trailing newline.)
- Angle: extreme ironing is a real absurd activity, so the sport sounds like something a broadcaster would have to explain with a straight face; the punchline "The IOC folded" lands at the end and plays on both folding laundry and folding under pressure.
- main.py is stdlib only (`import os`), writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. Final content from 1 write + 2 edits.
- Verified by running main.py with a fresh /tmp MAKEFUN_OUTPUT_DIR and checking the output bytes and sha256.

#!/usr/bin/env python3

import sys

a = []
for word in sys.stdin:
    s = word.strip()
    slow = s.lower().replace("qu", "")
    if "q" in slow:
        a.append(s)

print(f'Words with q but no u: {a}')

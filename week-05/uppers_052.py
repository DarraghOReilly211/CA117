#!/usr/bin/env python3

import sys

last_cap = ""
for line in sys.stdin.readlines():
    line = line.strip()
    a = []
    for char in line:
        if char.isupper() and char > last_cap:
            last_cap = char
            a.append(char)
    print("".join(a))

#!/usr/bin/env python3

import sys

args = sys.argv[1]

a = []
with open(args, "r") as f:
    for word in f:
        s = word.strip()
        a.append(s)

input = []
for line in sys.stdin:
    i = 0
    while i < len(a):
        if a[i] in line:
            line = line.replace(a[i], "@" * len(a[i]))
        i += 1
    input.append(line)

for line in input:
    print(f'{line.strip()}')

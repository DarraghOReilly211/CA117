#!/usr/bin/env python3

import sys
a = []
b = []
with open(sys.argv[1], "r") as f:
    for line in f:
        a.append(line.strip())
with open(sys.argv[2], "r") as g:
    for line in g:
        b.append(line.strip())

a_count = 0
b_count = 0
final = []
i = 0
while i < len(a) + len(b):
    if i % 2 == 0:
        final.append(a[a_count])
        print(a[a_count])
        a_count += 1
    else:
        final.append(b[b_count])
        print(b[b_count])
        b_count += 1
    i += 1

#!/usr/bin/env python3

import sys

for number in sys.stdin.readlines():
    n = int(number.strip())
    a = []
    for i in range(1, n + 1):
        if i % 3 != 0:
            a.append(i)
        else:
            a.append('X')
    print(f'Multiples of 3 replaced: {a}')

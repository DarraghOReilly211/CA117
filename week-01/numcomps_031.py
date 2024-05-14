#!/usr/bin/env python3

import sys

for number in sys.stdin.readlines():
    n = int(number.strip())
    a = []
    for digit in range(1, n + 1):
        a.append(digit)
    print(f'Multiples of 3: {[i for i in a if i % 3 == 0]}')
    print(f'Multiples of 3 squared: {[i ** 2 for i in a if i % 3 == 0]}')
    print(f'Multiples of 4 doubled: {[i * 2 for i in a if i % 4 == 0]}')
    print(f'Multiples of 3 or 4: {[i for i in a if i % 3 == 0 or i % 4 == 0]}')
    print(f'Multiples of 3 and 4: {[i for i in a if i % 3 == 0 and i % 4 == 0]}')

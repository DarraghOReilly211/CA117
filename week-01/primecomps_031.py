#!/usr/bin.env python3

import sys
d = {}
for line in sys.stdin:
    s = int(line.strip())
    a = []
    for i in range(1, s + 1):
        a.append(i)
        counter = 0
        j = 0
        while j < len(a):
            if i % a[j] == 0:
                counter += 1
            j += 1
        if counter == 2:
            d[j] = True
        else:
            d[j] = False
    print(f'Primes: {[n for n in a if d[n] == True]}')

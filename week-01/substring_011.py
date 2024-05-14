#!/usr/bin/env python3

import sys

for s in sys.stdin:
    a = s.lower().strip().split(' ')
    needle = a[0]
    haystack = a[1]
    print(needle in haystack)

#!/usr/bin/env python3

import sys

prev = ""
a = []
#s = sys.stdin.readline()

for line in sys.stdin:
   current = line.strip()
   a.append(current)
   if len(prev) < len(current):
      prev = current

for lines in a:
   print(f'{lines:^{len(prev)}s}')

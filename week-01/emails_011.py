#!/usr/bin/env python3

import sys

numbers = "123456789"

for s in sys.stdin:
   x = s.split(".")
   x1 = x[0]
   x2 = x[1]
   i = 0
   while x2[i] not in numbers:
      i = i + 1
   print(x1[0].upper() + x1[1:] + " " + x2[0].upper() + x2[1:i])

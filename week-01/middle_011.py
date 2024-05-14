#!/usr/bin/env python3

import sys

for line in sys.stdin:
   if ((len(line) - 1) % 2) == 0:
      print("No middle character!")
   else:
      n = len(line) - 1
      n = int((n / 2))
      print(line[n])

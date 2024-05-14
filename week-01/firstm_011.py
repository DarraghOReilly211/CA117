#!/usr/bin/env python3

import sys

for x in sys.stdin:
   s = x.strip()
   s = s.replace("m", "M", 1)
   print(s)

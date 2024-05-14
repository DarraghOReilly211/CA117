#!/usr/bin/env python3

import sys

for lines in sys.stdin:
   s = lines.strip()
   alphaU = False
   alphaL = False
   num = False
   spec = False
   for c in s:
      if c.islower() is True:
         alphaL = True
      elif c.isupper() is True:
         alphaU = True
      elif c.isdigit() is True:
         num = True
      else:
         spec = True
   print(alphaL + alphaU + num + spec)

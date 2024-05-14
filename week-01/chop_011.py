#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
def chop(s):
   return s[1:-1]


for i in s:
   s = i.strip()
   chop(s)
   chopped = chop(s)
   if len(chopped) > 0:
      print(chopped)

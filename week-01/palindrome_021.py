#!/usr/bin/env python3

import sys


def ispal(s):
   i = 0
   total = 0
   while i < len(s) // 2:
      if s[i] == s[len(s) - 1 - i]:
         total = total + 1
      i = i + 1
   if total == len(s) // 2:
      return True
   else:
      return False


for line in sys.stdin:
   s = line.strip()
   s = s.lower()
   i = 0
   while i < len(s):
      if not s[i].isalnum():
         s = s.replace(s[i], "")
      i = i + 1
   print(ispal(s))

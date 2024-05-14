#!/usr/bin/env python3

import sys

def apps(word):
   for char in s:
      if char.isalnum():
         a.append(char.lower())
         b = "".join(a)
   return(b)

for line in sys.stdin:
   s = line.strip()
   a = []
   b = apps(s)
   total = 0
   i = 0
   while i < (len(b) // 2):
      if b[i] == b[len(b) - 1 - i]:
         total = total + 1
      else:
         break
   if total == (len(b) // 2):
      print(True)
   else:
      print(False)

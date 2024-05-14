#!/usr/bin/env python3

import sys
#i = 0
#for s in sys.stdin:
#   a = s.strip().split(" ")
#   needle = a[0].lower()
#   haystack = a[1].lower()
#   count = 0
#   for i in needle:
#      if i in haystack:
#         count += 1
#         haystack = haystack.replace(i, " ")
#   print(count == len(needle))


#Darraghs O'Brians Method
def contains(chars,  s):

   for c in chars:
      if c not in s:
         return False
      s = s.replace(c, "", 1)
      return True


lines = sys.stdin.readlines()

for line in lines:
   [chars, s] = line.strip().split()
   print(contains(chars, s))

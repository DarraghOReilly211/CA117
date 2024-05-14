#!/usr/bin/env python3

import sys

def palindrome(s):

   s = s.lower()

   keep = []
   for c in s:
      if c.isalnum():
         a.append(c)

   return keep == keep[::-1]

s = sys.stdin.readlines()
palindrome(s)

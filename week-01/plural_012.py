#!/usr/bin/env pyrthon3

import sys

def final_digit(s):
   if s[-2:] == "ch" or s[-2:] == "sh":
      s = s + "es"
   elif s[-1] == "x" or s[-1] == "s" or s[-1] == "z":
      s = s + "es"
   elif s[-2] in "bcdfghjklmnpqrstvwxyz" and s[-1] == "y":
      s = s.replace(s[-1], "")
      s = s + "ies"
   elif s[-2:] == "fe":
      s = s.replace(s[-2:], "")
      s = s + "ves"
   elif s[-1] == "f":
      s = s.replace(s[-1:], "")
      s = s + "ves"
   elif s[-1] == "o":
      s = s + "es"
   else:
      s = s + "s"
   return s


for lines in sys.stdin:
   s = lines.strip()
   print(final_digit(s))

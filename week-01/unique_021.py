#!/usr/bin/env python3

import sys
import string

a = {}
spec = string.punctuation

for lines in sys.stdin:
   lines = lines.strip().lower()
   line = lines.split(" ")
   for word in line:
      for char in word:
         if char in spec:
            word = word.replace(char, "")
      a[word] = True

z = []
for x in a:
   if x.isalnum():
      z.append(x)
#print(z)
print(len(z))

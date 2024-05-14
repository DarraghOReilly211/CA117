#!/usr/bin/env python3

import sys
n = sorted(sys.stdin.readline().strip().split(), key=int)
dictionary = {}
dictionary["A"] = n[0]
dictionary["B"] = n[1]
dictionary["C"] = n[2]
a = []
for char in sys.stdin.readline().strip():
    a.append(dictionary[char])
print(" ".join(a))

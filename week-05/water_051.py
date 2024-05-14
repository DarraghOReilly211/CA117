#!/usr/bin/env python3


import sys
water = sys.stdin.readline().strip()
water = int(water)
buckets = sys.stdin.readline().strip().split(" ")
count = 0

for i in buckets:
   if water >= int(i):
      water = water - int(i)
      count += 1
   else:
      water = 0

print(count)

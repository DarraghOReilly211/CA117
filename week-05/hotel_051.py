#!/usr/bin/env python3

import sys

rooms = sys.stdin.readline().strip()
limit = int(rooms[0])

range = range(1, limit, 1)

free = []
for n in range:
    if str(n) not in rooms:
        free.append(str(n))

if len(free) == 0:
    print("no room")

else:
    print(" ".join(free))

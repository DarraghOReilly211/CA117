#!/usr/bon/env python3

import sys

for line in sys.stdin:
    line = int(line)
    if line <= 400:
        print(1)
    else:
        print(line // 400)

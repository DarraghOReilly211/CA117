#!/usr/bin/env python3

import sys
import string

checked = {
    "e": 0,
    "a": 0,
    "o": 0,
    "i": 0,
    "u": 0

}
for line in sys.stdin:
    line = line.split()
    for word in line:
        for word in word:
            word = word.strip(string.punctuation)
            word = word.lower().strip()
            for char in word:
                if char in checked:
                    checked[word] += 1

check = sorted(checked.items(), key=lambda x: x[1], reverse=True)
format = len(str(check[0][1]))
for (k, v) in check:
    print(f'{k} : {v:>{format}d}')

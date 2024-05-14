#!/usr/bin/env python3

import sys
import string

checked = {

}
for line in sys.stdin:
    line = line.split()
    for word in line:
        word = word.strip(string.punctuation)
        word = word.lower().strip()
        #print(word)
        if word not in checked:
            checked[word] = 1
        else:
            checked[word] += 1

for (k, v) in sorted(checked.items()):
    print(f'{k} : {v}')

#!/usr/bin/emv python3

import sys

for line in sys.stdin:
    line = line.lower().strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in line:
        alphabet = alphabet.replace(char, '')
    if len(alphabet) != 0:
        print(f'missing {alphabet}')
    else:
        print('pangram')

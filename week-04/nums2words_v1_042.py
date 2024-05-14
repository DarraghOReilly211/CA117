#!usr/bin/env python3

import sys

text = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    " ": " ",
    "\n": ""
}

def translate(char):
    return text[char]


s = sys.stdin.readlines()
for line in s:
    line = line.split()
    print(f'{" ".join([translate(char) for char in line if char != " "])}')

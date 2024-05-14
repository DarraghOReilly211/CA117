#!/usr/bin/env python3

import sys

text = {

}

text_to_num = {
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

with open(sys.argv[1], "r") as f:
    s = f.readlines()
    for translations in s:
        translations = translations.split()
        text[translations[0]] = translations[1][:len(translations[1])]

def translate(char):
    try:
        english = text_to_num[char]
    #print(text_to_num[char])
        return text[english]
    except KeyError:
        return("unknown")


s = sys.stdin.readlines()
for line in s:
    line = line.split()
    print(f'{" ".join([translate(char) for char in line if char != " "])}')

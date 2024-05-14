#!/usr/bin/env python3

import sys

def shortest(list):
    return min(list, key=len)

def is_vowel(word):
    vowels = "aeiou"
    total = 0
    for char in vowels:
        if char in word:
            total += 1
            vowels = vowels.replace(char, "")
    if total == 5:
        return True


def most_es(word):
    temp_es = 0
    for char in word:
        if char == "e":
            temp_es += 1
    if temp_es == highest_es:
        return True


a = []
highest_es = 0
highest_e_words = []
end_with_iary = []
for word in sys.stdin:
    s = word.strip()
    slow = s.lower()
    a.append(s)
    if slow.endswith("iary"):
        end_with_iary.append(s)
    temp_highest = 0
    for char in slow:
        if char == "e":
            temp_highest += 1
    if temp_highest > highest_es:
        highest_es = temp_highest

print(f'Shortest word containing all vowels: {shortest([word for word in a if is_vowel(word)])}')
print(f'Words ending in iary: {len(end_with_iary)}')
print(f"Words with most e's: {[word for word in a if most_es(word)]}")

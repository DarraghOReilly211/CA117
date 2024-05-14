#!/usr/bin/env python3

import sys
def a_count(word):
    count = 0
    for char in word.lower():
        if char == "a":
            count += 1
    if count >= 4:
        return word.strip()
    else:
        return None


def q_count(word):
    count = 0
    for char in word.lower():
        if char == "q":
            count += 1
    if count >= 2:
        return word.strip()
    else:
        return None


def anagram_for_angle(word):
    check = "angle"
    if len(word) == len(check):
        word = word.lower()
        for char in check:
            if char not in word or word == "angle":
                return False
            word = word.replace(char, "*", 1)
        return True
    else:
        return False


lines = sys.stdin.readlines()
for word in lines:
    word = word.strip()
print(f'Words containing 17 letters: {[word.strip() for word in lines if len(word.strip()) == 17]}')
print(f'Words containing 18+ letters: {[word.strip() for word in lines if len(word.strip()) >= 18]}')
print(f"Words with 4 a's: {[word.strip() for word in lines if a_count(word.strip()) != None]}")
print(f"Words with 2+ q's: {[word.strip() for word in lines if q_count(word.strip()) != None]}")
print(f'Words containing cie: {[word.strip() for word in lines if "cie" in word.strip()]}')
print(f"Anagrams of angle: {[word.strip() for word in lines if anagram_for_angle(word.strip())]}")

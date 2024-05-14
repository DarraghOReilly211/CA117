#!/usr/bin/env python3

import sys

hand = [card[0] for card in sys.stdin.readline().split()]

largest = 0
for card in hand:
    freq = hand.count(card)
    if largest < freq:
        largest = freq
print(largest)

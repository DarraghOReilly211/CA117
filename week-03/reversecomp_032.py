#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin if len(word) > 5]
s_words = [word.lower() for word in words]
s_words.sort()

# Binary Search
def binsearch(query, sorted_list):
    query = query.lower()
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < query:
            low = mid + 1
        elif sorted_list[mid] > query:
            high = mid - 1
        else:
            return True
    return False


final = [word for word in words if binsearch(word[::-1], s_words)]
print(final)

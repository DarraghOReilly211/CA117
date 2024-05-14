#!/usr/bin/env python3

def swap_keys_values(input):
    key = []
    value = []
    new_dick = {}
    for k, v in input.items():
        new_dick[v] = k
    return new_dick

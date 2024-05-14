#!/usr/bin/env python3

import sys

dict = {

}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split()
        dict[line[0]] = line[1:]
    #print(dict)

inputs = []
for name in sys.stdin:
    name = name.strip()
    inputs.append(name)

for name in inputs:
    try:
        print(f'Name: {name}')
        print(f'Phone: {dict[name][0]}')
        print(f'Email: {dict[name][1]}')
    except KeyError:
        print("No such contact")
        continue

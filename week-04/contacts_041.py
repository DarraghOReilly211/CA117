#!/usr/bin/env python3

import sys

dict = {

}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split()
        dict[line[0]] = line[1]

inputs = []
for name in sys.stdin:
    name = name.strip()
    inputs.append(name)

for name in inputs:
    try:
        print(f'Name: {name}')
        print(f'Phone: {dict[name]}')

    except KeyError:
        print("No such contact")
        continue

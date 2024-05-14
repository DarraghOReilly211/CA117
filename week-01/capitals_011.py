#!/usr/bin/env python3

import sys

def capitalise(s):
    return s[0].upper() + s[1:-1] + s[-1].upper()

def main():

    for line in sys.stdin:
        if len(line.strip()) >= 2:
            print(capitalise(line.strip()))


if __name__ == '__main__':
    main()

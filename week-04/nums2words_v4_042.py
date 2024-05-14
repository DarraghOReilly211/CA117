#!/usr/bin/env python3

import sys

num2word = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
notunique = {'20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety', '100': 'one hundred'}
a = [line.strip() for line in sys.stdin]
for line in a:
    token = line.split()
    b = []
    for c in token:
        if int(c) < 20:
            b.append(num2word[c])
        else:
            secondigit = int(c) % 10
            if secondigit == 0:
                b.append(notunique[c])
            elif secondigit != 0:
                secondigit = str(secondigit)
                c = str(c[0]) + "0"
                unique = (notunique[c] + "-" + num2word[secondigit])
                b.append(unique)
    print(" ".join(b))

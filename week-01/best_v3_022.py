#!/usr/bin/env python3

import sys

highest_score = 0
best_student = ""
try:
    with open(sys.argv[1], "r") as f:
        for line in f:
            try:
                s = line.split()
                student_name = s[1:]
                student_score = (int(s[0]))
                if int(highest_score) < student_score:
                    highest_score = student_score
                    best_student = student_name
            except ValueError:
                print(f'Invalid mark {s[0]} encountered. Skipping.')
        print(f'Best student: {" ".join(best_student)}')
        print(f'Best mark: {highest_score}')

except FileNotFoundError:
    print(f'{sys.argv[1]} does not exist.')

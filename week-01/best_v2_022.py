#!/usr/bin python3

import sys

highest_score = 0
best_student = ""
try:
    with open(sys.argv[1], "r") as f:
        try:
            for line in f:
                s = line.split()
                student_name = s[1:]
                student_score = (int(s[0]))
            if highest_score < student_score:
                highest_score = student_score
                best_student = line
            print(f'Best student: {best_student[3:].strip()}')
            print(f'Best mark: {highest_score}')

        except ValueError:
            print(f'Invalid mark {s[0]} encountered. Exiting.')

except FileNotFoundError:
    print(f'{sys.argv[1]} does not exist.')

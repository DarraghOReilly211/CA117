#!/usr/bin/env python3

import sys

highest_score = 0
best_student = ""
try:
    with open(sys.argv[1], "r") as f:
        for line in f:
            s = line.split()
            student_name = s[1:]
            students_score = s[0]
            #print(s[0], highest_score)
            if int(highest_score) < int(students_score):
                highest_score = students_score
                best_student = line

except FileNotFoundError:
    print(f'{sys.argv[1]} does not exist.')

print(f'Best student: {best_student[3:].strip()}')
print(f'Best mark: {highest_score}')

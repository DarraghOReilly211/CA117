#!/usr/bin/env python3

import sys
names = []
grades = []
winners = []
try:
   with open(sys.argv[1], "r") as f:
      for line in f:
         a = line.strip().split()
         try:
            grades.append(int(a[0]))
            names.append(" ".join(a[1:]))
         except ValueError:
            print("Invalid mark " + a[0] + " encountered. Skipping.")
      i = 0
      j = 0
      max = 0
      while i < len(grades):
         if max < grades[i]:
            max = grades[i]
            j = i
         i = i + 1
      i = 0
      while i < len(names):
         if grades[i] == grades[j]:
            winners.append(names[i] + ",")
         i = i + 1
      winners[-1] = winners[-1].replace(",", "")
      if len(winners) == 1:
         print("Best student(s): " + str(names[j]))
      else:
         print("Best student(s): " + " ".join(winners))
      print("Best mark: " + str(grades[j]))
except FileNotFoundError:
   print("The file " + sys.argv[1] + " could not be opened")

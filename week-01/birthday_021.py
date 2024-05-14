#!/usr/bin/env python3

import sys
import calendar

for line in sys.stdin:
   s = line.strip()
   [day, month, year] = s.split()
   day = int(day)
   month = int(month)
   year = int(year)
   n = (calendar.weekday(year, month, day))
   if n == 0:
      print("You were born on a Monday and Monday's child is fair of face.")
   elif n == 1:
      print("You were born on a Tuesday and Tuesday's child is full of grace.")
   elif n == 2:
      print("You were born on a Wednesday and Wednesday's child is full of woe.")
   elif n == 3:
      print("You were born on a Thursday and Thursday's child has far to go.")
   elif n == 4:
      print("You were born on a Friday and Friday's child is loving and giving.")
   elif n == 5:
      print("You were born on a Saturday and Saturday's child works hard for a living.")
   else:
      print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")

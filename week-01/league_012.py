#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

CLUB = "CLUB"

club_max = 0

for line in lines:
   line = line[:-1]
   data = line.strip().split()
   club_len = len(" ".join(data[1:-8]))
   if club_len > club_max:
      club_max = club_len
      print(club_max)

print(f'POS {CLUB: <{club_max}s}  P   W   D   L  GF  GA  GD PTS')
i = 1

for line in lines:
   data = line.strip().split()
   club_name = " ".join(data[1:-8])
   print(f'{i:>3d} {club_name:<{club_max}s}', end=" ")
   print(f'{data[-8]:>2s} {data[-7]:>3s} {data[-6]:>3s}', end=" ")
   print(f'{data[-5]:>3s} {data[-4]:>3s} {data[-3]:>3s} {data[-2]:>3s} {data[-1]:>3s}')
   i += 1

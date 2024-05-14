#!/usr/bin/env python3

import sys


def tagger(item):
   return item[1]


dis = []
dic = {

}

score_board = []
for lines in sys.stdin:
    lines = lines.split()
    name = lines[:-3]
    name = " ".join(name)
    score = lines[-3:]
    count = 0
    try:
        for s in score:
            count = count + int(s)
    except ValueError:
        dis.append(name)
    dic[name] = count

for (key, value) in sorted(dic.items(), key=tagger):
    if key not in dis:
        print(f'{key}: {value}')

dis_people = ""
if len(dis) > 0:
    for stuff in dis:
        dis_people = dis_people + stuff + ", "
    print("Disqualified: " + dis_people[:len(dis_people) - 2])

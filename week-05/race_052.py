#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]


runners_times = {

}

for line in sys.stdin:
    new_times = []
    line = line.strip().split()
    times = line[-5:]
    name = line[:-5]
    name = "".join(name)
    for time in times:
        time = time[:-3] + time[-2:]
        new_times.append(time)
    new_times = sorted(new_times)
    new_time = int(new_times[0])
    runners_times[name] = new_time

total = sorted(runners_times.items(), key=tagger)
winner = total[0]
time = str(winner[1])
time = (time[:-2] + ":" + time[-2:])
print(f'{winner[0]} : {time}')

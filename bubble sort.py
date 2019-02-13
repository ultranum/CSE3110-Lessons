'''
title: bubble sort
author: garrett
date: 12-2-2019
'''
import time, statistics, random

timetotal = []
for i in range(30):
    li = random.sample(range(100), 100)
    print(li)
    startTime = time.perf_counter()
    for i in range(len(li)):
        for i in range(len(li)-1):
            if li[i +1] < li[i]:
                tmpval = li[i+1]
                li[i+1] = li[i]
                li[i] = tmpval

    endTime = time.perf_counter()
    print(li)
    timetotal.append(endTime-startTime)

print(statistics.mean(timetotal))
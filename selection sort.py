'''
title: 
author: garrett
date created: 2019-02-14
'''
import time, statistics, random

timetotal = []
for i in range(30):
    li = random.sample(range(10000), 10000)
    startTime = time.perf_counter()
    for u in range(len(li)-1):
        smallval = li[u]
        for i in range(u, len(li)):
            if li[i] < smallval:
                smallval = li[i]
                valpos = i
        if smallval < li[u]:
            temval = li[u]
            li[u] = li[valpos]
            li[valpos] = temval
    endTime = time.perf_counter()
    print(endTime - startTime)
    timetotal.append(endTime - startTime)
print(statistics.mean(timetotal))
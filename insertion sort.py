'''
title: 
author: garrett
date created: 2019-02-15
'''
import random, time, statistics
timetotal = []
for i in range(30):
    li = random.sample(range(1000), 1000)
    startTime = time.perf_counter()
    for u in range(len(li)-1):
        smallval = li[u]
        for i in range(u, len(li)):
            if smallval > li[i]:
                smallval = li[i]
                pos = i
                li.insert(smallval, li.pop(pos))
    endTime = time.perf_counter()
    print(endTime - startTime)
    timetotal.append(endTime - startTime)
print('average is {} seconds'.format(statistics.mean(timetotal)))
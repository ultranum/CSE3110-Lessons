'''
title: 
author: garrett
date created: 2019-02-15
'''
import random, time, statistics
timetotal = []
for i in range(30):
    li = random.sample(range(100), 100)
    print(li)
    startTime = time.perf_counter()
    # for u in range(len(li)-1):
    #     smallval = li[u]
    #     print(li)
    #     for i in range(u, len(li)):
    #         if smallval > li[i]:
    #             smallval = li[i]
    #             pos = i
    #             li.insert(smallval, li.pop(pos))
    #             print(li)
    for i in range(len(li)):
        for j in range(i, len(li)):
            if li[j] < li[i]:
                li.insert(i,li.pop(j))
    print(li)
    endTime = time.perf_counter()
    timetotal.append(endTime - startTime)
print('average is {} seconds'.format(statistics.mean(timetotal)))


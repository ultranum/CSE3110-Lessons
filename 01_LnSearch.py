'''
Title: Linear Search EX 1
Author: garrett
Date Created: 07-02-2019
'''
#Create a big array
#Find number within array

import random, time

#Array
li = []
for i in range(10):
    if random.randrange(2) == 1:
        li.append(i)

#choose random number
num = li[random.randrange(len(li))]

startTime = time.perf_counter()
#linear search
for i in range(len(li)):
    print(i, li[i])
    if li[i] == num:
        break
endTime = time.perf_counter()
print(endTime-startTime)

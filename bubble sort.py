'''
title: bubble sort
author: garrett
date: 12-2-2019
'''
li = [2,4,6,8,10,1,3,5,7,9]
length = 10
store = 0
for i in range(10):
    if li[i+1] < li[i]:
        store = li[i+1]
        li[i].append(store)
        print(li)
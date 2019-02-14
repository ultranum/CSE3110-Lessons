'''
title: 
author: garrett
date created: 2019-02-14
'''

li = [5,3,13,11,1,17,7]
for u in range(len(li)-1):
    smallval = li[u]
    for i in range(u, len(li)):
        if li[i] < smallval:
            smallval = li[i]
            valpos = i
    temval = li[u]
    li[u] = li[valpos]
    li[valpos] = temval
    print(li)
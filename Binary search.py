'''
title: Binary search
author: garrett
date created: 8-2-2019
'''

'''
numlist = [2,3,4,5,6,7,8,9,10,11,20,30,40,50,60,69,70,80,90,91,92,93,94,95,100,999]
wantednum = 80
midpoint = len(numlist)//2
while numlist[midpoint] != wantednum:
    if numlist[midpoint] == wantednum:
        break
    elif numlist[midpoint] > wantednum:
        for i in range(len(numlist)//2):
            numlist.pop()
        print(numlist)
        midpoint = len(numlist) // 2
    else:
        for i in range(len(numlist) // 2):
            numlist.pop(0)
        print(numlist)
        midpoint = len(numlist) // 2
else:
    print('got {}'.format(numlist[midpoint]))
'''

dat = [1,3,5,7,11,13,17,19,23]

def binSearch(li,val):
    start = 0  # lowest index value to calculate midpoint
    end = len(li)-1  # highest index value to calculate midpoint

    while start <= end:
        midp = (start + end) //2  # midpoint calc
        print(li[midp])
        if li[midp] == val: # found test
            return True
        elif val > li[midp]: # if the value is bigger than the midpoint,
            # redefine the lowest index value to be one higher than the midpoint index value
            start = midp + 1
        else: # if the value is smaller than the midpoint, redefine the highest index value to be one lower than the
            # midpoint
            end = midp - 1
    return False

print(binSearch(dat, 1))
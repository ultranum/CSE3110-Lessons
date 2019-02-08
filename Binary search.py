numlist = [2,3,4,5,6,7,8,9,10,11,20,30,40,50,60,70,80,90,91,92,93,94,95,100,999]
wantednum = 95
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

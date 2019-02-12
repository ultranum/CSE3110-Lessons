import random, time, math, statistics

li = []
for i in range(60000):
    if len(li) < 30000:
        if random.randrange(2) == 1:
            li.append(i)
totaltimelin = []
ttl = 0
totaltimebin = []
ttb = 0
print(len(li))
print(li)
def linear():
    for m in range(30):
        num = li[random.randrange(len(li))]
        startTime = time.perf_counter()
        for i in range(len(li)):
            if li[i] == num:
                break
        endTime = time.perf_counter()
        totaltimelin.append(endTime - startTime)
    print(statistics.mean(totaltimelin))

def binary():
    start = 0  # lowest index value to calculate midpoint
    end = len(li) - 1  # highest index value to calculate midpoint

    while start <= end:
        midp = (start + end) // 2  # midpoint calc
        print(li[midp])
        if li[midp] == val:  # found test
            return True
        elif val > li[midp]:  # if the value is bigger than the midpoint,
            # redefine the lowest index value to be one higher than the midpoint index value
            start = midp + 1
        else:  # if the value is smaller than the midpoint, redefine the highest index value to be one lower than the
            # midpoint
            end = midp - 1
    return False
linear()
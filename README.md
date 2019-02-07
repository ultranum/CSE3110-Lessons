# CSE3110 Iterative Algorithms

Iterative algohithms explore algorithm efficiency (how fast different
algorithms process). For example, there are many different techniques to sort numbers, but some are faster than others.

## Search Algorithms

### Linear Search
Linear Search is finding information in an array item by item (line by line). This method is the easiest to program, but the least efficient
```
li = [some number of values]
for i in range(len(li))
if li[i] == value:
return True
``` 
Linear searches's time to process is directly proportional to the length of the data set being processed.  The bigger the set the longer it will take.
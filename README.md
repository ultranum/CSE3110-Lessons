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

### Binary Search

Binary search follows the _divide-and-conquer_ technique of finding a value.  It takes an ordered se of date and tests the middle number.  Then it cuts the set in half and reruns the test if the midpoint is not the searched value.

### Pseudocode
1. Determine the midpoint
2. Check if the midpoint is the value
3. Is the search value larger than the midpoint? If so, redefine the lowest value to be one above the midpoint.  If not, redefine the highest value to be one below the midpoint.
4. Repeat 1-3 until value is found
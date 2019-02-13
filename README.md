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

Binary search follows the _divide-and-conquer_ technique of finding a value.  It takes an ordered set of data and tests the middle number.  Then it cuts the set in half and reruns the test if the midpoint is not the searched value.

### Pseudocode
1. Determine the midpoint
2. Check if the midpoint is the value
3. Is the search value larger than the midpoint? If so, redefine the lowest value to be one above the midpoint.  If not, redefine the highest value to be one below the midpoint.
4. Repeat 1-3 until value is found

The advantage of binary search is that it is orders of magnitude faster than linear search because it is always taking a subset that is half the original set of data.  Binary search is most effective on larger data sets rather than smaller ones.  The disadvantage of using binary search is that the data must first be sorted.

## Sorting

Just like with search algorithms, sorting algorithms have varying levels of efficiency.  There are several types of sort algorithms including Bubble Sort, Selection Sort, Insertion Sort, and Merge Sort.  More complicated sort algorithms, like the .sort() for python arrays use a combination of simpler sorts.  Python uses Timsort which is combination of merge and insertion sort designed by Tim Peters.

### Bubble Sort

Bubble Sort compares two adjacent values on the list and rearranges them from lowest to highest.  Then it moves to the next index pair and repeats the process. At the end of each iteration, the highest value will appear at the end of the list.

| 5 | 17 | 13 | 11 | 1 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 13 | 11 | 1 | 7 | 3 | __17__ |
| 5 | 3 | 11 | 1 | 7 | __13__ | __17__ |
| 5 | 3 | 7 | 1 | __11__ | __13__ | __17__ |
| 5 | 3 | 1 | __7__ | __11__ | __13__ | __17__ |
| 3 | 1 | __5__ | __7__ | __11__ | __13__ | __17__ |
| 1 | __3__ | __5__ | __7__ | __11__ | __13__ | __17__ |
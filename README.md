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
| 5 | 11 | 1 | 7 | 3 | __13__ | __17__ |
| 5 | 1 | 7 | 3 | __11__ | __13__ | __17__ |
| 1 | 5 | 3 | __7__ | __11__ | __13__ | __17__ |
| 1 | 3 | __5__ | __7__ | __11__ | __13__ | __17__ |
| 1 | __3__ | __5__ | __7__ | __11__ | __13__ | __17__ |

### Selection Sort

Selection sort identifies the smallest value in the array and compares that value to the current smallest position in the array.  If the smallest value is not in the lowest position, selection sort will switch the two values so that the current lowest position has the current lowest value.

Unlike Bubble sort, Selection sort orders the values starting at the beginning of the list and sorts towards the end.

| 5 | 17 | 13 | 11 | 1 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- |
| __1__ | 17 | 13 | 11 | 5 | 7 | 3 |
| __1__ | __3__ | 13 | 11 | 5 | 7 | 17 |
| __1__ | __3__ | __5__ | 11 | 13 | 7 | 17 |
| __1__ | __3__ | __5__ | __7__ | 13 | 11 | 17 |
| __1__ | __3__ | __5__ | __7__ | __11__ | 13 | 17 |
| __1__ | __3__ | __5__ | __7__ | __11__ | __13__ | 17 |

### Insertion Sort

Insertion sort goes through the list and inserts the lowest value into the current testing position. As it progressed through the list, more and more of the list is sorted to the left of the testing position.

Aside: There are two common sorting algorithms. One searches to the left of the current testing position, the other to the right. In general, the right search is faster because it can arrange multiple values in a single pass.

| 5 | 17 | 13 | 11 | 1 | 7 | 3 |
| --- | --- | --- | --- | --- | --- | --- |
| __1__ | 5 | 17 | 13 | 11 | 7 | 3 |
| __1__ | __3__ | 5 | 17 | 13 | 11 | 7 |
| __1__ | __3__ | __5__ | 17 | 13 | 11 | 7 |
| __1__ | __3__ | __5__ | __7__ | 11 | 13 | 17 |
| __1__ | __3__ | __5__ | __7__ | __11__ | __13__ | 17 |
| __1__ | __3__ | __5__ | __7__ | __11__ | __13__ | 17 |
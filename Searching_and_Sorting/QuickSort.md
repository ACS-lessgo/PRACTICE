# QUICK SORT

- Quicksort is a sorting algorithm based on the divide and conquer approach where

- An array is divided into subarrays by selecting a pivot element (element selected from the array).

- While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
- The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
- At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

---

## Quick Sort Algorithm
```python
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
```
---

## WORKING

![WORK](https://cdn.programiz.com/cdn/farfuture/FxRG-2wIayocfWeQvHxMmUQTKhibQiI2FLqjkIr3Vi4/mtime:1608894915/sites/tutorial2program/files/quick-sort-working.png)


![WORK](https://cdn.programiz.com/cdn/farfuture/0k2dzQ8-WHeClPRTiv9CEdX1KkqBMpS_0St0lzT9RO8/mtime:1582112622/sites/tutorial2program/files/quick-sort-1.png)

---

## Quicksort Code in Python

```python
def quicksort(arr,low,high):
	if low<=high:
		pi=partition(arr,low,high)
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)
		
def partition(arr,low,high):
	pivot=arr[high]
	i=low-1
	for j in range(low,high):
		if arr[j]<=pivot:
				 i+=1
				 arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1
```
---
## Selection Sort Complexity

|Time Complexity|   |	 
|---|---|
|Best|	O(n*log n)|
|Worst|O(n2)|
|Average|	O(n*log n)|
|Space Complexity|	 O(log n)|
|Stability|	No|
---
## Quicksort Applications
- Quicksort algorithm is used when

1. the programming language is good for recursion
1. time complexity matters
1. space complexity matters
---


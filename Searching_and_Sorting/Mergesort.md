# MERGE SORT

- Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
  
![exp](https://cdn.programiz.com/cdn/farfuture/PRTu8e23Uz212XPrrzN_uqXkVZVY_E0Ta8GZp61-zvw/mtime:1586425911/sites/tutorial2program/files/merge-sort-example_0.png)

---

## MergeSort Algorithm

![exp](https://cdn.programiz.com/cdn/farfuture/QgWYSTEJPw6dD8z1dlTcZI-SBWqa8UhVJWvleCsiFA0/mtime:1586425928/sites/tutorial2program/files/merge-two-sorted-arrays.png)

---

## Merge Sort Code in Python

```python
# MergeSort in Python


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
```
---

## Merge Sort Complexity

|Time Complexity|   |	 
|---|---|
|Best|	O(n*log n)	|
|Worst|	O(n*log n)|
|Average|	O(n*log n)	|
|Space Complexity|	 O(n)|
|Stability|	Yes|

---

## Merge Sort Applications
- Inversion count problem
- External sorting
- E-commerce applications

---

# SORTING

## Bubble Sort

- Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

---

## Working of Bubble Sort

- Starting from the first index, compare the first and the second elements.
- If the first element is greater than the second element, they are swapped.
- Now, compare the second and the third elements. 
- Swap them if they are not in order.
- The above process goes on until the last element.
---
![Bubblesort](https://cdn.programiz.com/cdn/farfuture/kn1zM7ZGIj60jcTe3mv8gAtbrvFHqxgqfQ7F9MdjPuA/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-0.png)

---

## Bubble Sort Algorithm

```python
bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort
```

## Bubble Sort Code
```python
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
```
---
## Bubble Sort Complexity

|Time Complexity|      |
|---|---|
|Best|O(n)|
|Worst|	O(n2)|
|Average|	O(n2)|
|Space Complexity|	 O(1)|
|Stability|	Yes|

---
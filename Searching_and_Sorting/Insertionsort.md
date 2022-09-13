# INSERTION SORT

- We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place.

---

## Working of Insertion Sort

![step1](https://cdn.programiz.com/cdn/farfuture/K-kSm72ww4_afH0mQJDuR3Y-fPZYgBYo_Pclx7WlYUo/mtime:1582112622/sites/tutorial2program/files/Frame%204_0.png)

- The first element in the array is assumed to be sorted. Take the second element and store it separately in `key`.

- Compare `key` with the `first element`. If the `first element` is greater than `key`, then `key` is placed in front of the `first element`.

![step1](https://cdn.programiz.com/cdn/farfuture/l-X2VCkF2rp4i0X8mZX6BGJL_FQW9EL8PkKhBswQfpc/mtime:1582112622/sites/tutorial2program/files/Insertion-sort-0_1.png)

- Now, the first two elements are sorted
  
![step2](https://cdn.programiz.com/cdn/farfuture/MqcrLAaQHEhcuJTmF_m712GG_wMemTY9AID0J9w4T6E/mtime:1582112622/sites/tutorial2program/files/Insertion-sort-1_1.png)

- repeat the same until all elements get sorted.
---
## Insertion Sort Algorithm

```python
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
```
---
## Insertion Sort in Python

```python
# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

```
---
## Insertion Sort Complexity


|Time Complexity|   |	 
|---|---|
|Best|	O(n)|
|Worst|O(n2)|
|Average|	O(n2)|
|Space Complexity|	 O(1)|
|Stability|	Yes|

---
## Insertion Sort Applications
  
  The insertion sort is used when:

- the array is has a small number of elements.
- there are only a few elements left to be sorted.

---
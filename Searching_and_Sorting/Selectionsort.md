# SELECTION SORT

- Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

---

## Working of Selection Sort

![step1](https://cdn.programiz.com/cdn/farfuture/w1ZKsO2Obaw1WV03_lamX22SVyapwhbiKoLkT5Raiiw/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-initial-array.png)

- Set first element as `mininum`.

![step2](https://cdn.programiz.com/cdn/farfuture/9jjqXX0fGtJE2ul2Mga20fvf_GkNlFAFsDMwrrwFzbQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-comparision.png)

- Compare `minimum` with the second element. If the second element is smaller than `minimum`, assign the second element as `minimum`.

![step3](https://cdn.programiz.com/cdn/farfuture/6o-qergdHNq6D7eBxBi87yIuCLc7MJy2BHR4QHeNxxQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-swapping.png)

- After each iteration, `minimum` is placed in the front of the unsorted list.

![step4](https://cdn.programiz.com/cdn/farfuture/dsZIa58W_SRP0yB21QmrWGQvrmob8yAVa94iCtIPWoo/mtime:1582112622/sites/tutorial2program/files/Selection-sort-3_1.png)

- For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.

---
## Selection Sort Algorithm
```python
def selectionSort(array, size):
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
```
---
## Selection Sort Code in Python

```python
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
```
---

## Selection Sort Complexity

|Time Complexity|   |	 
|---|---|
|Best|	O(n2)|
|Worst|O(n2)|
|Average|	O(n2)|
|Space Complexity|	 O(1)|
|Stability|	No|

---

## Selection Sort Applications

  The selection sort is used when

- a small list is to be sorted
- cost of swapping does not matter
- checking of all the elements is compulsory
- cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)

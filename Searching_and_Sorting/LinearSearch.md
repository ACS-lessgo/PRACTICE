# Linear Search 
- Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. It is the simplest searching algorithm.

![exp](https://cdn.programiz.com/sites/tutorial2program/files/linear-search-comparisons.png)

---

## Linear Search Algorithm

```python
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
```
---
## Code

```python
def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

```
---
## Linear Search Complexities

- Time Complexity: O(n)

- Space Complexity: O(1)

---
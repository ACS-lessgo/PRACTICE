# HEAP SORT
---
## Working of Heap Sort
- Since the tree satisfies Max-Heap property, then the largest item is stored at the root node.
- Swap: Remove the root element and put at the end of the array (nth position) Put the last item of the tree (heap) at the vacant place.
- Remove: Reduce the size of the heap by 1.
- Heapify: Heapify the root element again so that we have the highest element at root.
- The process is repeated until all the items of the list are sorted.
---
- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802165905/1-660x366.png)

- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802170448/3-660x366.png)

- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802170744/4-571x660.png)

- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802170850/5-660x587.png)

- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802171042/6-660x402.png)

- ![](https://media.geeksforgeeks.org/wp-content/uploads/20220802171331/7-660x195.png)

---
## Implementation of Heap Sort

```python
def heapsort(arr):
	N=len(arr)
	for i in range(N//2-1,-1,-1):
		heapify(arr,N,i)
	for i in range(N-1,0,-1):
		arr[i],arr[0]=arr[0],arr[i]
		heapify(arr,i,0)
		
def heapify(arr,N,i):
	largest=i
	l=2*i+1
	r=2*i+2
	
	if l<N and arr[largest]<arr[l]:
		largest=l
	
	if r<N and arr[largest]<arr[r]:
		largest=r
	
	if largest!=i:
		arr[i],arr[largest]=arr[largest],arr[i]
		heapify(arr,N,largest)
```
---
## Selection Sort Complexity

|Time Complexity|   |	 
|---|---|
|Best|	O(nlogn)|
|Worst|O(nlogn)|
|Average|	O(nlogn)|
|Space Complexity|	 O(1)|
|Stability|	No|

---


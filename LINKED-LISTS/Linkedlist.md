# LINKED LIST

---

## What is Linked List? 
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers. They include a series of connected nodes. Here, each node stores the data and the address of the next node.

---

![LINKED-LIST](https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png)

---

## Construction of a simple linked list

```python

# A simple Python program to introduce a linked list

# Node class


class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


# Code execution starts here
if __name__ == '__main__':

	# Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	'''
	Three nodes have been created.
	We have references to these three blocks as head,
	second and third

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | None |	 | 2 | None |	 | 3 | None |
	+----+------+	 +----+------+	 +----+------+
	'''

	llist.head.next = second # Link first node with second

	'''
	Now next of first Node refers to second. So they
	both are linked.

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | null |	 | 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''

	second.next = third # Link second node with the third node

	'''
	Now next of second Node refers to third. So all three
	nodes are linked.

	llist.head	 second			 third
		|			 |				 |
		|			 |				 |
	+----+------+	 +----+------+	 +----+------+
	| 1 | o-------->| 2 | o-------->| 3 | null |
	+----+------+	 +----+------+	 +----+------+
	'''
```
---

## Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

## Using `iterative` approach
```python
def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values
```
## Using `recursive` approach
```python
def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)
```
---
## Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

## Using `iterative` approach
```python
def sum_list(head):
  total_sum = 0
  current = head
  while current is not None:
    total_sum += current.val
    current = current.next
  return total_sum
```
## Using `recursive` approach
```python
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
```
---
## Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.


## Using `iterative` approach
```python
def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    
    current = current.next
    count += 1
    
  return None
```
## Using `recursive` approach
```python
def get_node_value(head, index):
  if head is None:
    return None
  
  if index == 0:
    return head.val
  
  return get_node_value(head.next, index - 1)
```
---
## Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

## Using `iterative` approach
```python
def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev
```
## Using `recursive` approach
```python
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
```
---
## Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.

## Using `iterative` approach
```python
def zipper_lists(head_1, head_2):
  tail=head_1
  current1=head_1.next
  current2=head_2
  count=0
  while current2 and current1 is not None:
    if count%2==0:
      tail.next=current2
      current2=current2.next
    else:
      tail.next=current1
      current1=current1.next
    tail=tail.next
    count+=1
    
  if current1 is not None:
    tail.next=current1
  if current2 is not None:
    tail.next=current2
  return head_1
```

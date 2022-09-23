# BINARY TREE

- Binary Tree is defined as a Tree data structure with at most 2 children. 
- Since each element in a binary tree can have only 2 children
- we typically name them the left and right child.

---

## Binary Tree structure

- Data
- Pointer to left child
- Pointer to right child

![BinaryTree](https://cdn.programiz.com/sites/tutorial2program/files/binary-tree-representation_0.png)

---
## Advantages and Disadvantages of Binary Trees

- They can be used to reflect relationships between data.
- They can store an arbitrary number of data values.

---
## Create Node
```python
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
```
---

## Insert values to a tree
```python
def insert(self,value):
        if value<self.value:
            if self.left is  None:
                self.left  = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is  None:
                self.right=TreeNode(value)
            else:
                self.right.insert(value)
```
---
## Traverse through a Tree
- Inorder
```python
def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value,end="->")
        if self.right:
            self.right.inorder()
```
---
- Preorder
```python
def preoder(self):
        print(self.value,end="->")
        if self.left:
            self.left.preoder()
        if self.right:
            self.right.preoder()
```
---
- Postorder
```python
def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value,end="->")
```
---
- Levelorder
```python
def levelorder(root):
            traversed = []
            traversed.append(root)
            if root is None:
                return traversed
            while traversed != []:
                print(traversed[0].value,"->",end=" ")
                x = traversed.pop(0) 
                if x.left:
                    traversed.append(x.left)
                if x.right:
                    traversed.append(x.right)
```
---
## Finding an Element in a Tree
```python
    def find(self,value):
        if value<self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value>self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
```
---
## Count of nodes
```python
def countofnodes(root):
    if root is None:
        return 0
    leftnodes = countofnodes(root.left)
    rigthnodes= countofnodes(root.right)
    return 1+leftnodes+rigthnodes
```
---
## Sum of nodes
```python
def sumofnodes(root):
    if root is None:
        return 0
    leftsum=sumofnodes(root.left)
    roghtsum=sumofnodes(root.right)
    return root.value+leftsum+rightsum
```
---
## Height of a Tree
```python
def heightoftree(root):
    if root is None:
        return 0
    left_h=heightoftree(root.left)
    right_h=heightoftree(root.right)
    height=max(left_h,right_h)
    return 1+height
```
---
## Diameter of a Tree
```python
def diameter(root):
    if root is None:
        return 0
    dia1=diameter(root.left)
    dia2=diameter(root.right)
    dia3=heightoftree(root.left)+heightoftree(root.right)
    return max(dia3,max(dia2,dia1))
```
---
## Mirrot a Tree
```python
class Tree:
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

def inorder(root):
	if root.left:
		inorder(root.left)
	print(root.val,end=" ")
	if root.right:
		inorder(root.right)
		
def mirror(root):
	if root is None:
		return
	else:
		temp=root
		
		mirror(root.left)
		mirror(root.right)
		
		temp=root.left
		root.left=root.right
		root.right=temp
```
---

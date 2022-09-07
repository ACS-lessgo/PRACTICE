# BINARY TREE

## Binary Tree structure
![BinaryTree](https://cdn.programiz.com/sites/tutorial2program/files/binary-tree-representation_0.png)

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

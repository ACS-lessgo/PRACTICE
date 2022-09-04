# **GRAPHS**
---
## Depth first using recursion:
```python
def depfirst(graph,source):
	print(source)
	
	for neighbour in graph[source]:
		depfirst(graph,neighbour)
## driver code
graph={'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]}
depfirst(graph,'a')

```
---
## depth first traversal algo using iterative method :
```python
def depfirst(graph,node):
	stack=[node]
	while len(stack)>0:
		current=stack.pop()
		print(current)
		
		for neighbour in graph[current]:
			stack.extend(neighbour)

#driver code			
graph={'a':['c','b'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]}
depfirst(graph,'a')
```
---
## Breadth first algo :
```python
def breadfirst(graph,source):
	queue=[source]
	while len(queue)>0:
		current = queue.pop(0)
		print(current)
		
		for neighbour in graph[current]:
			queue.append(neighbour)

#driver code			
graph={'a':['c','b'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]}
breadfirst(graph,'a')  
```
---
## To find if a path exists bw 2 nodes
```python
def haspath(graph,src,dst):
	if (src==dst):
		print("path found")
	for neighbour in graph[src]:
			if haspath(graph,neighbour,dst)==True:
			 	 return True
	return False
	
#driver code					
graph = {'f': ['g', 'i'],'g': ['h'],'h': [], 'i': ['g', 'k'],'j': ['i'],'k': []}
haspath(graph, 'f', 'j')
```

---

# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

```python
from collections import defaultdict
visited=set()
def undirected_path(edges, node_A, node_B):
  	graph=build_graph(edges)
  	return haspath(graph,node_A,node_B,visited)

def haspath(graph,src,dst,visited):
	if src==dst:return True
	if src in visited:return False
	visited.add(src)
	for neighbour in graph[src]:
		if haspath(graph,neighbour,dst,visited)==True:
			return True
	return False


def build_graph(edges):
	graph = defaultdict(list)
	for edge in edges:
		a, b = edge[0], edge[1]
		graph[a].append(b)
		graph[b].append(a)
	return graph

#DRIVER CODE

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

x=undirected_path(edges, 'k', 'o')
print(x)
```
---
## CONNECTED COMPONENTS COUNT
```python
visited=set()
def connected_components_count(graph):
	count=0
	for node in graph:
		#print(graph)
		if explore(graph,node,visited)==True:
			count+=1
	return count
		
def explore(graph,current,visited):
	if str(current) in visited:
		return False
	visited.add(str(current))
	for neighbour in graph[current]:
		explore(graph,neighbour,visited)
	return True


#DRIVER CODE
x=connected_components_count({ 3: [],4: [6],6: [4, 5, 7, 8],8: [6], 7: [6], 5: [6], 1: [2], 2: [1] }) 
print(x)
```
---
## LARGEST COMPONENT
```python
visited=set()
def largestComponent(graph):
	longest=0
	for node in graph:
		size=exploreSize(graph,node,visited)
		if size>longest:
			longest=size
	return longest

def exploreSize(graph,node,visited):
	if node in visited:return False
	visited.add(node)
	size=1
	for neighbour in graph[node]:
		size+=exploreSize(graph,neighbour,visited)
	return size
	
#DRIVER CODE

x=largestComponent({ 0: [8, 1, 5], 1: [0],5: [0, 8],8: [0, 5], 2: [3, 4],3: [2, 4],4: [3, 2]})
print(x)
```
---
## SHORTEST PATH BW 2 NODES

```python
from collections import defaultdict
def buildgraph(edges):
	graph=defaultdict(list)
	for edge in edges:
		a,b=edge[0],edge[1]
		graph[a].append(b)
		graph[b].append(a)
	return graph


			
def shortest_path(edges,nodeA,nodeB):
	visited=set([nodeA])
	graph=buildgraph(edges)
	queue=[[nodeA,0]]
	while len(queue)>0:
		[node,distance]=queue.pop(0)
		if node==nodeB:
			return distance
		for neighbour in graph[node]:
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append([neighbour,distance+1])
	return -1	

#driver code

edges = [['w', 'x'],['x', 'y'],['z', 'y'],['z', 'v'],['w', 'v']]
x=shortest_path(edges, 'w', 'z')
print(x)
```
---
## ISLAND COUNT
```python
def island_count(grid):
	visited=set()
	count=0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if explore(grid,i,j,visited)==True:
				count+=1
	return count
			

def explore(grid,i,j,visited):
	rowinbounds=0<=i<len(grid)
	colinbounds=0<=j<len(grid[0])
	if not  rowinbounds or not colinbounds:return False
	if grid[i][j]=='W':return False
	pos=i,j
	if pos in visited:return False
	visited.add(pos)
	explore(grid,i-1,j,visited)
	explore(grid,i+1,j,visited)
	explore(grid,i,j+1,visited)
	explore(grid,i,j-1,visited)
	
	return True
	
#driver code
grid = [
  ['W', 'W'],
  ['W', 'W']]

x=island_count(grid)	
print(x)
```
---
## MINIMUM ISLAND FINDER
```python
def minimum_island(grid):
	visited=set()
	minsize=20
	for r in range(len(grid)):
		for c in range(len(grid[0])):
					size = exploresize(grid,r,c,visited)
					if size>0 and size<minsize:
					  	 minsize=size
	return minsize
					   
def exploresize(grid,r,c,visited):
						ri= 0<=r<len(grid)
						ci= 0<=c<len(grid[0])
						if not ri or not ci:
							return 0
						if grid[r][c]=='W':
							return 0
						pos=(r,c)
						if pos in visited:
							return 0
						visited.add(pos)
						size=1
						size+=exploresize(grid,r-1,c,visited)
						size+=exploresize(grid,r+1,c,visited)
						size+=exploresize(grid,r,c-1,visited)
						size+=exploresize(grid,r,c+1,visited)
						return size
						
					
#DRIVER CODE
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

X=minimum_island(grid)
print(X)
```
---

					    
					    
					    
					  	
					 	
					  	
		
					   
					   
					   
		
		



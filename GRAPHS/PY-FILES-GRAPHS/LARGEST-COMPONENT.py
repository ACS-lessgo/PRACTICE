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
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
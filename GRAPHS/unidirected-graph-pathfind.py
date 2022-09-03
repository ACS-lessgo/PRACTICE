"""
Write a function, undirected_path, that takes in a list of edges 
for an undirected graph and two nodes (node_A, node_B). 
The function should return a boolean 
indicating whether or not there exists a 
path between node_A and node_B.
"""
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
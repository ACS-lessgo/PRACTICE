#To find if a path exists bw 2 nodes

def haspath(graph,src,dst):
	if (src==dst):
		print("path found")
	for neighbour in graph[src]:
			if haspath(graph,neighbour,dst)==True:
			 	 return True
	return False
	
#driver code					
graph = {'f': ['g', 'i'],'g': ['h'],'h': [], 'i': ['g', 'k'],'j': ['i'],'k': []}
haspath(graph, 'f', 'i')

#Depth first using recursion:
def depfirst(graph,source):
	print(source)
	
	for neighbour in graph[source]:
		depfirst(graph,neighbour)

#driver code			
graph={'a':['b','c'],'b':['d'],'c':['e'],'d':['f'],'e':[],'f':[]}
depfirst(graph,'a')
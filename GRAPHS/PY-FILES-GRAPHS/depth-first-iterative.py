#depth first traversal algo using iterative method :
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
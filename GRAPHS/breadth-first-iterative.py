#Breadth first algo :
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
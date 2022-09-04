#CONNECTED COMPONENTS COUNT

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


class graph:
	def __init__(self,vertices):
		self.V=vertices
		self.graph=[[0 for col in range(vertices)] for row in range(vertices)]
	
	
	def dijkstra(self,src):
		arr=[1e7]*self.V
		arr[src]=0
		sptset = [False] * self.V
		for i in range(self.V):
			u=self.minD(arr,sptset)
			sptset[u]=True
			
			for v in range(self.V):
				if self.graph[u][v]>0 and sptset[v] == False and arr[v]>arr[u]+self.graph[u][v]:
					arr[v]=arr[u]+self.graph[u][v]
		self.printer(arr)
	
	def minD(self,arr,sptset):
		min=1e7
		for v in range(self.V):
			if arr[v]<min and sptset[v]==False:
					min=arr[v]
					min_index=v
		return min_index
	
	def printer(self,arr):
		print("Source \t shortest dist from src")
		for node in range(self.V):
					print(node,"\t\t",arr[node])

		
		
		
# DRIVER CODE		
g = graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(4)
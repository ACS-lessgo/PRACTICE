#MINIMUM ISLAND FINDER

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
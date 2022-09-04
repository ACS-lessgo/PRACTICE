#ISLAND COUNT

def island_count(grid):
	visited=set()
	count=0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if explore(grid,i,j,visited)==True:
				count+=1
	return count
			

def explore(grid,i,j,visited):
	rowinbounds=0<=i<len(grid)
	colinbounds=0<=j<len(grid[0])
	if not  rowinbounds or not colinbounds:return False
	if grid[i][j]=='W':return False
	pos=i,j
	if pos in visited:return False
	visited.add(pos)
	explore(grid,i-1,j,visited)
	explore(grid,i+1,j,visited)
	explore(grid,i,j+1,visited)
	explore(grid,i,j-1,visited)
	
	return True
	
#driver code
grid = [['W', 'W','L'],['L', 'W','L'],['L', 'W','L']]

x=island_count(grid)	
print(x)
	
#MINIMUM ISLAND FINDER
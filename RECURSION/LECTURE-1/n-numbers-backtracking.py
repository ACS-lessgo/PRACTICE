#3. PRINT N NOS USING BACKTRACKING

def printer(i,n):
	if i<1:
		return
	printer(i-1,n)
	print(i)

n=int(input("enter a no"))
i=int(input("enter a upto"))
x=printer(i,n)
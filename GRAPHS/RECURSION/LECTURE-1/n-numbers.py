#2. PRINT N NOS USING RECURSION
def printer(n):
	if n:
		print(n)
		return printer(n-1)

n=int(input("enter a no"))
x=printer(n)
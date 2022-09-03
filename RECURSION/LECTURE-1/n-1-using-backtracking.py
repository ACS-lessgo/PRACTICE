#4. PRINT NOS FROM N->1 USING BACKTRACKING

def printer(i,n):
	if i>n:
		return
	printer(i+1,n)
	print(i)

n=int(input("enter a no"))
x=printer(1,n)
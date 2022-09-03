#1. PRINT UR NAME N TIMES
def printer(name,n):
	if n>0:
		print(name)
		printer(name,n-1)
x=input("enter name")
times=int(input("enter the times to print"))
new=printer(x,times)
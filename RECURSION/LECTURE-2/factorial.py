#6. FACTORIAL ON N NUMBERS

def facto(n):
	if n==0:
		return 1
	elif n<=1:
		return n
	return n*facto(n-1)

n=int(input("enter a no"))
x=facto(n)
print(x)
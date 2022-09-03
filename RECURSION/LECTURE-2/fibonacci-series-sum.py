#9. FIBONACCI OF N NUMBERS

def fibo(n):
	if n<=1:
		return n
	last=fibo(n-1)
	slast=fibo(n-2)
	return last+slast

n=int(input("enter a no"))
x=fibo(n)
print(x)
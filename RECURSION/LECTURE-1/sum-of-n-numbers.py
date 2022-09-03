#5. SUM OF N NUMBERS USING RECURSION

def rsum(n):
	if n<=1:
		return n
	return n + rsum(n-1)
x=rsum(2)
print(x)
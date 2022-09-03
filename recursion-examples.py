#1. PRINT UR NAME N TIMES
def printer(name,n):
	if n>0:
		print(name)
		printer(name,n-1)
x=input("enter name")
times=int(input("enter the times to print"))
new=printer(x,times)

#2. PRINT N NOS USING RECURSION
def printer(n):
	if n:
		print(n)
		return printer(n-1)

n=int(input("enter a no"))
x=printer(n)

#3. PRINT N NOS USING BACKTRACKING

def printer(i,n):
	if i<1:
		return
	printer(i-1,n)
	print(i)

n=int(input("enter a no"))
i=int(input("enter a upto"))
x=printer(i,n)


#4. PRINT NOS FROM N->1 USING BACKTRACKING

def printer(i,n):
	if i>n:
		return
	printer(i+1,n)
	print(i)

n=int(input("enter a no"))
x=printer(1,n)

#5. SUM OF N NUMBERS USING RECURSION

def rsum(n):
	if n<=1:
		return n
	return n + rsum(n-1)
x=rsum(2)
print(x)

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

#7. REVERSING AN ARRAY

def rswap(arr,i=0):
	n=len(arr)
	if i>(len(arr)/2):
		return
	arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
	rswap(arr,i+1)

arr=[1,2,3,4,5]
print("before reverse",arr)
rswap(arr)
print("after reverse",arr)

#8. PALINDROME USING RECURSION

def palindrome(s,i=0):
	n=len(s)
	if i>(n/2):
		return
	if s[i]!=s[n-i-1]:
		return False
	return(s,i+1)

s="awa"
print(s)
print(palindrome(s))

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

#10. PRINT ALL THE SUBSEQUENCE OF AN ARRAY USING RECCURSION

def subs(arr, i, subarr):
	if i == len(arr):
		if len(subarr) != 0:
			print(subarr)
	else:
		subs(arr, i + 1, subarr)
		subs(arr, i + 1,subarr+[arr[i]])
	return
		
arr = [3,1,2]
subs(arr, 0, [])

#11. SUBSEQUENCE SUM

def subs(arr, i, subarr):
	if i == len(arr):
		if sum(subarr)==2 :
			print(subarr)
	else:
		subs(arr, i + 1, subarr)
		subs(arr, i + 1,subarr+[arr[i]])
	return
		
arr = [1,2,1]
subs(arr, 0, [])

#12. PRINT ONLY ONE SUBSEQUENCE

def subs(arr, i, subarr):
	if i == len(arr):
		if sum(subarr)==2 :
			print(subarr)
			return True
	else:
		if(subs(arr, i + 1, subarr)==True):return True
		if(subs(arr, i + 1,subarr+[arr[i]])):return True
		
	return False
		
arr = [1,2,1]
subs(arr, 0, [])


#13. COMBINATION SUM

def combo(ind,target,arr,ans,sub):
	if ind==len(arr):
		if target==0:
			ans.append(sub)
			print(ans)
		return
	if arr[ind]<=target:
		sub.append(arr[ind])
		combo(ind,target-arr[ind],arr,ans,sub)
		sub.remove(arr[ind])
	combo(ind+1,target,arr,ans,sub)

arr=[1,2,3,1,1]
target=4
combo(0,target,arr,[],[])

#COMBINATION SUM-2

def combo(ind,target,arr,ans,sarr):
	if target==0:
		ans.append(sarr)
		return ans
	for i in range(len(arr)):
		if(i>ind and arr[i]==arr[i-1]):continue
		if(arr[i]>target):break
		sarr.append(arr[i])
		combo(i+1,target-arr[i],arr,ans,sarr)
		sarr.remove(arr[i])

arr=[1,1,2,2]
target=4
combo(0,target,arr,[],[])





















	

	


















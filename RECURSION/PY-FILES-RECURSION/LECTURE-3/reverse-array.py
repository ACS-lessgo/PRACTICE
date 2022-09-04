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
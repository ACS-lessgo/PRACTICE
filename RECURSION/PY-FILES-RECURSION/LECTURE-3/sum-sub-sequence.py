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
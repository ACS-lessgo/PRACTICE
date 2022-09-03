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
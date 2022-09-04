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
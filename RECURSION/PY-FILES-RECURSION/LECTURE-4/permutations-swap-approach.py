#PRINT ALL PERMUTATIONS OF A LIST
def conv(list):
	return ''.join(list)


def rpermute(arr,start,end):
	if start==end:
		print(conv(arr))
	else:
		for i in range(start,end):
			arr[start],arr[i]=arr[i],arr[start]
			rpermute(arr,start+1,end)
			arr[start],arr[i]=arr[i],arr[start]

string="AA"
n=len(string)
a=list(string)
rpermute(a,0,n)


			
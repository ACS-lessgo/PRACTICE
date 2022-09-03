def countOfSubsequencesWithSumK(arr, desiredSum, index = 0, sum = 0):
    	if index >= len(arr):
         	if sum == desiredSum:
         	   	return 1
         	return 0
    

    	l = countOfSubsequencesWithSumK(arr, desiredSum, index + 1, sum + arr[index])
    	r = countOfSubsequencesWithSumK(arr, desiredSum, index + 1, sum)
     	return l + r

print(countOfSubsequencesWithSumK([1, 2, 1], 2))
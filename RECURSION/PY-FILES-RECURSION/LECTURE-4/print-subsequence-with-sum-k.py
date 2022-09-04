def printAnySubsequenceWithSumK(arr, desiredSum, index=0, tempArr=list(), sum=0):
     	if index >= len(arr):
         # Condition satisfied - return True
         	if sum == desiredSum:
            	 print(tempArr)
             	return True
        # Return false if condition not satisfied
        return False

     	tempArr.append(arr[index])
     	if(printAnySubsequenceWithSumK(arr, desiredSum, index + 1, tempArr, sum + arr[index])):
         	return True
     	tempArr.pop()
     	if(printAnySubsequenceWithSumK(arr, desiredSum, index + 1, tempArr, sum)):
         	return True
    	return False
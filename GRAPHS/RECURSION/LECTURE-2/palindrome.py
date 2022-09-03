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
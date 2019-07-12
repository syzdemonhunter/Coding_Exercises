# T: O(n)
# S: O(1)

def isPalindrome(string):
	if not string or len(string) == 0:
		return True
	
	i, j = 0, len(string) - 1
	while i < j:
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1
		
	return True
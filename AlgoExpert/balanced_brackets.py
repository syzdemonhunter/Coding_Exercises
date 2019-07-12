# T: O(n)
# S: O(n)

def balancedBrackets(string):
	if not string or len(string) == 0:
		return True
	
	stack = []
	for s in string:
		if s == '(':
			stack.append(')')
		elif s == '[':
			stack.append(']')
		elif s == '{':
			stack.append('}')
		else:
			if not stack or stack.pop() != s:
				return False
			
	return not stack
# T: O(2^n)
# S: O(n)
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n - 1) + getNthFib(n - 2)

# T: O(n)
# S: O(n)
def getNthFib(n, memoize={1:0, 2:1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
		return memoize[n]


# T: O(n)
# S: O(1)
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
		
	last_two = [0, 1]
	count = 3

	while count <= n:
		next_fib = last_two[0] + last_two[1]
		last_two[0] = last_two[1]
		last_two[1] = next_fib
		count += 1

	return last_two[1]



# T: O(n)
# S: O(1)

def getNthFib(n):
    # Write your code here.
	if n == 1:
		return 0
	if n == 2:
		return 1
	
	pre_pre = 0
	pre = 1
	
	for _ in range(2, n):
		cur = pre_pre + pre
		pre_pre = pre
		pre = cur
		
	return pre
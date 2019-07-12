# T: O(n^2)
# S: O(1)

def twoNumberSum(array, targetSum):
	if not array or len(array) < 2:
		return []

	for i in range(len(array) - 1):
		first_num = array[i]
		for j in range(i + 1, len(array)):
			second_num = array[j]
			if first_num + second_num == targetSum:
				return sorted([first_num, second_num])
	return []

# T: O(n)
# S: O(n)

def twoNumberSum(array, targetSum):
	if not array or len(array) < 2:
		return []

	seen = {}
	for num in array:
		potential_match = targetSum - num
		if potential_match in seen:
			return sorted([potential_match, num])
		else:
			seen[num] = True

	return []

# T: O(nlogn)
# S: O(1)

def twoNumberSum(array, targetSum):
	if not array or len(array) < 2:
		return []

	array.sort()
	i, j = 0, len(array) - 1
	while i < j:
		current_sum = array[i] + array[j]
		if current_sum == targetSum:
			return [array[i], array[j]]

		elif current_sum < targetSum:
			i += 1
		elif current_sum > targetSum:
			j -= 1

	return []
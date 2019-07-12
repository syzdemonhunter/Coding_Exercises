# T: O(n)
# S: O(1)

def kadanesAlgorithm(nums):
	result = nums[0]
	max_end = nums[0]

	for num in nums[1:]:
		max_end = max(num, max_end + num)
		result = max(result, max_end)

	return result
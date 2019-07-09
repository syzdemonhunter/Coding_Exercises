# T: O(n)
# S: O(1)

def maxSubsetSumNoAdjacent(arr):
	if not arr or len(arr) == 0:
		return 0

	elif len(arr) == 1:
		return arr[0]

	first = arr[0]
	second = max(arr[0], arr[1])
	for i in range(2, len(arr)):
		cur = max(second, first + arr[i])
		first = second
		second = cur

	return second

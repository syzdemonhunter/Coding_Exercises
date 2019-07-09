# T: O(nlog(n) + mlog(m))
# S: O(1)

def smallestDifference(arr1, arr2):
	arr1.sort()
	arr2.sort()

	idx_1, idx_2 = 0, 0
	min_val, cur, min_pair = float('inf'), float('inf'), []

	while idx_1 < len(arr1) and idx_2 < len(arr2):
		first = arr1[idx_1]
		second = arr2[idx_2]

		if first < second:
			cur = second - first
			idx_1 += 1
		elif second < first:
			cur = first - second
			idx_2 += 1

		else:
			return [first, second]

		if min_val > cur:
			min_val = cur
			min_pair = [first, second]

	return min_pair

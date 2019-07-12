# T: O(nlogn)
# S: O(1)

def binarySearch(array, target):
    # Write your code here.
	if not array:
		return -1

	start = 0
	end = len(array) - 1
	while start + 1 < end:
		mid = start + (end - start)//2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid
		else:
			start = mid
			
	if array[start] == target:
		return start
	if array[end] == target:
		return end
	return -1
			
			
			

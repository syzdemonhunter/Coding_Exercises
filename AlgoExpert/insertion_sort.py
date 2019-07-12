# T: O(n)
# S: O(1)

def insertionSort(array):
    # Write your code here.
	i = 1
	while i < len(array):
		j = i
		while j > 0 and array[j - 1] > array[j]:
			array[j], array[j - 1] = array[j - 1], array[j]
			j -= 1
		i += 1
		
	return array
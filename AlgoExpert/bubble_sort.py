# T: O(n^2)
# S: O(1)

def bubbleSort(array):
	is_sorted = False
	count = 0
	
	while not is_sorted:
		is_sorted = True
		for i in range(len(array) - 1 - count):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				is_sorted = False
				
		count += 1

	return array
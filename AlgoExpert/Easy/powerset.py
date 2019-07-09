# T: O(n*2^n)
# S: O(n*2^n)

def powerset(array):
	if not array or len(array) == 0:
		return [[]]

	result = []
	dfs(result, [], array, 0)
	return result

def dfs(result, path, array, idx):
	result.append(path)
	for i in range(idx, len(array)):
		dfs(result, path + [array[i]], array, i + 1)
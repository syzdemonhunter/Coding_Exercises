# T: O(n!*n)
# S: O(n)

def getPermutations(nums):
    if not nums or len(nums) == 0:
        return []
    
    result = []
    dfs(result, [], nums)
    return result
    
def dfs(result, path, nums):
    if len(path) == len(nums):
        result.append(path)
        return

    for i in range(len(nums)):
        if nums[i] in path:
            continue
        dfs(result, path + [nums[i]], nums)
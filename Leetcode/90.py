# https://leetcode.com/problems/subsets-ii/
# T: O(2^n)
# S: O(n)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return result
        
        nums.sort()
        result = []
        self.dfs(result, [], nums, 0)
        return result
    
    def dfs(self, result, path, nums, index):
        result.append(path)
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]: #去重
                continue
            self.dfs(result, path + [nums[i]], nums, i + 1)
        
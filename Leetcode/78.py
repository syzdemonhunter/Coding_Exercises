# https://leetcode.com/problems/subsets/
# T: O(2^n)
# S: O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        
        result = []
        self.dfs(result, [], nums, 0)
        return result
    
    def dfs(self, result, path, nums, index):
        result.append(path)
        for i in range(index, len(nums)):
            self.dfs(result, path + [nums[i]], nums, i + 1)
        
        
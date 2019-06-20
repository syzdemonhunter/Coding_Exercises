# https://leetcode.com/problems/permutations/
# T: O(n!*n)
# S: O(n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        result = []
        self.dfs(result, [], nums)
        return result
    
    def dfs(self, result, path, nums):
        if len(path) == len(nums):
            result.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self.dfs(result, path + [nums[i]], nums)
            
            
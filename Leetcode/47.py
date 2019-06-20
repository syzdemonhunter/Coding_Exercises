# https://leetcode.com/problems/permutations-ii/
# T: O(n!*n)
# S: O(n)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        result = []
        nums.sort()
        self.dfs(result, [], nums, [False]*len(nums))
        return result
        
    def dfs(self, result, path, nums, used):
        if len(path) == len(nums):
            result.append(path)
            
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            self.dfs(result, path + [nums[i]], nums, used[:i] + [True] + used[i + 1:])
        
        
        
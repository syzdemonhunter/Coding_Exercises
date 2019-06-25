# https://leetcode.com/problems/combination-sum-iv/
# DP: result[i] += result[i - num]
# DFS + {}

'''
# T: O(n*k)
# S: O(k)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = [0]*(target + 1)
        result[0] = 1
        
        for i in range(1, len(result)):
            for num in nums:
                if i - num >= 0:
                    result[i] += result[i - num]
                    
        return result[target]
'''
# T: O(2^n)
# S: O(n)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        dic = {}
        return self.helper(nums, target, dic)
    
    def helper(self, nums, target, dic):
        if target == 0:
            return 1
        if target < 0:
            return 0
        
        if target in dic:
            return dic[target]
        
        result = 0
        for i in range(len(nums)):
            result += self.helper(nums, target - nums[i], dic)
            
        dic[target] = result
        return result
        
        

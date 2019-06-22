# https://leetcode.com/problems/first-missing-positive/
# T: O(n)
# S: O(1)
# 这道题需要重视

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 1
        
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] -1] != nums[i]:
                nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
            
        return len(nums) + 1
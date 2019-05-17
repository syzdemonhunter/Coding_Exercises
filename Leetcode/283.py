# https://leetcode.com/problems/move-zeroes/
# T: O(n)
# S: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return 0
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                
        for i in range(slow, len(nums)):
            nums[i] = 0
# https://leetcode.com/problems/move-zeroes/

'''
# T: O(n)
# S: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return
        
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
                
        while start < len(nums):
            nums[start] = 0
            start += 1
'''
# T: O(n)
# S: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        if not nums or len(nums) == 0:
            return
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
        
                
        
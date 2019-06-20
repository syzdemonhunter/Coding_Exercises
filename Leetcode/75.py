# https://leetcode.com/problems/sort-colors/
# T: O(n)
# S: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return
        left, right = 0, len(nums) - 1 # left 0 position, right 1 starting point
        index = 0
        while index <= right:
            if nums[index] == 0:
                self.swap(nums, index, left)
                index += 1
                left += 1
            elif nums[index] == 1:
                index += 1
            else:
                self.swap(nums, index, right)
                right -= 1
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
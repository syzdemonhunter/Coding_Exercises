# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# T: O(log(n))
# S: O(1)


class Solution(object):
    def bin_search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        end = self.bin_search(nums, target)
        start = self.bin_search(nums, target - 1) + 1
        if start >= 0 and start <= end and end < len(nums):
            return [start, end]
        else:
            return [-1, -1]
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# T: O(log(n))
# S: O(1)


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        low, high = 0, len(nums) - 1
        
        while low < high:
            if nums[low] < nums[high]:
                return nums[low]
            
            mid = low + (high - low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# T: O(log(n))
# S: O(1)

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                mid -= 1
            elif mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                pass
            else:
                return nums[mid]
            
            if (mid - low) % 2 == 1:
                high = mid - 1
            else:
                low = mid + 2
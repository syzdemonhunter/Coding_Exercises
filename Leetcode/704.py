# https://leetcode.com/problems/binary-search/
# T: O(log(n))
# S: O(1)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low)//2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
            
        return -1
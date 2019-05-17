# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# T: O(n)
# S: O(1)


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        i, j = 0, length - 1
        
        while i < length - 1 and nums[i] <= nums[i + 1]:
            i += 1
        while j > 0 and nums[j] >= nums[j - 1]:
            j -= 1
    
        min_val, max_val= 2 ** 31, - (2 ** 31)
        for k in range(i, j + 1):
            min_val = min(nums[k], min_val)
            max_val = max(nums[k], max_val)
        while i >= 0 and min_val < nums[i]:
            i -= 1
        while j < length and max_val > nums[j]:
            j += 1
        # i + 1 ~ j - 1
        return max(j - i - 1, 0)
            
        
# https://leetcode.com/problems/maximum-subarray/
# T: O(n)
# S: O(1)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -float('inf')
        cur = 0
        
        for i in range(len(nums)):
            if cur <= 0:
                cur = nums[i]
            else:
                cur += nums[i]
            max_so_far = max(max_so_far, cur)
            
        return max_so_far
            
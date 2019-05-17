# https://leetcode.com/problems/maximum-product-subarray/
# T: O(n)
# S: O(1)


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cur_max = cur_min = global_max = nums[0]
        for i in range(1, len(nums)):
            a = cur_max*nums[i]
            b = cur_min*nums[i]
            c = nums[i]
            
            cur_max = max(max(a, b), c)
            cur_min = min(min(a, b), c)
            global_max = max(cur_max, global_max)
            
        return global_max
# https://leetcode.com/problems/house-robber/
# T: O(n)
# S: O(1)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        pre, pre_pre = 0, 0
        for num in nums:
            cur = max(pre, pre_pre + num)
            pre_pre = pre
            pre = cur
        return pre
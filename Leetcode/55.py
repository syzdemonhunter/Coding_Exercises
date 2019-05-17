# https://leetcode.com/problems/jump-game/
# time: O(n)
# space: O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        max_len = 0
        for i in range(len(nums)):
            if max_len >= len(nums) - 1:
                return True
            if i > max_len:
                return False
            max_len = max(nums[i] + i, max_len)
        return False
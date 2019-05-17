# https://leetcode.com/problems/rotate-array/submissions/
# T: O(n)
# S: O(1)


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if not nums or len(nums) == 0 or k <= 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        
# https://leetcode.com/problems/two-sum/submissions/
# T: O(n)
# S: O(n)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return seen[target - num], idx
            
            seen[num] = idx
            
# https://leetcode.com/problems/single-number/
# T: O(n)
# S: O(n)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)
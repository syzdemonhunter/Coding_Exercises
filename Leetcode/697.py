# https://leetcode.com/problems/degree-of-an-array/
# first keep 第一次出现的index
# last keep最后一次出现的index
# T: O(n)
# S: O(n)
import collections

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        count = collections.Counter(nums)
        first, last = {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            
        degree = max(count.values())
        return min(last[v] - first[v] + 1 for v in count if count[v] == degree)
        
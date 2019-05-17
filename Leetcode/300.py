# https://leetcode.com/problems/longest-increasing-subsequence/
# T: O(n^2)
# S: O(n)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        n = len(nums)
        max_so_far = 1
        d = [1]*n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[i], d[j] + 1)
                    
            max_so_far = max(max_so_far, d[i])
            
        return max_so_far
        
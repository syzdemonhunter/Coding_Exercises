# https://leetcode.com/problems/longest-increasing-subsequence/
# 这道题非常重要
# T: O(nlogn)
# S: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0]*len(nums)
        result = 0
        for num in nums:
            i, j = 0, result
            while i != j:
                mid = (i + j)//2
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            if i == result:
                result += 1
                
        return result
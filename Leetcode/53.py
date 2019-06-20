# https://leetcode.com/problems/maximum-subarray/
# T: O(n)
# S: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]
            result = max(result, dp[i])
            
        return result
        
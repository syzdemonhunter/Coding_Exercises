# https://leetcode.com/problems/maximum-subarray/
'''
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
'''
# T: O(n)
# S: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        max_end = nums[0]
        
        for num in nums[1:]:
            max_end = max(num, max_end + num)
            result = max(result, max_end)
            
        return result

        
# https://leetcode.com/problems/burst-balloons/
# T: O(n^3)
# S: O(n^2)

# dp 为打破的气球为i ~ j之间
# nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> [1]
# coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167
# dp[i][j] = max(dp[i][j], dp[i][x - 1] + nums[i - 1]*nums[x]*nums[j + 1] + dp[x + 1][j])

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*(n + 2)
        
        for i in range(n):
            arr[i + 1] = nums[i]
            
        arr[0] = arr[n + 1] = 1
        dp = [[0]*(n+2) for _ in range(n + 2)]
        return self.helper(1, n, arr, dp)
    
    def helper(self, i, j, nums, dp):
        if i > j:
            return 0
        if dp[i][j] > 0:
            return dp[i][j]
        
        for x in range(i, j + 1):
            dp[i][j] = max(dp[i][j], self.helper(i, x - 1, nums, dp) + 
                           nums[i - 1]*nums[x]*nums[j + 1] + 
                           self.helper(x + 1, j, nums, dp))
            
        return dp[i][j]
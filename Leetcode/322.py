# https://leetcode.com/problems/coin-change/
# T: O(n*amount)
# S: O(amount)

# dp[]: 当前钱数需要多少coins
# min_val = min(min_val, dp[i - coins[j]] + 1)
# dp[5] = 3
# coins[j] = 2
# dp[7] = dp[7 - 2] + 1 = dp[5] + 1 = 4

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or len(coins) == 0:
            return -1
        
        dp = [0]*(amount + 1)
        for i in range(1, amount + 1):
            min_val = float('inf')
            for j in range(len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != -1:
                     min_val = min(min_val, dp[i - coins[j]] + 1)          
            dp[i] = -1 if min_val == float('inf') else min_val
            
        return dp[amount]
        
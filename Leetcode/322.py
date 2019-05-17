# https://leetcode.com/problems/coin-change/
# space O(amount * len coins) , Time O(amount)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = 2**32
        dp = [0] + amount * [MAX]
        for i in range(1, len(coins) + 1):
            for j in range(coins[i - 1], amount + 1):
                if dp[j - coins[i - 1]] != MAX:
                    dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
        
        if dp[amount] == MAX:
            return -1
        else:
            return dp[amount]
        
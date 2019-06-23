# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# 面试中出的不太多，这道题太难了。
# T: O(k*n)
# S: O(k*n)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        price_len = len(prices)
        if k >= price_len//2:
            return self.helper(prices)
        
        dp = [[0]*price_len for _ in range(k + 1)] # dp[i][j] 当前到达第j天最多进行i次交易，最大利润是多少
        for i in range(1, k + 1):
            tmp_max = -prices[0] # tmp_max means the maximum profit of just doing at most i-1 transactions, using at most first j-1 prices, and buying the stick at price[j]- this is used for the next loop
            for j in range(1, price_len):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
                
        return dp[k][price_len - 1]
        
        
    def helper(self, prices):
        price_len = len(prices)
        result = 0
        
        for i in range(1, price_len):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
                
        return result
        
        
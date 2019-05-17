# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# T: O(n)
# S: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - buy)
                
        return max_profit
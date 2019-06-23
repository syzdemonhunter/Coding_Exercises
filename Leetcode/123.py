# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# T: O(n)
# S: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -float('inf')
        buy2 = -float('inf')
        sell1, sell2 = 0, 0
        
        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
            
        return sell2
            
        
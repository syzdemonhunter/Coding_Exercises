# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://www.cnblogs.com/grandyang/p/4997417.html
# T: O(n)
# S: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        pre_sell = 0
        buy = -float('inf')
        pre_buy = 0
        
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
            
        return sell
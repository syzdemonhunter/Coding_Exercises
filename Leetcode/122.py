# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# T: O(n)
# S: O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += (prices[i] - prices[i - 1])
        return result
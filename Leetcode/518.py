# https://www.youtube.com/watch?v=jaNZ83Q3QGc&t=530s
# https://leetcode.com/problems/coin-change-2/
# T: O(amount*len(coins))
# S: O(amount*len(coins))

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        combinations = [0] * (amount + 1)
        combinations[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                combinations[i] += combinations[i - coin]

        return combinations[amount]
# https://leetcode.com/problems/unique-binary-search-trees/
# T: O(n^2)
# S: O(n)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        dp = [1] + [0]*n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1]*dp[i - j]
        return dp[n]
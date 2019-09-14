# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# T: O(n^3)
# S: O(n^2)

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n + 1) for _ in range(n + 1)]
        
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(x + 
                max(dp[i][x - 1], dp[x + 1][j]) for x in range(i, j))
        return dp[1][n]
            
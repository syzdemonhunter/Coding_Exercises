# https://leetcode.com/problems/maximal-square/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        result = 0
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(min(dp[i][j - 1], dp[i - 1][j - 1]), dp[i - 1][j]) + 1
                    result = max(result, dp[i][j])
                    
        return result*result
        
        
        
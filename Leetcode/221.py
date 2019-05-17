# https://leetcode.com/problems/maximal-square/
# T: O(m*n)
# S: O(n)

class Solution(object):
    def min_of_three(self, a, b, c):
        return min(a, min(b, c))
    
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or not matrix[0] or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0]*n
        max_side, pre = 0, 0
        
        for i in range(m):
            for j in range(n):
                tmp = dp[j]
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[j] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[j] = self.min_of_three(dp[j], pre, dp[j - 1]) + 1
                max_side = max(max_side, dp[j])
                pre = tmp
        return max_side ** 2
        
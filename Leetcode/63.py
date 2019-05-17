# https://leetcode.com/problems/unique-paths-ii/
# T: O(m*n)
# S: O(min(m, n))


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        for i in range(m):
            dp[0] = 0 if obstacleGrid[i][0] == 1 else dp[0]
            for j in range(1, n):
                dp[j] = 0 if obstacleGrid[i][j] == 1 else dp[j] + dp[j - 1]
                
        return dp[n - 1]
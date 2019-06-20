# https://leetcode.com/problems/unique-paths-ii/
# T: O(m*n)
# S: O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        result = [1] + [0]*(n - 1)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                elif j > 0:
                    result[j] += result[j - 1]
                    
        return result[n - 1]
        
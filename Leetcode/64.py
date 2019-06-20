# https://leetcode.com/problems/minimum-path-sum/
# T: O(m*n)
# S: O(1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                if i != 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                if i != 0 and j != 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                    
        return grid[m - 1][n - 1]
                    
        
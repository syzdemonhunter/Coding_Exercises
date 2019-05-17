# https://leetcode.com/problems/minimum-path-sum/
# T: O(m*n)
# S: O(n)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        d = [0]*n
        d[0] = grid[0][0]
        
        for j in range(1, n):
            d[j] = d[j - 1] + grid[0][j]
            
        for i in range(1, m):
            d[0] += grid[i][0]
            for j in range(1, n):
                d[j] = min(d[j], d[j - 1]) + grid[i][j]
                
        return d[n - 1]
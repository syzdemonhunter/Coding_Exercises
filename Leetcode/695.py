# https://www.youtube.com/watch?v=W8VuDt0eb5c
# https://leetcode.com/problems/max-area-of-island/
# T: O(n*m)
# S: O(n*m)

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0 
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))

        return max_area

    def dfs(self, grid, i, j):
        rows, cols = len(grid), len(grid[0])
        
        if (i < 0)  or (i >= rows) or (j < 0) or (j >= cols) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        count = 1
        count += self.dfs(grid, i + 1, j)
        count += self.dfs(grid, i - 1, j)
        count += self.dfs(grid, i, j + 1)
        count += self.dfs(grid, i, j - 1)

        return count
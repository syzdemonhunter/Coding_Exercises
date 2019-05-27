# https://leetcode.com/problems/island-perimeter/
# T: O(n^2)
# S: O(1)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 4
                    if i > 0 and grid[i - 1][j]:
                        result -= 2
                    if j > 0 and grid[i][j - 1]:
                        result -= 2
                        
        return result
                        
        
        
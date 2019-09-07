# https://leetcode.com/problems/pacific-atlantic-water-flow/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.dir = [[0,1], [1, 0], [0, -1], [-1, 0]]
        result = []
        self.m = len(matrix)
        if self.m == 0:
            return result
        self.n = len(matrix[0])
        
        pac = [[False]*self.n for _ in range(self.m)]
        atl = [[False]*self.n for _ in range(self.m)]
        
        for i in range(self.m):
            self.helper(matrix, pac, i, 0)
            self.helper(matrix, atl, i, self.n - 1)
            
        for j in range(self.n):
            self.helper(matrix, pac, 0, j)
            self.helper(matrix, atl, self.m - 1, j)
            
        for i in range(self.m):
            for j in range(self.n):
                if pac[i][j] and atl[i][j]:
                    result.append([i, j])
                    
        return result
            
    def helper(self, matrix, is_visited, i, j):
        is_visited[i][j] = True
        for d in self.dir:
            x, y = i + d[0], j + d[1]
            if x < 0 or y < 0 \
            or x >= self.m or y >= self.n \
            or is_visited[x][y] \
            or matrix[i][j] > matrix[x][y]:
                continue
            
            self.helper(matrix, is_visited, x, y)
            
        
        
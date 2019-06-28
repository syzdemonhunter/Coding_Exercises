# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0:
            return 0
        
        result = 0
        m, n = len(matrix), len(matrix[0])
        cache = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                max_val = self.dfs(matrix, -float('inf'), i, j, m, n, cache)
                result = max(result, max_val)
        
        return result
    
    def dfs(self, matrix, min_val, i, j, m, n, cache):
        if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= min_val:
            return 0
        
        if cache[i][j] != 0:
            return cache[i][j]
        
        min_val = matrix[i][j]
        a = self.dfs(matrix, min_val, i - 1, j, m, n, cache) + 1
        b = self.dfs(matrix, min_val, i + 1, j, m, n, cache) + 1
        c = self.dfs(matrix, min_val, i, j - 1, m, n, cache) + 1
        d = self.dfs(matrix, min_val, i, j + 1, m, n, cache) + 1
        max_val = max(a, max(b, max(c, d)))
        cache[i][j] = max_val
        return max_val
        
        
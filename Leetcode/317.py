# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# 这题很重要
# T: O(m^2*n^2)
# S: O(m*n)


import collections
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        dist = [[0]*n for _ in range(m)]
        nums = [[0]*n for _ in range(m)]
        bld_num = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bld_num += 1
                    self.bfs(grid, i, j, dist, nums)
                    
        result = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dist[i][j] != 0 and nums[i][j] == bld_num:
                    result = min(result, dist[i][j])
                    
        return -1 if result == float('inf') else result
                    
                    
    def bfs(self, grid, row, col, dist, nums):
        m, n = len(grid), len(grid[0])
        q = collections.deque([[row, col]])
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False]*n for _ in range(m)]
        distance = 0
        
        while q:
            distance += 1
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                for k in range(len(dirs)):
                    x = cur[0] + dirs[k][0]
                    y = cur[1] + dirs[k][1]
                    if x >= 0 and x < m and y >= 0 \
                    and y < n and not visited[x][y] and grid[x][y] == 0:
                        visited[x][y] = True
                        dist[x][y] += distance
                        nums[x][y] += 1
                        q.append([x,y])
                        
        
            
        
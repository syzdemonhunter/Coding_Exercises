# https://leetcode.com/problems/01-matrix/
# T: O(m*n)
# S: O


import collections

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append([i, j])
                else:
                    matrix[i][j] = sys.maxsize
                    
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 上下左右
        while q:
            point = q.popleft()
            for d in dirs:
                r = point[0] + d[0]
                c = point[1] + d[1]
                if r < 0 or r >= m or c < 0 or c >= n or \
                matrix[r][c] <= matrix[point[0]][point[1]] + 1:
                    continue
                q.append([r, c])
                matrix[r][c] = matrix[point[0]][point[1]] + 1
                
        return matrix
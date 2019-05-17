# https://leetcode.com/problems/set-matrix-zeroes/
# time: O(m * n)
# space O(1)
# https://www.youtube.com/watch?v=T-_ZdgvO-oU

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) ==0 or len(matrix[0]) == 0:
            return

        m, n = len(matrix), len(matrix[0])
        row, col = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if row:
            for j in range(n):
                matrix[0][j] = 0

        if col:
            for i in range(m):
                matrix[i][0] = 0
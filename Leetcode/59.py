# https://leetcode.com/problems/spiral-matrix-ii/
# T: O(n)
# S: O(n)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row_begin = 0
        row_end = n - 1
        col_begin = 0
        col_end = n - 1
        num = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        while row_begin <= row_end and col_begin <= col_end:
            for i in range(col_begin, col_end + 1):
                matrix[row_begin][i] = num
                num += 1
            row_begin += 1
            
            for i in range(row_begin, row_end + 1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1
            
            for i in range(col_end, col_begin - 1, -1):
                matrix[row_end][i] = num
                num += 1
            row_end -= 1
            
            for i in range(row_end, row_begin - 1, -1):
                matrix[i][col_begin] = num
                num += 1
            col_begin += 1
            
        return matrix
                
            
        
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# T: O(m + n)
# S: O(1)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while col >= 0 and row <= len(matrix) - 1:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
                
        return False
        
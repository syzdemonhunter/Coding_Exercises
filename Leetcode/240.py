# https://leetcode.com/problems/search-a-2d-matrix-ii/
# T: O(m + n)
# S: O(1)


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 \
           or not matrix[0] or len(matrix[0]) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while i < m and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
            
        return False
        
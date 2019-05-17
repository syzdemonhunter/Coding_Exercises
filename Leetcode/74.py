# https://leetcode.com/problems/search-a-2d-matrix/
# T: O(log(m*n))
# S: O(1)


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        low, high = 0, row*col - 1
        while low <= high:
            mid = low + (high - low)//2
            m_row = mid//col
            m_col = mid%col
            if matrix[m_row][m_col] == target:
                return True
            if matrix[m_row][m_col] > target:
                high = mid - 1
            if matrix[m_row][m_col] < target:
                low = mid + 1
                
        return False
# https://leetcode.com/problems/search-a-2d-matrix/
# T: O(log(n*m))
# S: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        begin = 0
        end = m*n - 1
        
        while begin <= end:
            mid = end + (begin - end)//2
            value = matrix[mid//n][mid % n]
            if value == target:
                return True
            elif value < target:
                begin = mid + 1
            else:
                end = mid - 1
                
        return False
            
        
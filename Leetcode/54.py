# https://leetcode.com/problems/spiral-matrix/
# T: O(m*n)
# S: O(1)

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        up, down, left, right = \
        0, len(matrix) - 1, 0, len(matrix[0]) - 1
        # 0: go right   1: go down  2: go left  3: go up
        direct = 0
        res = []
        
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
                
            if direct == 1:
                for j in range(up, down + 1):
                    res.append(matrix[j][right])
                right -= 1
                
            if direct == 2:
                for k in range(right, left - 1, -1):
                    res.append(matrix[down][k])
                down -= 1
                
            if direct == 3:
                for l in range(down, up - 1, -1):
                    res.append(matrix[l][left])
                left += 1
                
            if up > down or left > right:
                return res
            
            direct = (direct + 1) % 4
# https://leetcode.com/problems/diagonal-traverse/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        ans = []
        m, n = len(matrix), len(matrix[0])
        
        number = m*n
        
        i = j = 0
        up = True
        
        while number:
            number -= 1
            ans.append(matrix[i][j])
            
            if up:
                if j == n - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1  
            else:
                if i == m - 1:
                    up = True
                    j += 1
                elif j == 0:
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1
                    
        return ans
        
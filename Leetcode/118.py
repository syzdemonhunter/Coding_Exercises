# https://leetcode.com/problems/pascals-triangle/
# T: O(n^2)
# S: O(n^2)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = []
        for i in range(numRows):
            result.append([1]*(i + 1))
            
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result
        
        
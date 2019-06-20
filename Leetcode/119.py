# https://leetcode.com/problems/pascals-triangle-ii/
# T: O(n^2)
# S: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
        result = [1]*(rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] = result[i - j] + result[i - j- 1]
        return result
        
# https://leetcode.com/problems/spiral-matrix-ii/
# https://www.youtube.com/watch?v=dfGhf-Ko0L4
# T: O(m*n)
# S: O(m*n)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return [[]]
        results = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        k = 1
        while top < bottom and left < right:
            for i in range(left, right):
                results[top][i] = k
                k += 1
                
            for i in range(top, bottom):
                results[i][right] = k
                k += 1
                
            for i in range(right, left, -1):
                results[bottom][i] = k
                k += 1
                
            for i in range(bottom, top, -1):
                results[i][left] = k
                k += 1
                
            top += 1
            bottom -= 1
            left += 1
            right -= 1
            
        if n%2 != 0:
            results[n//2][n//2] = k
        return results
        
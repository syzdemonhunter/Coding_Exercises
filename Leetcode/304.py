# https://leetcode.com/problems/range-sum-query-2d-immutable/
# http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-304-range-sum-query-2d-immutable/
# Dynamic programming

# Time complexity: O(m*n)
# sumRegion: O(m*n)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.dp[i][j] = matrix[i - 1][j - 1] \
                              + self.dp[i - 1][j] \
                              + self.dp[i][j - 1] \
                              - self.dp[i - 1][j - 1]
                 
        
    # Time complexity: O(1)
    # sumRegion: O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] \
             - self.dp[row1][col2 + 1]  \
             - self.dp[row2 + 1][col1] \
             + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
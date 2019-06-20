# https://leetcode.com/problems/unique-paths/
# T: O(n*m)
# S: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [1] + [0]*(n - 1)
        for i in range(m):
            for j in range(1, n):
                result[j] = result[j] + result[j - 1]
                
        return result[n - 1]
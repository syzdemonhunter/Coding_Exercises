# https://leetcode.com/problems/integer-break/
# T: < O(n) 
# S: O(1)

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        result = 1
        while n > 4:
            result *= 3
            n -= 3
            
        return result*n
        
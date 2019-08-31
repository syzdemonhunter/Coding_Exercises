# https://leetcode.com/problems/number-of-digit-one/
# T: < O(n)
# S: O(1)

class Solution:
    def countDigitOne(self, n: int) -> int:
        result = 0
        m = 1
        
        while m <= n:
            a = n//m
            b = n % m
            result += (a + 8)//10*m
            
            if a % 10 == 1:
                result += b + 1
            
            m *= 10
            
        return result
            
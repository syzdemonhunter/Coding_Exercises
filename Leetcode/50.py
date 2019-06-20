# https://leetcode.com/problems/powx-n/
#Time Complexity: O(log N)
#Space Complexity: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
            
        result = 1
        n_abs = abs(n)
        
        while n_abs > 0:
            if n_abs % 2 == 1:
                result *= x
            x *= x
            n_abs //= 2
            
        if n < 0:
            return 1.0/result
        return result
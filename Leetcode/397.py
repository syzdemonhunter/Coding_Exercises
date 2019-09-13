# https://leetcode.com/problems/integer-replacement/
# T: about O(log(n))
# S: O(1)

class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 2^31 - 1:
            return 32

        result = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if (n + 1) % 4 == 0 and n - 1 != 2:
                    n += 1
                else:
                    n -= 1
            result += 1
            
        return result
            
                    
        
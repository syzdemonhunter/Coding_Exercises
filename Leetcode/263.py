# https://leetcode.com/problems/ugly-number/
# 面试中没怎么见过
# Time: O(n) or linear time
# Time: O(1)
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num == 0:
            return False
        
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
            
        return num == 1
        
        
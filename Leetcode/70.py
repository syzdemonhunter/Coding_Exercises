# https://leetcode.com/problems/climbing-stairs/
# T: O(n)
# S: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        one_step = 1
        two_step = 1
        result = 0
        
        for i in range(2, n + 1):
            result = one_step + two_step
            two_step = one_step
            one_step = result
            
        return result
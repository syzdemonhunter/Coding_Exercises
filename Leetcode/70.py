# https://leetcode.com/problems/climbing-stairs/
# T: O(n)
# S: O(1)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        zero, first = 1, 1
        
        for i in range(1, n):
            second = zero + first
            zero = first
            first = second
            
        return first
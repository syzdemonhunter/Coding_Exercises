# https://leetcode.com/problems/sqrtx/
# T: O(log(n))
# S: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x
        while x*x > n:
            x = (x + n//x)//2
        return x
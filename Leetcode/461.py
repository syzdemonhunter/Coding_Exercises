# https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def helper(self, n):
        count = 0
        while n!= 0:
            count += 1
            n &= (n - 1)
        return count
    
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.helper(x^y)
        
        
# https://leetcode.com/problems/number-of-1-bits/
# T: O(k) <- k: # of 1 in bin(n)
# S: O(1)


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!= 0:
            count += 1
            n = n & (n-1)
        return count
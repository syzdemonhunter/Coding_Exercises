# https://leetcode.com/problems/number-of-1-bits/
# 位运算，不用多看
# T: O(1)
# S: O(1)

'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result += n & 1
            n >>= 1
        return result
'''
class Solution(object):
    def hammingWeight(self, n):
        result = 0
        while n != 0:
            n = n & (n - 1)
            result += 1
        return result
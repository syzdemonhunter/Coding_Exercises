# https://leetcode.com/problems/reverse-bits/
# T: O(1)
# S: O(1)
# 位运算，不用多看了

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        result = 0
        for i in range(32):
            result <<= 1
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result
        
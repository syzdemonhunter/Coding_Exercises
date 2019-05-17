# https://leetcode.com/problems/sum-of-two-integers/
# T: O(m)
# S: O(1)

# https://www.youtube.com/watch?v=Pi7sMZWIIXE
#101 + 110 => 011 + 1000 => ....sum(n, 0) -> n
import ctypes

class Solution:
    def getSum(self, x, y):
        if y == 0:
            return x
        else:
            carry = ctypes.c_int32(x & y)
            return self.getSum(x ^ y, carry.value << 1)
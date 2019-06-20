# https://leetcode.com/problems/power-of-two/
# T: O(1)
# S: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and ((n & (n - 1)) == 0)
        
        
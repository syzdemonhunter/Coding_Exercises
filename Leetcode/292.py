# https://leetcode.com/problems/nim-game/
# 不用在意，这种题不会考
# T: O(1)
# S: O(1)

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        
        
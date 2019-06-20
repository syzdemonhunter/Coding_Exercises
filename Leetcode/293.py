# https://leetcode.com/problems/flip-game/
# T: O(n)
# SL O(n)

class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        result = []
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                result.append(s[:i - 1] + '--' + s[i + 1:len(s)])
                
        return result
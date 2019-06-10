# https://leetcode.com/problems/excel-sheet-column-number/
# T: O(n)
# S: O(1)

class Solution:
    def titleToNumber(self, s: str) -> int:
        # input ACB
        # for each char, result = ord([s[i]]) - ord('A') + 1
        # for each postiion, result *= 26
        
        result = 0
        
        for i in range(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
            
        return result
        
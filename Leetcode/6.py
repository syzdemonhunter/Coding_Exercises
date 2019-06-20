# https://leetcode.com/problems/zigzag-conversion/
# T: O(n)
# S: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        sb = ['' for _ in range(numRows)]
        for i in range(len(s)):
            index = i %  (2*numRows - 2)
            index = index if index < numRows else 2*numRows - 2 - index
            sb[index] += s[i]
            
        for i in range(1, len(sb)):
            sb[0] += sb[i]
            
        return sb[0]
        
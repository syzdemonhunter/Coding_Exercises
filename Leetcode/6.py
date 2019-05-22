# https://leetcode.com/problems/zigzag-conversion/
# T: O(n)
# S: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        sb = ['']*numRows
        for i in range(len(s)):
            idx = i % (2*numRows - 2)
            if idx >= numRows:
                idx = 2*numRows -2 -idx
            sb[idx] += s[i]
                
        for j in range(1, len(sb)):
            sb[0] += sb[j]
            
        return sb[0]
        
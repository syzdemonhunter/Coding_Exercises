# https://leetcode.com/problems/add-binary/
# T: O(n)
# S: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        i, j = len(a) - 1, len(b) - 1
        remainder = 0
        while i >= 0 or j >= 0:
            total = remainder
            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1
                
            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1
                
            result += str(total % 2)
            remainder = total // 2
            
        if remainder != 0:
            result += str(remainder)
            
        return result[::-1]
                
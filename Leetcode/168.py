# https://leetcode.com/problems/excel-sheet-column-title/
# T: O(n) linear complexity
# S: O(n)

class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        
        while n > 0:
            n -= 1
            result.append(capitals[n % 26])
            n //= 26
            
        return ''.join(result[::-1])
        
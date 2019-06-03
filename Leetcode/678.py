# https://leetcode.com/problems/valid-parenthesis-string/
# https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
# One pass O(N) time, Space O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
                
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
                
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
                
            if cmax < 0:
                return False
            
        return cmin == 0
        
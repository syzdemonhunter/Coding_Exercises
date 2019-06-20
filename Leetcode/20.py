# https://leetcode.com/problems/valid-parentheses/
# T: O(n)
# S: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != ch:
                    return False
                
        return not stack
        
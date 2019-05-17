# https://leetcode.com/problems/valid-parentheses/
# T: O(n)
# S: O(1)


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif not stack:
                return False
            else:
                if i == ')' and stack[-1] != '(':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                elif i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
                
        if not stack:
            return True
        return False
                
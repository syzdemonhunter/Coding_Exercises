# https://leetcode.com/problems/longest-valid-parentheses/
# T: O(n)
# S: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = 0
        start = -1
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        result = max(result, i - start)
                    else:
                        result = max(result, i - stack[-1])
                        
        return result
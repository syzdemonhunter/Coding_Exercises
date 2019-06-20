# https://leetcode.com/problems/generate-parentheses/
# T: O(n!)
# S: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        result = []
        self.helper(result, '', n, n)
        return result
    
    def helper(self, result, s, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(s)
            return
        if left > 0:
            self.helper(result, s + '(', left - 1, right)
        
        if right > 0:
            self.helper(result, s + ')', left, right - 1)
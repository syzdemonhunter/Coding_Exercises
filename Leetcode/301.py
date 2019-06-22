# https://leetcode.com/problems/remove-invalid-parentheses/
# T: ???
# S: O(n)

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        self.helper(result, s, 0, 0, ('(', ')'))
        return result
    
    def helper(self, result, s, last_i, last_j, pair):
        # 删除右括号
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == pair[0]:
                count += 1
            if s[i] == pair[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
                    self.helper(result, s[0:j] + s[j + 1:], i, j, pair)
                    
            return
        # 实现删除左括号
        s_reversed = s[::-1]
        if pair[0] == '(':
            self.helper(result, s_reversed, 0, 0,  (')', '('))
        else:
            result.append(s_reversed)
        
        
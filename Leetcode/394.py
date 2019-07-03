# https://leetcode.com/problems/decode-string/
# T: O(n)
# S: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        stack = []
        cur_num = 0
        cur_str = ''
        
        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                pre_str = stack.pop()
                cur_str = pre_str + num*cur_str
            elif c.isdigit():
                cur_num = cur_num*10 + int(c)
            else:
                cur_str += c
        return cur_str
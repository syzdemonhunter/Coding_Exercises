# https://leetcode.com/problems/basic-calculator-ii/
# T: O(n)
# S: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        stack = []
        res = 0
        sign = '+'
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i]) 
                    
            if (not s[i].isdigit() and s[i] != ' ' ) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop()*num)
                if sign == '/':
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num + 1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
            
        for j in stack:
            res += j
        return res
                    
                    
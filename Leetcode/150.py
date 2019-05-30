# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# T: O(n)
# S: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
                
            else:
                obj_2 = stack.pop()
                obj_1 = stack.pop()
                
                if token == '+':
                    stack.append(obj_1 + obj_2)
                elif token == '-':
                    stack.append(obj_1 - obj_2)
                elif token == '*':
                    stack.append(obj_1*obj_2)
                else:
                    stack.append(int(obj_1*1.0/obj_2))
                    
        return stack[0]
        
# https://leetcode.com/problems/remove-k-digits/
# T: O(n)
# S: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        
        stack = []
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
            
        while k > 0: #corner case 112 remove 1
            stack.pop()
            k -= 1
            
        return ''.join(stack).lstrip('0') or '0'
        
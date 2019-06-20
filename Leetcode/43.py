# https://leetcode.com/problems/multiply-strings/submissions/

# https://leetcode.com/problems/multiply-strings/submissions/
# T: O(m*n)
# S: O(m + n)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return '0'
        
        digits = [0]*(len(num1) + len(num2))
        for i, v1 in enumerate(num1[::-1]):
            for j, v2 in enumerate(num2[::-1]):
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')
                digits[i + j] += int1*int2
                digits[i + j + 1] += digits[i + j] // 10
                digits[i + j] %= 10
                
        while len(digits) > 1 and digits[-1] == 0:
            digits.pop()
        return ''.join(str(digit) for digit in digits)[::-1]
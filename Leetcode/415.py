# https://leetcode.com/problems/add-strings/
# T: O(n)
# S: O(1)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        m, n = len(num1), len(num2)
        i, j = m - 1, n - 1
        carry = 0
        
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >=0 else 0
            i -= 1
            b = int(num2[j]) if j >=0 else 0
            j -= 1
            total = a + b + carry
            result = str(total % 10 ) + result;
            carry = total // 10
            
        if carry == 0:
            return result
        else:
            return str(carry) + result
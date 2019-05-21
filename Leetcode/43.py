# https://leetcode.com/problems/multiply-strings/
# T: O(m*n)
# S: O(m + n)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]*(len(num1) + len(num2))
        for i, v1 in enumerate(num1[::-1]):
            for j, v2 in enumerate(num2[::-1]):
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')
                res[i + j] += int1*int2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
                
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(str(s) for s in res)[::-1]
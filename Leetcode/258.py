# https://leetcode.com/problems/add-digits/
# If an integer is like 100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
# T: O(1)
# S: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num%9 if num%9 != 0 else 9
        
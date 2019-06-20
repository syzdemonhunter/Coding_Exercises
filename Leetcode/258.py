# https://leetcode.com/problems/add-digits/

# T: O(logn)
# S: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num != 0:
            total += num % 10
            num //= 10
        if total >= 10:
            return self.addDigits(total)
        else:
            return total
        
'''
# T: O(1)
# S: O(1)
# If an integer is like 100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num%9 if num%9 != 0 else 9
'''
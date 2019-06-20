# https://leetcode.com/problems/palindrome-number/
# T: O(logn)
# S: o(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        palind = x
        rev = 0
        
        while x > 0:
            rev = rev*10 + x % 10
            x //= 10
            
        return palind == rev
        
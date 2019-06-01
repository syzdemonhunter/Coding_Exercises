# https://leetcode.com/problems/valid-palindrome-ii/
# 双指针算法。从两头走到中间，发现第一对不一样的字符之后，要么删左边的，要么删右边的。
# T: O(n)
# S: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
            
        if left >= right:
            return True
        
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
            
        
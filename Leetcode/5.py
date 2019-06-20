# https://leetcode.com/problems/longest-palindromic-substring/
# T: O(n^2)
# S: O(1)

class Solution:
    result = ''
    
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)
            
        return self.result
            
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        cur = s[left + 1:right]
        if len(cur) > len(self.result):
            self.result = cur
        
        
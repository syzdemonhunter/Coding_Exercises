# https://leetcode.com/problems/shortest-palindrome/
# T: O(n^2)
# S: O(1)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i, j = 0, len(s) - 1
        end = len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                i = 0
                end -= 1
                j = end
                
        return s[end + 1:][::-1] + s
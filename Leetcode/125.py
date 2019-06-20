# https://leetcode.com/problems/valid-palindrome/
# T: O(n)
# S: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
                
            left = s[i].lower()
            right = s[j].lower()
            if left != right:
                return False
            i += 1
            j -= 1
                
        return True
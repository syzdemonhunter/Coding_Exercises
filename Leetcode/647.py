# https://leetcode.com/problems/palindromic-substrings/
# T: O(n^2)
# S: O(1)


class Solution(object):
    def expand(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            count += 1
            left -= 1
            right += 1
        return count
        
        
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count = 0
        for i in range(len(s)):
            count += self.expand(s, i, i)
            count += self.expand(s, i, i + 1)
        return count
        
        
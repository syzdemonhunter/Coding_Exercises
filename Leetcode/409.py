# https://leetcode.com/problems/longest-palindrome/
# T: O(n)
# S: O(m)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        count, odd = {}, 0
        
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
                
        for key in count:
            if count[key] % 2 != 0:
                odd += 1
                
        unused = max(0, odd-1)
        return len(s) - unused
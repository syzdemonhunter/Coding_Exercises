# https://leetcode.com/problems/longest-palindromic-substring/
# T: O(n^2)
# S: O(1)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ''

        for i in range(len(s)):
        	# 1. 轴对称
        	len_1 = len(self.get_longest_palindrome(s, i, i))

        	if len_1 > len(palindrome):
        		palindrome = self.get_longest_palindrome(s, i, i)

        	# 2. 两边扩展
        	len_2 = len(self.get_longest_palindrome(s, i, i + 1))

        	if len_2 > len(palindrome):
        		palindrome = self.get_longest_palindrome(s, i, i + 1)
                
        return palindrome
        
        
    def get_longest_palindrome(self, s, l, r):
    	while l >= 0 and r < len(s) and s[l] == s[r]:
    		l -= 1
    		r += 1
    	return s[l + 1:r]
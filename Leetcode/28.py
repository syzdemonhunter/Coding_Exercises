# https://leetcode.com/problems/implement-strstr/
# T: O(n - m + 1)*m
# S: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        
        for idx in range(len(haystack) - len(needle) + 1):
        	if haystack[idx:idx+len(needle)] == needle:
        		return idx 

        return -1
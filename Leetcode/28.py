# https://leetcode.com/problems/implement-strstr/
# T: O(m*n)
# S: O(1)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or len(needle) == 0:
            return 0
        
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                break
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
                
        return -1
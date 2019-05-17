# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# T: O(n)
# S: O(n)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        
        result = ''
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                sub = s[start:i]
                sub = sub[::-1]
                result = "{}{} ".format(result, sub)
                start = i + 1
            elif i == len(s) - 1:
                sub = s[start:i+1]
                sub = sub[::-1]
                result = result + sub
        return result
        
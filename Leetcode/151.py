# https://leetcode.com/problems/reverse-words-in-a-string/
# T: O(n)
# S: O(n)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        result = ""
        s_len = len(s_list)
        
        for i in range(s_len):
            if i == s_len - 1:
                result = s_list[i] + result
                
            else:
                result = " " + s_list[i] + result
                
        return result
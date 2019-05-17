# https://leetcode.com/problems/first-unique-character-in-a-string/
# T: O(n)
# S: O(m)

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        
        for x in s:
            s_dict[x] = s_dict.get(x, 0) + 1
            
        for i in range(len(s)):
            
            if s_dict.get(s[i]) == 1:
                return i
            
        return -1
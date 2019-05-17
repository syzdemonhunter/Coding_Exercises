# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# T: O(n)
# S: O(m)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_dict = {}
        max_len = 0
        p = 0
        
        for i, v in enumerate(s):
            if v in count_dict:
                p = max(count_dict[v] + 1, p)
            
            max_len = max(i - p + 1, max_len)
            count_dict[v] = i
            
        return max_len
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# T: O(n)
# S: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        dic = {}
        result = 0
        j = 0
        for i in range(len(s)):
            if s[i] in dic:
                j = max(j, dic[s[i]] + 1)
            dic[s[i]] = i
            result = max(result, i - j + 1)
            
        return result
        
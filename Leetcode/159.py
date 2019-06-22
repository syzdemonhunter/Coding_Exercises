# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# T: O(n)
# S: O(n)

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        dic = {}
        start, end, result = 0, 0, 0
        while end < len(s):
            if len(dic) <= 2:
                dic[s[end]] = end
                end += 1
            if len(dic) > 2:
                left_most = len(s)
                for num in dic.values():
                    left_most = min(left_most, num)
                del dic[s[left_most]]
                start = left_most + 1
                    
            result = max(result, end - start)
            
        return result
                
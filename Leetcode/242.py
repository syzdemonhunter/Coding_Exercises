# https://leetcode.com/problems/valid-anagram/
# 这种题不太会考
# T: O(m + n) = O(n)
# S: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        for num in count:
            if num != 0:
                return False
        return True
            
# https://leetcode.com/problems/first-unique-character-in-a-string/
# T: O(n)
# S: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i
            
        return -1
        
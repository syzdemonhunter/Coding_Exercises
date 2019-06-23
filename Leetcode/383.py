# https://leetcode.com/problems/ransom-note/
# 这题太简单了
# T: O(n)
# S: O(1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26
        
        for i in range(len(magazine)):
            count[ord(magazine[i]) - ord('a')] += 1
            
        for i in range(len(ransomNote)):
            count[ord(ransomNote[i]) - ord('a')] -= 1
            if count[ord(ransomNote[i]) - ord('a')] < 0:
                return False
            
        return True
            
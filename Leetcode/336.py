# https://leetcode.com/problems/palindrome-pairs/
# T: O(n*k^2)
# S: O(n)

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words or len(words) < 2:
            return []
        
        result = []
        dic = {}
        for i, word in enumerate(words):
            dic[word] = i
            
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                str1 = words[i][:j]
                str2 = words[i][j:]
                if self.is_palindrome(str1):
                    str2_rev = str2[::-1]
                    if str2_rev in dic and dic[str2_rev] != i:
                        result.append([dic[str2_rev], i])
                        
                if len(str2) != 0 and self.is_palindrome(str2):
                    str1_rev = str1[::-1]
                    if str1_rev in dic and dic[str1_rev] != i:
                        result.append([i, dic[str1_rev]])
                        
        return result
        
    def is_palindrome(self, s):
        return s == s[::-1]

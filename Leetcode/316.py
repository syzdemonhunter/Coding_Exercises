# https://leetcode.com/problems/remove-duplicate-letters/
# 这道题比较重要，在实现题中很难
# T: O(n)
# S: O(n)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        result = [0]*len(dic)
        start, end = 0, self.find_min_last_pos(dic)
        
        for i in range(len(result)):
            min_char = ord('z') + 1
            for k in range(start, end + 1):
                if s[k] in dic and ord(s[k]) < min_char:
                    min_char = ord(s[k])
                    start = k + 1
                    
            result[i] = chr(min_char)
            del dic[chr(min_char)]
            if s[end] == chr(min_char):
                end = self.find_min_last_pos(dic)
                    
        return ''.join(result)
        
    def find_min_last_pos(self, dic):
        result = float('inf')
        for value in dic.values():
            result = min(result, value)
            
        return result
        
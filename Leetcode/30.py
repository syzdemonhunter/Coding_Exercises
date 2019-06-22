# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# T: O(n^2)
# S: O(n)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or len(words) == 0:
            return []
        
        result = []
        n = len(words)
        m = len(words[0])
        dic = {}
        
        for word in words:
            dic[word] = dic.get(word, 0) + 1
            
        for i in range(len(s) - n*m + 1):
            dic_copy = dic.copy()
            k = n
            j = i
            while k > 0:
                string = s[j:j + m]
                if string not in dic_copy or dic_copy[string] < 1:
                    break
                dic_copy[string] = dic_copy[string] - 1
                k -= 1
                j += m
            if k == 0:
                result.append(i)
            
        return result
            
        
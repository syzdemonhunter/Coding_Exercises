# https://leetcode.com/problems/alien-dictionary/
# T: O(V + E)
# S: O(n)

import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words or len(words) == 0:
            return
        
        dic = {}
        letters = [0 for i in range(26)]  
        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                letters[key] = 0
                dic[key] = set()
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            idx = 0
            for j in range(min(len(word1),len(word2))):
                if(word1[j] != word2[j]):
                    key1 = ord(word1[j]) - ord('a')
                    key2 = ord(word2[j]) - ord('a')
                    count = letters[key2]
                    if(key2 not in dic[key1]):
                        letters[key2] = count + 1
                        dic[key1].add(key2)
                    break
                    
        q = collections.deque()
        res = ''
        
        for i in range(26):
            if letters[i] == 0 and i in dic:
                q.append(i)
        
        while len(q) != 0:
            nextup = q.popleft()
            res += chr(nextup + ord('a'))
            greater_set = dic[nextup]
            for greater in greater_set:
                letters[greater] -= 1
                if letters[greater] == 0:
                    q.append(greater)
                    
        if len(dic) != len(res):
            return ""
        
        return res
                    
                
            
        
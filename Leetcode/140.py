# https://leetcode.com/problems/word-break-ii/
# 这道题非常重要，这个写法要记忆一下
# T: O(n^3)
# S: O(n^3)

class Solution:
    def __init__(self):
        self.dic = {}
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, wordDict, 0)
    
    def dfs(self, s, wordDict, start):
        if start in self.dic:
            return self.dic[start]
        
        result = []
        if start == len(s):
            result.append('')
            
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict:
                path = self.dfs(s, wordDict, end)
                for tmp in path:
                    if tmp == '':
                        result.append(s[start:end] + '')
                    else:
                        result.append(s[start:end] + ' ' + tmp)
                        
        self.dic[start] = result
        return result
                        
            
        
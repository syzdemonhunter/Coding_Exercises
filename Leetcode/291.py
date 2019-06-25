# https://leetcode.com/problems/word-pattern-ii/
# T: O(2^n) ???
# S: O(n)

class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        dic = {}
        my_set = set()
        return self.is_match(string, 0, pattern, 0, dic, my_set)
    
    def is_match(self, string, i, pattern, j, dic, my_set):
        if i == len(string) and j == len(pattern):
            return True
        if i == len(string) or j == len(pattern):
            return False
        
        c = pattern[j]
        if c in dic:
            s = dic[c]
            if not string.startswith(s, i):
                return False
            return self.is_match(string, i + len(s), pattern, j + 1, dic, my_set)
        
        for k in range(i, len(string)):
            p = string[i:k + 1]
            if p in my_set:
                continue
            dic[c] = p
            my_set.add(p)
            if self.is_match(string, k + 1, pattern, j + 1, dic, my_set):
                return True
            del dic[c]
            my_set.remove(p)
            
        return False
            
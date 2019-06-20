# https://leetcode.com/problems/isomorphic-strings/submissions/
# 这道题很重要
'''
# T: O(n^2)
# S: O(1)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return True
        
        dic = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a in dic:
                if dic[a] == b:
                    continue
                else:
                    return False
            else:
                if b not in dic.values():
                    dic[a] = b
                else:
                    return False
                
        return True
'''
# T: O(n)
# S: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_chars = [0]*256
        t_chars = [0]*256
        
        for i in range(len(s)):
            if s_chars[ord(s[i])] != t_chars[ord(t[i])]:
                return False
            else:
                s_chars[ord(s[i])] = t_chars[ord(t[i])] = ord(t[i])
        return True        
        
# https://leetcode.com/problems/one-edit-distance/
# T: O(n^2)
# S: O(1)

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                elif len(s) > len(t):
                    return s[i + 1:] == t[i:]
                else:
                    return t[i + 1:] == s[i:]
                
        return abs(len(s) - len(t)) == 1
                
        
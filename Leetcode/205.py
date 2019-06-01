# https://leetcode.com/problems/isomorphic-strings/
# 开一个map尽量将s的字符替换为t对应的字符，再开一个map尽量将t的字符替换为s,如果两个都能成功，那么就能满足题目条件。
# T: O(n)
# S: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1, map_2 = {}, {}
        for i in range(len(s)):
            if s[i] not in map_1:
                map_1[s[i]] = t[i]
            elif map_1[s[i]] != t[i]:
                return False
            
        for j in range(len(t)):
            if t[j] not in map_2:
                map_2[t[j]] = s[j]
            elif map_2[t[j]] != s[j]:
                return False
            
        return True
        
# https://leetcode.com/problems/one-edit-distance/
# T: O(n)
# S: O(1)

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False

        if m > n:
            return self.isOneEditDistance(t, s)

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]

        return m != n
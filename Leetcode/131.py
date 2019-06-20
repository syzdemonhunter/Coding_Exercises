# https://leetcode.com/problems/palindrome-partitioning/
# T: O(2^n)
# S: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s or len(s) == 0:
            return []
        self.res = []
        self.dfs(s, [])
        return self.res
        
    def dfs(self, s, temp):
        # Return Condition
        if len(s) == 0:
            self.res.append(temp[:])
            return
        
        # Backtracking
        for i in range(len(s)):
            if self.is_pa(s[:i + 1]):
                temp.append(s[:i + 1])
                self.dfs(s[i + 1:], temp)
                temp.pop()
        
    def is_pa(self, s):
        return s == s[::-1]
        
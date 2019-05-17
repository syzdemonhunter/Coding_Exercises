# https://www.youtube.com/watch?v=UFdSC_ml4TQ&feature=youtu.be
# Time: O(N*(2^N))
# Space: O(N)

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, [])
        return self.res
        
    def dfs(self, s, temp):
        # Return Condition
        if not s:
            self.res.append(temp[:])
            return
        
        # Backtracking
        for i in range(1, len(s) + 1):
            if self.is_pa(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp)
                temp.pop()
        
    def is_pa(self, s):
        return s == s[::-1]
            
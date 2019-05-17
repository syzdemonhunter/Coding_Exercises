# https://leetcode.com/problems/word-break/
# T: O(n^2)
# S: O(n + m), m是列表大小

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        n = len(s)
        dp = [True] + [False]*(n)
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                    
        return dp[n]
        
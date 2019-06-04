# https://leetcode.com/problems/longest-palindromic-subsequence/
# https://www.jiuzhang.com/solution/longest-palindromic-subsequence/#tag-highlight-lang-python
# 设dp[i][j]表示第i到第j个字符间的最长回文序列的长度（i<=j）
# T: O(n^2)
# S: O(n)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0:
            return 0
        
        dp = [[0 for _ in range(s_len)] for _ in range(s_len)]
        for i in range(s_len - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, s_len):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][s_len - 1]
        
        
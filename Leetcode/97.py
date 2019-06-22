# https://leetcode.com/problems/interleaving-string/
# DP
# T: O(m*n)
# S: O(m*n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False]*(len(s1) + 1) for _ in range(len(s2) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] and (s2[i - 1] == s3[i - 1])
            
        for j in range(1, len(dp[0])):
            dp[0][j] = dp[0][j - 1] and (s1[j - 1] == s3[j - 1])
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = (dp[i - 1][j] and (s2[i - 1] == s3[i + j -1])) or \
                           (dp[i][j - 1] and (s1[j - 1] == s3[i + j -1])) 
                
        return dp[len(s2)][len(s1)]
                          
        
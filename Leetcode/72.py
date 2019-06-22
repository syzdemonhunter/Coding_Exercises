# https://leetcode.com/problems/edit-distance/
# DP 模板题
# T: O(m*n)
# S: O(m*n)

# dp[i][j] 表示的是，从字符串1到i的位置转换到字符串2的j的位置，所需要的最少步数
# 1，字符串中的字符相等： dp[i][j] = dp[i - 1][j - 1]
# 2, 字符串中的字符不等：
    # insert: dp[i][j] = dp[i][j - 1 ] + 1
    # replace: dp[i][j] = dp[i - 1][j - 1] + 1
    # deleter: dp[i][j] = dp[i - 1][j] + 1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0]*(len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            dp[i][0] = i
             
        for j in range(len2 + 1):
            dp[0][j] = j
            
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(min(dp[i][j - 1 ],
                                       dp[i - 1][j]),
                                       dp[i - 1][j - 1]) + 1
                    
        return dp[len1][len2]
                    
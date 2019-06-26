# https://leetcode.com/problems/regular-expression-matching/
# https://www.youtube.com/watch?v=c5vsle60Uw8
# T: O(m*n)
# S: O(m*n)
# 这题非常重要，一定要会

class Solution:
    def isMatch(self, s: str, p: str) -> bool:    
        if p == '':              #如果p串为空
            return s == ''		 #判断s串是否为空
        if s == '':              #如果s串为空
            if len(p) % 2 == 1:  
                return False
            i = 1
            while i < len(p):    #需要满足"x*x*"的形式
                if p[i] != '*':
                    return False
                i += 2
            return True
        
        s_len, p_len = len(s), len(p)
        dp = [[False]*(p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for j in range(p_len):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
                
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                
                if p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                    
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                        
                    else:
                        dp[i + 1][j + 1] = (dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1])
                        
        return dp[s_len][p_len]
                    
                    
        
        
# https://leetcode.com/problems/decode-ways/

# T: O(n)
# S: O(n)
#class Solution:
#    def numDecodings(self, s: str) -> int:
#        if not s or len(s) == 0:
#            return 0
#        n = len(s)
#        dp = [1] + [0]*n
        
#        if s[0] != '0':
#            dp[1] = 1
#        else:
#            dp[1] = 0
            
#        for i in range(2, n + 1):
#            first = int(s[i-1:i])
#            second = int(s[i-2:i])
#            if first >= 1 and first <= 9:
#                dp[i] += dp[i - 1]
#            if second >= 10 and second <= 26:
#                dp[i] += dp[i - 2]
                
#        return dp[n]

# T: O(n)
# S: O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        # empty string or leading zero means no way
        if not s or len(s) == 0 or s[0] == '0':
            return 0
        # c1 and c2 store ways of the last and the last of the last
        c1, c2 = 1, 1
        for i in range(1, len(s)):
            # zero voids ways of the last because zero cannot be used separately
            if s[i] == '0':
                c1 = 0
            # possible two-digit letter, so new c1 is sum of both while new c2 is the old c1
            if s[i - 1] == '1' or (s[i - 1] == '2' and ord(s[i]) <= ord('6')):
                c1 = c1 + c2
                c2 = c1 - c2
            # one-digit letter, no new way added
            else:
                c2 = c1
                
        return c1
        
        
        
        
# https://leetcode.com/problems/perfect-squares/
# https://www.youtube.com/watch?v=KaXeidsmvVQ

# 12
# 1, 4, 9
# 1 + numSquares(12 - 1)
# 4 + numSquares(12 - 4) = 4 + 1 + numSquares(8 - 1)
#                        = 4 + 4 + numSquares(8 - 4)     
# Time O(n * sqrt(n))
# Space O(n)
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n]*(n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                
        return dp[n]
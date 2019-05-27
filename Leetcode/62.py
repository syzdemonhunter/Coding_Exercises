# https://leetcode.com/problems/unique-paths/
# https://www.youtube.com/watch?v=mWV1b9IbosY
# time O(m*n), space O(n)
# 按层扫

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [0]*n
        res[0] = 1
        
        for i in range(m):
            for j in range(1, n):
                res[j] = res[j] + res[j - 1]
                
        return res[n - 1]
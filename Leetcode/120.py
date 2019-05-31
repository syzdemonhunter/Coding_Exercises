# https://leetcode.com/problems/triangle/
# 自底向上的动态规划，多重循环实现
# 使用滚动数组进行空间优化

# 时间复杂度 O(n^2)
# 空间复杂度 O(n)（额外空间耗费）


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # state: dp[i][j] 代表从 i,j  走到最底层的最短路径值
        dp = [[0] * n, [0] * n]
        
        # initialize: 初始化终点（最后一层）
        for i in range(n):
            dp[(n - 1) % 2][i] = triangle[n - 1][i]
            
        # function: 从下往上倒过来推导，计算每个坐标到哪儿去
        # dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i % 2][j] = min(dp[(i + 1) % 2][j], dp[(i + 1) % 2][j + 1]) + triangle[i][j]
                
        # answer: 起点就是答案
        return dp[0][0]
        
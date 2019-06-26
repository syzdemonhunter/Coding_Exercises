# https://leetcode.com/problems/dungeon-game/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or len(dungeon) == 0 or len(dungeon[0]) == 0:
            return 0
        
        m, n = len(dungeon), len(dungeon[0]) 
        dp = [[0]*n for _ in range(m)]
        
        dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
            
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
            
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = max(dp[i + 1][j] - dungeon[i][j], 1)
                right = max(dp[i][j + 1] - dungeon[i][j], 1)
                dp[i][j] = min(down, right)
                
        return dp[0][0]
                
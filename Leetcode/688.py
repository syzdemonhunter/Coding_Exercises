#https://leetcode.com/problems/knight-probability-in-chessboard/
#http://zxi.mytechroad.com/blog/dynamic-programming/688-knight-probability-in-chessboard/
# O(K*N^2), Space Complexity: O(N^2)

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp0 = [[0]*N for _ in range(N)]
        dp0[r][c] = 1.0
        dirs = [[1, 2], [-1, -2], [1, -2], [-1, 2],
                          [2, 1], [-2, -1], [2, -1], [-2, 1]]
        for k in range(K):
            dp1 = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for m in range(8):
                        x = j + dirs[m][0]
                        y = i + dirs[m][1]
                        if x < 0 or y < 0 or x >= N or y >= N:
                            continue
                        dp1[i][j] += dp0[x][y]
                        
            dp0, dp1 = dp1, dp0
            
        total = 0
        for i in range(N):
            for j in range(N):
                total += dp0[i][j]
                
        return total / pow(8, K)
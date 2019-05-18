# https://leetcode.com/problems/game-of-life/
# https://www.jiuzhang.com/solution/game-of-life/#tag-highlight-lang-python
# T: O(M*N)
# S: O(1)

class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        m = len(board)
        n = len(board[0])
    
        for i in range(m):
            for j in range(n):
                # 计算与board[i][j]相邻的活细胞数量
                lives = self.liveNeighbors(board, m, n, i, j);
                
                # 如果当前位置为活细胞，且相邻活细胞数量为2个或者3个，则下一状态仍为活细胞
                if board[i][j] == 1 and lives >= 2 and lives <= 3:  
                    board[i][j] = 3
                
                # 如果当前位置为死细胞，且相邻活细胞数量为3个，则下一状态为活细胞
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        
        # 更新细胞状态
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
    
    def liveNeighbors(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives
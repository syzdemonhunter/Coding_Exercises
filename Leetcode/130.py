# https://leetcode.com/problems/surrounded-regions/
# T: O(m*n)
# S: O(n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board) - 1, len(board[0]) - 1
        
        for i in range(m + 1):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
                
            if board[i][n] == 'O':
                self.dfs(board, i, n)
                
        for j in range(n + 1):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
                
            if board[m][j] == 'O':
                self.dfs(board, m, j)
                
        for i in range(m + 1):
            for j in range(n + 1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'checked':
                    board[i][j] = 'O'
                
                
    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return
        
        board[i][j] = 'checked'
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
                
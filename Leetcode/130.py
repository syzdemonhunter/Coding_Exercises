# https://leetcode.com/problems/surrounded-regions/
# T: O(m*n)
# S: O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        # if board[i][j] is connected with 'O' from boundary, mark it as '?'
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
                return
            board[i][j] = '?'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # detect from boundary
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                     dfs(i,j)
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                     dfs(i,j)    

        for i in range(m):
            for j in range(n):
                if board[i][j] == '?':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
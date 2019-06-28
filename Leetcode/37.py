# https://leetcode.com/problems/sudoku-solver/
# T: ???
# S: ???

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        
        self.solve(board)
        
        
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.is_valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                                
                    return False
                
        return True
                
    def is_valid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i % 3] != '.' and\
               board[3*(row//3) + i//3][3*(col//3) + i % 3] == c:
                    return False
                
        return True
            
        
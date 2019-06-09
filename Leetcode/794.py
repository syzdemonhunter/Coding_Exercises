# https://leetcode.com/problems/valid-tic-tac-toe-state/
# T: O(n)
# S: O(1)

class Solution:
    def isWin(self, board, c):
        for i in range(3):  # Row check
            if board[i] == c*3:
                return True
        for i in range(3):  # Column check
            if board[0][i] == c and board[1][i] == c and board[2][i] == c:
                return True
        if board[0][0] == c and board[1][1] == c and board[2][2] == c or \
                board[0][2] == c and board[1][1] == c and board[2][0] == c:  # Diagonal check
            return True
        return False
    
    def validTicTacToe(self, board: List[str]) -> bool:
        count_X = count_O = 0
        for i in range(3):
            for j in range(3):
                count_X += 1 if board[i][j] == 'X' else 0
                count_O += 1 if board[i][j] == 'O' else 0
        if count_O > count_X or count_X > count_O + 1:
            return False
        if count_O == count_X and self.isWin(board, 'X') or \
           count_X == count_O + 1 and self.isWin(board, 'O'):
            return False
        return True
        
        
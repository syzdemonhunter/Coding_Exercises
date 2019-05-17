# https://leetcode.com/problems/design-tic-tac-toe/
# https://www.youtube.com/watch?v=_BDXk5mkxzQ&t=897s
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row_counter = [0]*n
        self.col_counter = [0]*n
        self.diag_left = 0
        self.diag_right = 0
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        move = 1 if player == 1 else -1
        self.row_counter[row] += move
        self.col_counter[col] += move
        if row == col:
            self.diag_left += move
        if row == self.n - col - 1:
            self.diag_right += move
        
        if self.row_counter[row] == self.n \
        or self.col_counter[col] == self.n \
        or self.diag_left == self.n \
        or self.diag_right == self.n:
            return 1
        elif self.row_counter[row] == -self.n \
        or self.col_counter[col] == -self.n \
        or self.diag_left == -self.n \
        or self.diag_right == -self.n:
            return 2
        else:
            return 0
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
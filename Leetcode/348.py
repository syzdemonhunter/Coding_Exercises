# https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.anti_diag = 0
        self.size = n
        
    # T: O(1)
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        to_add = 1 if player == 1 else -1
        
        self.rows[row] += to_add
        self.cols[col] += to_add
        if row == col:
            self.diag += to_add
            
        if col == len(self.cols) - row - 1:
            self.anti_diag += to_add
        
        if abs(self.rows[row]) == self.size \
        or abs(self.cols[col]) == self.size \
        or abs(self.diag) == self.size \
        or abs(self.anti_diag) == self.size:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
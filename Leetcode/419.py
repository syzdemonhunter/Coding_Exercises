# https://leetcode.com/problems/battleships-in-a-board/
# T: O(n)
# S: O(n)

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        result = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    result += 1
                    self.sink(board, i, j)
                    
        return result
                    
    def sink(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) \
        or board[i][j] != 'X':
            return
        board[i][j] = '.'
        self.sink(board, i + 1, j)
        self.sink(board, i - 1, j)
        self.sink(board, i, j + 1)
        self.sink(board, i, j - 1)
        
        
        
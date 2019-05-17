# https://leetcode.com/problems/word-search/
# https://www.youtube.com/watch?v=Hcj1qVBD3YM
# T: O(m*n*(3^k))
# S: O(m*n)

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    # check whether can find word, start at (i,j) position     
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        
        if i < 0 or i >= len(board) or j < 0 \
        or j >= len(board[0]) or word[0]!=board[i][j]:
            return False
        
        tmp = board[i][j] # first character is found, check the remaining part
        board[i][j] = '#' # avoid visit agian 
        
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or \
              self.dfs(board, i - 1, j, word[1:]) or \
              self.dfs(board, i, j + 1, word[1:]) or \
              self.dfs(board, i, j - 1, word[1:])

        board[i][j] = tmp
        return res
            
        
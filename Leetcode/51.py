# https://leetcode.com/problems/n-queens/
# T: O(n^n)
# S: O(n)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []
        
        result = []
        self.helper(result, [0]*n, 0)
        return result
    
    def helper(self, result, queens, pos):
        if pos == len(queens):
            self.add_solution(result, queens)
            return
        
        for i in range(len(queens)):
            queens[pos] = i
            if self.is_valid(queens, pos):
                self.helper(result, queens, pos + 1)
                
                
    def is_valid(self, queens, pos):
        for i in range(pos):
            if queens[i] == queens[pos]:
                return False
            elif abs(queens[pos] - queens[i]) == abs(i - pos):
                return False
            
        return True
    
    def add_solution(self, result, queens):
        path = []
        for i in range(len(queens)):
            sb = ''
            for j in range(len(queens)):
                if queens[i] == j:
                    sb += 'Q'
                else:
                    sb += '.'
                    
            path.append(sb)
        result.append(path)
                    
        
    
    
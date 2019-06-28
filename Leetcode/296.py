# https://leetcode.com/problems/best-meeting-point/
# T: O(m*n)
# S: O(max(m, n))

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        I, J = [], []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    I.append(i)
                    
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    J.append(j)
                    
        return self.get_min(I) + self.get_min(J)
        
                    
    def get_min(self, lst):
        i, j = 0, len(lst) - 1
        total = 0
        while i < j:
            total += lst[j] - lst[i]
            i += 1
            j -= 1
        return total

        
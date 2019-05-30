# https://leetcode.com/problems/walls-and-gates/
# https://www.youtube.com/watch?v=Pj9378ZsCh4
# Time complexity : O(mn) (from editorial)
# Space complexity : O(mn)


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    self.dfs(i, j, 0, rooms)
                    
    def dfs(self, i, j, count, rooms):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[i]) or rooms[i][j] < count:
            return
        
        rooms[i][j] = count
        self.dfs(i + 1, j, count + 1, rooms)
        self.dfs(i - 1, j, count + 1, rooms)
        self.dfs(i, j + 1, count + 1, rooms)
        self.dfs(i, j - 1, count + 1, rooms)
        
        
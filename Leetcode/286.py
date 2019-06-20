# https://leetcode.com/problems/walls-and-gates/
# T: O(m*n)
# S: O(n)

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)
                    
    def dfs(self, rooms, i, j, dist):
        if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[0]) or rooms[i][j] < dist:
            return
        
        rooms[i][j] = dist
        self.dfs(rooms, i - 1, j, dist + 1)
        self.dfs(rooms, i + 1, j, dist + 1)
        self.dfs(rooms, i, j + 1, dist + 1)
        self.dfs(rooms, i, j - 1, dist + 1)


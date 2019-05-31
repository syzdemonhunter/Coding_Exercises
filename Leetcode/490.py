# https://leetcode.com/problems/the-maze/
# https://leetcode.com/problems/the-maze/discuss/198453/Python-BFS-tm
# Time: O(m * n): worst case visit the entire matrix
# Space: O(m * n): Visited Matrix

import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)] # up down left right
        visited = [[False]*len(maze[0]) for _ in range(len(maze))]
        visited[start[0]][start[1]] = True
        
        q = collections.deque([start])
        
        while q:
            tmp = q.popleft()
            if tmp[0] == destination[0] and tmp[1] == destination[1]:
                return True
            
            for each_dir in dirs:
                # Roll the ball until it hits a wall
                row = tmp[0] + each_dir[0]
                col = tmp[1] + each_dir[1]
                
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
                    row += each_dir[0]
                    col += each_dir[1]
                    
                # x and y locates @ a wall when exiting the above while loop, so we need to backtrack 1 position
                (new_x, new_y) = (row - each_dir[0], col - each_dir[1])
                
                # Check if the new starting position has been visited
                if not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    
        return False
                
            
        
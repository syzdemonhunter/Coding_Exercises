# https://leetcode.com/problems/friend-circles/
# https://www.youtube.com/watch?v=HHiHno66j40
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)
        visited = [0]*n
        result = 0
        for i in range(n):
            if visited[i]:
                continue
            self.dfs(M, i, n, visited)
            result += 1
        return result
    
    def dfs(self, M, curr, n, visited):
        if visited[curr]:
            return
        visited[curr] = 1
        # visit all friends (neighbors)
        for i in range(n):
            if M[curr][i] and not visited[i]:
                self.dfs(M, i, n, visited)
        
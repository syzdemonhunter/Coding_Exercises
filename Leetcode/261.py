# https://leetcode.com/problems/graph-valid-tree/
'''
# T: O(V*E)
# S: O(n)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = []
        
        for i in range(n):
            graph.append([])
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
            
        visited = set()
        visited.add(0)
        
        result = self.dfs(graph, visited, 0, -1)
        if not result:
            return False
        return len(visited) == n
        
    def dfs(self, graph, visited, node, parent):
        sub = graph[node]
        for v in sub:
            if v == parent:
                continue
            if v in visited:
                return False
            visited.add(v)
            result = self.dfs(graph, visited, v, node)
            if not result:
                return False
        return True
'''
# T: O(V*E)
# S: O(n)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and len(edges) == 0:
            return True
        if n < 1 or not edges or len(edges) != n - 1:
            return False
        
        roots = [0]*n
        for i in range(n):
            roots[i] = -1
        
        for pair in edges:
            x = self.find(roots, pair[0])
            y = self.find(roots, pair[1])
            if x == y:
                return False
            roots[x] = y
        return True
            
    def find(self, roots, i):
        while roots[i] != -1:
            i = roots[i]
        return i
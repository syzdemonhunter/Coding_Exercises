# https://leetcode.com/problems/is-graph-bipartite/
# O(V + E)
# O(V + E)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0]*len(graph)
        for i in range(len(graph)):
            if colors[i] == 0 and not self.dfs(graph, colors, 1, i):
                return False
        return True
    
    def dfs(self, graph, colors, color, node):
        if colors[node] != 0:
            return colors[node] == color
        else:
            colors[node] = color
            for neighbor in graph[node]:
                # use another color to color the neighbors (-1)
                if not self.dfs(graph, colors, -color, neighbor): 
                    return False
            return True
                
                
        
# https://leetcode.com/problems/evaluate-division/

#Regarding the time complexity, if there are m queries, q equations and n distinct values, the without optimization, by definition of BFS, it will be O(m(q+n)) ~ O(m * n^2) as q can grow to the order of n^2.

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for ([x,y],value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1/value
        
        def find_prod(s,e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e: 
                return 1.0
            
            q = deque([(s, 1.0)])
            visited = {s}
            while q:
                n, curr = q.popleft()
                for child,value in graph[n].items():
                    if child in visited:
                        continue
                    nc = curr*value
                    if child == e:
                        return nc
                    
                    graph[s][child] = nc
                    graph[child][s] = 1/nc
                    visited.add(child)
                    q.append((child, nc))
            return -1.0
        
        return [find_prod(s,e) for [s,e] in queries]
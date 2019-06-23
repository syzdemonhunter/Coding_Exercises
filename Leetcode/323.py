# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# T: O(edges*nodes)
# S: O(n)
# 参考261

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = n
        roots = [0]*n
        for i in range(n):
            roots[i] = -1
        
        for pair in edges:
            x = self.find(roots, pair[0])
            y = self.find(roots, pair[1])
            if x != y:
                roots[x] = y
                result -= 1
    
        return result
            
    def find(self, roots, i):
        while roots[i] != -1:
            i = roots[i]
        return i
        
        
        
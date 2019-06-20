# https://leetcode.com/problems/minimum-height-trees/
# T: O(n)
# S: O(n)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        result = []
        if n == 1:
            result.append(0)
            return result
        
        adj = [set() for i in range(n)]
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
            
        for i in range(n):
            if len(adj[i]) == 1:
                result.append(i)
                
        while n > 2:
            n -= len(result)
            leaves = []
            for i in result:
                for j in adj[i]:
                    adj[j].remove(i)
                    if len(adj[j]) == 1:
                        leaves.append(j) 
            result = leaves
            
        return result
            
        
        
        
        
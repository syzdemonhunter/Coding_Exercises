# https://leetcode.com/problems/clone-graph/
# T: O(n*e)
# S: O(n)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    my_map = {}
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        result = Node(node.val, [])
        self.my_map[node] = result
        
        for n in node.neighbors:
            if n in self.my_map:
                result.neighbors.append(self.my_map[n])
            else:
                result.neighbors.append(self.cloneGraph(n))
        return result
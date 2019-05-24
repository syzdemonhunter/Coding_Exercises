# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# 时间复杂度O(n)
# 空间复杂度O(n)

import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: 
            return
        
        dummy = Node(0, None, None)
        prev = dummy
        stack = []
        
        while root:
            stack.append(root)
            root = root.left
            
        while stack:
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
    
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right
        


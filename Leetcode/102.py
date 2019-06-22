# https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
# T: O(n)
# S: O(n)
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        q = collections.deque([root])
        while q:
            size = len(q)
            level = []
            for i in range(size):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                level.append(cur.val)
                
            result.append(level)
            
        return result
'''
# T: O(n)
# S: O(n)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        self.helper(result, root, 0)
        return result
    
    def helper(self, result, root, level):
        if not root:
            return
        if level >= len(result):
            result.append([])
        result[level].append(root.val)
        self.helper(result, root.left, level + 1)
        self.helper(result, root.right, level + 1)
    
    
            
        
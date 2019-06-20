# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = collections.deque([root])
        x = True
        while q:
            size = len(q)
            level = []
            for i in range(size):
                cur = q.popleft()
                if x:
                    level.append(cur.val)
                else:
                    level.insert(0, cur.val)
                    
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            result.append(level)
            if x:
                x = False
            else:
                x = True
                
        return result
        
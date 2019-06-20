# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
            result.insert(0, level)
            
        return result
                        
        
# https://leetcode.com/problems/inorder-successor-in-bst/
# T: O(h)
# S: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
                
        return succ
        
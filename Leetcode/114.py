# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# T: O(n)
# S: O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, result):
        if not root:
            return root
        result.append(root)
        self.preorder(root.left, result)
        self.preorder(root.right, result)
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        result = []
        self.preorder(root, result)
        cur = root
        for i in range(1, len(result)):
            cur.left = None
            cur.right = result[i]
            cur = cur.right
        
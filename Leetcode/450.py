# https://leetcode.com/problems/delete-node-in-a-bst/
# T: O(h)
# S: O(h)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < key:
            root.right =  self.deleteNode(root.right, key)
        elif root.val > key:
            root.left =  self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            left_max = root.left
            while left_max.right:
                left_max = left_max.right
            left_max.right = root.right
            root = root.left
        return root

        
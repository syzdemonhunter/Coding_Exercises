# https://leetcode.com/problems/search-in-a-binary-search-tree/
# T: O(h)
# S: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        while root is not None and val != root.val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
                
        return root
        
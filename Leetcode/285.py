# https://leetcode.com/problems/inorder-successor-in-bst/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
# T: O(n)
# S: O(1)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        result = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                result = root
                root = root.left
                
        return result
'''
# T: O(n)
# S: O(n)
class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            tmp = self.inorderSuccessor(root.left, p)
            return tmp if tmp is not None else root
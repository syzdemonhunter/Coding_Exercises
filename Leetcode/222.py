# https://leetcode.com/problems/count-complete-tree-nodes/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_depth = self.helper(root, True)
        right_depth = self.helper(root, False)
        
        if left_depth == right_depth:
            return 2**left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def helper(self, root, is_left):
        # helper: get depth
        if not root:
            return 0
        if is_left:
            return 1 + self.helper(root.left, is_left)
        else:
            return 1 + self.helper(root.right, is_left)
        
# https://leetcode.com/problems/diameter-of-binary-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, d):
        if not root:
            return 0
        left = self.dfs(root.left, d)
        right = self.dfs(root.right, d)
        d[0] = max(d[0], (left + right))
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = [0]
        self.dfs(root, d)
        return d[0]
        
        
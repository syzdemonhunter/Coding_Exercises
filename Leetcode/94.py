# https://leetcode.com/problems/binary-tree-inorder-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, result, p = [], [], root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            result.append(p.val)
            p = p.right

        return result
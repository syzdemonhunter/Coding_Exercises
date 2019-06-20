# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.helper(result, root)
        return result
    
    def helper(self, result, root):
        if not root:
            return
        result.append(root.val)
        self.helper(result, root.left)
        self.helper(result, root.right)
'''
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            result.append(cur.val)
        return result
        

        
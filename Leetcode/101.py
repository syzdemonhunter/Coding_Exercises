# https://leetcode.com/problems/symmetric-tree/
# T: O(n)
# S: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while len(stack) > 0:
            r = stack.pop()
            l = stack.pop()
            if not r and not l:
                continue
            if not r or not l:
                return False
            if r.val == l.val:
                stack.append(r.right)
                stack.append(l.left)
                stack.append(r.left)
                stack.append(l.right)
                
            else:
                return False
        return True

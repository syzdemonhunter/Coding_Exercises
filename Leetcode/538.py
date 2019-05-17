# https://leetcode.com/problems/convert-bst-to-greater-tree/
# T: O(n)
# S: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        cur = root
        total = 0
        
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur.val += total
            total = cur.val
            cur = cur.left
            
        return root
        
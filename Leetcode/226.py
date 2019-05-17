# https://leetcode.com/problems/invert-binary-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        q = [root]
        
        while q:
            node = q.pop(0)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return root
        
        
            
        
        
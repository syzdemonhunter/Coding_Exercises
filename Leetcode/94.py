# https://leetcode.com/problems/binary-tree-inorder-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.helper(result, root)
        return result
    
    def helper(self, result, root):
        if not root:
            return
        self.helper(result, root.left)
        result.append(root.val)
        self.helper(result, root.right)
        
        
#class Solution:
#    def inorderTraversal(self, root: TreeNode) -> List[int]:
#        if not root:
#            return []
        
#        result = []
#        stack = []
#        cur = root
#        while cur or stack:
#            while cur:
#                stack.append(cur)
#                cur = cur.left
#            cur = stack.pop()
#            result.append(cur.val)
#            cur = cur.right
#        return result
        
        
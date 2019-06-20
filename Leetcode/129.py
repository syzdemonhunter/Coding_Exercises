# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root, 0)
        
    def helper(self, root, num):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return num*10 + root.val
        
        left_total = self.helper(root.left, num*10 + root.val)
        right_total = self.helper(root.right, num*10 + root.val)
        
        return left_total + right_total
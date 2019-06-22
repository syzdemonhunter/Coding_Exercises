# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Postorder
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = 0
        
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.result = -float('inf')
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if not root:
            return 0
        
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.result = max(self.result, left + right + root.val)
        return max(left, right) + root.val
        
        
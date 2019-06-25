# https://leetcode.com/problems/house-robber-iii/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root)[1]
        
    def helper(self, root):
        if not root:
            return (0, 0)
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        return (left[1] + right[1], 
                max(left[1] + right[1], left[0] + right[0] + root.val))
        
            